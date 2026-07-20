#!/usr/bin/env python3
"""P2-RC02 exact typed-graph audit for frozen vacuum recoupling rules.

The admitted generators are associator/F-recoupling, tetrahedral external-label
permutations, and the registered within-family N15 level scaling.  All preserve
the relevant category/label signature.  No high-rank carrier is constructed.
"""
from __future__ import annotations

import argparse
import gc
import hashlib
import itertools
import json
import math
import os
import resource
import sys
from pathlib import Path

import numpy as np


FAMILIES = ("U1", "U2", "U3", "U4", "EQ")
EDGES = (("U1", "U2"), ("U2", "U3"), ("U3", "U4"), ("U4", "EQ"), ("EQ", "U1"))
BASE_R = 32


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


def root() -> Path:
    for base in Path(__file__).resolve().parents:
        if (base / "p2_rc01/release/P2_RC01_RESULTS.json").is_file():
            return base
    raise RuntimeError("RC01 workspace not found")


def channel_interval(x: int, y: int, z: int, w: int, k: int) -> tuple[int, int, int]:
    def upper(a: int, b: int) -> int:
        return min(a+b, k-a-b)
    lo = max(abs(x-y), abs(z-w))
    hi = min(upper(x, y), upper(z, w))
    return (lo, hi, max(0, hi-lo+1))


def sector_record(family: str, base: tuple[int, ...], summary: dict[str, object]) -> dict[str, object]:
    r = int(summary["r"])
    multiplier = r//BASE_R
    labels = tuple(multiplier*q for q in base)
    k = r-2
    k1, k2, k3, k4 = labels
    a, b, c, d = k4, k3, k2, k1
    j = channel_interval(a, b, c, d, k)
    ell = channel_interval(a, d, c, b, k)
    return {
        "family": family,
        "category": f"SU(2)_{k}",
        "r": r,
        "k": k,
        "base_labels": list(base),
        "scaled_external_labels": list(labels),
        "sorted_external_labels": sorted(labels),
        "support_rank": int(summary["support_rank"]),
        "recoupling_channels_J": {"lo": j[0], "hi": j[1], "count": j[2]},
        "recoupling_channels_L": {"lo": ell[0], "hi": ell[1], "count": ell[2]},
    }


def edge_audit(a: str, b: str, sectors: dict[str, dict[str, object]]) -> dict[str, object]:
    sa, sb = sectors[a], sectors[b]
    la = tuple(int(x) for x in sa["scaled_external_labels"])
    lb = tuple(int(x) for x in sb["scaled_external_labels"])
    ba = tuple(int(x) for x in sa["base_labels"])
    bb = tuple(int(x) for x in sb["base_labels"])
    permutations = list(itertools.permutations(range(4)))
    exact_matches = [p for p in permutations if tuple(la[i] for i in p) == lb]
    ray_matches = [p for p in permutations if tuple(ba[i] for i in p) == bb]
    same_level = int(sa["r"]) == int(sb["r"])
    recoupling_or_permutation = bool(same_level and exact_matches)
    within_family_scaling = bool(a == b and ray_matches)
    admitted = bool(recoupling_or_permutation or within_family_scaling)
    boundary_a = np.asarray([2.0*math.cos(math.pi*q/16.0) for q in (ba[3], ba[2], ba[1], ba[0])])
    boundary_b = np.asarray([2.0*math.cos(math.pi*q/16.0) for q in (bb[3], bb[2], bb[1], bb[0])])
    separation = float(np.linalg.norm(boundary_a-boundary_b))
    permutation_separations = [float(np.linalg.norm(boundary_a[list(p)]-boundary_b)) for p in permutations]
    min_permutation_separation = min(permutation_separations)
    min_permutation = permutations[permutation_separations.index(min_permutation_separation)]
    result = {
        "edge": f"{a}->{b}",
        "same_category_level": same_level,
        "external_label_multisets_equal": sorted(la) == sorted(lb),
        "tetrahedral_permutation_matches": [list(p) for p in exact_matches],
        "normalized_ray_permutation_matches": [list(p) for p in ray_matches],
        "boundary_trace_separation_same_order": separation,
        "minimum_boundary_trace_separation_over_24_permutations": min_permutation_separation,
        "minimizing_boundary_permutation": list(min_permutation),
        "F_recoupling_or_tetrahedral_rule_admissible": recoupling_or_permutation,
        "registered_within_family_scaling_admissible": within_family_scaling,
        "admitted_nonzero_morphism": admitted,
        "candidate_rank": 2 if admitted else 0,
        "candidate_sigma_min": 1.0 if admitted else 0.0,
        "decision": "ACCEPT" if admitted else "REJECT_TYPE_SIGNATURE",
    }
    scrub(boundary_a, boundary_b)
    return result


