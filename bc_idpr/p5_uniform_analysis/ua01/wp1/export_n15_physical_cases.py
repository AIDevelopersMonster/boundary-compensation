#!/usr/bin/env python3
"""Export frozen N15 physical residual-frame cases to the UA01 ingestion format.

This wrapper does not redefine the N15 mathematics. It imports the frozen N15
implementation and its configuration, reconstructs each case with the same q-6j,
projected-torus coherent states, support projector, wall split and quadrature,
and writes the exact arrays required by physical_residual_frame_matrix.py.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
from typing import Any

import numpy as np


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def build_case(n15, cfg: dict[str, Any], family: str, multiplier: int):
    n12 = n15.n12
    base = tuple(map(int, cfg["families"][family]))
    r = int(cfg["base_level_r"] * multiplier)
    k = r - 2
    labels = tuple(multiplier * x for x in base)
    qcfg = cfg["quadrature"]
    cscfg = cfg["coherent_states"]
    dps = int(cfg["q6j"]["mpmath_decimal_precision"])
    tau = float(cscfg["geometric_support_threshold"])
    mmax = int(cscfg["period_sum_mmax"])

    sides = [2.0 * np.pi * x / cfg["base_level_r"] for x in base]
    grid = n12.build_registered_grid(
        sides,
        int(qcfg["symbol_x_nodes"]),
        int(qcfg["symbol_y_nodes"]),
        float(qcfg["endpoint_epsilon"]),
        int(qcfg["simplex_order"]),
        float(cfg["bulk_wall"]["normalized_wall_fraction"]),
    )
    exact = n12.general_exact_xy(k, labels, dps)
    comp = n12.build_target_components(k, exact["J"], grid, mmax)

    evals, evecs = np.linalg.eigh(comp["R"])
    selected = evals >= tau
    U = evecs[:, selected]
    Pgeo = U @ U.conj().T
    inv = (U * (evals[selected] ** -0.5)) @ U.conj().T

    def cond(V: np.ndarray) -> np.ndarray:
        return n15.herm(Pgeo @ inv @ V @ inv @ Pgeo)

    Tf = cond(comp["V_full"])
    Tb = cond(comp["V_bulk"])
    Tw = cond(comp["V_wall"])
    A = n15.herm(Pgeo @ exact["Vxy"] @ Pgeo)
    target_norm = n15.hs_norm(Tf)
    approx_norm = n15.hs_norm(A)
    B = Tb / max(target_norm, 1e-30)
    W = Tw / max(target_norm, 1e-30)
    Au = A / max(approx_norm, 1e-30)
    Rb = n15.herm(B - Au)

    P = n15.coherent_matrix(k, exact["J"], grid["records"], mmax)
    states = P.T.copy()
    weights = n15.grid_cache(
        grid,
        int(cfg["residual_spectrum"]["legendre_max_degree_x"]),
        int(cfg["residual_spectrum"]["legendre_max_degree_y"]),
    )["wprob"].copy()

    sRb = n15.lower_symbol(P, Rb)
    sW = n15.lower_symbol(P, W)
    Gop = np.array([
        [n15.hs_inner(Rb, Rb), n15.hs_inner(Rb, W)],
        [n15.hs_inner(W, Rb), n15.hs_inner(W, W)],
    ])
    Gsym = np.array([
        [n15.symbol_inner(sRb, sRb, weights), n15.symbol_inner(sRb, sW, weights)],
        [n15.symbol_inner(sW, sRb, weights), n15.symbol_inner(sW, sW, weights)],
    ])
    alpha, beta, rank = n15.generalized_frame_bounds(Gop, Gsym)

    arrays = {
        "generators": np.asarray([Rb, W]),
        "coherent_states": states,
        "weights": weights,
    }
    meta = {
        "case_id": f"N15-{family}-r{r}",
        "level_r": r,
        "level_k": k,
        "family": family,
        "labels": list(labels),
        "generator_order": ["R_bulk", "W"],
        "dimensions": {
            "fusion": int(len(exact["J"])),
            "geometric_support": int(selected.sum()),
            "quadrature_points": int(len(weights)),
            "frame_span_rank": int(rank),
        },
        "coherent_state_protocol": {
            "family": "projected torus coherent states",
            "chart": "registered N15 chart",
            "normalization": "unit Hilbert norm",
            "period_sum_mmax": mmax,
        },
        "quadrature_protocol": {
            "grid_shape": [int(qcfg["symbol_x_nodes"]), int(qcfg["symbol_y_nodes"])],
            "weight_convention": "frozen N15 wprob",
            "weights_renormalized": False,
        },
        "ordering_protocol": {
            "candidate": "registered XY ordering",
            "support_threshold": tau,
            "wall_definition": f"normalized wall fraction {cfg['bulk_wall']['normalized_wall_fraction']}",
        },
        "expected_n15_alpha_U": float(alpha),
        "expected_n15_beta_U": float(beta),
        "reproduction_tolerance": 1e-10,
    }
    return arrays, meta


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--n15-script", type=Path, required=True)
    p.add_argument("--config", type=Path, required=True)
    p.add_argument("--output-dir", type=Path, required=True)
    p.add_argument("--family", action="append")
    p.add_argument("--multiplier", type=int, action="append")
    a = p.parse_args()

    n15 = load_module(a.n15_script, "n15_frozen_reference")
    cfg = json.loads(a.config.read_text(encoding="utf-8"))
    families = a.family or list(cfg["families"])
    multipliers = a.multiplier or [int(x) for x in cfg["level_multipliers"]]
    a.output_dir.mkdir(parents=True, exist_ok=True)

    manifest = []
    for family in families:
        for multiplier in multipliers:
            arrays, meta = build_case(n15, cfg, family, multiplier)
            stem = meta["case_id"]
            npz_path = a.output_dir / f"{stem}.npz"
            np.savez_compressed(npz_path, **arrays)
            meta.update({
                "array_file": npz_path.name,
                "array_sha256": sha256(npz_path),
                "source_provenance": {
                    "manuscript": "BC-Spec L1-P04-P/N15 v0.1.0",
                    "implementation": str(a.n15_script),
                    "data_origin": "direct reconstruction from frozen N15 configuration",
                    "source_hashes": {
                        "n15_script": sha256(a.n15_script),
                        "n15_config": sha256(a.config),
                    },
                },
            })
            meta_path = a.output_dir / f"{stem}.json"
            meta_path.write_text(json.dumps(meta, indent=2, sort_keys=True) + "\n", encoding="utf-8")
            manifest.append({
                "case_id": stem,
                "npz": npz_path.name,
                "metadata": meta_path.name,
                "alpha_U": meta["expected_n15_alpha_U"],
            })

    manifest_path = a.output_dir / "N15_PHYSICAL_CASE_MANIFEST.json"
    manifest_path.write_text(json.dumps({
        "schema_version": "1.0",
        "status": "N15_PHYSICAL_CASES_EXPORTED",
        "case_count": len(manifest),
        "cases": manifest,
    }, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"status": "N15_PHYSICAL_CASES_EXPORTED", "case_count": len(manifest)}))


if __name__ == "__main__":
    main()
