from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from bc_origin_v_gauge_ensemble_core import (
    analytic_single_triangle_partition,
    analytic_single_triangle_wilson,
    build_adjacency,
    build_kernels,
    check_gauge_covariance,
    cycle_kernel_product,
    cycle_product,
    mean_triangle_holonomy,
    partition_function_trace3,
    shadow_operator,
    single_triangle,
    two_triangles_shared_edge,
    triangulated_fan,
    trace_power,
    triangle_susceptibility,
    triangle_trace_formula,
    wilson_expectation,
    admissibility_fraction,
    enumerate_edge_configurations,
    metropolis_sample,
)


def ensure(out: Path) -> None:
    out.mkdir(parents=True, exist_ok=True)


def savefig(path: Path) -> None:
    plt.savefig(path, dpi=220, bbox_inches="tight")
    plt.close()
    print(f"saved {path}")


def figure_trace_cycle_identity(out: Path) -> None:
    graph = single_triangle((1, 2, 4))
    kernels = build_kernels(graph, normalization=2.0)
    eps = {e: 1 for e in graph.edges}
    eps[(0, 2)] = -1
    A = build_adjacency(graph, kernels, eps)
    tr3 = trace_power(A, 3)
    formula = triangle_trace_formula(graph, kernels, eps)
    omega = cycle_product((0, 1, 2), eps)
    kprod = cycle_kernel_product((0, 1, 2), kernels)
    labels = [r"$Tr(A_\varepsilon^3)$", r"$6\Omega_\triangle K_{12}K_{23}K_{31}$"]
    values = [tr3, formula]
    plt.figure(figsize=(7, 4.5))
    plt.bar(labels, values)
    plt.axhline(0, linewidth=0.8)
    plt.ylabel("value")
    plt.title("Triangle trace-cycle identity")
    plt.text(0.02, 0.92, rf"$\Omega_\triangle={omega}$, $K_\triangle={kprod:.4f}$", transform=plt.gca().transAxes)
    savefig(out / "trace_cycle_triangle_identity.png")


def figure_gauge_orbit_spectrum(out: Path) -> None:
    graph = two_triangles_shared_edge((1, 2, 4, 5))
    kernels = build_kernels(graph, normalization=1.6)
    eps = {e: 1 for e in graph.edges}
    eps[(0, 2)] = -1
    eps[(1, 3)] = -1
    signs = {0: 1, 1: -1, 2: 1, 3: -1}
    cov, inv, eig1, eig2 = check_gauge_covariance(graph, kernels, eps, signs)
    x = np.arange(len(eig1))
    plt.figure(figsize=(7, 4.5))
    plt.plot(x, eig1, "o-", label="original")
    plt.plot(x, eig2, "s--", label="vertex-gauge transformed")
    plt.xlabel("eigenvalue index")
    plt.ylabel("eigenvalue")
    plt.title("Gauge orbit spectrum invariance")
    plt.text(0.03, 0.92, f"covariant={cov}, spectrum invariant={inv}", transform=plt.gca().transAxes)
    plt.grid(alpha=0.25)
    plt.legend()
    savefig(out / "gauge_orbit_spectrum_invariance.png")


def figure_single_triangle_partition(out: Path) -> None:
    graph = single_triangle((1, 2, 4))
    kernels = build_kernels(graph, normalization=1.5)
    kprod = cycle_kernel_product((0, 1, 2), kernels)
    gammas = np.linspace(0, 4.0, 120)
    exact = np.array([partition_function_trace3(graph, kernels, g) for g in gammas])
    analytic = np.array([analytic_single_triangle_partition(kprod, g) for g in gammas])
    wilson = np.array([wilson_expectation(graph, kernels, (0, 1, 2), g) for g in gammas])
    wilson_analytic = np.array([analytic_single_triangle_wilson(kprod, g) for g in gammas])
    plt.figure(figsize=(7.5, 5))
    plt.plot(gammas, exact, label="exact enumeration Z")
    plt.plot(gammas, analytic, "--", label=r"$8\cosh(6\gamma K_\triangle)$")
    plt.xlabel(r"trace-weight parameter $\gamma$")
    plt.ylabel("partition function")
    plt.title("Single triangle partition function")
    plt.grid(alpha=0.25)
    plt.legend()
    savefig(out / "single_triangle_exact_partition.png")

    plt.figure(figsize=(7.5, 5))
    plt.plot(gammas, wilson, label="exact enumeration")
    plt.plot(gammas, wilson_analytic, "--", label=r"$\tanh(6\gamma K_\triangle)$")
    plt.xlabel(r"trace-weight parameter $\gamma$")
    plt.ylabel(r"$\langle\Omega_\triangle\rangle_\gamma$")
    plt.title("Single triangle Wilson-cycle expectation")
    plt.ylim(-0.05, 1.05)
    plt.grid(alpha=0.25)
    plt.legend()
    savefig(out / "single_triangle_wilson_expectation.png")


