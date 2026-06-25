#!/usr/bin/env python3
"""Generate BC-Origin IV lifted phase-flow figures, v0.1.1 software patch."""

from __future__ import annotations

import argparse
from pathlib import Path
import math
import numpy as np
import matplotlib.pyplot as plt

from bc_origin_iv_phase_flow_core import (
    TAU,
    PhaseFlowBranch,
    build_two_shadow_operator,
    two_shadow_eigenvalues,
    two_shadow_gap,
    two_shadow_invariants,
    horizon_value,
    find_zero_crossings_linear,
    lifted_phase_reindex_denominator,
    build_multi_shadow_operator,
    scan_spectrum,
)


def save_avoided_crossing_phase_flow(out: Path) -> None:
    lam_grid = np.linspace(0.0, 1.0, 401)
    b1 = PhaseFlowBranch(n_abs=2, theta0=0.0, phase_lift_coefficient=TAU)
    b2 = PhaseFlowBranch(n_abs=1, theta0=-0.8 * math.pi, phase_lift_coefficient=0.30 * TAU)
    structural_overlap = 0.8
    eigs = np.asarray([two_shadow_eigenvalues(b1, b2, lam, structural_overlap) for lam in lam_grid])
    uncoupled1 = np.asarray([b1.denominator(lam) for lam in lam_grid])
    uncoupled2 = np.asarray([b2.denominator(lam) for lam in lam_grid])

    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    ax.plot(lam_grid, uncoupled1, linestyle="--", linewidth=1, label="uncoupled d1")
    ax.plot(lam_grid, uncoupled2, linestyle="--", linewidth=1, label="uncoupled d2")
    ax.plot(lam_grid, eigs[:, 0], linewidth=2, label="lambda_minus")
    ax.plot(lam_grid, eigs[:, 1], linewidth=2, label="lambda_plus")
    ax.axhline(0.0, linewidth=1)
    idx = int(np.argmin(eigs[:, 1] - eigs[:, 0]))
    ax.annotate(
        "",
        xy=(lam_grid[idx], eigs[idx, 1]),
        xytext=(lam_grid[idx], eigs[idx, 0]),
        arrowprops=dict(arrowstyle="<->", linewidth=1.2),
    )
    ax.text(lam_grid[idx] + 0.015, np.mean(eigs[idx, :]), "gap >= 2|K|", fontsize=8, va="center")
    ax.set_xlabel("lifted phase-flow parameter lambda")
    ax.set_ylabel("eigen-denominator")
    ax.set_title("Two-shadow lifted phase flow and structural-overlap gap")
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(out / "two_shadow_avoided_crossing.png", dpi=220)
    plt.close(fig)


def save_horizon_event_curve(out: Path) -> None:
    lam_grid = np.linspace(0.0, 1.0, 401)
    b1 = PhaseFlowBranch(n_abs=1, theta0=-0.2 * math.pi, phase_lift_coefficient=1.4 * TAU)
    b2 = PhaseFlowBranch(n_abs=1, theta0=0.4 * math.pi, phase_lift_coefficient=0.4 * TAU)
    structural_overlap = 0.55
    inv = [two_shadow_invariants(b1, b2, float(lam), structural_overlap) for lam in lam_grid]
    lm = np.asarray([x.lambda_minus for x in inv])
    det = np.asarray([x.determinant for x in inv])
    roots_lm = find_zero_crossings_linear(lam_grid, lm)
    roots_det = find_zero_crossings_linear(lam_grid, det)

    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    ax.plot(lam_grid, lm, linewidth=2, label="lambda_min")
    ax.plot(lam_grid, det, linestyle="--", linewidth=1.4, label="det D2")
    ax.axhline(0.0, linewidth=1, label="admissibility horizon")
    for root in roots_lm[:2]:
        ax.axvline(root, linewidth=1, alpha=0.6)
        ax.text(root, 0.2, f"lambda*~{root:.3f}", rotation=90, fontsize=8, va="bottom")
    ax.set_xlabel("lifted phase-flow parameter lambda")
    ax.set_ylabel("diagnostic value")
    ax.set_title("Interpolated horizon event: lambda_min(D2(lambda)) = 0")
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(out / "horizon_event_curve.png", dpi=220)
    plt.close(fig)

    with open(out / "horizon_event_roots.txt", "w", encoding="utf-8") as f:
        f.write("BC-Origin IV v0.1.1 horizon-event estimates\n")
        f.write("lambda_min roots: " + ", ".join(f"{r:.8f}" for r in roots_lm) + "\n")
        f.write("det(D2) roots: " + ", ".join(f"{r:.8f}" for r in roots_det) + "\n")
        f.write("For a 2x2 self-adjoint operator, det(D2)=0 marks a zero eigenvalue.\n")


def save_horizon_event_map(out: Path) -> None:
    lam_grid = np.linspace(0.0, 1.0, 300)
    k_grid = np.linspace(0.0, 1.8, 260)
    b1 = PhaseFlowBranch(n_abs=1, theta0=-0.2 * math.pi, phase_lift_coefficient=1.4 * TAU)
    b2 = PhaseFlowBranch(n_abs=1, theta0=0.4 * math.pi, phase_lift_coefficient=0.4 * TAU)
    Z = np.zeros((len(k_grid), len(lam_grid)))
    for i, structural_overlap in enumerate(k_grid):
        for j, lam in enumerate(lam_grid):
            D = build_two_shadow_operator(b1, b2, float(lam), float(structural_overlap))
            Z[i, j] = horizon_value(D)

    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    im = ax.imshow(
        Z,
        origin="lower",
        aspect="auto",
        extent=[lam_grid[0], lam_grid[-1], k_grid[0], k_grid[-1]],
    )
    ax.contour(lam_grid, k_grid, Z, levels=[0.0], linewidths=2)
    ax.set_xlabel("lifted phase-flow parameter lambda")
    ax.set_ylabel("structural overlap K")
    ax.set_title("Horizon event map: lambda_min(D2(lambda)) = 0")
    fig.colorbar(im, ax=ax, label="lambda_min")
    fig.tight_layout()
    fig.savefig(out / "horizon_event_map.png", dpi=220)
    plt.close(fig)


