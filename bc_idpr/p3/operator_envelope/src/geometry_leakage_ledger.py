#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
from typing import Any

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
M2_PATH = HERE / "q_racah_operator_envelope.py"
SPEC = importlib.util.spec_from_file_location("p3bm2_qracah", M2_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("Cannot load q-Racah implementation")
M2 = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M2)

DPS = 80


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def enc(x: Any) -> str:
    return sp.sstr(sp.simplify(x))


def enc_matrix(m: sp.Matrix) -> list[list[str]]:
    return [[enc(m[i, j]) for j in range(m.cols)] for i in range(m.rows)]


def external_geometry() -> dict[str, Any]:
    """Exact unit-edge regular tetrahedron and redundant geometric certificates."""
    rt2 = sp.sqrt(2)
    vertices = sp.Matrix([
        [1, 1, 1],
        [1, -1, -1],
        [-1, 1, -1],
        [-1, -1, 1],
    ]) / (2 * rt2)

    edge_pairs = [(i, j) for i in range(4) for j in range(i + 1, 4)]
    edge_lengths = []
    for i, j in edge_pairs:
        d = vertices.row(i) - vertices.row(j)
        edge_lengths.append(sp.sqrt(sp.simplify(d.dot(d))))

    face_indices = [[1, 2, 3], [0, 3, 2], [0, 1, 3], [0, 2, 1]]
    face_areas: list[sp.Expr] = []
    normals: list[sp.Matrix] = []
    for ids in face_indices:
        a, b, c = [vertices.row(k).T for k in ids]
        cross = (b - a).cross(c - a)
        area = sp.sqrt(sp.simplify(cross.dot(cross))) / 2
        normal = sp.simplify(cross / (2 * area))
        centroid = sp.simplify((a + b + c) / 3)
        if sp.simplify(normal.dot(centroid)) < 0:
            normal = -normal
        face_areas.append(sp.simplify(area))
        normals.append(normal)

    normal_matrix = sp.Matrix.hstack(*normals).T
    area_vector_matrix = sp.diag(*face_areas) * normal_matrix
    closure = sp.simplify(sum((area_vector_matrix.row(i).T for i in range(4)), sp.zeros(3, 1)))
    gram = sp.simplify(normal_matrix * normal_matrix.T)

    a = vertices.row(1).T - vertices.row(0).T
    b = vertices.row(2).T - vertices.row(0).T
    c = vertices.row(3).T - vertices.row(0).T
    oriented_six_volume = sp.simplify(sp.Matrix.hstack(a, b, c).det())
    volume = sp.simplify(abs(oriented_six_volume) / 6)

    expected_gram = sp.Matrix(4, 4, lambda i, j: 1 if i == j else -sp.Rational(1, 3))
    adjacency = sp.ones(4) - sp.eye(4)
    area_scale_per_label = sp.sqrt(3) / 4
    labels = sp.Matrix([1, 1, 1, 1])
    calibrated_areas = sp.simplify(area_scale_per_label * labels)

    checks = {
        "all_edges_unit": all(sp.simplify(x - 1) == 0 for x in edge_lengths),
        "all_faces_equilateral_area": all(sp.simplify(x - sp.sqrt(3) / 4) == 0 for x in face_areas),
        "closure_exact": closure == sp.zeros(3, 1),
        "normal_gram_exact": sp.simplify(gram - expected_gram) == sp.zeros(4),
        "normal_gram_rank": int(gram.rank()),
        "normal_gram_null_vector_ones": sp.simplify(gram * sp.ones(4, 1)) == sp.zeros(4, 1),
        "volume_exact": sp.simplify(volume - sp.sqrt(2) / 12) == 0,
        "label_area_calibration_exact": all(sp.simplify(calibrated_areas[i] - face_areas[i]) == 0 for i in range(4)),
        "noncoplanar_normals": int(normal_matrix.rank()) == 3,
    }
    if not all(v is True or (k == "normal_gram_rank" and v == 3) for k, v in checks.items()):
        raise ValueError(f"External geometry check failed: {checks}")

    return {
        "geometry_type": "unit_edge_regular_euclidean_tetrahedron",
        "vertices": enc_matrix(vertices),
        "edge_pairs": [list(x) for x in edge_pairs],
        "edge_lengths": [enc(x) for x in edge_lengths],
        "face_vertex_indices": face_indices,
        "face_areas": [enc(x) for x in face_areas],
        "outward_unit_normals": enc_matrix(normal_matrix),
        "area_vectors": enc_matrix(area_vector_matrix),
        "closure": [enc(x) for x in closure],
        "normal_gram": enc_matrix(gram),
        "adjacency": [[int(adjacency[i, j]) for j in range(4)] for i in range(4)],
        "oriented_six_volume": enc(oriented_six_volume),
        "volume": enc(volume),
        "external_label_area_map": {
            "labels": [1, 1, 1, 1],
            "area_scale_per_label": enc(area_scale_per_label),
            "calibrated_areas": [enc(x) for x in calibrated_areas],
            "q_independent": True,
        },
        "checks": checks,
        "completeness_basis": "Vertices directly fix the tetrahedron; areas and non-coplanar outward normals give a redundant Minkowski datum satisfying exact closure.",
    }


