#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import numpy as np

SQRT2 = math.sqrt(2.0)
E_Z = np.array([[1.0, 0.0], [0.0, -1.0]]) / SQRT2
E_X = np.array([[0.0, 1.0], [1.0, 0.0]]) / SQRT2
BASIS = (E_Z, E_X)

STATES = {
    "z_plus": np.array([1.0, 0.0]),
    "z_minus": np.array([0.0, 1.0]),
    "x_plus": np.array([1.0, 1.0]) / SQRT2,
    "x_minus": np.array([1.0, -1.0]) / SQRT2,
}
WEIGHTS = {name: 0.25 for name in STATES}


def measurement_vector(z: np.ndarray) -> np.ndarray:
    return np.array([float(z.T @ b @ z) for b in BASIS])


def frame_matrix() -> np.ndarray:
    out = np.zeros((2, 2))
    for name, z in STATES.items():
        v = measurement_vector(z)
        out += WEIGHTS[name] * np.outer(v, v)
    return out


def main() -> None:
    vectors = {name: measurement_vector(z) for name, z in STATES.items()}
    frame = frame_matrix()
    assert np.linalg.norm(frame - 0.25 * np.eye(2), ord=2) < 1e-14

    primal_t = float(np.linalg.eigvalsh(frame)[0])
    dual_z = 0.5 * np.eye(2)
    contacts = {name: float(v.T @ dual_z @ v) for name, v in vectors.items()}
    dual_mu = max(contacts.values())
    assert abs(primal_t - 0.25) < 1e-14
    assert abs(dual_mu - 0.25) < 1e-14

    # Nonorthogonal test map for the operator-adapted transfer identity.
    c_map = np.array([[2.0, 0.3], [0.0, 0.7]])
    adapted = c_map.T @ frame @ c_map
    assert np.linalg.norm(adapted - 0.25 * c_map.T @ c_map, ord=2) < 1e-14
    sigma_min = float(np.linalg.svd(c_map, compute_uv=False)[-1])
    assert abs(float(np.linalg.eigvalsh(adapted)[0]) - 0.25 * sigma_min**2) < 1e-14

    result = {
        "schema_version": "1.0",
        "contract": "BC-IDPR-P5-UA01-WP1-WP2",
        "status": "EXACT_TWO_CHANNEL_E_OPTIMAL_FRAME_CERTIFIED",
        "residual_space": {
            "type": "Sym_0(2,R)",
            "dimension": 2,
            "basis": ["sigma_z/sqrt(2)", "sigma_x/sqrt(2)"],
            "basis_normalization": "Hilbert-Schmidt orthonormal",
        },
        "candidate_pool": list(STATES.keys()),
        "weights": WEIGHTS,
        "measurement_vectors": {name: v.tolist() for name, v in vectors.items()},
        "primal": {
            "frame_matrix": frame.tolist(),
            "minimum_eigenvalue": primal_t,
            "exact_value": "1/4",
        },
        "dual": {
            "Z": dual_z.tolist(),
            "trace_Z": float(np.trace(dual_z)),
            "contact_values": contacts,
            "mu": dual_mu,
            "exact_value": "1/4",
        },
        "optimality": {
            "trace_upper_bound": 0.25,
            "primal_dual_gap": dual_mu - primal_t,
            "all_four_candidates_are_contacts": all(abs(x - 0.25) < 1e-14 for x in contacts.values()),
        },
        "operator_adapted_transfer": {
            "identity": "F_B = (1/4) C^T C",
            "lower_bound": "c_frame = (1/4) sigma_min(C)^2",
            "rank_wall": "sigma_min(C)=0",
        },
        "claim_ceiling": "exact finite-dimensional two-channel real-symmetric residual theorem",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
