"""Generate BC-Origin III holonomy/frustration figures."""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from bc_origin_iii_holonomy_core import (
    build_holonomy_operator,
    complete_epsilon,
    spectrum,
    triangle_spectra,
    triangle_cycle_products,
)


def save_triangle_spectra(out: Path) -> None:
    d = 5.0
    xs = np.linspace(0.0, 2.4, 120)
    bal_low, bal_mid, bal_high = [], [], []
    fr_low, fr_mid, fr_high = [], [], []
    for x in xs:
        s = triangle_spectra(d=d, eta_k=x)
        bal_low.append(s["balanced"][0])
        bal_mid.append(s["balanced"][1])
        bal_high.append(s["balanced"][2])
        fr_low.append(s["frustrated"][0])
        fr_mid.append(s["frustrated"][1])
        fr_high.append(s["frustrated"][2])
    plt.figure(figsize=(8, 5))
    plt.plot(xs, bal_high, label="balanced: d+2eta k")
    plt.plot(xs, bal_low, label="balanced: d-eta k (double)")
    plt.plot(xs, fr_mid, "--", label="frustrated: d+eta k (double)")
    plt.plot(xs, fr_low, "--", label="frustrated: d-2eta k")
    plt.axhline(0, linewidth=1)
    plt.xlabel("eta k")
    plt.ylabel("eigen-denominator lambda")
    plt.title("Balanced vs frustrated triangle spectral types")
    plt.legend()
    plt.tight_layout()
    plt.savefig(out / "triangle_holonomy_spectra.png", dpi=180)
    plt.close()


def save_heatmaps(out: Path) -> None:
    n = [1, 2, 3]
    d = [5, 5, 5]
    E_bal = complete_epsilon(3)
    E_fr = complete_epsilon(3, negative_edges=[(0, 2)])
    D_bal = build_holonomy_operator(n, d_values=d, epsilon=E_bal, eta=1.0, kernel_kind="exponential", alpha=0.0)
    D_fr = build_holonomy_operator(n, d_values=d, epsilon=E_fr, eta=1.0, kernel_kind="exponential", alpha=0.0)
    fig, axes = plt.subplots(1, 2, figsize=(8, 4))
    for ax, D, title in zip(axes, [D_bal, D_fr], ["balanced operator", "frustrated operator"]):
        im = ax.imshow(D)
        ax.set_title(title)
        ax.set_xticks([0, 1, 2]); ax.set_yticks([0, 1, 2])
        for i in range(3):
            for j in range(3):
                ax.text(j, i, f"{D[i,j]:.1f}", ha="center", va="center")
    fig.colorbar(im, ax=axes.ravel().tolist(), shrink=0.75)
    fig.suptitle("Minimal triangle operators")
    plt.savefig(out / "balanced_vs_frustrated_heatmaps.png", dpi=180, bbox_inches="tight")
    plt.close()


def save_cycle_products(out: Path) -> None:
    E_bal = complete_epsilon(3)
    E_fr = complete_epsilon(3, negative_edges=[(0, 2)])
    vals = [list(triangle_cycle_products(E_bal).values())[0], list(triangle_cycle_products(E_fr).values())[0]]
    labels = ["balanced triangle", "frustrated triangle"]
    plt.figure(figsize=(7, 4))
    plt.bar(labels, vals)
    plt.ylim(-1.2, 1.2)
    plt.axhline(0, linewidth=1)
    plt.ylabel("cycle product Omega")
    plt.title("Gauge-invariant Z2 cycle product")
    plt.tight_layout()
    plt.savefig(out / "cycle_holonomy_product.png", dpi=180)
    plt.close()


def save_gap_as_localization_price(out: Path) -> None:
    # 2x2 avoided-crossing geometry used only as companion intuition.
    k = 0.8
    d0 = 5.0
    v1, v2 = 1.0, -0.5
    t = np.linspace(-6, 8, 300)
    lminus, lplus, scale_minus, scale_plus = [], [], [], []
    for x in t:
        d1 = d0 - v1 * x
        d2 = d0 - v2 * x
        base = 0.5 * (d1 + d2)
        r = np.sqrt(((d1 - d2) / 2) ** 2 + k ** 2)
        lm, lp = base - r, base + r
        lminus.append(lm)
        lplus.append(lp)
        scale_minus.append(np.nan if lm <= 0 else 1 / lm)
        scale_plus.append(np.nan if lp <= 0 else 1 / lp)
    plt.figure(figsize=(8, 5))
    plt.plot(t, lplus, label="lambda plus")
    plt.plot(t, lminus, label="lambda minus")
    plt.axhline(0, linewidth=1)
    plt.xlabel("flow parameter")
    plt.ylabel("eigen-denominator lambda")
    plt.title("Avoided-crossing geometry and horizon event")
    plt.legend()
    plt.tight_layout()
    plt.savefig(out / "flow_avoided_crossing_horizon.png", dpi=180)
    plt.close()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, default=Path("figures"))
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    save_triangle_spectra(args.out)
    save_heatmaps(args.out)
    save_cycle_products(args.out)
    save_gap_as_localization_price(args.out)
    print(f"Generated BC-Origin III figures in {args.out}")


if __name__ == "__main__":
    main()
