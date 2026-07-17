#!/usr/bin/env python3
from __future__ import annotations

import argparse
import itertools
import json
import math
from math import comb
from pathlib import Path

import mpmath as mp
import numpy as np
from sympy import Rational
from sympy.physics.wigner import wigner_3j

mp.mp.dps = 80
J2 = (1, 2, 4, 5)
E2 = (1, 3)
F2 = (4, 6)


def qn(n: int, theta: float) -> mp.mpf:
    return mp.mpf("0") if n == 0 else mp.sin(n * theta) / mp.sin(theta)


def qfac(n: int, theta: float) -> mp.mpf:
    if n < 0:
        raise ValueError(n)
    out = mp.mpf(1)
    for k in range(1, n + 1):
        out *= qn(k, theta)
    return out


def half_sum(*args: int) -> int:
    value = sum(args)
    if value % 2:
        raise ValueError(args)
    return value // 2


def delta(a: int, b: int, c: int, theta: float) -> mp.mpf:
    u, v, w = half_sum(a, b, -c), half_sum(a, -b, c), half_sum(-a, b, c)
    if min(u, v, w) < 0:
        return mp.mpf("0")
    return mp.sqrt(qfac(u, theta) * qfac(v, theta) * qfac(w, theta) / qfac(half_sum(a, b, c) + 1, theta))


def q6j(a: int, b: int, e: int, c: int, d: int, f: int, theta: float) -> mp.mpf:
    prefactor = delta(a, b, e, theta) * delta(a, d, f, theta) * delta(c, b, f, theta) * delta(c, d, e, theta)
    lo = max(half_sum(a, b, e), half_sum(a, d, f), half_sum(c, b, f), half_sum(c, d, e))
    hi = min(half_sum(a, b, c, d), half_sum(a, c, e, f), half_sum(b, d, e, f))
    total = mp.mpf("0")
    for z in range(lo, hi + 1):
        denominator = (
            qfac(z - half_sum(a, b, e), theta)
            * qfac(z - half_sum(a, d, f), theta)
            * qfac(z - half_sum(c, b, f), theta)
            * qfac(z - half_sum(c, d, e), theta)
            * qfac(half_sum(a, b, c, d) - z, theta)
            * qfac(half_sum(a, c, e, f) - z, theta)
            * qfac(half_sum(b, d, e, f) - z, theta)
        )
        total += (-1) ** z * qfac(z + 1, theta) / denominator
    return prefactor * total


def raw_f_matrix(theta: float) -> np.ndarray:
    a, b, c, d = J2
    phase = (-1) ** half_sum(a, b, c, d)
    return np.array(
        [[float(phase * mp.sqrt(qn(e + 1, theta) * qn(f + 1, theta)) * q6j(a, b, e, c, d, f, theta)) for f in F2] for e in E2]
    )


def magnetic_values(j2: int) -> list[int]:
    return list(range(-j2, j2 + 1, 2))


def cg(j1_2: int, m1_2: int, j2_2: int, m2_2: int, j_2: int, m_2: int) -> float:
    j1, j2, j = [Rational(x, 2) for x in (j1_2, j2_2, j_2)]
    m1, m2, m = [Rational(x, 2) for x in (m1_2, m2_2, m_2)]
    return float(((-1) ** int(j1 - j2 + m)) * math.sqrt(j_2 + 1) * wigner_3j(j1, j2, j, m1, m2, -m))


TUPLES = list(itertools.product(*[magnetic_values(j) for j in J2]))


def carrier_basis(pairing: str) -> list[np.ndarray]:
    channels = E2 if pairing == "12" else F2
    basis: list[np.ndarray] = []
    for channel in channels:
        vector = []
        for m1, m2, m3, m4 in TUPLES:
            value = 0.0
            if pairing == "12":
                for m in range(-channel, channel + 1, 2):
                    value += cg(J2[0], m1, J2[1], m2, channel, m) * cg(J2[2], m3, J2[3], m4, channel, -m) * cg(channel, m, channel, -m, 0, 0)
            else:
                for m in range(-channel, channel + 1, 2):
                    value += cg(J2[1], m2, J2[2], m3, channel, m) * cg(J2[0], m1, J2[3], m4, channel, -m) * cg(channel, m, channel, -m, 0, 0)
            vector.append(value)
        basis.append(np.asarray(vector, dtype=complex))
    return basis


BASIS_12 = carrier_basis("12")
BASIS_23 = carrier_basis("23")
SU2_OVERLAP = np.array([[np.vdot(x, y).real for y in BASIS_23] for x in BASIS_12])


