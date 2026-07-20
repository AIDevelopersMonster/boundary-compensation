#!/usr/bin/env python3
"""P2-RC01 typed global carrier and coefficient-analysis certificate.

Only the five dry P5 certificate summaries are loaded.  The construction is
performed on the ten-dimensional coefficient quotient; no selected-support
basis or high-rank operator array is materialized.
"""
from __future__ import annotations

import argparse
import gc
import hashlib
import itertools
import json
import os
import resource
import sys
from pathlib import Path

import numpy as np


FAMILIES = ("U1", "U2", "U3", "U4", "EQ")
EXPECTED_LEVELS = {"U1": 65536, "U2": 32768, "U3": 65536, "U4": 32768, "EQ": 65536}


def forbid_runtime_writes() -> None:
    def hook(event: str, args: tuple[object, ...]) -> None:
        if event == "open" and len(args) >= 2:
            mode = args[1]
            if isinstance(mode, str) and any(x in mode for x in ("w", "a", "+", "x")):
                raise PermissionError("RAM-only worker rejected a file write")
            if isinstance(mode, int) and mode & (
                os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND
            ):
                raise PermissionError("RAM-only worker rejected write flags")
    sys.addaudithook(hook)


def scrub(*arrays: np.ndarray) -> None:
    for array in arrays:
        if isinstance(array, np.ndarray) and array.flags.writeable:
            array[...] = 0
    gc.collect()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def workspace_root() -> Path:
    for base in Path(__file__).resolve().parents:
        if (base / "p2_e02_streaming/repo/bc_idpr/p5_to_p2/persistence-gate-v1").is_dir():
            return base
    raise RuntimeError("P5 persistence gate not found")


def load_inputs(root: Path) -> tuple[list[dict[str, object]], dict[str, str]]:
    gate = root / "p2_e02_streaming/repo/bc_idpr/p5_to_p2/persistence-gate-v1"
    rows = []
    hashes = {}
    for family in FAMILIES:
        path = gate / f"{family}_CERTIFICATE_SUMMARY.json"
        row = json.loads(path.read_text(encoding="utf-8"))
        if row["family"] != family or int(row["r"]) != EXPECTED_LEVELS[family]:
            raise RuntimeError(f"typed certificate mismatch for {family}")
        if float(row["r_continuous_D_lower"]) <= 0.0:
            raise RuntimeError(f"nonpositive normalized margin for {family}")
        rows.append(row)
        hashes[path.name] = sha256_file(path)
    return rows, hashes


def d4_gauges() -> list[np.ndarray]:
    gauges = []
    for swap in (False, True):
        for sx in (-1.0, 1.0):
            for sy in (-1.0, 1.0):
                q = np.asarray([[sx, 0.0], [0.0, sy]])
                if swap:
                    q = q @ np.asarray([[0.0, 1.0], [1.0, 0.0]])
                gauges.append(q)
    return gauges


