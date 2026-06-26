#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

from bc_origin_vi_projection_core import (
    build_two_triangles, build_triangulated_disk, kernel_dict, default_denominators,
    build_A_epsilon, build_D_epsilon, eigenvalues, lambda_min, gershgorin_margins,
    exact_ensemble_records, projection_failure_probability, weighted_average,
    mcmc_projection_failure_summary, compare_exact_and_mcmc, canonical_edge, face_omega,
    cycle_omega, frustration_density, beta_faces
)


def ensure(out):
    Path(out).mkdir(parents=True, exist_ok=True)


def savefig(out, name):
    path = Path(out)/name
    plt.savefig(path, dpi=220, bbox_inches='tight')
    plt.close()
    print(f"Saved {path}")


def disk_setup():
    c = build_two_triangles()
    kernels = kernel_dict(c, kind='lorentzian', normalization=2.0)
    denominators = default_denominators(c, d0=1.5, spread=0.02)
    return c, kernels, denominators


def fig_pfail_vs_gamma(out):
    c, kernels, denominators = disk_setup()
    gammas = np.linspace(0, 2.4, 31)
    vals = [projection_failure_probability(c, kernels, denominators, gamma=g, eta=1.25, delta=0.0) for g in gammas]
    plt.figure(figsize=(7.2,4.6))
    plt.plot(gammas, vals, marker='o', ms=2.6)
    plt.ylim(-0.03, 1.03)
    plt.title('Projection-failure probability from the BC-Origin V ensemble')
    plt.xlabel(r'trace-weighting parameter $\gamma$')
    plt.ylabel(r'$P_{\rm fail}(\gamma,0)$')
    plt.grid(alpha=0.25)
    savefig(out, 'p_fail_vs_gamma.png')


def fig_frustration_vs_gamma(out):
    c, kernels, denominators = disk_setup()
    gammas = np.linspace(0, 2.4, 31)
    means = []
    for g in gammas:
        rec = exact_ensemble_records(c, kernels, denominators, gamma=g, eta=1.25, delta=0.0)
        means.append(weighted_average(rec, 'frustration_density'))
    plt.figure(figsize=(7.2,4.6))
    plt.plot(gammas, means, marker='o', ms=2.6)
    plt.ylim(-0.03, 1.03)
    plt.title('Measured frustration density is induced by gamma')
    plt.xlabel(r'$\gamma$')
    plt.ylabel(r'$\langle\Phi\rangle_\gamma$')
    plt.grid(alpha=0.25)
    savefig(out, 'frustration_density_vs_gamma.png')


def fig_lambda_min_distributions(out):
    c, kernels, denominators = disk_setup()
    gammas = [0.0, 0.6, 1.2, 2.0]
    plt.figure(figsize=(7.2,4.6))
    bins = np.linspace(-1.6, 2.2, 32)
    for g in gammas:
        rec = exact_ensemble_records(c, kernels, denominators, gamma=g, eta=1.25, delta=0.0)
        vals = np.array([r['lambda_min'] for r in rec])
        weights = np.array([r['weight'] for r in rec])
        hist, edges = np.histogram(vals, bins=bins, weights=weights)
        centers = 0.5*(edges[:-1]+edges[1:])
        plt.plot(centers, hist, label=fr'$\gamma={g:.1f}$')
    plt.axvline(0, linestyle='--', linewidth=1)
    plt.title('Ensemble distribution of the spectral readout margin')
    plt.xlabel(r'$\lambda_{\min}(D_\varepsilon)$')
    plt.ylabel('weighted density')
    plt.legend(fontsize=8)
    plt.grid(alpha=0.25)
    savefig(out, 'lambda_min_distribution_vs_gamma.png')


def fig_frustration_lambda_scatter(out):
    c, kernels, denominators = disk_setup()
    rec = exact_ensemble_records(c, kernels, denominators, gamma=0.8, eta=1.25, delta=0.0)
    xs = [r['frustration_density'] for r in rec]
    ys = [r['lambda_min'] for r in rec]
    ws = [20 + 900*r['weight'] for r in rec]
    plt.figure(figsize=(7.2,4.6))
    plt.scatter(xs, ys, s=ws, alpha=0.45)
    plt.axhline(0, linestyle='--', linewidth=1)
    plt.title('Frustration density versus spectral collapse under ensemble weighting')
    plt.xlabel(r'frustration density $\Phi$')
    plt.ylabel(r'$\lambda_{\min}(D_\varepsilon)$')
    plt.grid(alpha=0.25)
    savefig(out, 'frustration_vs_lambda_min_ensemble.png')


