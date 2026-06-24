"""
BC-Origin III holonomy core

Boundary Compensation Origin III:
Non-Factorizable Holonomy and Frustrated Multi-Shadow Spectral Geometry

This module implements the finite-dimensional toy-model core used by
``generate_bc_origin_iii_figures.py``.

It is not a physics simulator. It is a reproducible computational scaffold for
checking the graph-holonomy and spectral examples used in the BC-Origin III
manuscript.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Sequence

import numpy as np


@dataclass(frozen=True)
class Edge:
    """Undirected edge with a Z2 holonomy sign epsilon = +/-1."""

    i: int
    j: int
    epsilon: int = 1

    def normalized(self) -> "Edge":
        if self.i == self.j:
            raise ValueError("Self-edges are not used in the minimal BC-Origin III graph model.")
        if self.epsilon not in (-1, 1):
            raise ValueError("Edge holonomy epsilon must be +1 or -1.")
        return self if self.i < self.j else Edge(self.j, self.i, self.epsilon)


def sign(x: float) -> int:
    """Return sign(x) in {-1, 0, +1}."""
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0


def structural_kernel(n_i: int, n_j: int, kind: str = "lorentzian", alpha: float = 0.5) -> float:
    """
    Declared index-space structural kernel K(n_i,n_j).

    The lorentzian kernel here is an index-space kernel, not a Fourier matrix
    element of (1-Delta_S1)^(-1) between pure Fourier modes.
    """
    m = abs(int(n_i) - int(n_j))
    if kind == "lorentzian":
        return 1.0 / (1.0 + m * m)
    if kind == "exponential":
        return float(np.exp(-alpha * m))
    raise ValueError(f"Unknown kernel kind: {kind}")


def kernel_matrix(n_values: Sequence[int], kind: str = "lorentzian", alpha: float = 0.5) -> np.ndarray:
    """Build K_ij for hidden winding labels."""
    n = list(n_values)
    if any(v == 0 for v in n):
        raise ValueError("BC-Origin winding labels must be nonzero.")
    N = len(n)
    K = np.zeros((N, N), dtype=float)
    for i in range(N):
        for j in range(N):
            K[i, j] = structural_kernel(n[i], n[j], kind=kind, alpha=alpha)
    return K


def baseline_vertex_signs(n_values: Sequence[int]) -> np.ndarray:
    """Return sigma_i = sign(n_i)."""
    sig = np.asarray([sign(v) for v in n_values], dtype=int)
    if np.any(sig == 0):
        raise ValueError("BC-Origin winding labels must be nonzero.")
    return sig


def epsilon_matrix(num_vertices: int, edges: Iterable[Edge]) -> np.ndarray:
    """Build symmetric Z2 edge-holonomy matrix E with diagonal zero."""
    E = np.zeros((num_vertices, num_vertices), dtype=int)
    for edge in edges:
        e = edge.normalized()
        if e.i < 0 or e.j >= num_vertices:
            raise ValueError("Edge index outside graph.")
        E[e.i, e.j] = e.epsilon
        E[e.j, e.i] = e.epsilon
    return E


def complete_epsilon(num_vertices: int, default: int = 1, negative_edges: Iterable[tuple[int, int]] = ()) -> np.ndarray:
    """Convenience constructor for complete graph edge signs."""
    if default not in (-1, 1):
        raise ValueError("default must be +1 or -1")
    E = np.zeros((num_vertices, num_vertices), dtype=int)
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            E[i, j] = E[j, i] = default
    for i, j in negative_edges:
        if i == j:
            raise ValueError("No self-edges.")
        E[i, j] = E[j, i] = -1
    return E


def chi_matrix(n_values: Sequence[int], epsilon: np.ndarray) -> np.ndarray:
    """
    Full signed edge field chi_ij = sigma_i * epsilon_ij * sigma_j.

    Diagonal is zero because chi is only used for edges in the baseline
    off-diagonal holonomy model.
    """
    sigma = baseline_vertex_signs(n_values)
    E = np.asarray(epsilon, dtype=int)
    if E.shape != (len(n_values), len(n_values)):
        raise ValueError("epsilon matrix shape mismatch")
    return (sigma[:, None] * E * sigma[None, :]).astype(int)


def cycle_product(epsilon: np.ndarray, cycle: Sequence[int]) -> int:
    """Compute Z2 cycle product along a closed vertex list."""
    if len(cycle) < 3:
        raise ValueError("Cycle must have at least three vertices.")
    E = np.asarray(epsilon, dtype=int)
    prod = 1
    for a, b in zip(cycle, list(cycle[1:]) + [cycle[0]]):
        if E[a, b] == 0:
            raise ValueError("Cycle uses a missing edge.")
        prod *= int(E[a, b])
    return int(prod)


def triangle_cycle_products(epsilon: np.ndarray) -> dict[tuple[int, int, int], int]:
    """Return all triangle products for a graph represented by epsilon matrix."""
    E = np.asarray(epsilon, dtype=int)
    N = E.shape[0]
    out: dict[tuple[int, int, int], int] = {}
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                if E[i, j] != 0 and E[j, k] != 0 and E[i, k] != 0:
                    out[(i, j, k)] = int(E[i, j] * E[j, k] * E[i, k])
    return out


def is_triangle_balanced(epsilon: np.ndarray) -> bool:
    """Check all triangle products where triangles exist."""
    return all(v == 1 for v in triangle_cycle_products(epsilon).values())


def build_holonomy_operator(
    n_values: Sequence[int],
    d_values: Sequence[float] | None = None,
    epsilon: np.ndarray | None = None,
    eta: float = 1.0,
    kernel_kind: str = "lorentzian",
    alpha: float = 0.5,
) -> np.ndarray:
    """
    Build the gauge-clean holonomy-weighted off-diagonal toy operator.

        D_ii = d_i
        D_ij = eta * chi_ij * K_ij, i != j

    This is the preferred BC-Origin III baseline for spectral statements because
    vertex sign changes act by orthogonal conjugation and do not change spectra.
    """
    n = list(n_values)
    N = len(n)
    if d_values is None:
        d = np.asarray([2.0 * np.pi * abs(v) - np.pi for v in n], dtype=float)
    else:
        d = np.asarray(d_values, dtype=float)
        if len(d) != N:
            raise ValueError("d_values length mismatch")
    K = kernel_matrix(n, kind=kernel_kind, alpha=alpha)
    E = complete_epsilon(N) if epsilon is None else np.asarray(epsilon, dtype=int)
    C = chi_matrix(n, E)
    D = np.zeros((N, N), dtype=float)
    np.fill_diagonal(D, d)
    for i in range(N):
        for j in range(N):
            if i != j and E[i, j] != 0:
                D[i, j] = eta * C[i, j] * K[i, j]
    return D


def spectrum(D: np.ndarray) -> np.ndarray:
    """Return sorted eigenvalues for a real symmetric operator."""
    return np.linalg.eigvalsh(np.asarray(D, dtype=float))


def triangle_spectra(d: float = 5.0, eta_k: float = 1.0) -> dict[str, np.ndarray]:
    """Closed-form minimal triangle spectra for balanced and frustrated signs."""
    return {
        "balanced": np.asarray([d - eta_k, d - eta_k, d + 2.0 * eta_k]),
        "frustrated": np.asarray([d - 2.0 * eta_k, d + eta_k, d + eta_k]),
    }


def horizon_status(eigenvalues: Sequence[float]) -> str:
    """Toy-model admissibility status based on lambda_min."""
    return "LOCALIZED" if min(eigenvalues) > 0 else "HORIZON_CROSSED"