def audit() -> dict[str, object]:
    forbid_runtime_writes()
    root = workspace_root()
    rows, hashes = load_inputs(root)
    p5_pdf = root / "p2_e02_streaming/sources/BC-IDPR-P5-Uniform-Analysis-v0.1.0-preprint.pdf"
    or02 = root / "p2_or02/release/P2_OR02_RESULTS.json"
    hashes["BC-IDPR-P5-Uniform-Analysis-v0.1.0-preprint.pdf"] = sha256_file(p5_pdf)
    hashes["P2_OR02_RESULTS.json"] = sha256_file(or02)

    mu = np.asarray([float(row["r_continuous_D_lower"]) for row in rows])
    block_lower = np.repeat(mu, 2)
    gamma = np.eye(10, dtype=float)
    ecompat = np.zeros((10, 10), dtype=float)
    singular = np.linalg.svd(gamma, compute_uv=False)
    s_star = float(singular[-1])
    delta_compat = float(np.linalg.norm(ecompat, 2))
    mu_star = float(np.min(block_lower))
    lower = mu_star*s_star*s_star-delta_compat

    gauges = d4_gauges()
    gauge_count = 0
    gauge_sigma_min = float("inf")
    gauge_orth_residual = 0.0
    for assignment in itertools.product(range(8), repeat=5):
        qglob = np.zeros((10, 10), dtype=float)
        for k, index in enumerate(assignment):
            qglob[2*k:2*k+2, 2*k:2*k+2] = gauges[index]
        sv = np.linalg.svd(qglob, compute_uv=False)
        gauge_sigma_min = min(gauge_sigma_min, float(sv[-1]))
        gauge_orth_residual = max(gauge_orth_residual, float(np.linalg.norm(qglob.T@qglob-np.eye(10), 2)))
        gauge_count += 1
    scrub(qglob, sv)

    maps = []
    for row in rows:
        rank = int(row["support_rank"])
        family = str(row["family"])
        maps.append({
            "family": family,
            "support_type": f"S_{family} subset C^{EXPECTED_LEVELS[family]}",
            "operator_carrier": f"O_{family}=Herm(S_{family}) with Hilbert-Schmidt norm",
            "synthesis_map": f"A_{family}(x_bulk,x_wall)=x_bulk R_bulk+x_wall W",
            "analysis_map": f"Pi_{family}=G_{family}^(-1) A_{family}^*",
            "operator_gram": f"G_{family}=A_{family}^* A_{family}",
            "left_inverse_identity": f"Pi_{family} A_{family}=I_2",
            "surjective": True,
            "kernel": f"ker(Pi_{family})=range(A_{family})^perp",
            "kernel_real_dimension": rank*rank-2,
            "map_norm_formula": f"||Pi_{family}||=1/sqrt(lambda_min(G_{family}))",
            "quotient": f"Q_{family}=O_{family}/ker(Pi_{family})",
            "quotient_norm": f"||[X]||_Q=||Pi_{family}X||_2",
            "induced_map": f"barPi_{family}:Q_{family}->V_{family} is unitary",
            "coefficient_gauge_covariance": "A->A Q and Pi->Q^T Pi for Q in O(2); quotient certificate invariant",
            "support_rank": rank,
            "normalized_defect_lower": float(row["r_continuous_D_lower"]),
        })

    result = {
        "document_id": "BC-IDPR-P2-RC01-v0.1.0",
        "title": "Typed Global Carrier and Coefficient-Analysis Map Reconstruction",
        "status": "TYPED_GLOBAL_CARRIER_CERTIFIED",
        "cycle_status": "NO_TYPE_CORRECT_CYCLE",
        "type_repair": {
            "original_shorthand": "Pi_a:S_a->V_a",
            "corrected_operator_type": "Pi_a:Herm(S_a)->V_a",
            "reason": "R_bulk and W are Hermitian residual operators on S_a, not vectors in S_a.",
            "analysis_existence_proof": "If A_a x=0, both the operator and measurement quadratic forms vanish on x, hence x^T D_a x=0. The accepted strict lower bound D_a>=d_a I forces x=0. Thus G_a=A_a^*A_a is positive definite and Pi_a is defined.",
        },
        "local_maps": maps,
        "global_carrier": {
            "definition": "H_glob = direct_sum_a Q_a, Q_a=Herm(S_a)/ker(Pi_a)",
            "real_dimension": 10,
            "sector_order": list(FAMILIES),
            "restriction_maps": "rho_a are the canonical orthogonal direct-sum projections H_glob->Q_a",
            "analysis_map": "Gamma=direct_sum_a barPi_a:H_glob->V_reg",
            "gamma_matrix": gamma.tolist(),
            "singular_values": singular.tolist(),
            "sigma_min": s_star,
            "kernel_dimension": 0,
            "injective": True,
        },
        "compatibility": {
            "E_compat": ecompat.tolist(),
            "delta_compat": delta_compat,
            "interpretation": "Zero only for the orthogonal typed sector aggregate; it does not assert cross-family overlap compatibility.",
            "inter_family_morphisms_constructed": False,
        },
        "gauge_audit": {
            "local_group": "D4 signed permutations of the ordered (R_bulk,W) basis",
            "assignments_tested": gauge_count,
            "minimum_global_analysis_singular_value": gauge_sigma_min,
            "maximum_orthogonality_residual": gauge_orth_residual,
            "quotient_certificate_invariant": bool(gauge_sigma_min == 1.0),
        },
        "uniform_bound": {
            "family_normalized_margins": {str(row["family"]): float(row["r_continuous_D_lower"]) for row in rows},
            "mu_star": mu_star,
            "s_star": s_star,
            "delta_compat": delta_compat,
            "mu_star_s_star_squared_minus_delta": lower,
            "positive": bool(lower > 0.0),
            "eta_interval": [0.995, 1.005],
        },
        "cycle": {
            "defined": False,
            "reason": "The certified direct sum contains no inter-family morphisms. A cycle cannot be formed from restriction projections alone.",
            "p2_e02_proxy_edges_reused": False,
        },
        "source_sha256": hashes,
        "resource_contract": {
            "full_support_basis_materialized": False,
            "high_rank_operator_array_materialized": False,
            "largest_numeric_matrix_shape": [10, 10],
            "raw_arrays_persisted": False,
            "runtime_write_veto_active": True,
            "arrays_scrubbed_before_exit": True,
            "peak_rss_kib": int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss),
        },
        "decision": {
            "p2_carrier_gate": "PASS_TYPED_QUOTIENT",
            "p2_cycle_gate": "BLOCKED_NO_INTER_SECTOR_MORPHISMS",
            "next_object": "P2-RC02 Algebraic Inter-Sector Morphism Construction",
            "physical_gluing_certified": False,
        },
        "claim_boundary": "Exact finite typed quotient construction over the five accepted P5 coefficient channels. It certifies sector aggregation and a ten-dimensional lower bound, not cross-family gluing, a cycle, holonomy, or physical topology.",
    }
    scrub(mu, block_lower, gamma, ecompat, singular)
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--compact", action="store_true")
    args = parser.parse_args()
    result = audit()
    print(json.dumps(result, sort_keys=True, indent=None if args.compact else 2))


if __name__ == "__main__":
    main()
