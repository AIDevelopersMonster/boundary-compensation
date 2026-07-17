#!/usr/bin/env python3
"""Compute the N15 physical residual-frame constant from frozen arrays.

Input NPZ arrays:
  generators       shape (m,d,d), Hermitian U_i
  coherent_states  shape (n,d) or (d,n), normalized |psi_a>
  weights          shape (n,), frozen nonnegative quadrature weights
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

import numpy as np


def herm(a: np.ndarray) -> np.ndarray:
    return 0.5 * (a + a.conj().T)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def compute(
    generators: np.ndarray,
    coherent_states: np.ndarray,
    weights: np.ndarray,
    rank_tolerance: float = 1e-12,
    hermiticity_tolerance: float = 1e-11,
    normalization_tolerance: float = 1e-10,
) -> dict[str, Any]:
    u = np.asarray(generators, dtype=complex)
    psi = np.asarray(coherent_states, dtype=complex)
    w = np.asarray(weights, dtype=float)

    if u.ndim != 3 or u.shape[1] != u.shape[2]:
        raise ValueError("generators must have shape (m,d,d)")
    m, d, _ = u.shape
    if psi.ndim != 2:
        raise ValueError("coherent_states must be a matrix")
    if psi.shape[1] != d and psi.shape[0] == d:
        psi = psi.T
    if psi.shape[1] != d or w.shape != (psi.shape[0],):
        raise ValueError("state/weight dimensions do not match generators")
    if np.any(~np.isfinite(w)) or np.any(w < 0.0) or float(w.sum()) <= 0.0:
        raise ValueError("weights must be finite, nonnegative and have positive mass")

    herm_res = [float(np.linalg.norm(x - x.conj().T, ord="fro")) for x in u]
    if max(herm_res, default=0.0) > hermiticity_tolerance:
        raise ValueError("generator Hermiticity gate failed")
    u = np.asarray([herm(x) for x in u])

    norm_res = float(np.max(np.abs(np.sum(np.abs(psi) ** 2, axis=1) - 1.0)))
    if norm_res > normalization_tolerance:
        raise ValueError("coherent-state normalization gate failed")

    g_hs = np.empty((m, m), dtype=complex)
    symbols = np.empty((psi.shape[0], m), dtype=float)
    symbol_imag_res = 0.0
    for i, ui in enumerate(u):
        for j, uj in enumerate(u):
            g_hs[i, j] = np.trace(ui.conj().T @ uj)
        vals = np.einsum("ai,ij,aj->a", psi.conj(), ui, psi)
        symbol_imag_res = max(symbol_imag_res, float(np.max(np.abs(vals.imag))))
        if symbol_imag_res > hermiticity_tolerance:
            raise ValueError("lower-symbol reality gate failed")
        symbols[:, i] = vals.real

    g_hs = herm(g_hs)
    measurement = np.sqrt(w)[:, None] * symbols
    g_symbol = herm(measurement.conj().T @ measurement)

    evals, evecs = np.linalg.eigh(g_hs)
    scale = max(float(np.max(np.abs(evals))), 1.0)
    keep = evals > rank_tolerance * scale
    if not np.any(keep):
        raise ValueError("Hilbert-Schmidt quotient has rank zero")
    whitening = evecs[:, keep] @ np.diag(evals[keep] ** -0.5)
    m_hat = measurement @ whitening
    singular_values = np.sort(np.linalg.svd(m_hat, compute_uv=False))[::-1]
    generalized = np.linalg.eigvalsh(herm(whitening.conj().T @ g_symbol @ whitening))
    alpha = float(singular_values[-1] ** 2)
    beta = float(singular_values[0] ** 2)

    return {
        "schema_version": "1.0",
        "contract": "BC-IDPR-P5-UA01-PHYSICAL-RESIDUAL-FRAME-MATRIX",
        "status": "PHYSICAL_FRAME_MATRIX_COMPUTED",
        "dimensions": {
            "hilbert_space": d,
            "generator_count": m,
            "coherent_state_count": int(psi.shape[0]),
            "hs_quotient_rank": int(np.count_nonzero(keep)),
        },
        "protocol": {
            "weight_total_mass": float(w.sum()),
            "weights_normalized_by_adapter": False,
            "state_normalization_max_residual": norm_res,
            "generator_hermiticity_residuals": herm_res,
            "symbol_imaginary_max_residual": symbol_imag_res,
        },
        "gram": {
            "hilbert_schmidt": g_hs.real.tolist(),
            "lower_symbol": g_symbol.real.tolist(),
            "hs_eigenvalues": evals.real.tolist(),
        },
        "whitened_measurement": {
            "singular_values": singular_values.tolist(),
            "generalized_eigenvalues": generalized.real.tolist(),
            "alpha_U": alpha,
            "beta_U": beta,
            "condition_number": beta / alpha if alpha > 0.0 else None,
            "consistency_residual": float(
                np.max(np.abs(np.sort(generalized) - np.sort(singular_values**2)))
            ),
        },
        "gate": {
            "positive_lower_frame": bool(alpha > rank_tolerance),
            "physical_p5_gate_closed": False,
            "reason": "N15 frozen-case ingestion and corpus reproduction remain required.",
        },
        "claim_ceiling": "finite supplied residual subspace under the supplied physical coherent-state protocol",
    }


def self_test() -> dict[str, Any]:
    s2 = np.sqrt(2.0)
    ez = np.array([[1.0, 0.0], [0.0, -1.0]]) / s2
    ex = np.array([[0.0, 1.0], [1.0, 0.0]]) / s2
    states = np.array([[1, 0], [0, 1], [1, 1], [1, -1]], dtype=complex)
    states[2:] /= s2
    weights = np.full(4, 0.25)
    canonical = compute(np.array([ez, ex]), states, weights)
    nonorthogonal = compute(np.array([2 * ez + 0.3 * ex, 0.7 * ex]), states, weights)
    quotient = compute(np.array([ez, 2 * ez]), states, weights)
    assert abs(canonical["whitened_measurement"]["alpha_U"] - 0.25) < 1e-13
    assert abs(nonorthogonal["whitened_measurement"]["alpha_U"] - 0.25) < 1e-12
    assert quotient["dimensions"]["hs_quotient_rank"] == 1
    return {"status": "SELF_TEST_PASS", "canonical_alpha": 0.25, "quotient_rank": 1}


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--input", type=Path)
    p.add_argument("--output", type=Path)
    p.add_argument("--self-test", action="store_true")
    a = p.parse_args()
    if a.self_test:
        result = self_test()
    else:
        if a.input is None:
            p.error("--input is required unless --self-test is used")
        data = np.load(a.input, allow_pickle=False)
        result = compute(data["generators"], data["coherent_states"], data["weights"])
        result["provenance"] = {
            "input_npz_sha256": sha256(a.input),
            "implementation_sha256": sha256(Path(__file__)),
        }
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if a.output:
        a.output.parent.mkdir(parents=True, exist_ok=True)
        a.output.write_text(text, encoding="utf-8")
        print(json.dumps({"status": result["status"]}))
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