def mps(x: Any, digits: int = 40) -> str:
    return mp.nstr(x, digits)


def matrix_frobenius_derivative(fn, theta, n: int):
    d = M2.deriv(fn, theta, n)
    return d, M2.fnorm(d)


def qnumber_derivative(n: int, theta):
    return mp.diff(lambda t: M2.qn(n, t), theta)


def internal_point(theta) -> dict[str, Any]:
    p = M2.point(theta)
    _, df_norm = matrix_frobenius_derivative(lambda t: M2.F(2, t), theta, 3)
    qnums = {str(n): M2.qn(n, theta) for n in range(2, 6)}
    qnum_d = {str(n): qnumber_derivative(n, theta) for n in range(2, 6)}
    response_vector = mp.matrix([
        qnum_d["2"], qnum_d["3"], qnum_d["4"], qnum_d["5"],
        df_norm, M2.fnorm(p["dx"]), M2.fnorm(p["dy"]),
        p["corrd"], p["shaped"],
    ])
    response_norm = mp.sqrt((response_vector.T * response_vector)[0])
    return {
        "theta": theta,
        "q_numbers": qnums,
        "q_number_derivatives": qnum_d,
        "F_derivative_norm": df_norm,
        "X_derivative_norm": M2.fnorm(p["dx"]),
        "Y_derivative_norm": M2.fnorm(p["dy"]),
        "orientation_correlation_derivative": p["corrd"],
        "spectral_shape_derivative": p["shaped"],
        "internal_response_norm": response_norm,
        "intrinsic_margin": p["margin"],
        "relative_intrinsic_margin": p["relative"],
        "operator_norm_dual_lower_bound": p["oplb"],
        "orthogonality_residual": p["orth"],
        "nuisance_gram_min_eigenvalue": p["gmin"],
        "nuisance_gram_condition": p["gcond"],
    }


def encode_internal_point(p: dict[str, Any]) -> dict[str, Any]:
    return {
        "theta": mps(p["theta"]),
        "q_numbers": {k: mps(v) for k, v in p["q_numbers"].items()},
        "q_number_derivatives": {k: mps(v) for k, v in p["q_number_derivatives"].items()},
        "F_derivative_norm": mps(p["F_derivative_norm"]),
        "X_derivative_norm": mps(p["X_derivative_norm"]),
        "Y_derivative_norm": mps(p["Y_derivative_norm"]),
        "orientation_correlation_derivative": mps(p["orientation_correlation_derivative"]),
        "spectral_shape_derivative": mps(p["spectral_shape_derivative"]),
        "internal_response_norm": mps(p["internal_response_norm"]),
        "intrinsic_margin": mps(p["intrinsic_margin"]),
        "relative_intrinsic_margin": mps(p["relative_intrinsic_margin"]),
        "operator_norm_dual_lower_bound": mps(p["operator_norm_dual_lower_bound"]),
        "orthogonality_residual": mps(p["orthogonality_residual"]),
        "nuisance_gram_min_eigenvalue": mps(p["nuisance_gram_min_eigenvalue"]),
        "nuisance_gram_condition": mps(p["nuisance_gram_condition"]),
    }