def fig_gershgorin_vs_spectral(out):
    c, kernels, denominators = disk_setup()
    etas = np.linspace(0, 2.4, 40)
    gamma = 0.8
    pfail = []
    gmarg = []
    for eta in etas:
        pfail.append(projection_failure_probability(c, kernels, denominators, gamma=gamma, eta=eta, delta=0.0))
        m = gershgorin_margins(c, denominators, kernels, eta=eta, delta=0.0)
        gmarg.append(min(m.values()))
    plt.figure(figsize=(7.2,4.6))
    plt.plot(etas, pfail, label=r'$P_{\rm fail}$')
    # Scale margin to fit same plot without pretending unit equality.
    gm = np.array(gmarg)
    gm_scaled = (gm - gm.min())/(gm.max()-gm.min()+1e-12)
    plt.plot(etas, gm_scaled, label='scaled minimum Gershgorin margin')
    plt.axhline(0, linestyle='--', linewidth=1)
    plt.title('Gershgorin certificate versus spectral failure statistics')
    plt.xlabel(r'overlap scale $\eta$')
    plt.ylabel('diagnostic value')
    plt.legend(fontsize=8)
    plt.grid(alpha=0.25)
    savefig(out, 'gershgorin_vs_spectral_margin.png')


def fig_wilson_bridge(out):
    c, kernels, denominators = disk_setup()
    boundary = (0,1,3,2)
    gammas = np.linspace(0, 2.4, 31)
    pfs, wloops = [], []
    for g in gammas:
        rec = exact_ensemble_records(c, kernels, denominators, gamma=g, eta=1.25, delta=0.0, boundary_cycle=boundary)
        pfs.append(sum(r['weight'] for r in rec if r['projection_failure']))
        wloops.append(abs(weighted_average(rec, 'boundary_loop')))
    plt.figure(figsize=(7.2,4.6))
    plt.plot(gammas, pfs, label=r'$P_{\rm fail}$')
    plt.plot(gammas, wloops, label=r'$|\langle\Omega_C\rangle_\gamma|$')
    plt.title('Wilson-loop background and projection-failure foreground')
    plt.xlabel(r'$\gamma$')
    plt.ylabel('ensemble observable')
    plt.legend(fontsize=8)
    plt.grid(alpha=0.25)
    savefig(out, 'wilson_loop_vs_projection_failure.png')


def fig_mcmc_trace(out):
    c, kernels, denominators = disk_setup()
    gamma = 0.8
    # Generate a simple trajectory of Phi and lambda_min.
    from bc_origin_vi_projection_core import mcmc_sample_z2_shadow_gauge_ensemble
    samples = mcmc_sample_z2_shadow_gauge_ensemble(c, kernels, gamma=gamma, steps=900, burn_in=100, thinning=4, seed=11)
    phis, lmins = [], []
    for eps in samples:
        A = build_A_epsilon(c, kernels, eps)
        D = build_D_epsilon(denominators, A, eta=1.25, vertices=c.vertices)
        phis.append(frustration_density(c.faces, eps))
        lmins.append(lambda_min(D))
    xs = np.arange(len(samples))
    plt.figure(figsize=(7.2,4.6))
    plt.plot(xs, phis, label=r'$\Phi$')
    # normalize lambda for overlay
    lm = np.array(lmins)
    lm_scaled = (lm-lm.min())/(lm.max()-lm.min()+1e-12)
    plt.plot(xs, lm_scaled, label='scaled lambda_min')
    plt.title('MCMC trace diagnostics from the BC-Origin V ensemble')
    plt.xlabel('thinned sample index')
    plt.ylabel('diagnostic value')
    plt.legend(fontsize=8)
    plt.grid(alpha=0.25)
    savefig(out, 'mcmc_trace_diagnostics.png')


