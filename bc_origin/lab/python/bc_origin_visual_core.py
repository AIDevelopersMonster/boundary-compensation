"""Core calculations for BC-Origin signed-shadow visual experiments."""
from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Iterable

import numpy as np


@dataclass(frozen=True)
class SignedShadowResult:
    n1: int
    n2: int
    d1: float
    d2: float
    gamma: float
    kappa: float
    mu: float
    orientation: int
    lambda_minus: float
    lambda_plus: float
    scale_minus: float
    scale_plus: float
    gap: float
    localized_minus: bool
    localized_plus: bool


def sign(x: float) -> int:
    return 1 if x > 0 else -1 if x < 0 else 0


def signed_shadow(n1: int, n2: int, d1: float, d2: float, gamma: float, kappa: float, mu: float = 1.0) -> SignedShadowResult:
    """Compute signed common-shift eigen-denominators and observable scales.

    D = [[d1 + gamma*s, kappa],
         [kappa,        d2 + gamma*s]]

    where s = sign(n1*n2). Localized branches require lambda > 0.
    """
    s = sign(n1 * n2)
    base = 0.5 * (d1 + d2) + gamma * s
    radius = math.sqrt((0.5 * (d1 - d2)) ** 2 + kappa**2)
    lm = base - radius
    lp = base + radius
    sm = mu / lm if lm > 0 else math.inf
    sp = mu / lp if lp > 0 else math.inf
    return SignedShadowResult(
        n1=n1,
        n2=n2,
        d1=d1,
        d2=d2,
        gamma=gamma,
        kappa=kappa,
        mu=mu,
        orientation=s,
        lambda_minus=lm,
        lambda_plus=lp,
        scale_minus=sm,
        scale_plus=sp,
        gap=lp - lm,
        localized_minus=lm > 0,
        localized_plus=lp > 0,
    )


def one_generator_scale(q: int, n: int, alpha: float = 1.0, theta_odd: float = math.pi) -> float:
    """One-generator oriented winding scale.

    Scale depends on |n|. Orientation sign is sign(n) and is kept separately.
    """
    if n == 0:
        return math.inf
    theta = theta_odd if abs(q) % 2 == 1 else 0.0
    mu = alpha * max(abs(q), 1)
    denom = 2 * math.pi * abs(n) - theta
    return mu / denom if denom > 0 else math.inf


def phase_grid(n_values: Iterable[int], gamma_values: Iterable[float], d1: float, d2: float, kappa: float) -> np.ndarray:
    """Return lambda_minus grid over n-product sign/amplitude and gamma.

    Rows correspond to n1*n2 values, columns to gamma values.
    """
    pairs = list(n_values)
    gammas = list(gamma_values)
    grid = np.zeros((len(pairs), len(gammas)))
    for i, prod in enumerate(pairs):
        s = sign(prod)
        for j, gam in enumerate(gammas):
            grid[i, j] = signed_shadow(prod, 1 if prod != 0 else 0, d1, d2, gam, kappa).lambda_minus
    return grid
