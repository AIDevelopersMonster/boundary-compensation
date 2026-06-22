"""Coarse comparator metrics."""

from __future__ import annotations

import numpy as np


def coarse_dephasing_distance(gamma_abs: np.ndarray | float, gamma: float, t: np.ndarray | float) -> np.ndarray:
    """Rotating-frame coarse trace-distance proxy for the |+><+| probe state."""
    gamma_abs = np.asarray(gamma_abs, dtype=float)
    t = np.asarray(t, dtype=float)
    return 0.5 * np.abs(gamma_abs - np.exp(-gamma * t))
