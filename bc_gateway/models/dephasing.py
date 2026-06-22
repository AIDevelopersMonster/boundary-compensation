"""Analytic pure-dephasing central-spin demonstrator."""

from __future__ import annotations

import numpy as np


def gamma_abs_two_spin_bath(t: np.ndarray | float, g1: float = 0.5, g2: float = 0.7) -> np.ndarray:
    """Return |Gamma(t)| for a qubit coupled to a maximally mixed two-spin bath."""
    t = np.asarray(t, dtype=float)
    return np.abs(np.cos(2.0 * g1 * t) * np.cos(2.0 * g2 * t))


def lambda_minus_from_gamma_abs(gamma_abs: np.ndarray | float) -> np.ndarray:
    """Return the moving lower normalized Choi eigenvalue."""
    gamma_abs = np.asarray(gamma_abs, dtype=float)
    return 0.5 * (1.0 - gamma_abs)