def fig_exact_mcmc(out):
    c = build_two_triangles()
    kernels = kernel_dict(c, kind='lorentzian', normalization=2.4)
    denominators = default_denominators(c, d0=1.25)
    gammas = np.linspace(0, 2.0, 10)
    ex, mc = [], []
    for idx,g in enumerate(gammas):
        cmp = compare_exact_and_mcmc(c, kernels, denominators, gamma=g, eta=1.2, delta=0.0, seed=100+idx)
        ex.append(cmp['P_fail_exact']); mc.append(cmp['P_fail_mcmc'])
    plt.figure(figsize=(7.2,4.6))
    plt.plot(gammas, ex, label='exact enumeration', marker='o', ms=3)
    plt.plot(gammas, mc, label='MCMC estimate', marker='x', ms=4)
    plt.title('Exact versus MCMC validation on a small complex')
    plt.xlabel(r'$\gamma$')
    plt.ylabel(r'$P_{\rm fail}$')
    plt.legend(fontsize=8)
    plt.grid(alpha=0.25)
    savefig(out, 'exact_vs_mcmc_validation.png')



def fig_scalar_diagonal_boundary(out):
    c, kernels, denominators = disk_setup()
    # Use the highest-weight family of A spectra at gamma=0 as a representative finite sample.
    rec = exact_ensemble_records(c, kernels, denominators, gamma=0.0, eta=1.0, delta=0.0)
    lambda_A_min = []
    for r in rec:
        A = build_A_epsilon(c, kernels, r['eps'])
        lambda_A_min.append(lambda_min(A))
    lam_star = min(lambda_A_min)
    etas = np.linspace(0, 2.4, 80)
    d0_boundary = -etas * lam_star
    plt.figure(figsize=(7.2,4.6))
    plt.plot(etas, d0_boundary, label=r'exact boundary $d_0+\eta\lambda_{\min}(A)=0$')
    plt.fill_between(etas, 0, d0_boundary, alpha=0.18, label='projection-failure side')
    plt.title('Scalar-diagonal exact-collapse boundary')
    plt.xlabel(r'overlap scale $\eta$')
    plt.ylabel(r'critical diagonal strength $d_0$')
    plt.legend(fontsize=8)
    plt.grid(alpha=0.25)
    savefig(out, 'scalar_diagonal_collapse_boundary.png')


def fig_hidden_graph(out):
    c = build_triangulated_disk()
    kernels = kernel_dict(c, kind='lorentzian', normalization=2.0)
    denominators = default_denominators(c, d0=1.35, spread=0.02)
    coords = {0:(0,0)}
    for k in range(1,7):
        ang = 2*np.pi*(k-1)/6
        coords[k] = (np.cos(ang), np.sin(ang))
    rec = exact_ensemble_records(c, kernels, denominators, gamma=0.8, eta=1.25, delta=0.0)
    # choose highest-weight failing state if exists, else highest-weight state
    fail = [r for r in rec if r['projection_failure']]
    chosen = max(fail or rec, key=lambda r:r['weight'])
    eps = chosen['eps']
    plt.figure(figsize=(6.2,6.2))
    for f in c.faces:
        pts = np.array([coords[v] for v in f] + [coords[f[0]]])
        omega = face_omega(f, eps)
        alpha = 0.16 if omega > 0 else 0.42
        plt.fill(pts[:,0], pts[:,1], alpha=alpha)
    for i,j in c.edges:
        x = [coords[i][0], coords[j][0]]; y = [coords[i][1], coords[j][1]]
        sign = eps[canonical_edge(i,j)]
        plt.plot(x, y, linewidth=2.4 if sign > 0 else 1.1, linestyle='-' if sign > 0 else '--')
    for v,(x,y) in coords.items():
        plt.scatter([x],[y], s=140, zorder=3)
        plt.text(x, y, str(v), ha='center', va='center', color='white', weight='bold')
    status = 'projection failure' if chosen['projection_failure'] else 'admissible'
    plt.title(f'Hidden two-complex sampled from Z(gamma): {status}')
    plt.axis('equal'); plt.axis('off')
    savefig(out, 'hidden_graph_projection_failure_lab.png')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', default='figures')
    args = parser.parse_args()
    ensure(args.out)
    fig_pfail_vs_gamma(args.out)
    fig_frustration_vs_gamma(args.out)
    fig_lambda_min_distributions(args.out)
    fig_frustration_lambda_scatter(args.out)
    fig_gershgorin_vs_spectral(args.out)
    fig_wilson_bridge(args.out)
    fig_mcmc_trace(args.out)
    fig_exact_mcmc(args.out)
    fig_scalar_diagonal_boundary(args.out)
    fig_hidden_graph(args.out)

if __name__ == '__main__':
    main()
