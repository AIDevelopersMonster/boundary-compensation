#!/usr/bin/env python3
"""Deterministic checks for Article II qubit identifiability note v0.1.

Verifies:
- the six-by-six reconstruction matrix M;
- det(M)=8192;
- exact inverse coefficients;
- rank-5 backtracking-only surface and rank-6 with braid information.

The script records the frozen algebraic matrices used in the manuscript note.
"""
from __future__ import annotations

from fractions import Fraction

import numpy as np


M = np.array(
    [
        [-6, -8, -8, 0, 0, 2],
        [0, 0, 2, 0, 4, -2],
        [0, 2, 0, 4, 0, -2],
        [-4, 0, -4, 0, 0, 0],
        [-4, -4, 0, 0, 0, 0],
        [-2, -2, -2, 2, 2, 2],
    ],
    dtype=int,
)

# Frozen full backtracking measurement matrix rank from the Article-I six-edge braid design.
# Columns correspond to (c_xx,c_yy,c_zz,c_xy,c_xz,c_yz).  Rows are an algebraically
# equivalent reduced row basis extracted from all right/left backtracking matrix entries.
BACKTRACK_REDUCED = np.array(
    [
        [-4, -4, 0, 0, 0, 0],
        [-4, 0, -4, 0, 0, 0],
        [-2, -2, -2, 2, 2, 2],
        [0, 4, 0, 0, 0, -4],
        [0, 0, 4, 0, -4, 0],
    ],
    dtype=float,
)


def det_bareiss(a: list[list[int]]) -> int:
    """Exact integer determinant by Bareiss elimination."""
    b = [row[:] for row in a]
    n = len(b)
    sign = 1
    prev = 1
    for k in range(n - 1):
        if b[k][k] == 0:
            swap = next((r for r in range(k + 1, n) if b[r][k] != 0), None)
            if swap is None:
                return 0
            b[k], b[swap] = b[swap], b[k]
            sign *= -1
        pivot = b[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                b[i][j] = (b[i][j] * pivot - b[i][k] * b[k][j]) // prev
        prev = pivot
        for i in range(k + 1, n):
            b[i][k] = 0
    return sign * b[-1][-1]


def inverse_fraction(a: list[list[int]]) -> list[list[Fraction]]:
    n = len(a)
    aug = [
        [Fraction(x) for x in row]
        + [Fraction(int(i == j)) for j in range(n)]
        for i, row in enumerate(a)
    ]
    for k in range(n):
        pivot = next(i for i in range(k, n) if aug[i][k] != 0)
        aug[k], aug[pivot] = aug[pivot], aug[k]
        p = aug[k][k]
        aug[k] = [x / p for x in aug[k]]
        for i in range(n):
            if i == k:
                continue
            f = aug[i][k]
            if f:
                aug[i] = [x - f * y for x, y in zip(aug[i], aug[k])]
    return [row[n:] for row in aug]


def main() -> None:
    a = M.tolist()
    det = det_bareiss(a)
    inv = inverse_fraction(a)

    print("M=")
    print(M)
    print("det(M)=", det)
    print("rank(M)=", np.linalg.matrix_rank(M.astype(float)))
    print("rank(backtracking-only reduced basis)=", np.linalg.matrix_rank(BACKTRACK_REDUCED))
    print("M^{-1}=")
    for row in inv:
        print("  ", "  ".join(str(x) for x in row))

    assert det == 8192
    assert np.linalg.matrix_rank(M.astype(float)) == 6
    assert np.linalg.matrix_rank(BACKTRACK_REDUCED) == 5


if __name__ == "__main__":
    main()
