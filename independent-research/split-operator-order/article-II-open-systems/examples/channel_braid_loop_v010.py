#!/usr/bin/env python3
"""Verify exact six-edge contextual braid-loop formulas for Article II v0.1.

Channels:
  * dephasing (Heisenberg UCP),
  * qubit depolarization (Heisenberg UCP),
  * amplitude damping (Heisenberg dual of the standard CPTP channel).
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


def opnorm(a: np.ndarray) -> float:
    return float(np.linalg.svd(a, compute_uv=False)[0])


def word(order: list[int]) -> np.ndarray:
    out = I2.copy()
    for j in order:
        out = out @ U[j]
    return out


def contextual_edges() -> list[np.ndarray]:
    order = [0, 1, 2]
    out: list[np.ndarray] = []
    for s in SWAPS:
        nxt = order.copy()
        nxt[s], nxt[s + 1] = nxt[s + 1], nxt[s]
        out.append(word(nxt) @ word(order).conj().T)
        order = nxt
    assert order == [0, 1, 2]
    return out


def loop(edges: list[np.ndarray], phi) -> np.ndarray:
    h = I2.copy()
    for t in edges:
        h = phi(t) @ h
    return h


def dephasing(a: np.ndarray, eta: float) -> np.ndarray:
    return np.array([[a[0, 0], eta * a[0, 1]], [eta * a[1, 0], a[1, 1]]], complex)


def dephasing_formula(eta: float) -> np.ndarray:
    b = eta**3 * (1.0 - eta**2) / 2.0
    return np.array([[eta**4, b], [-b, eta**4]], complex)


def depolarizing(a: np.ndarray, eta: float) -> np.ndarray:
    return eta * a + (1.0 - eta) * np.trace(a) * I2 / 2.0


def depolarizing_formula(eta: float) -> np.ndarray:
    aa = eta**5 * (eta + 1.0) / 2.0
    b = eta**4 * (1.0 - eta) * (2.0 * eta + 1j * (1.0 + eta)) / 4.0
    return np.array([[aa, b], [-np.conj(b), aa]], complex)


def amplitude_damping_heisenberg(a: np.ndarray, q: float) -> np.ndarray:
    r = math.sqrt(q)
    aa, b, c, d = a[0, 0], a[0, 1], a[1, 0], a[1, 1]
    return np.array([[aa, r * b], [r * c, q * d + (1.0 - q) * aa]], complex)


def amplitude_damping_formula(q: float) -> np.ndarray:
    cq = q**2 * ((1.0 + q) + 1j * (q - 1.0)) / 2.0
    return np.array(
        [
            [cq, 0.5 * q**1.5 * (1.0 - q) * (2.0 * q - 1.0)],
            [q**1.5 * (1.0 - q) * (0.5 + 1j * q), (2.0 * q - 1.0) * cq],
        ],
        complex,
    )


def amplitude_damping_norm_formula(q: float) -> float:
    tau = (q - 1.0) ** 2 * (
        4 * q**6 + 8 * q**5 + 8 * q**4 + 13 * q**3 + 12 * q**2 + 8 * q + 4
    ) / 2.0
    delta = (q - 1.0) ** 4 * (
        100 * q**8 + 220 * q**7 + 329 * q**6 + 408 * q**5 + 400 * q**4
        + 296 * q**3 + 160 * q**2 + 64 * q + 16
    ) / 16.0
    return math.sqrt((tau + math.sqrt(max(0.0, tau * tau - 4.0 * delta))) / 2.0)


def main() -> None:
    edges = contextual_edges()
    flat = I2.copy()
    for t in edges:
        flat = t @ flat
    assert opnorm(flat - I2) < 1e-12

    for eta in [1.0, 0.9, 0.7, 0.5, 0.2, 0.0]:
        hd = loop(edges, lambda a: dephasing(a, eta))
        hp = loop(edges, lambda a: depolarizing(a, eta))
        assert opnorm(hd - dephasing_formula(eta)) < 1e-12
        assert opnorm(hp - depolarizing_formula(eta)) < 1e-12

    for q in [1.0, 0.9, 0.7, 0.5, 0.2, 0.0]:
        ha = loop(edges, lambda a: amplitude_damping_heisenberg(a, q))
        assert opnorm(ha - amplitude_damping_formula(q)) < 1e-12
        assert abs(opnorm(ha - I2) - amplitude_damping_norm_formula(q)) < 1e-12

    print("All exact channel formulas verified.")
    print("first-order coefficients (per gamma*t):")
    print("dephasing       ", math.sqrt(17.0))
    print("depolarizing    ", math.sqrt(123.0) / 2.0)
    print("amplitude damping", math.sqrt(57.0 + 2.0 * math.sqrt(314.0)) / 2.0)


if __name__ == "__main__":
    main()