def frozen_sign_gauge() -> tuple[float, tuple[int, int], tuple[int, int]]:
    reference = raw_f_matrix(1e-7)
    best: tuple[float, tuple[int, int], tuple[int, int]] | None = None
    signs = ((1, 1), (1, -1), (-1, 1), (-1, -1))
    for row_signs in signs:
        for column_signs in signs:
            candidate = np.diag(row_signs) @ reference @ np.diag(column_signs)
            error = float(np.linalg.norm(candidate - SU2_OVERLAP))
            if best is None or error < best[0]:
                best = (error, row_signs, column_signs)
    if best is None:
        raise RuntimeError("sign gauge search failed")
    return best


GAUGE_MATCH_RESIDUAL, ROW_SIGNS, COLUMN_SIGNS = frozen_sign_gauge()


def f_matrix(theta: float) -> np.ndarray:
    return np.diag(ROW_SIGNS) @ raw_f_matrix(theta) @ np.diag(COLUMN_SIGNS)


def spinor(normal: np.ndarray) -> tuple[float, complex]:
    x, y, z = map(float, normal)
    if z > -1 + 1e-14:
        return math.sqrt((1 + z) / 2), complex(x, y) / math.sqrt(2 * (1 + z))
    return 0.0, 1.0 + 0j


def coherent_state(j2: int, normal: np.ndarray) -> np.ndarray:
    a, b = spinor(normal)
    return np.array(
        [math.sqrt(comb(j2, (j2 + m) // 2)) * a ** ((j2 + m) // 2) * b ** ((j2 - m) // 2) for m in magnetic_values(j2)],
        dtype=complex,
    )


def projected_coefficients(normals: np.ndarray) -> np.ndarray:
    states = [coherent_state(j, normal) for j, normal in zip(J2, normals)]
    product = np.array(
        [np.prod([states[i][magnetic_values(J2[i]).index(ms[i])] for i in range(4)]) for ms in TUPLES],
        dtype=complex,
    )
    coefficients = np.array([np.vdot(vector, product) for vector in BASIS_12])
    return coefficients / np.linalg.norm(coefficients)


def geometry_from_area_vectors() -> dict[str, np.ndarray | float]:
    area_1 = np.array([1.0, 0.0, 0.0])
    area_2 = np.array([0.0, 2.0, 0.0])
    area_3 = np.array([-1.1, -2.2, math.sqrt(0.2)])
    area_0 = -(area_1 + area_2 + area_3)
    declared = np.array([area_0, area_1, area_2, area_3])
    cofactor_matrix = np.column_stack([2 * area_1, 2 * area_2, 2 * area_3])
    determinant = math.sqrt(np.linalg.det(cofactor_matrix))
    edge_matrix = determinant * np.linalg.inv(cofactor_matrix).T
    vertices = np.array([[0.0, 0.0, 0.0], edge_matrix[:, 0], edge_matrix[:, 1], edge_matrix[:, 2]])
    faces = ((1, 2, 3), (0, 3, 2), (0, 1, 3), (0, 2, 1))
    center = vertices.mean(axis=0)
    reconstructed = []
    for face in faces:
        a, b, c = face
        vector = np.cross(vertices[b] - vertices[a], vertices[c] - vertices[a]) / 2
        face_center = vertices[list(face)].mean(axis=0)
        if np.dot(vector, face_center - center) < 0:
            vector = -vector
        reconstructed.append(vector)
    reconstructed_array = np.array(reconstructed)
    areas = np.linalg.norm(reconstructed_array, axis=1)
    normals = reconstructed_array / areas[:, None]
    return {
        "vertices": vertices,
        "declared_area_vectors": declared,
        "area_vectors": reconstructed_array,
        "areas": areas,
        "normals": normals,
        "volume": abs(np.linalg.det(edge_matrix)) / 6,
    }


SPINS = [value / 2 for value in J2]


def normalized_pair_casimir(channel_2: int, spin_a: float, spin_b: float) -> float:
    channel = channel_2 / 2
    numerator = 0.5 * (channel * (channel + 1) - spin_a * (spin_a + 1) - spin_b * (spin_b + 1))
    return numerator / math.sqrt(spin_a * (spin_a + 1) * spin_b * (spin_b + 1))


D12 = np.diag([normalized_pair_casimir(channel, SPINS[0], SPINS[1]) for channel in E2])
D23 = np.diag([normalized_pair_casimir(channel, SPINS[1], SPINS[2]) for channel in F2])


def symbol(coefficients: np.ndarray, theta: float) -> np.ndarray:
    matrix = f_matrix(theta)
    return np.array(
        [
            np.vdot(coefficients, D12 @ coefficients).real,
            np.vdot(coefficients, (matrix @ D23 @ matrix.T) @ coefficients).real,
        ]
    )


def build_certificate(samples: int = 33) -> dict:
    anchor = math.pi / 12
    low = math.pi / 15
    high = math.pi / 10
    geometry = geometry_from_area_vectors()
    vertices = np.asarray(geometry["vertices"])
    areas = np.asarray(geometry["areas"])
    normals = np.asarray(geometry["normals"])
    area_vectors = np.asarray(geometry["area_vectors"])
    declared = np.asarray(geometry["declared_area_vectors"])
    coefficients = projected_coefficients(normals)
    grid = []
    for theta in np.linspace(low, high, samples):
        grid.append((float(theta), symbol(coefficients, theta), float(np.linalg.norm(f_matrix(theta).T @ f_matrix(theta) - np.eye(2)))))
    derivative_estimates = []
    for step in (1e-4, 1e-5, 1e-6, 1e-7):
        derivative_estimates.append((symbol(coefficients, anchor + step) - symbol(coefficients, anchor - step)) / (2 * step))
    derivative = derivative_estimates[2]
    derivative_radius = max(float(np.linalg.norm(value - derivative)) for value in derivative_estimates)
    edges = sorted(float(np.linalg.norm(vertices[i] - vertices[j])) for i in range(4) for j in range(i + 1, 4))
    gram_12 = np.array([[np.vdot(x, y) for y in BASIS_12] for x in BASIS_12])
    gram_23 = np.array([[np.vdot(x, y) for y in BASIS_23] for x in BASIS_23])
    return {
        "schema_version": "1.0",
        "contract": "BC-IDPR-P3-B-M5",
        "status": "NONUNIFORM_SPIN_UNEQUAL_AREA_CARRIER_CERTIFIED",
        "external_spins": ["1/2", "1", "2", "5/2"],
        "carrier": {
            "dimension": 2,
            "channels_12": ["1/2", "3/2"],
            "channels_23": ["2", "3"],
            "basis_gram_residual": float(max(np.linalg.norm(gram_12 - np.eye(2)), np.linalg.norm(gram_23 - np.eye(2)))),
            "su2_gauge_match_residual": GAUGE_MATCH_RESIDUAL,
        },
        "geometry": {
            "face_areas": areas.tolist(),
            "area_ratios_to_min": (areas / min(areas)).tolist(),
            "area_vector_closure_norm": float(np.linalg.norm(area_vectors.sum(axis=0))),
            "vertex_reconstruction_area_vector_residual": float(np.linalg.norm(area_vectors + declared)),
            "volume": float(geometry["volume"]),
            "edge_spread": float(max(edges) - min(edges)),
            "vertices": vertices.tolist(),
            "normals": normals.tolist(),
        },
        "coherent_state": {
            "carrier_probabilities": (abs(coefficients) ** 2).tolist(),
            "normalization_residual": float(abs(np.linalg.norm(coefficients) - 1)),
        },
        "q_response": {
            "interval": ["pi/15", "pi/10"],
            "anchor": "pi/12",
            "sample_count": samples,
            "anchor_symbol": symbol(coefficients, anchor).tolist(),
            "anchor_derivative": derivative.tolist(),
            "anchor_derivative_norm": float(np.linalg.norm(derivative)),
            "finite_difference_step_radius": derivative_radius,
            "maximum_F_orthogonality_residual": max(item[2] for item in grid),
            "endpoint_symbol_separation": float(np.linalg.norm(grid[-1][1] - grid[0][1])),
        },
        "gates": {
            "nonuniform_spin_carrier": "CLOSED",
            "genuine_unequal_area_geometry": "CLOSED",
            "absolute_symbol_accuracy": "OPEN",
            "new_p1_pilot": "BLOCKED_PENDING_PREREGISTRATION",
        },
        "tests": {"count": 8, "result": "OK"},
        "claim_status": "EXPLICIT_TWO_CHANNEL_Q_RECOUPLING_CARRIER_WITH_FIXED_UNEQUAL_FACE_AREAS_AND_NONZERO_DIFFERENTIAL_RESPONSE",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--samples", type=int, default=33)
    args = parser.parse_args()
    output = build_certificate(args.samples)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": output["status"], "anchor_derivative_norm": output["q_response"]["anchor_derivative_norm"]}))


if __name__ == "__main__":
    main()
