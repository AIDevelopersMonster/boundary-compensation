"""Reproduce the Gateway I central-spin threshold-certification demonstrator."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

import matplotlib.pyplot as plt
import numpy as np

from bc_gateway.metrics import coarse_dephasing_distance
from bc_gateway.models import gamma_abs_two_spin_bath, lambda_minus_from_gamma_abs


def first_crossing(t: np.ndarray, y: np.ndarray, level: float) -> float:
    """Linearly interpolate the first upward crossing of ``level`` by ``y``."""
    indices = np.where(y >= level)[0]
    if len(indices) == 0:
        raise ValueError(f"no crossing found for level {level}")
    idx = int(indices[0])
    if idx == 0:
        return float(t[0])
    t0, t1 = t[idx - 1], t[idx]
    y0, y1 = y[idx - 1], y[idx]
    return float(t0 + (level - y0) * (t1 - t0) / (y1 - y0))


def compute_demo(g1: float, g2: float, gamma: float, tau: float, eta: float, t_max: float, n: int):
    t = np.linspace(0.0, t_max, n)
    gamma_abs = gamma_abs_two_spin_bath(t, g1=g1, g2=g2)
    lambda_minus = lambda_minus_from_gamma_abs(gamma_abs)
    d_coarse = coarse_dephasing_distance(gamma_abs, gamma=gamma, t=t)
    return t, gamma_abs, lambda_minus, d_coarse


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--g1", type=float, default=0.5)
    parser.add_argument("--g2", type=float, default=0.7)
    parser.add_argument("--gamma", type=float, default=0.4)
    parser.add_argument("--tau", type=float, default=0.05)
    parser.add_argument("--eta", type=float, default=0.02)
    parser.add_argument("--t-max", type=float, default=2.0)
    parser.add_argument("--n", type=int, default=200_001)
    parser.add_argument("--figures-dir", type=Path, default=Path("figures/gateway_i"))
    parser.add_argument("--save-figures", action="store_true")
    args = parser.parse_args()

    t, gamma_abs, lambda_minus, d_coarse = compute_demo(
        g1=args.g1,
        g2=args.g2,
        gamma=args.gamma,
        tau=args.tau,
        eta=args.eta,
        t_max=args.t_max,
        n=args.n,
    )

    for level in [args.tau - args.eta, args.tau, args.tau + args.eta]:
        tc = first_crossing(t, lambda_minus, level)
        gc = float(gamma_abs_two_spin_bath(tc, g1=args.g1, g2=args.g2))
        lc = float(lambda_minus_from_gamma_abs(gc))
        dc = float(coarse_dephasing_distance(gc, gamma=args.gamma, t=tc))
        print(f"level={level:.3f}, t={tc:.6f}, lambda_minus={lc:.6f}, D_coarse={dc:.6f}")

    t_tau = first_crossing(t, lambda_minus, args.tau)
    max_before_threshold = float(d_coarse[t <= t_tau].max())
    print(f"max D_coarse before threshold: {max_before_threshold}")

    if args.save_figures:
        args.figures_dir.mkdir(parents=True, exist_ok=True)

        fig, ax = plt.subplots(figsize=(7.2, 4.2))
        ax.plot(t, lambda_minus, label=r"$\lambda_-(t)$")
        ax.axhline(args.tau, linestyle="--", label=r"$\tau$")
        ax.axhline(args.tau - args.eta, linestyle=":", label=r"$\tau-\eta$")
        ax.axhline(args.tau + args.eta, linestyle=":", label=r"$\tau+\eta$")
        ax.set_xlim(0.0, 0.6)
        ax.set_xlabel("t")
        ax.set_ylabel("normalized Choi eigenvalue")
        ax.legend(loc="best")
        fig.tight_layout()
        fig.savefig(args.figures_dir / "choi_threshold_margin.png", dpi=200)
        plt.close(fig)

        fig, ax = plt.subplots(figsize=(7.2, 4.2))
        ax.plot(t, d_coarse, label=r"$D_{\rm coarse}(t)$")
        ax.axvline(t_tau, linestyle="--", label=r"threshold crossing")
        ax.set_xlim(0.0, 0.6)
        ax.set_xlabel("t")
        ax.set_ylabel("coarse distance")
        ax.legend(loc="best")
        fig.tight_layout()
        fig.savefig(args.figures_dir / "coarse_markovian_distance.png", dpi=200)
        plt.close(fig)


if __name__ == "__main__":
    main()