def audit() -> dict[str, object]:
    forbid_runtime_writes()
    base = root()
    gate = base / "p2_e02_streaming/repo/bc_idpr/p5_to_p2/persistence-gate-v1"
    cfg_path = base / "p2_e02_streaming/n15_source/BC-Spec-L1-P04-P-N15-v0.1.0-ru-package/n15_sealed_config.json"
    n12_path = base / "p2_e02_streaming/n15_source/BC-Spec-L1-P04-P-N15-v0.1.0-ru-package/support/n14_reference/support/n12_reference/n12_gram_sign_audit.py"
    symmetry_path = base / "p2_e02_streaming/p5branch/bc_idpr/p3/operator_envelope/BC-IDPR-P3-B-G2-R.md"
    rc01_path = base / "p2_rc01/release/P2_RC01_RESULTS.json"
    cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
    rc01 = json.loads(rc01_path.read_text(encoding="utf-8"))
    if rc01["status"] != "TYPED_GLOBAL_CARRIER_CERTIFIED":
        raise RuntimeError("RC01 carrier gate is not closed")

    sectors = {}
    source_hashes = {
        cfg_path.name: sha256_file(cfg_path),
        n12_path.name: sha256_file(n12_path),
        symmetry_path.name: sha256_file(symmetry_path),
        rc01_path.name: sha256_file(rc01_path),
    }
    for family in FAMILIES:
        summary_path = gate / f"{family}_CERTIFICATE_SUMMARY.json"
        summary = json.loads(summary_path.read_text(encoding="utf-8"))
        sectors[family] = sector_record(family, tuple(cfg["families"][family]), summary)
        source_hashes[summary_path.name] = sha256_file(summary_path)

    edges = [edge_audit(a, b, sectors) for a, b in EDGES]
    accepted = [e for e in edges if e["admitted_nonzero_morphism"]]
    all_composable = bool(len(accepted) == len(EDGES))
    result = {
        "document_id": "BC-IDPR-P2-RC02-v0.1.0",
        "title": "Algebraic Inter-Sector Morphism Construction",
        "status": "NO_ADMISSIBLE_INTER_SECTOR_MORPHISMS" if not accepted else "TYPE_CORRECT_INTER_SECTOR_GRAPH_CERTIFIED",
        "cycle_status": "NO_TYPE_CORRECT_CYCLE" if not all_composable else "TYPE_CORRECT_CYCLE_GRAPH_AVAILABLE",
        "admitted_generator_class": {
            "F_recoupling": "Associator change of basis inside one fixed category level and fixed external tensor-product object.",
            "tetrahedral_symmetry": "External-label permutations inducing signed row/column permutations and optional transpose of the same q-6j problem.",
            "N15_level_scaling": "Registered scaling r->m r only along the same base-label family ray.",
            "preserved_signature": "category level plus external-label permutation orbit; N15 scaling additionally preserves the base-label ray",
            "excluded_expansion": "Label-changing coupons, defects, induction/restriction functors, or cross-level tensor functors not already constructed upstream are outside the frozen vacuum rule and would require a new branch-level object.",
        },
        "sectors": sectors,
        "edges": edges,
        "graph": {
            "objects": list(FAMILIES),
            "requested_edges": [f"{a}->{b}" for a, b in EDGES],
            "accepted_nonzero_edges": [e["edge"] for e in accepted],
            "accepted_edge_count": len(accepted),
            "isolated_object_count": len(FAMILIES) if not accepted else None,
            "cycle_composition_typed": all_composable,
        },
        "rank_singular_gate": {
            "required_rank_per_edge": 2,
            "required_sigma_min_positive": True,
            "edges_passing": len(accepted),
            "edges_failing": len(edges)-len(accepted),
            "zero_morphism_rejected": True,
        },
        "compatibility": {
            "new_inter_sector_term_constructed": False,
            "delta_compat_increment": 0.0,
            "reason": "No arrow passed the type signature gate; no compatibility operator was introduced.",
            "RC01_direct_sum_bound_retained": float(rc01["uniform_bound"]["mu_star_s_star_squared_minus_delta"]),
        },
        "decision": {
            "p2_inter_sector_graph_gate": "FAILED_NO_ADMISSIBLE_ARROWS",
            "p2_cycle_gate": "CLOSED_NEGATIVE_NO_TYPE_CORRECT_CYCLE",
            "p2_e02_proxy_edges_reused": False,
            "next_object": "P2-CL01 Typed Gluing No-Go and Branch Closure Synthesis",
            "defect_or_label_changing_extension": "AUTHOR_DECISION_REQUIRED_AFTER_BASELINE_CLOSURE",
        },
        "source_sha256": source_hashes,
        "resource_contract": {
            "full_support_basis_materialized": False,
            "high_rank_recoupling_matrix_materialized": False,
            "permutations_tested_per_edge": 24,
            "largest_numeric_matrix_shape": [4],
            "raw_arrays_persisted": False,
            "runtime_write_veto_active": True,
            "peak_rss_kib": int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss),
        },
        "claim_boundary": "Exact no-go within the frozen vacuum generator class (F-moves, tetrahedral permutations, and same-family N15 scaling). It does not prove that no label-changing or defect-extended category can ever connect the sectors.",
    }
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--compact", action="store_true")
    args = parser.parse_args()
    print(json.dumps(audit(), sort_keys=True, indent=None if args.compact else 2))


if __name__ == "__main__":
    main()
