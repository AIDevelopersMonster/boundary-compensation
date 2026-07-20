#!/usr/bin/env python3
"""P2-CL01 closure-chain verifier for the frozen baseline gluing branch."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import resource
import sys
from pathlib import Path


EXPECTED = {
    "P2-E01": "INCONCLUSIVE_GLUING__CENTER_REGISTRY_CONSTRUCTED",
    "P2-E02": "ORIENTATION_UNIDENTIFIABLE",
    "P2-OR01": "CONDITIONAL_Z2_SIGNAL__ORIENTATION_WALL_AND_PULLBACK_DEPENDENCE_FOUND",
    "P2-OR02": "P2_CERTIFICATE_RESET",
    "P2-RC01": "TYPED_GLOBAL_CARRIER_CERTIFIED",
    "P2-RC02": "NO_ADMISSIBLE_INTER_SECTOR_MORPHISMS",
}
FROZEN_GRAPH = ["U1->U2", "U2->U3", "U3->U4", "U4->EQ", "EQ->U1"]


def forbid_runtime_writes() -> None:
    def hook(event: str, args: tuple[object, ...]) -> None:
        if event == "open" and len(args) >= 2:
            mode = args[1]
            if isinstance(mode, str) and any(x in mode for x in ("w", "a", "+", "x")):
                raise PermissionError("closure verifier rejected a file write")
            if isinstance(mode, int) and mode & (
                os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND
            ):
                raise PermissionError("closure verifier rejected write flags")
    sys.addaudithook(hook)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def root() -> Path:
    for base in Path(__file__).resolve().parents:
        if (base / "p2_rc02/release/P2_RC02_RESULTS.json").is_file():
            return base
    raise RuntimeError("P2 result chain not found")


def audit() -> dict[str, object]:
    forbid_runtime_writes()
    base = root()
    paths = {
        "P2-E01": base / "p2_e02_streaming/repo/bc_idpr/p2/e01/P2_E01_RESULTS.json",
        "P2-E02": base / "p2_e02_streaming/release/P2_E02_RESULTS.json",
        "P2-OR01": base / "p2_or01/release/P2_OR01_RESULTS.json",
        "P2-OR02": base / "p2_or02/release/P2_OR02_RESULTS.json",
        "P2-RC01": base / "p2_rc01/release/P2_RC01_RESULTS.json",
        "P2-RC02": base / "p2_rc02/release/P2_RC02_RESULTS.json",
    }
    records = {code: json.loads(path.read_text(encoding="utf-8")) for code, path in paths.items()}
    hashes = {code: sha256_file(path) for code, path in paths.items()}
    for code, status in EXPECTED.items():
        if records[code].get("status") != status:
            raise RuntimeError(f"unexpected {code} status")
    if records["P2-RC01"].get("cycle_status") != "NO_TYPE_CORRECT_CYCLE":
        raise RuntimeError("RC01 cycle gate mismatch")
    if records["P2-RC02"].get("cycle_status") != "NO_TYPE_CORRECT_CYCLE":
        raise RuntimeError("RC02 cycle gate mismatch")
    if records["P2-E01"].get("graph") != FROZEN_GRAPH or records["P2-E02"].get("graph") != FROZEN_GRAPH:
        raise RuntimeError("frozen graph mismatch")
    if records["P2-RC02"]["graph"]["accepted_edge_count"] != 0:
        raise RuntimeError("RC02 graph is not empty")
    chain_root = hashlib.sha256("".join(hashes[code] for code in EXPECTED).encode()).hexdigest()

    ledger = [
        {
            "object": "P2-E01",
            "retained": "Center-derived coefficient transition registry and its uncertainty comparison.",
            "not_retained": "Any inference of exact closure or nonzero global defect.",
        },
        {
            "object": "P2-E02",
            "retained": "RAM-only same-index proxy transition matrices, singular values, and resource audit.",
            "not_retained": "Physical overlap, physical edge orientation, or physical cycle interpretation.",
        },
        {
            "object": "P2-OR01",
            "retained": "Robust conditional Z2 signal inside the proxy construction and its singular orientation wall.",
            "not_retained": "Physical nonorientability or Mobius interpretation.",
        },
        {
            "object": "P2-OR02",
            "retained": "Exact U3/U4 ordered-boundary sector separation and carrier reset.",
            "not_retained": "Existence of a U3/U4 physical pullback or cross-Gram.",
        },
        {
            "object": "P2-RC01",
            "retained": "Typed ten-dimensional quotient carrier, sigma_min(Gamma)=1, and direct-sum lower bound.",
            "not_retained": "Cross-family compatibility or a cycle inferred from direct-sum projections.",
        },
        {
            "object": "P2-RC02",
            "retained": "Exact zero-arrow no-go in the frozen vacuum generator class.",
            "not_retained": "A universal prohibition on future defect or label-changing extensions.",
        },
    ]

    return {
        "document_id": "BC-IDPR-P2-CL01-v0.1.0",
        "title": "Typed Gluing No-Go and Branch Closure Synthesis",
        "status": "P2_BASELINE_TYPED_GLUING_CLOSED_NEGATIVE",
        "branch_state": "COMPLETED_NEGATIVE_AND_FROZEN",
        "cycle_status": "NO_TYPE_CORRECT_CYCLE",
        "evidence_chain": {
            "objects": list(EXPECTED),
            "statuses": EXPECTED,
            "input_sha256": hashes,
            "chain_root_sha256": chain_root,
            "all_expected_statuses_verified": True,
            "frozen_graph_verified": True,
        },
        "baseline_theorem": {
            "domain": "Five frozen typed P5 sectors (U1,U2,U3,U4,EQ) at their registered levels and the requested five-edge graph.",
            "admitted_generator_class": "F-recoupling, tetrahedral external-label permutations, and registered same-family N15 scaling.",
            "statement": "No nonzero type-correct inter-sector arrow exists on any requested edge; therefore no type-correct five-edge cycle exists in the frozen baseline.",
            "proof_dependencies": [
                "OR02 proves the alleged U3/U4 physical overlap is empty.",
                "RC01 constructs the only certified global baseline object as a disconnected typed quotient sum.",
                "RC02 exhausts the frozen vacuum algebraic generators and accepts zero of five requested arrows.",
            ],
            "failure_is_data_absence": False,
        },
        "retained_result_ledger": ledger,
        "quantitative_facts": {
            "E01_center_angle_degrees": float(records["P2-E01"]["cycle"]["projective_angle_degrees"]),
            "E01_uncertainty_degrees": float(records["P2-E01"]["cycle"]["propagated_angle_error_upper_degrees"]),
            "OR02_U3_U4_boundary_separation_lower": float(records["P2-OR02"]["physical_overlap_test"]["certified_separation_lower"]),
            "RC01_sigma_min_Gamma": float(records["P2-RC01"]["global_carrier"]["sigma_min"]),
            "RC01_direct_sum_lower_bound": float(records["P2-RC01"]["uniform_bound"]["mu_star_s_star_squared_minus_delta"]),
            "RC02_accepted_nonzero_edges": int(records["P2-RC02"]["graph"]["accepted_edge_count"]),
        },
        "closure_gates": {
            "P2_BASELINE": "CLOSED_NEGATIVE",
            "P2_TYPED_CARRIER": "CERTIFIED_DISCONNECTED",
            "P2_INTERSECTOR_GRAPH": "CLOSED_NEGATIVE_ZERO_ARROWS",
            "P2_CYCLE": "CLOSED_NEGATIVE_NO_TYPE_CORRECT_CYCLE",
            "P2_E03": "PROHIBITED_ON_BASELINE",
            "P2_G3": "BLOCKED_BY_NO_CYCLE",
            "P2_G4": "BLOCKED_BY_NO_CYCLE",
        },
        "permanent_rules": [
            "Do not reuse local Gram-center congruence fits as overlap evidence.",
            "Do not use same grid indices as physical equality across family sectors.",
            "Do not reuse P2-E02 proxy transitions as algebraic morphisms.",
            "Do not form a cycle from direct-sum restriction projections.",
            "Do not materialize full 32768- or 65536-dimensional family bases.",
            "Raw local arrays remain RAM-only and are scrubbed after contraction.",
            "Cache absence triggers local computation and never an absence-certificate artifact.",
            "Do not reopen P2-E03 under renamed same-index, Gram-fit, or post-hoc sign constructions.",
        ],
        "post_closure_options": {
            "automatic_next_object": None,
            "author_decision_required": True,
            "possible_new_objects": [
                "Defect or label-changing coupon extension routed through the appropriate non-baseline branch.",
                "Explicit cross-level tensor functor construction with new type and coherence obligations.",
                "No continuation; retain the negative baseline theorem as terminal.",
            ],
        },
        "resource_contract": {
            "large_basis_materialized": False,
            "raw_arrays_persisted": False,
            "runtime_write_veto_active": True,
            "peak_rss_kib": int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss),
        },
        "claim_boundary": "Finite frozen-baseline no-go. No universal categorical, continuum, spacetime, holonomy, nonorientability, or defect-extended impossibility claim.",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--compact", action="store_true")
    args = parser.parse_args()
    print(json.dumps(audit(), sort_keys=True, indent=None if args.compact else 2))


if __name__ == "__main__":
    main()
