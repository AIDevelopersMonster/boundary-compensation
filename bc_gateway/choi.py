"""Choi response-object helpers."""

from __future__ import annotations

import numpy as np


def qubit_dephasing_choi(gamma_factor: complex, normalized: bool = True) -> np.ndarray:
    """Return the Choi matrix for a qubit pure-dephasing channel.

    The channel is

        [[a, b], [c, d]] -> [[a, Gamma b], [Gamma* c, d]].

    With the unnormalized maximally entangled vector |00> + |11>, the Choi matrix is

        [[1, 0, 0, Gamma],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [Gamma*, 0, 0, 1]].

    If ``normalized`` is true, the matrix is divided by d_S=2.
    """
    gamma_factor = complex(gamma_factor)
    choi = np.array(
        [
            [1.0, 0.0, 0.0, gamma_factor],
            [0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0],
            [np.conjugate(gamma_factor), 0.0, 0.0, 1.0],
        ],
        dtype=complex,
    )
    return 0.5 * choi if normalized else choi


def qubit_dephasing_choi_eigenvalues(gamma_abs: np.ndarray | float) -> np.ndarray:
    """Analytic normalized Choi eigenvalues for a qubit dephasing channel."""
    gamma_abs = np.asarray(gamma_abs, dtype=float)
    plus = 0.5 * (1.0 + gamma_abs)
    minus = 0.5 * (1.0 - gamma_abs)
    return np.stack([plus, minus, np.zeros_like(plus), np.zeros_like(plus)], axis=0)