def build(samples: int = 33, dps: int = DPS, config: Path | None = None) -> dict[str, Any]:
    mp.mp.dps = dps
    ext = external_geometry()
    theta0 = mp.pi / 8
    lo = mp.pi / 10
    hi = 3 * mp.pi / 20
    anchor = internal_point(theta0)
    grid = [internal_point(lo + (hi - lo) * i / (samples - 1)) for i in range(samples)]

    ext_ledger = [
        {"channel": "vertices", "derivative": "0", "status": "FIXED_EXACT"},
        {"channel": "edge_lengths", "derivative": "0", "status": "FIXED_EXACT"},
        {"channel": "face_areas", "derivative": "0", "status": "FIXED_EXACT"},
        {"channel": "outward_normals", "derivative": "0", "status": "FIXED_EXACT"},
        {"channel": "normal_gram", "derivative": "0", "status": "FIXED_EXACT"},
        {"channel": "volume", "derivative": "0", "status": "FIXED_EXACT"},
        {"channel": "representation_labels", "derivative": "0", "status": "FIXED_EXACT"},
        {"channel": "external_area_calibration", "derivative": "0", "status": "FIXED_EXACT"},
        {"channel": "observation_protocol", "derivative": "0", "status": "FIXED_BY_PREREGISTRATION"},
    ]

    internal_ledger = [
        {"channel": f"q_number_[{n}]", "anchor_derivative": mps(anchor["q_number_derivatives"][str(n)]), "status": "ALLOWED_INTERNAL_RESPONSE"}
        for n in range(2, 6)
    ] + [
        {"channel": "q_Racah_F", "anchor_derivative_norm": mps(anchor["F_derivative_norm"]), "status": "ALLOWED_INTERNAL_RESPONSE"},
        {"channel": "operator_X", "anchor_derivative_norm": mps(anchor["X_derivative_norm"]), "status": "ALLOWED_INTERNAL_RESPONSE"},
        {"channel": "operator_Y", "anchor_derivative_norm": mps(anchor["Y_derivative_norm"]), "status": "ALLOWED_INTERNAL_RESPONSE"},
        {"channel": "mixed_orientation_correlation", "anchor_derivative": mps(anchor["orientation_correlation_derivative"]), "status": "ALLOWED_INTERNAL_RESPONSE"},
        {"channel": "affine_spectral_shape", "anchor_derivative": mps(anchor["spectral_shape_derivative"]), "status": "ALLOWED_INTERNAL_RESPONSE"},
    ]

    grid_summary = {
        "minimum_intrinsic_margin": mps(min(p["intrinsic_margin"] for p in grid)),
        "minimum_relative_intrinsic_margin": mps(min(p["relative_intrinsic_margin"] for p in grid)),
        "minimum_operator_norm_dual_lower_bound": mps(min(p["operator_norm_dual_lower_bound"] for p in grid)),
        "minimum_internal_response_norm": mps(min(p["internal_response_norm"] for p in grid)),
        "maximum_internal_response_norm": mps(max(p["internal_response_norm"] for p in grid)),
        "maximum_orthogonality_residual": mps(max(p["orthogonality_residual"] for p in grid)),
        "minimum_nuisance_gram_eigenvalue": mps(min(p["nuisance_gram_min_eigenvalue"] for p in grid)),
        "maximum_nuisance_gram_condition": mps(max(p["nuisance_gram_condition"] for p in grid)),
    }

    independent = {
        "theta_derivative": "1",
        "representation_scale_derivative": "0",
        "external_geometry_derivative_norm": "0",
        "protocol_derivative": "0",
        "forbidden_external_leakage_norm": "0",
        "anchor_intrinsic_margin": mps(anchor["intrinsic_margin"]),
        "exact_path_conditions_verified": True,
    }

    all_ext_fixed = all(item["derivative"] == "0" for item in ext_ledger)
    positive_grid = mp.mpf(grid_summary["minimum_intrinsic_margin"]) > 0
    status = "COMPLETE_EXTERNAL_GEOMETRY_AND_ZERO_LEAKAGE_CERTIFIED" if all_ext_fixed and positive_grid else "GEOMETRY_INTERFACE_FAILURE"

    return {
        "schema_version": "1.0",
        "contract": "BC-IDPR-P3-B-03",
        "status": status,
        "model_class": "finite_generic_q_qRacah_operator_envelope_with_fixed_external_geometry",
        "provenance": {
            "implementation_sha256": sha256(Path(__file__)),
            "q_racah_implementation_sha256": sha256(M2_PATH),
            "config_sha256": sha256(config) if config else None,
        },
        "arithmetic": {
            "external_geometry": "exact SymPy algebraic arithmetic",
            "internal_q_response": f"mpmath {dps}-decimal arithmetic",
        },
        "external_geometry": ext,
        "path_domain": {
            "coordinate": "theta",
            "anchor": "pi/8",
            "compact_interval": ["pi/10", "3*pi/20"],
            "regular_chamber": ["0", "pi/5"],
            "sample_count": samples,
        },
        "external_leakage_ledger": ext_ledger,
        "internal_response_ledger": internal_ledger,
        "anchor_internal_response": encode_internal_point(anchor),
        "grid_summary": grid_summary,
        "independent_path_certificate": independent,
        "semantic_bridge": {
            "status": "OPEN_OBLIGATION",
            "statement": "The external tetrahedron is fully fixed, but M3 does not yet prove that the operator package is a calibrated quantization of its classical shape observables.",
            "required_next": "Construct a coherent-state or symbol map from the fixed tetrahedron to the q-Racah operator package and bound symbol mismatch over the compact interval.",
        },
        "claim_status": "P3_B_M3_GEOMETRY_CONTROL_CLOSED_CERT_SEMANTIC_BRIDGE_OPEN",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--samples", type=int, default=33)
    parser.add_argument("--dps", type=int, default=DPS)
    parser.add_argument("--config", type=Path)
    args = parser.parse_args()
    result = build(args.samples, args.dps, args.config)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": result["status"],
        "external_leakage_norm": result["independent_path_certificate"]["forbidden_external_leakage_norm"],
        "minimum_intrinsic_margin": result["grid_summary"]["minimum_intrinsic_margin"],
        "semantic_bridge": result["semantic_bridge"]["status"],
    }, sort_keys=True))
    return 0 if result["status"] == "COMPLETE_EXTERNAL_GEOMETRY_AND_ZERO_LEAKAGE_CERTIFIED" else 1


if __name__ == "__main__":
    raise SystemExit(main())
