#!/usr/bin/env python3
from __future__ import annotations
import json, math
import numpy as np
from scipy.linalg import expm


def herm(a):
    return 0.5 * (a + a.conj().T)


def contour_jets(R, R1, R2, center, radius, nodes, weight):
    n = R.shape[0]
    I = np.eye(n, dtype=complex)
    f0 = np.zeros_like(R, dtype=complex)
    f1 = np.zeros_like(R, dtype=complex)
    f2 = np.zeros_like(R, dtype=complex)
    for k in range(nodes):
        t = 2 * math.pi * (k + 0.5) / nodes
        e = complex(math.cos(t), math.sin(t))
        z = center + radius * e
        G = np.linalg.inv(z * I - R)
        factor = radius * e / nodes
        wz = weight(z)
        f0 += factor * wz * G
        f1 += factor * wz * (G @ R1 @ G)
        f2 += factor * wz * (G @ R2 @ G + 2 * G @ R1 @ G @ R1 @ G)
    return herm(f0), herm(f1), herm(f2)


def exact_functions(theta, tau):
    K = np.array([
        [0, -0.35, -0.22, 0.05],
        [0.35, 0, 0.12, -0.18],
        [0.22, -0.12, 0, -0.27],
        [-0.05, 0.18, 0.27, 0],
    ], float)
    Q = expm(theta * K)
    Q1 = K @ Q
    Q2 = (K @ K) @ Q
    vals = np.array([
        0.16 + 0.015 * math.sin(theta),
        0.33 + 0.01 * math.cos(2 * theta),
        1.28 + 0.06 * math.sin(1.3 * theta),
        1.92 + 0.05 * math.cos(0.8 * theta),
    ])
    vals1 = np.array([
        0.015 * math.cos(theta),
        -0.02 * math.sin(2 * theta),
        0.078 * math.cos(1.3 * theta),
        -0.04 * math.sin(0.8 * theta),
    ])
    vals2 = np.array([
        -0.015 * math.sin(theta),
        -0.04 * math.cos(2 * theta),
        -0.1014 * math.sin(1.3 * theta),
        -0.032 * math.cos(0.8 * theta),
    ])
    D, D1, D2 = np.diag(vals), np.diag(vals1), np.diag(vals2)
    R = Q @ D @ Q.T
    R1 = Q1 @ D @ Q.T + Q @ D1 @ Q.T + Q @ D @ Q1.T
    R2 = (
        Q2 @ D @ Q.T + Q @ D2 @ Q.T + Q @ D @ Q2.T
        + 2 * Q1 @ D1 @ Q.T + 2 * Q1 @ D @ Q1.T + 2 * Q @ D1 @ Q1.T
    )
    E, U = np.linalg.eigh(herm(R))
    selected = E >= tau
    P = U[:, selected] @ U[:, selected].T
    S = (U[:, selected] * (E[selected] ** -0.5)) @ U[:, selected].T
    V = np.array([
        [0.8 + 0.1 * math.cos(theta), 0.2 * math.sin(theta), 0.04, 0.01],
        [0.2 * math.sin(theta), -0.5 + 0.08 * math.sin(1.2 * theta), 0.03, 0.02],
        [0.04, 0.03, 0.6 + 0.05 * math.cos(0.6 * theta), 0.1 * math.sin(0.7 * theta)],
        [0.01, 0.02, 0.1 * math.sin(0.7 * theta), -0.2 + 0.04 * math.cos(theta)],
    ], float)
    V1 = np.array([
        [-0.1 * math.sin(theta), 0.2 * math.cos(theta), 0, 0],
        [0.2 * math.cos(theta), 0.096 * math.cos(1.2 * theta), 0, 0],
        [0, 0, -0.03 * math.sin(0.6 * theta), 0.07 * math.cos(0.7 * theta)],
        [0, 0, 0.07 * math.cos(0.7 * theta), -0.04 * math.sin(theta)],
    ], float)
    V2 = np.array([
        [-0.1 * math.cos(theta), -0.2 * math.sin(theta), 0, 0],
        [-0.2 * math.sin(theta), -0.1152 * math.sin(1.2 * theta), 0, 0],
        [0, 0, -0.018 * math.cos(0.6 * theta), -0.049 * math.sin(0.7 * theta)],
        [0, 0, -0.049 * math.sin(0.7 * theta), -0.04 * math.cos(theta)],
    ], float)
    C = herm(S @ V @ S)
    return R, R1, R2, P, S, V, V1, V2, C, E


def fd5(fun, x, h):
    fm2, fm1, f0, fp1, fp2 = fun(x - 2*h), fun(x - h), fun(x), fun(x + h), fun(x + 2*h)
    d1 = (fm2 - 8*fm1 + 8*fp1 - fp2) / (12*h)
    d2 = (-fm2 + 16*fm1 - 30*f0 + 16*fp1 - fp2) / (12*h*h)
    return d1, d2


def rel(a, b):
    return float(np.linalg.norm(a - b, 2) / max(np.linalg.norm(b, 2), 1e-30))


def main():
    theta, tau = 0.37, 0.8
    R, R1, R2, P, S, V, V1, V2, C, E = exact_functions(theta, tau)
    center, radius, nodes = 1.60, 0.55, 2048
    Pc, P1, P2 = contour_jets(R, R1, R2, center, radius, nodes, lambda z: 1.0 + 0j)
    Sc, S1, S2 = contour_jets(R, R1, R2, center, radius, nodes, lambda z: z ** (-0.5))
    C1 = herm(S1 @ V @ S + S @ V1 @ S + S @ V @ S1)
    C2 = herm(S2 @ V @ S + S @ V2 @ S + S @ V @ S2 + 2*S1 @ V1 @ S + 2*S1 @ V @ S1 + 2*S @ V1 @ S1)
    h = 2e-4
    P1fd, P2fd = fd5(lambda t: exact_functions(t, tau)[3], theta, h)
    S1fd, S2fd = fd5(lambda t: exact_functions(t, tau)[4], theta, h)
    C1fd, C2fd = fd5(lambda t: exact_functions(t, tau)[8], theta, h)
    result = {
        "status": "SELF_TEST_PASS",
        "support_rank": int(np.sum(E >= tau)),
        "threshold_gap": float(np.min(np.abs(E - tau))),
        "contour_reconstruction": {"P": rel(Pc, P), "S": rel(Sc, S)},
        "jet_relative_errors": {
            "P1": rel(P1, P1fd), "P2": rel(P2, P2fd),
            "S1": rel(S1, S1fd), "S2": rel(S2, S2fd),
            "C1": rel(C1, C1fd), "C2": rel(C2, C2fd),
        },
        "norms": {
            "P1": float(np.linalg.norm(P1, 2)), "P2": float(np.linalg.norm(P2, 2)),
            "S1": float(np.linalg.norm(S1, 2)), "S2": float(np.linalg.norm(S2, 2)),
            "C1": float(np.linalg.norm(C1, 2)), "C2": float(np.linalg.norm(C2, 2)),
        },
    }
    assert result["contour_reconstruction"]["P"] < 1e-10
    assert result["contour_reconstruction"]["S"] < 1e-10
    assert result["jet_relative_errors"]["P1"] < 1e-7
    assert result["jet_relative_errors"]["P2"] < 2e-5
    assert result["jet_relative_errors"]["S1"] < 1e-7
    assert result["jet_relative_errors"]["S2"] < 2e-5
    assert result["jet_relative_errors"]["C1"] < 1e-7
    assert result["jet_relative_errors"]["C2"] < 3e-5
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
