"""
BC-Origin II kernel core

Boundary Compensation Origin II:
Structural Coupling Kernels and Multi-Shadow Spectral Geometry

This module implements the finite-dimensional toy-model core used by
generate_bc_origin_ii_figures.py.

It is not a general physics simulator. It is a reproducible computational
scaffold for the structural-kernel multi-shadow operator in BC-Origin II.
"""

from __future__ import annotations

import numpy as np


def sign(x: float) -> int:
    """Return the sign of a nonzero or zero real number."""
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0


def theta_default(q: int) -> float:
    """
    Default structural phase function.

    The minimal BC-Origin II software keeps theta simple by default.
    More elaborate theta(|q|) rules can be inserted later, but should be
    documented in the manuscript and README if used.
    """
    return 0.0


def closure_denominator(q: int, n: int, theta=None) -> float:
    """
    Compute the BC-Origin closure denominator

        d_i = 2*pi*|n_i| - theta(|q_i|).

    Parameters
    ----------
    q:
        Index-like residual label.
    n:
        Hidden winding index.
    theta:
        Optional callable theta(q). If omitted, theta_default is used.
    """
    if n == 0:
        raise ValueError("BC-Origin winding labels must be nonzero.")

    theta_fn = theta_default if theta is None else theta
    return 2.0 * np.pi * abs(n) - theta_fn(abs(q))


def structural_kernel(n_i: int, n_j: int, kind: str = "lorentz", alpha: float = 0.5) -> float:
    """
    Structural kernel K(n_i, n_j) on hidden winding-index space.

    Supported kernels
    -----------------
    lorentz:
        K_ij = 1 / (1 + (n_i - n_j)^2)

    exp:
        K_ij = exp(-alpha * |n_i - n_j|)
    """
    m = n_i - n_j

    if kind == "lorentz":
        return 1.0 / (1.0 + m * m)

    if kind == "exp":
        return float(np.exp(-alpha * abs(m)))

    raise ValueError(f"Unknown kernel kind: {kind}")


def kernel_matrix(n_list, kind: str = "lorentz", alpha: float = 0.5) -> np.ndarray:
    """Build the finite structural kernel matrix K_ij."""
    n_values = list(n_list)
    N = len(n_values)

    K = np.zeros((N, N), dtype=float)

    for i in range(N):
        for j in range(N):
            K[i, j] = structural_kernel(
                n_values[i],
                n_values[j],
                kind=kind,
                alpha=alpha,
            )

    return K


def sign_matrix(n_list) -> np.ndarray:
    """
    Build the balanced sign matrix

        s_ij = sign(n_i n_j) = sigma_i sigma_j.
    """
    n_values = list(n_list)
    sigma = np.asarray([sign(n) for n in n_values], dtype=float)
    return sigma[:, None] * sigma[None, :]


def build_D(
    n_list,
    q_list,
    gamma: float = 0.0,
    eta: float = 1.0,
    kind: str = "lorentz",
    alpha: float = 0.5,
    theta=None,
    signed_offdiag: bool = False,
) -> np.ndarray:
    """
    Build the BC-Origin II multi-shadow signed spectral operator.

    Baseline manuscript convention:

        (D_N)_ii = d_i + gamma * sum_{j != i} s_ij K_ij
        (D_N)_ij = eta * K_ij,  i != j

    Optional diagnostic variant:

        (D_N)_ij = eta * s_ij * K_ij,  i != j

    The signed_offdiag variant is implemented for diagnostics only and
    should not be confused with the baseline unless the manuscript adopts it.
    """
    n_values = list(n_list)
    q_values = list(q_list)

    if len(n_values) != len(q_values):
        raise ValueError("n_list and q_list must have the same length.")

    if any(n == 0 for n in n_values):
        raise ValueError("BC-Origin II uses nonzero winding labels.")

    N = len(n_values)
    K = kernel_matrix(n_values, kind=kind, alpha=alpha)
    S = sign_matrix(n_values)

    D = np.zeros((N, N), dtype=float)

    for i in range(N):
        d_i = closure_denominator(q_values[i], n_values[i], theta=theta)

        signed_kernel_sum = 0.0
        for j in range(N):
            if i != j:
                signed_kernel_sum += S[i, j] * K[i, j]

        D[i, i] = d_i + gamma * signed_kernel_sum

        for j in range(N):
            if i == j:
                continue

            if signed_offdiag:
                D[i, j] = eta * S[i, j] * K[i, j]
            else:
                D[i, j] = eta * K[i, j]

    return D


def spectrum(D: np.ndarray) -> np.ndarray:
    """
    Return real eigen-denominators of the finite self-adjoint toy operator.
    """
    return np.linalg.eigvalsh(D)


def horizon(D: np.ndarray) -> float:
    """
    Return the admissibility-horizon diagnostic:

        lambda_min(D_N).

    The generalized toy-model horizon is lambda_min(D_N) = 0.
    """
    return float(np.min(spectrum(D)))


def localized_branches(D: np.ndarray) -> np.ndarray:
    """
    Boolean mask for branches satisfying lambda_a > 0.
    """
    return spectrum(D) > 0.0


def run_demo() -> None:
    """
    Minimal command-line check.
    """
    n_values = [-5, -3, -1, 1, 2, 4, 7]
    q_values = [1, 1, 2, 1, 2, 2, 3]

    D = build_D(
        n_values,
        q_values,
        gamma=-3.0,
        eta=1.0,
        kind="lorentz",
    )

    print("D_N:")
    print(D)
    print()
    print("eigen-denominators:")
    print(spectrum(D))
    print()
    print("lambda_min:")
    print(horizon(D))


if __name__ == "__main__":
    run_demo()