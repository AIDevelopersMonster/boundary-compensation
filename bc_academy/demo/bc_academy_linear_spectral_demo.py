#!/usr/bin/env python3
"""
BC-Academy finite-dimensional spectral-access demo.

This script is intentionally small and dependency-free. It demonstrates the
educational spine used in BC-Academy:

  near-zero spectrum -> D_gap -> A_gap -> finite-resolution access -> sector weights

The model is a 2x2 avoided-crossing family A(t) with two fixed sector projectors.
It is not a physical simulation and makes no hidden-sector reconstruction claim.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import sqrt


@dataclass(frozen=True)
class SpectralPoint:
    t: float
    gap: float
    lambda_minus: float
    lambda_plus: float
    weight_sector_1: float
    weight_sector_2: float
    accessible_count: int


def eigen_data_for_avoided_crossing(t: float, eps: float, delta: float) -> SpectralPoint:
    """Return eigenvalues and sector weights for [[t, eps], [eps, -t]]."""
    r = sqrt(t * t + eps * eps)
    lam_minus = -r
    lam_plus = r

    # Eigenvector for the positive branch can be represented by (eps, r - t).
    # The normalized squared components are overlaps with the fixed coordinate sectors.
    v1 = eps
    v2 = r - t
    norm2 = v1 * v1 + v2 * v2
    if norm2 == 0.0:
        weight_1 = 1.0
        weight_2 = 0.0
    else:
        weight_1 = (v1 * v1) / norm2
        weight_2 = (v2 * v2) / norm2

    # A simple finite-resolution window: count branches with |lambda| <= delta.
    accessible = int(abs(lam_minus) <= delta) + int(abs(lam_plus) <= delta)
    return SpectralPoint(t, 2.0 * r, lam_minus, lam_plus, weight_1, weight_2, accessible)


def main() -> None:
    eps = 0.15
    delta = 0.40
    print("BC-Academy demo: finite-resolution access in a 2x2 avoided crossing")
    print("Model: A(t) = [[t, eps], [eps, -t]]")
    print(f"eps={eps:.2f}, finite-resolution threshold delta={delta:.2f}")
    print()
    print("   t      lambda-   lambda+     gap     w_sector1  w_sector2  N_eff")
    print("--------------------------------------------------------------------")
    for t in [-0.50, -0.25, 0.00, 0.25, 0.50]:
        p = eigen_data_for_avoided_crossing(t, eps, delta)
        print(
            f"{p.t:6.2f}  {p.lambda_minus:8.3f}  {p.lambda_plus:8.3f}"
            f"  {p.gap:7.3f}  {p.weight_sector_1:9.3f}  {p.weight_sector_2:9.3f}  {p.accessible_count:5d}"
        )

    print()
    print("Reading:")
    print("- the full gap moves with t;")
    print("- sector weights flow across the avoided crossing;")
    print("- finite-resolution access depends on the declared threshold delta;")
    print("- no unique hidden sector is reconstructed from this table.")


if __name__ == "__main__":
    main()
