"""BC-Origin V gauge-ensemble core.

Finite graph Z2 shadow-gauge laboratory for spectral trace cycles.
This module is deliberately finite-dimensional. It is not a physical lattice-QFT
simulator and does not claim continuum confinement.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from math import cosh, exp, tanh
from typing import Dict, Iterable, List, Sequence, Tuple

import numpy as np

Vertex = int
Edge = Tuple[Vertex, Vertex]
Triangle = Tuple[Vertex, Vertex, Vertex]
Cycle = Tuple[Vertex, ...]


def canonical_edge(i: Vertex, j: Vertex) -> Edge:
    if i == j:
        raise ValueError("self-edges are not used in this finite graph lab")
    return (i, j) if i < j else (j, i)


def structural_kernel(n_i: int, n_j: int, normalization: float = 1.0,
                      kind: str = "lorentzian", alpha: float = 0.7,
                      cutoff: int = 1) -> float:
    """Return a structural edge kernel K(n_i,n_j).

    The labels n_i,n_j must be nonzero winding labels. The normalization is
    global and is not a pairwise fitted coupling.
    """
    if n_i == 0 or n_j == 0:
        raise ValueError("BC-Origin winding labels must be nonzero")
    delta = abs(n_i - n_j)
    if kind == "lorentzian":
        return float(normalization / (1.0 + delta * delta))
    if kind == "exponential":
        return float(normalization * np.exp(-alpha * delta))
    if kind == "binary_nearest":
        return float(normalization if delta <= cutoff else 0.0)
    raise ValueError(f"unknown kernel kind: {kind}")


@dataclass(frozen=True)
class FiniteGraph:
    vertices: Tuple[Vertex, ...]
    edges: Tuple[Edge, ...]
    triangles: Tuple[Triangle, ...]
    labels: Tuple[int, ...]

    def edge_index(self) -> Dict[Edge, int]:
        return {e: k for k, e in enumerate(self.edges)}


def single_triangle(labels: Sequence[int] = (1, 2, 4)) -> FiniteGraph:
    vertices = (0, 1, 2)
    edges = tuple(sorted([canonical_edge(0, 1), canonical_edge(1, 2), canonical_edge(0, 2)]))
    triangles = ((0, 1, 2),)
    return FiniteGraph(vertices, edges, triangles, tuple(labels))


def two_triangles_shared_edge(labels: Sequence[int] = (1, 2, 4, 5)) -> FiniteGraph:
    # triangles (0,1,2) and (1,2,3) share edge (1,2)
    vertices = (0, 1, 2, 3)
    raw_edges = [(0, 1), (1, 2), (0, 2), (1, 3), (2, 3)]
    edges = tuple(sorted(canonical_edge(i, j) for i, j in raw_edges))
    triangles = ((0, 1, 2), (1, 2, 3))
    return FiniteGraph(vertices, edges, triangles, tuple(labels))


def triangulated_fan(num_triangles: int = 4, labels: Sequence[int] | None = None) -> FiniteGraph:
    """A small triangulated fan: center 0 connected to a chain boundary.

    Triangles: (0,1,2), (0,2,3), ..., (0,T,T+1).
    Useful for finite graph Wilson-loop diagnostics.
    """
    if num_triangles < 1:
        raise ValueError("num_triangles must be positive")
    vertices = tuple(range(num_triangles + 2))
    raw_edges = []
    for j in range(1, num_triangles + 2):
        raw_edges.append((0, j))
    for j in range(1, num_triangles + 1):
        raw_edges.append((j, j + 1))
    edges = tuple(sorted(set(canonical_edge(i, j) for i, j in raw_edges)))
    triangles = tuple((0, j, j + 1) for j in range(1, num_triangles + 1))
    if labels is None:
        labels = tuple(range(1, num_triangles + 3))
    return FiniteGraph(vertices, edges, triangles, tuple(labels))


def build_kernels(graph: FiniteGraph, normalization: float = 1.0,
                  kind: str = "lorentzian") -> Dict[Edge, float]:
    kernels: Dict[Edge, float] = {}
    for i, j in graph.edges:
        kernels[(i, j)] = structural_kernel(graph.labels[i], graph.labels[j], normalization, kind)
    return kernels


def enumerate_edge_configurations(edges: Sequence[Edge]) -> Iterable[Dict[Edge, int]]:
    """Exact enumeration of all Z2 edge-holonomy configurations."""
    for signs in product((-1, 1), repeat=len(edges)):
        yield {e: int(s) for e, s in zip(edges, signs)}


def build_adjacency(graph: FiniteGraph, kernels: Dict[Edge, float],
                    epsilons: Dict[Edge, int]) -> np.ndarray:
    n = len(graph.vertices)
    A = np.zeros((n, n), dtype=float)
    for e in graph.edges:
        i, j = e
        val = float(epsilons[e]) * float(kernels[e])
        A[i, j] = val
        A[j, i] = val
    return A


def gauge_transform_epsilons(graph: FiniteGraph, epsilons: Dict[Edge, int],
                             vertex_signs: Dict[Vertex, int]) -> Dict[Edge, int]:
    out: Dict[Edge, int] = {}
    for i, j in graph.edges:
        gi = int(vertex_signs[i])
        gj = int(vertex_signs[j])
        out[(i, j)] = gi * int(epsilons[(i, j)]) * gj
    return out


def gauge_matrix(graph: FiniteGraph, vertex_signs: Dict[Vertex, int]) -> np.ndarray:
    return np.diag([int(vertex_signs[i]) for i in graph.vertices])


def check_gauge_covariance(graph: FiniteGraph, kernels: Dict[Edge, float],
                           epsilons: Dict[Edge, int], vertex_signs: Dict[Vertex, int],
                           tol: float = 1e-10) -> Tuple[bool, bool, np.ndarray, np.ndarray]:
    A = build_adjacency(graph, kernels, epsilons)
    eps2 = gauge_transform_epsilons(graph, epsilons, vertex_signs)
    A2 = build_adjacency(graph, kernels, eps2)
    G = gauge_matrix(graph, vertex_signs)
    covariant = np.allclose(A2, G @ A @ G, atol=tol)
    eig1 = np.linalg.eigvalsh(A)
    eig2 = np.linalg.eigvalsh(A2)
    spectrum_invariant = np.allclose(eig1, eig2, atol=tol)
    return covariant, spectrum_invariant, eig1, eig2


def cycle_product(cycle: Cycle, epsilons: Dict[Edge, int]) -> int:
    if len(cycle) < 3:
        raise ValueError("cycle must contain at least three vertices")
    prod_sign = 1
    closed = list(cycle)
    if closed[0] != closed[-1]:
        closed.append(closed[0])
    for i, j in zip(closed[:-1], closed[1:]):
        prod_sign *= int(epsilons[canonical_edge(i, j)])
    return int(prod_sign)


def cycle_kernel_product(cycle: Cycle, kernels: Dict[Edge, float]) -> float:
    prod_kernel = 1.0
    closed = list(cycle)
    if closed[0] != closed[-1]:
        closed.append(closed[0])
    for i, j in zip(closed[:-1], closed[1:]):
        prod_kernel *= float(kernels[canonical_edge(i, j)])
    return float(prod_kernel)


def trace_power(A: np.ndarray, m: int) -> float:
    return float(np.trace(np.linalg.matrix_power(A, m)))


def closed_walk_trace_sum(graph: FiniteGraph, kernels: Dict[Edge, float],
                          epsilons: Dict[Edge, int], m: int) -> float:
    """Explicit closed-walk expansion of Tr(A^m)."""
    n = len(graph.vertices)
    edge_set = set(graph.edges)
    total = 0.0
    for walk in product(range(n), repeat=m):
        closed = walk + (walk[0],)
        term = 1.0
        valid = True
        for i, j in zip(closed[:-1], closed[1:]):
            if i == j or canonical_edge(i, j) not in edge_set:
                valid = False
                break
            e = canonical_edge(i, j)
            term *= float(epsilons[e]) * float(kernels[e])
        if valid:
            total += term
    return float(total)


def triangle_weight(triangle: Triangle, kernels: Dict[Edge, float],
                    epsilons: Dict[Edge, int]) -> float:
    i, j, k = triangle
    omega = cycle_product((i, j, k), epsilons)
    kval = cycle_kernel_product((i, j, k), kernels)
    return float(omega * kval)


def triangle_trace_formula(graph: FiniteGraph, kernels: Dict[Edge, float],
                           epsilons: Dict[Edge, int]) -> float:
    return float(6.0 * sum(triangle_weight(t, kernels, epsilons) for t in graph.triangles))


def trace3_energy(graph: FiniteGraph, kernels: Dict[Edge, float],
                  epsilons: Dict[Edge, int], gamma: float = 1.0) -> float:
    return float(gamma * triangle_trace_formula(graph, kernels, epsilons))


def partition_function_trace3(graph: FiniteGraph, kernels: Dict[Edge, float],
                              gamma: float) -> float:
    total = 0.0
    for eps in enumerate_edge_configurations(graph.edges):
        total += exp(trace3_energy(graph, kernels, eps, gamma))
    return float(total)


def expectation_trace3(graph: FiniteGraph, kernels: Dict[Edge, float], gamma: float,
                       observable) -> float:
    Z = 0.0
    num = 0.0
    for eps in enumerate_edge_configurations(graph.edges):
        w = exp(trace3_energy(graph, kernels, eps, gamma))
        Z += w
        num += float(observable(eps)) * w
    return float(num / Z)


def wilson_expectation(graph: FiniteGraph, kernels: Dict[Edge, float], cycle: Cycle,
                       gamma: float) -> float:
    return expectation_trace3(graph, kernels, gamma, lambda eps: cycle_product(cycle, eps))


def mean_triangle_holonomy(graph: FiniteGraph, kernels: Dict[Edge, float], gamma: float) -> float:
    def obs(eps: Dict[Edge, int]) -> float:
        return float(np.mean([cycle_product(t, eps) for t in graph.triangles]))
    return expectation_trace3(graph, kernels, gamma, obs)


def triangle_susceptibility(graph: FiniteGraph, kernels: Dict[Edge, float], gamma: float) -> float:
    def obs(eps: Dict[Edge, int]) -> float:
        return float(np.mean([cycle_product(t, eps) for t in graph.triangles]))
    mean = expectation_trace3(graph, kernels, gamma, obs)
    mean2 = expectation_trace3(graph, kernels, gamma, lambda eps: obs(eps) ** 2)
    return float(mean2 - mean ** 2)


def analytic_single_triangle_partition(kprod: float, gamma: float) -> float:
    return float(8.0 * cosh(6.0 * gamma * kprod))


def analytic_single_triangle_wilson(kprod: float, gamma: float) -> float:
    return float(tanh(6.0 * gamma * kprod))


def shadow_operator(denominators: Sequence[float], A: np.ndarray, eta: float = 1.0) -> np.ndarray:
    return np.diag(np.asarray(denominators, dtype=float)) + eta * A


def admissibility_fraction(graph: FiniteGraph, kernels: Dict[Edge, float],
                           denominators: Sequence[float], gamma: float, eta: float = 1.0) -> float:
    def obs(eps: Dict[Edge, int]) -> float:
        A = build_adjacency(graph, kernels, eps)
        D = shadow_operator(denominators, A, eta=eta)
        lam_min = float(np.min(np.linalg.eigvalsh(D)))
        return 1.0 if lam_min > 0 else 0.0
    return expectation_trace3(graph, kernels, gamma, obs)


def metropolis_sample(graph: FiniteGraph, kernels: Dict[Edge, float], gamma: float,
                      steps: int = 10000, burn_in: int = 1000, seed: int = 123) -> Dict[str, np.ndarray]:
    """Optional Metropolis sampler for larger finite graphs.

    Exact enumeration is preferred for all small review examples. This sampler is included
    only as a visual exploration tool.
    """
    rng = np.random.default_rng(seed)
    eps = {e: int(rng.choice([-1, 1])) for e in graph.edges}
    energy = trace3_energy(graph, kernels, eps, gamma)
    mean_triangle = []
    for step in range(steps):
        e = graph.edges[int(rng.integers(0, len(graph.edges)))]
        eps_new = dict(eps)
        eps_new[e] *= -1
        energy_new = trace3_energy(graph, kernels, eps_new, gamma)
        dE = energy_new - energy
        if dE >= 0 or rng.random() < np.exp(dE):
            eps = eps_new
            energy = energy_new
        if step >= burn_in:
            mean_triangle.append(np.mean([cycle_product(t, eps) for t in graph.triangles]))
    return {"mean_triangle_holonomy": np.array(mean_triangle, dtype=float)}
