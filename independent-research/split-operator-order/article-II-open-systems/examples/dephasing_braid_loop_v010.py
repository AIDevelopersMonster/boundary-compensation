#!/usr/bin/env python3
"""Exact/numerical verification for Article II v0.1.0.

Contextual braid loop:
123 -> 213 -> 231 -> 321 -> 312 -> 132 -> 123
for the Article-I spin-1/2 triple.

The script verifies:
  1. exact contextual flatness T6...T1 = I;
  2. the closed dephasing formula for H_eta;
  3. the exact reduced-loop norm;
  4. the general multiplicativity-defect upper bound.
"""

from __future__ import annotations

import math
import numpy as np

I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)

U = [X, (X + Y) / math.sqrt(2.0), (X + Z) / math.sqrt(2.0)]
SWAPS = [0, 1, 0, 1, 0, 1]


def word(order: list[int]) -> np.ndarray:
    out = I2.copy()
    for j in order:
        out = out @ U[j]
    return out


def contextual_edges() -> list[np.ndarray]:
    order = [0, 1, 2]
    edges: list[np.ndarray] = []
    for s in SWAPS:
        nxt = order.copy()
        nxt[s], nxt[s + 1] = nxt[s + 1], nxt[s]
        edges.append(word(nxt) @ word(order).conj().T)
        order = nxt
    assert order == [0, 1, 2]
    return edges


def dephasing(a: np.ndarray, eta: float) -> np.ndarray:
    return np.array(
        [[a[0, 0], eta * a[0, 1]], [eta * a[1, 0], a[1, 1]]],
        dtype=complex,
    )


def opnorm(a: np.ndarray) -> float:
    return float(np.linalg.svd(a, compute_uv=False)[0])


def reduced_loop(edges: list[np.ndarray], eta: float) -> np.ndarray:
    out = I2.copy()
    for t in edges:
        out = dephasing(t, eta) @ out
    return out


def closed_formula(eta: float) -> np.ndarray:
    b = eta**3 * (1.0 - eta**2) / 2.0
    return np.array([[eta**4, b], [-b, eta**4]], dtype=complex)


def exact_norm_formula(eta: float) -> float:
    return math.sqrt((1.0 - eta**4) ** 2 + (eta**6 * (1.0 - eta**2) ** 2) / 4.0)


def defect_bound(edges: list[np.ndarray], eta: float) -> float:
    prefix = I2.copy()
    total = 0.0
    for k, t in enumerate(edges):
        if k >= 1:
            delta = dephasing(t @ prefix, eta) - dephasing(t, eta) @ dephasing(prefix, eta)
            total += opnorm(delta)
        prefix = t @ prefix
    return total


def main() -> None:
    edges = contextual_edges()

    flat = I2.copy()
    for t in edges:
        flat = t @ flat
    print("contextual_flatness_error", opnorm(flat - I2))

    print("eta,exact_norm,defect_bound,bound_ratio")
    for eta in [1.0, 0.95, 0.90, 0.80, 0.60, 0.40, 0.20, 0.0]:
        h = reduced_loop(edges, eta)
        err_formula = opnorm(h - closed_formula(eta))
        exact = opnorm(h - I2)
        exact_formula = exact_norm_formula(eta)
        bound = defect_bound(edges, eta)
        assert err_formula < 1e-12
        assert abs(exact - exact_formula) < 1e-12
        assert exact <= bound + 1e-12
        ratio = float("nan") if exact < 1e-12 else bound / exact
        print(f"{eta:.2f},{exact:.12f},{bound:.12f},{ratio:.9f}")


if __name__ == "__main__":
    main()