def save_gap_protection_vs_kernel(out: Path) -> None:
    k_grid = np.linspace(0.0, 2.0, 300)
    b1 = PhaseFlowBranch(n_abs=1, theta0=0.0, phase_lift_coefficient=0.0)
    b2 = PhaseFlowBranch(n_abs=1, theta0=0.0, phase_lift_coefficient=0.0)
    gaps = np.asarray([two_shadow_gap(b1, b2, 0.0, float(k)) for k in k_grid])

    fig, ax = plt.subplots(figsize=(7.2, 4.2))
    ax.plot(k_grid, gaps, linewidth=2, label="computed eigenvalue gap")
    ax.plot(k_grid, 2 * k_grid, linestyle="--", linewidth=1, label="2*K lower bound")
    ax.set_xlabel("structural overlap K")
    ax.set_ylabel("lambda_plus - lambda_minus")
    ax.set_title("Gap protection by nonzero structural overlap")
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(out / "gap_protection_vs_structural_overlap.png", dpi=220)
    plt.close(fig)


def save_lifted_phase_reindexing(out: Path) -> None:
    theta = np.linspace(0.0, TAU, 300)
    n_abs = 3
    d_original_shifted = TAU * n_abs - (theta + TAU)
    d_reindexed = TAU * (n_abs - 1) - theta
    diff = d_original_shifted - d_reindexed
    lhs, rhs = lifted_phase_reindex_denominator(n_abs, theta=0.37 * TAU, periods=1)

    fig, ax = plt.subplots(figsize=(7.2, 4.2))
    ax.plot(theta / TAU, d_original_shifted, linewidth=2, label="d(|n|, Theta+2*pi)")
    ax.plot(theta / TAU, d_reindexed, linestyle="--", linewidth=2, label="d(|n|-1, Theta)")
    ax.set_xlabel("Theta / 2*pi")
    ax.set_ylabel("closure denominator")
    ax.set_title("Lifted phase reindexing identity")
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.text(0.05, 0.08, f"sample check: lhs-rhs = {lhs-rhs:.2e}", transform=ax.transAxes, fontsize=8)
    inset = ax.inset_axes([0.62, 0.18, 0.33, 0.28])
    inset.plot(theta / TAU, diff)
    inset.set_title("difference", fontsize=8)
    inset.tick_params(labelsize=7)
    fig.tight_layout()
    fig.savefig(out / "lifted_phase_reindexing.png", dpi=220)
    plt.close(fig)


def save_multi_shadow_phase_flow_spectrum(out: Path) -> None:
    lam_grid = np.linspace(0.0, 1.0, 401)
    n_values = [1, 2, -3, 4]
    branches = [
        PhaseFlowBranch(1, theta0=-0.2 * TAU, phase_lift_coefficient=1.2 * TAU),
        PhaseFlowBranch(2, theta0=0.1 * TAU, phase_lift_coefficient=0.55 * TAU),
        PhaseFlowBranch(3, theta0=-0.1 * TAU, phase_lift_coefficient=0.85 * TAU),
        PhaseFlowBranch(4, theta0=0.2 * TAU, phase_lift_coefficient=0.25 * TAU),
    ]
    edge_holonomy = np.ones((4, 4))
    edge_holonomy[0, 2] = edge_holonomy[2, 0] = -1.0

    def D_of_lam(lam: float) -> np.ndarray:
        return build_multi_shadow_operator(
            n_values,
            branches,
            lam,
            global_kernel_normalization=1.0,
            edge_holonomy=edge_holonomy,
        )

    eigs = scan_spectrum(D_of_lam, lam_grid)
    loc_count = np.sum(eigs > 0, axis=1)

    fig, ax = plt.subplots(figsize=(7.2, 4.5))
    for j in range(eigs.shape[1]):
        ax.plot(lam_grid, eigs[:, j], linewidth=1.8, label=f"lambda_{j+1}")
    ax.axhline(0.0, linewidth=1)
    ax.set_xlabel("lifted phase-flow parameter lambda")
    ax.set_ylabel("eigen-denominator")
    ax.set_title("Multi-shadow lifted phase-flow spectrum")
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=7, ncol=2)
    fig.tight_layout()
    fig.savefig(out / "multi_shadow_flow_spectrum.png", dpi=220)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(7.2, 3.8))
    ax.step(lam_grid, loc_count, where="mid", linewidth=2)
    ax.set_xlabel("lifted phase-flow parameter lambda")
    ax.set_ylabel("number of positive branches")
    ax.set_title("Localized branch count along lifted phase flow")
    ax.set_ylim(-0.2, eigs.shape[1] + 0.5)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(out / "localized_branch_count.png", dpi=220)
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, default=Path("origin_iv/figures"))
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    save_avoided_crossing_phase_flow(args.out)
    save_horizon_event_curve(args.out)
    save_horizon_event_map(args.out)
    save_gap_protection_vs_kernel(args.out)
    save_lifted_phase_reindexing(args.out)
    save_multi_shadow_phase_flow_spectrum(args.out)

    print(f"Generated BC-Origin IV v0.1.1 software-patch figures in {args.out}")


if __name__ == "__main__":
    main()