def figure_two_triangle_correlation(out: Path) -> None:
    graph = two_triangles_shared_edge((1, 2, 4, 5))
    kernels = build_kernels(graph, normalization=1.6)
    gammas = np.linspace(0, 5.0, 130)
    w1 = np.array([wilson_expectation(graph, kernels, graph.triangles[0], g) for g in gammas])
    w2 = np.array([wilson_expectation(graph, kernels, graph.triangles[1], g) for g in gammas])
    mean = np.array([mean_triangle_holonomy(graph, kernels, g) for g in gammas])
    sus = np.array([triangle_susceptibility(graph, kernels, g) for g in gammas])
    plt.figure(figsize=(7.5, 5))
    plt.plot(gammas, w1, label=r"$\langle\Omega_{012}\rangle$")
    plt.plot(gammas, w2, label=r"$\langle\Omega_{123}\rangle$")
    plt.plot(gammas, mean, "--", label="mean triangle holonomy")
    plt.xlabel(r"trace-weight parameter $\gamma$")
    plt.ylabel("expectation")
    plt.title("Two triangles sharing one edge")
    plt.ylim(-0.05, 1.05)
    plt.grid(alpha=0.25)
    plt.legend()
    savefig(out / "two_triangle_shared_edge_expectations.png")

    plt.figure(figsize=(7.5, 5))
    plt.plot(gammas, 1 - mean, label=r"frustration density $1-\langle\Omega_\triangle\rangle$")
    plt.plot(gammas, sus, label="finite-graph susceptibility")
    plt.xlabel(r"trace-weight parameter $\gamma$")
    plt.ylabel("diagnostic")
    plt.title("Finite-graph crossover diagnostics")
    plt.grid(alpha=0.25)
    plt.legend()
    savefig(out / "plaquette_energy_and_susceptibility.png")


def figure_structural_weight_landscape(out: Path) -> None:
    graph = triangulated_fan(5, labels=(1, 2, 4, 5, 8, 9, 13))
    kernels = build_kernels(graph, normalization=2.5)
    weights = [6.0 * cycle_kernel_product(t, kernels) for t in graph.triangles]
    plt.figure(figsize=(8, 4.5))
    plt.bar([str(t) for t in graph.triangles], weights)
    plt.ylabel(r"structural triangle factor $6K_{ij}K_{jk}K_{ki}$")
    plt.title("Inhomogeneous structural Wilson-like weights")
    plt.xticks(rotation=30, ha="right")
    plt.grid(axis="y", alpha=0.25)
    savefig(out / "deterministic_inhomogeneous_bond_weights.png")


def figure_wilson_area_diagnostic(out: Path) -> None:
    graph = triangulated_fan(4, labels=(1, 2, 3, 5, 8, 13))
    kernels = build_kernels(graph, normalization=1.4)
    gamma = 3.0
    # Boundary loops enclosing 1..4 fan triangles: (0,1,2), (0,1,2,3), etc.
    areas = []
    vals = []
    for a in range(1, 5):
        loop = tuple([0] + list(range(1, a + 2)))
        # This loop has edges (0,1), boundary chain, (a+1,0)
        areas.append(a)
        vals.append(abs(wilson_expectation(graph, kernels, loop, gamma)))
    vals = np.maximum(np.array(vals), 1e-12)
    plt.figure(figsize=(7.5, 5))
    plt.plot(areas, -np.log(vals), "o-", label=rf"$-\log|\langle\Omega_C\rangle|$, $\gamma={gamma}$")
    plt.xlabel("finite enclosed triangle count")
    plt.ylabel("diagnostic")
    plt.title("Finite graph Wilson-loop area diagnostic")
    plt.grid(alpha=0.25)
    plt.legend()
    savefig(out / "finite_graph_area_law_diagnostic.png")


def figure_shadow_admissibility(out: Path) -> None:
    graph = two_triangles_shared_edge((1, 2, 4, 5))
    kernels = build_kernels(graph, normalization=1.8)
    denominators = [1.2, 1.1, 1.0, 1.3]
    gammas = np.linspace(0, 5.0, 100)
    pvals = np.array([admissibility_fraction(graph, kernels, denominators, g, eta=1.0) for g in gammas])
    plt.figure(figsize=(7.5, 5))
    plt.plot(gammas, pvals, lw=2)
    plt.xlabel(r"trace-weight parameter $\gamma$")
    plt.ylabel(r"$P_{adm}(\gamma)$")
    plt.title("Shadow admissibility fraction over holonomy ensemble")
    plt.ylim(-0.05, 1.05)
    plt.grid(alpha=0.25)
    savefig(out / "shadow_admissibility_fraction.png")


def figure_mcmc_trace(out: Path) -> None:
    graph = triangulated_fan(8)
    kernels = build_kernels(graph, normalization=1.5)
    samples = metropolis_sample(graph, kernels, gamma=2.5, steps=3000, burn_in=200, seed=42)["mean_triangle_holonomy"]
    plt.figure(figsize=(7.5, 4.5))
    plt.plot(samples, alpha=0.8)
    plt.xlabel("recorded MCMC step")
    plt.ylabel("mean triangle holonomy")
    plt.title("Optional MCMC exploration trace (finite graph only)")
    plt.grid(alpha=0.25)
    savefig(out / "mcmc_thermalization_trace.png")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="origin_v/figures")
    args = parser.parse_args()
    out = Path(args.out)
    ensure(out)
    figure_trace_cycle_identity(out)
    figure_gauge_orbit_spectrum(out)
    figure_single_triangle_partition(out)
    figure_two_triangle_correlation(out)
    figure_structural_weight_landscape(out)
    figure_wilson_area_diagnostic(out)
    figure_shadow_admissibility(out)
    figure_mcmc_trace(out)


if __name__ == "__main__":
    main()
