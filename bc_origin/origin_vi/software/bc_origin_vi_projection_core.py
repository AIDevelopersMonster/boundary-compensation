#!/usr/bin/env python3
"""
BC-Origin VI projection-failure core, v0.1.2.

This module samples Z2 edge-holonomy configurations from the finite
BC-Origin V shadow-gauge ensemble and computes spectral readout diagnostics
for D_epsilon = Delta + eta A_epsilon.

It deliberately does not use an external frustration_ratio as the main source
of sign disorder. Frustration is measured after sampling from Z(gamma).
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from typing import Dict, Iterable, List, Tuple, Any, Optional
import math
import random
import numpy as np

Edge = Tuple[int, int]
Face = Tuple[int, int, int]
Cycle = Tuple[int, ...]


def canonical_edge(i: int, j: int) -> Edge:
    if i == j:
        raise ValueError("self-edges are not used in this finite two-complex")
    return (i, j) if i < j else (j, i)


@dataclass(frozen=True)
class StructuralTwoComplex:
    vertices: Tuple[int, ...]
    edges: Tuple[Edge, ...]
    faces: Tuple[Face, ...]
    labels: Dict[int, int]

    def __post_init__(self):
        for v in self.vertices:
            if v not in self.labels:
                raise ValueError(f"missing winding label for vertex {v}")
            if self.labels[v] == 0:
                raise ValueError("BC-Origin winding labels must be nonzero")
        edge_set = set(self.edges)
        for f in self.faces:
            a, b, c = f
            for e in [canonical_edge(a, b), canonical_edge(b, c), canonical_edge(c, a)]:
                if e not in edge_set:
                    raise ValueError(f"face {f} uses missing edge {e}")


def build_single_triangle(labels: Optional[Dict[int, int]] = None) -> StructuralTwoComplex:
    labels = labels or {0: 1, 1: 2, 2: 4}
    vertices = (0, 1, 2)
    edges = tuple(canonical_edge(i, j) for i, j in [(0, 1), (1, 2), (0, 2)])
    faces = ((0, 1, 2),)
    return StructuralTwoComplex(vertices, edges, faces, labels)


def build_two_triangles(labels: Optional[Dict[int, int]] = None) -> StructuralTwoComplex:
    labels = labels or {0: 1, 1: 2, 2: 4, 3: 5}
    vertices = (0, 1, 2, 3)
    raw_edges = [(0, 1), (1, 2), (0, 2), (1, 3), (2, 3)]
    edges = tuple(canonical_edge(i, j) for i, j in raw_edges)
    faces = ((0, 1, 2), (1, 3, 2))
    return StructuralTwoComplex(vertices, edges, faces, labels)


def build_triangulated_disk(labels: Optional[Dict[int, int]] = None) -> StructuralTwoComplex:
    labels = labels or {0: 1, 1: 2, 2: 3, 3: 5, 4: 7, 5: 8, 6: 11}
    vertices = tuple(range(7))
    raw_edges = []
    for i in range(1, 7):
        j = i + 1 if i < 6 else 1
        raw_edges.append((i, j))
        raw_edges.append((0, i))
    edges = tuple(sorted(set(canonical_edge(i, j) for i, j in raw_edges)))
    faces = tuple((0, i, i + 1 if i < 6 else 1) for i in range(1, 7))
    return StructuralTwoComplex(vertices, edges, faces, labels)


def structural_kernel(n_i: int, n_j: int, kind: str = "lorentzian", normalization: float = 1.0,
                      alpha: float = 0.7, cutoff: int = 2) -> float:
    if n_i == 0 or n_j == 0:
        raise ValueError("BC-Origin winding labels must be nonzero")
    d = abs(n_i - n_j)
    if kind == "lorentzian":
        return normalization / (1.0 + d * d)
    if kind == "exponential":
        return normalization * math.exp(-alpha * d)
    if kind == "uniform":
        return normalization
    if kind == "nearest":
        return normalization if d <= cutoff else 0.0
    raise ValueError(f"unknown kernel kind: {kind}")


def kernel_dict(complex_: StructuralTwoComplex, kind: str = "lorentzian", normalization: float = 1.0,
                **kwargs) -> Dict[Edge, float]:
    return {
        e: structural_kernel(complex_.labels[e[0]], complex_.labels[e[1]], kind=kind,
                             normalization=normalization, **kwargs)
        for e in complex_.edges
    }


def default_denominators(complex_: StructuralTwoComplex, d0: float = 1.0, spread: float = 0.0) -> Dict[int, float]:
    return {v: d0 + spread * k for k, v in enumerate(complex_.vertices)}


def enumerate_edge_configurations(edges: Iterable[Edge]) -> Iterable[Dict[Edge, int]]:
    edges = tuple(edges)
    for signs in product([-1, 1], repeat=len(edges)):
        yield dict(zip(edges, signs))


def face_omega(face: Face, eps: Dict[Edge, int]) -> int:
    a, b, c = face
    return eps[canonical_edge(a, b)] * eps[canonical_edge(b, c)] * eps[canonical_edge(c, a)]


def cycle_omega(cycle: Cycle, eps: Dict[Edge, int]) -> int:
    prod = 1
    for a, b in zip(cycle, cycle[1:] + cycle[:1]):
        prod *= eps[canonical_edge(a, b)]
    return prod


def frustration_density(faces: Iterable[Face], eps: Dict[Edge, int]) -> float:
    faces = tuple(faces)
    if not faces:
        return 0.0
    avg = sum(face_omega(f, eps) for f in faces) / len(faces)
    return 0.5 * (1.0 - avg)  # normalized to [0, 1]


def beta_faces(complex_: StructuralTwoComplex, kernels: Dict[Edge, float], gamma: float) -> Dict[Face, float]:
    out: Dict[Face, float] = {}
    for f in complex_.faces:
        a, b, c = f
        prod_k = kernels[canonical_edge(a, b)] * kernels[canonical_edge(b, c)] * kernels[canonical_edge(c, a)]
        out[f] = 6.0 * gamma * prod_k
    return out


def log_weight(faces: Iterable[Face], eps: Dict[Edge, int], beta: Dict[Face, float]) -> float:
    return float(sum(beta[f] * face_omega(f, eps) for f in faces))


def build_faces_by_edge(faces: Iterable[Face]) -> Dict[Edge, List[Face]]:
    out: Dict[Edge, List[Face]] = {}
    for f in faces:
        a, b, c = f
        for e in [canonical_edge(a, b), canonical_edge(b, c), canonical_edge(c, a)]:
            out.setdefault(e, []).append(f)
    return out


def edge_flip_delta_log_weight(edge: Edge, faces_by_edge: Dict[Edge, List[Face]], eps: Dict[Edge, int], beta: Dict[Face, float]) -> float:
    # Flipping one edge flips omega on exactly faces containing the edge.
    delta = 0.0
    for f in faces_by_edge.get(edge, []):
        old = face_omega(f, eps)
        new = -old
        delta += beta[f] * (new - old)
    return float(delta)


def build_A_epsilon(complex_: StructuralTwoComplex, kernels: Dict[Edge, float], eps: Dict[Edge, int]) -> np.ndarray:
    n = len(complex_.vertices)
    index = {v: k for k, v in enumerate(complex_.vertices)}
    A = np.zeros((n, n), dtype=float)
    for e in complex_.edges:
        i, j = e
        val = eps[e] * kernels[e]
        A[index[i], index[j]] = val
        A[index[j], index[i]] = val
    return A


def build_D_epsilon(denominators: Dict[int, float] | List[float] | np.ndarray,
                    A: np.ndarray, eta: float = 1.0, vertices: Optional[Tuple[int, ...]] = None) -> np.ndarray:
    if isinstance(denominators, dict):
        if vertices is None:
            vertices = tuple(sorted(denominators.keys()))
        d = np.array([denominators[v] for v in vertices], dtype=float)
    else:
        d = np.asarray(denominators, dtype=float)
    return np.diag(d) + eta * A


def eigenvalues(M: np.ndarray) -> np.ndarray:
    return np.linalg.eigvalsh(M)


def lambda_min(M: np.ndarray) -> float:
    return float(np.min(eigenvalues(M)))


def spectral_margin(D: np.ndarray, delta: float = 0.0) -> float:
    return float(lambda_min(D) - delta)


def gershgorin_margins(complex_: StructuralTwoComplex, denominators: Dict[int, float] | List[float] | np.ndarray,
                       kernels: Dict[Edge, float], eta: float = 1.0, delta: float = 0.0) -> Dict[int, float]:
    if isinstance(denominators, dict):
        d = {v: float(denominators[v]) for v in complex_.vertices}
    else:
        arr = np.asarray(denominators, dtype=float)
        d = {v: float(arr[k]) for k, v in enumerate(complex_.vertices)}
    sums = {v: 0.0 for v in complex_.vertices}
    for i, j in complex_.edges:
        kval = kernels[(i, j)]
        sums[i] += kval
        sums[j] += kval
    return {v: d[v] - eta * sums[v] - delta for v in complex_.vertices}


def rayleigh_value(D: np.ndarray, x: np.ndarray) -> float:
    x = np.asarray(x, dtype=float)
    denom = float(x @ x)
    if denom == 0:
        raise ValueError("Rayleigh vector must be nonzero")
    return float(x @ D @ x / denom)


def scalar_diagonal_collapse_margin(d0: float, eta: float, A: np.ndarray, delta: float = 0.0) -> float:
    return float(d0 + eta * lambda_min(A) - delta)


def exact_ensemble_records(complex_: StructuralTwoComplex, kernels: Dict[Edge, float], denominators: Dict[int, float] | List[float],
                           gamma: float, eta: float = 1.0, delta: float = 0.0,
                           boundary_cycle: Optional[Cycle] = None) -> List[Dict[str, Any]]:
    beta = beta_faces(complex_, kernels, gamma)
    records: List[Dict[str, Any]] = []
    logs: List[float] = []
    for eps in enumerate_edge_configurations(complex_.edges):
        A = build_A_epsilon(complex_, kernels, eps)
        D = build_D_epsilon(denominators, A, eta=eta, vertices=complex_.vertices)
        lm = lambda_min(D)
        lw = log_weight(complex_.faces, eps, beta)
        logs.append(lw)
        rec = {
            "eps": eps,
            "lambda_min": lm,
            "spectral_margin": lm - delta,
            "projection_failure": lm <= delta,
            "frustration_density": frustration_density(complex_.faces, eps),
            "log_weight": lw,
        }
        if boundary_cycle is not None:
            rec["boundary_loop"] = cycle_omega(boundary_cycle, eps)
        records.append(rec)
    maxlog = max(logs) if logs else 0.0
    weights = [math.exp(r["log_weight"] - maxlog) for r in records]
    z = sum(weights)
    for r, w in zip(records, weights):
        r["weight"] = w / z if z else 0.0
    return records


def weighted_average(records: List[Dict[str, Any]], key: str) -> float:
    return float(sum(r["weight"] * r[key] for r in records))


def weighted_probability(records: List[Dict[str, Any]], key: str) -> float:
    return float(sum(r["weight"] for r in records if r[key]))


def projection_failure_probability(complex_: StructuralTwoComplex, kernels: Dict[Edge, float], denominators: Dict[int, float] | List[float],
                                   gamma: float, eta: float = 1.0, delta: float = 0.0) -> float:
    rec = exact_ensemble_records(complex_, kernels, denominators, gamma, eta=eta, delta=delta)
    return weighted_probability(rec, "projection_failure")


def mcmc_sample_z2_shadow_gauge_ensemble(complex_: StructuralTwoComplex, kernels: Dict[Edge, float], gamma: float,
                                         steps: int = 10000, burn_in: int = 1000, thinning: int = 10,
                                         seed: int = 7, start: str = "random") -> List[Dict[Edge, int]]:
    rng = random.Random(seed)
    edges = tuple(complex_.edges)
    if start == "all_positive":
        eps = {e: 1 for e in edges}
    elif start == "all_negative":
        eps = {e: -1 for e in edges}
    else:
        eps = {e: rng.choice([-1, 1]) for e in edges}
    beta = beta_faces(complex_, kernels, gamma)
    faces_by_edge = build_faces_by_edge(complex_.faces)
    samples: List[Dict[Edge, int]] = []
    for t in range(steps):
        e = rng.choice(edges)
        delta_lw = edge_flip_delta_log_weight(e, faces_by_edge, eps, beta)
        if delta_lw >= 0 or rng.random() < math.exp(delta_lw):
            eps = dict(eps)
            eps[e] *= -1
        if t >= burn_in and ((t - burn_in) % max(1, thinning) == 0):
            samples.append(dict(eps))
    return samples


def mcmc_projection_failure_summary(complex_: StructuralTwoComplex, kernels: Dict[Edge, float], denominators: Dict[int, float] | List[float],
                                    gamma: float, eta: float = 1.0, delta: float = 0.0,
                                    steps: int = 10000, burn_in: int = 1000, thinning: int = 10, seed: int = 7) -> Dict[str, float]:
    samples = mcmc_sample_z2_shadow_gauge_ensemble(complex_, kernels, gamma, steps, burn_in, thinning, seed)
    fails = 0
    phis = []
    lmins = []
    for eps in samples:
        A = build_A_epsilon(complex_, kernels, eps)
        D = build_D_epsilon(denominators, A, eta=eta, vertices=complex_.vertices)
        lm = lambda_min(D)
        fails += int(lm <= delta)
        phis.append(frustration_density(complex_.faces, eps))
        lmins.append(lm)
    n = max(1, len(samples))
    return {
        "samples": float(n),
        "P_fail_mcmc": fails / n,
        "mean_frustration": float(np.mean(phis)) if phis else 0.0,
        "mean_lambda_min": float(np.mean(lmins)) if lmins else 0.0,
    }


def compare_exact_and_mcmc(complex_: StructuralTwoComplex, kernels: Dict[Edge, float], denominators: Dict[int, float] | List[float],
                           gamma: float, eta: float = 1.0, delta: float = 0.0, seed: int = 7) -> Dict[str, float]:
    exact = projection_failure_probability(complex_, kernels, denominators, gamma, eta=eta, delta=delta)
    mcmc = mcmc_projection_failure_summary(complex_, kernels, denominators, gamma, eta=eta, delta=delta, seed=seed)
    return {
        "P_fail_exact": exact,
        "P_fail_mcmc": mcmc["P_fail_mcmc"],
        "abs_error": abs(exact - mcmc["P_fail_mcmc"]),
        "samples": mcmc["samples"],
    }


if __name__ == "__main__":
    c = build_triangulated_disk()
    kernels = kernel_dict(c, kind="lorentzian", normalization=2.0)
    denominators = default_denominators(c, d0=1.35)
    for gamma in [0.0, 0.5, 1.0, 1.5]:
        p = projection_failure_probability(c, kernels, denominators, gamma=gamma, eta=1.2, delta=0.0)
        print(f"gamma={gamma:.2f} P_fail={p:.4f}")
