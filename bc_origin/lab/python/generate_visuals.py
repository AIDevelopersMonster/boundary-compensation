"""Generate publication-style static visuals for BC-Origin I."""
from __future__ import annotations

import argparse
from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from bc_origin_visual_core import signed_shadow


def save_spectrum(out: Path) -> None:
    gamma_values = np.linspace(0, 6, 301)
    rows = [(1, 1, "same orientation"), (1, -1, "opposite orientation")]
    plt.figure(figsize=(8, 4.8))
    for n1, n2, label in rows:
        minus = [signed_shadow(n1, n2, 4.0, 5.0, g, 1.0).lambda_minus for g in gamma_values]
        plus = [signed_shadow(n1, n2, 4.0, 5.0, g, 1.0).lambda_plus for g in gamma_values]
        plt.plot(gamma_values, minus, label=f"lambda- {label}")
        plt.plot(gamma_values, plus, linestyle="--", label=f"lambda+ {label}")
    plt.axhline(0, linewidth=1)
    plt.xlabel("gamma signed shift strength")
    plt.ylabel("inverse-scale denominator lambda")
    plt.title("BC-Origin signed spectral displacement")
    plt.legend(fontsize=8)
    plt.tight_layout()
    plt.savefig(out / "spectrum_signed_shift.png", dpi=180)
    plt.close()


def save_horizon(out: Path) -> None:
    kappa_values = np.linspace(0, 4, 241)
    base = 4.5
    delta = 0.5
    gamma_c = [base - np.sqrt(delta**2 + k**2) for k in kappa_values]
    plt.figure(figsize=(7.5, 4.8))
    plt.plot(kappa_values, gamma_c)
    plt.fill_between(kappa_values, gamma_c, 6, alpha=0.15)
    plt.xlabel("kappa coupling")
    plt.ylabel("critical gamma for lambda- = 0")
    plt.title("Admissibility horizon for opposite orientation branch")
    plt.tight_layout()
    plt.savefig(out / "admissibility_horizon.png", dpi=180)
    plt.close()


def save_phase_map(out: Path) -> None:
    gamma_values = np.linspace(0, 7, 260)
    kappa_values = np.linspace(0, 5, 220)
    d1, d2 = 4.0, 5.0
    z = np.zeros((len(kappa_values), len(gamma_values)))
    for i, k in enumerate(kappa_values):
        for j, g in enumerate(gamma_values):
            z[i, j] = signed_shadow(1, -1, d1, d2, g, k).lambda_minus
    plt.figure(figsize=(8, 5.2))
    im = plt.imshow(z, origin="lower", aspect="auto", extent=[gamma_values.min(), gamma_values.max(), kappa_values.min(), kappa_values.max()])
    plt.contour(gamma_values, kappa_values, z, levels=[0], linewidths=2)
    plt.colorbar(im, label="lambda- for opposite orientation")
    plt.xlabel("gamma")
    plt.ylabel("kappa")
    plt.title("Phase map: localized vs horizon-crossed shadow branch")
    plt.tight_layout()
    plt.savefig(out / "phase_map.png", dpi=180)
    plt.close()


def save_scheme(out: Path) -> None:
    plt.figure(figsize=(9, 4.8))
    ax = plt.gca()
    ax.axis("off")
    boxes = [
        (0.05, 0.62, "hidden winding\nn in Z"),
        (0.32, 0.72, "scale channel\n|n|"),
        (0.32, 0.42, "sign channel\nsgn(n)"),
        (0.62, 0.72, "closure equation\nell/L"),
        (0.62, 0.42, "signed operator\nD_signed"),
        (0.84, 0.56, "observable\nshadow"),
    ]
    for x, y, text in boxes:
        ax.add_patch(plt.Rectangle((x, y), 0.18, 0.16, fill=False, linewidth=1.8))
        ax.text(x + 0.09, y + 0.08, text, ha="center", va="center", fontsize=10)
    arrows = [((0.23, 0.70), (0.32, 0.80)), ((0.23, 0.70), (0.32, 0.50)), ((0.50, 0.80), (0.62, 0.80)), ((0.50, 0.50), (0.62, 0.50)), ((0.80, 0.80), (0.84, 0.64)), ((0.80, 0.50), (0.84, 0.60))]
    for a, b in arrows:
        ax.annotate("", xy=b, xytext=a, arrowprops=dict(arrowstyle="->", lw=1.8))
    ax.set_title("BC-Origin shadow-channel decomposition", fontsize=14)
    plt.tight_layout()
    plt.savefig(out / "model_scheme.png", dpi=180)
    plt.close()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, default=Path("bc_origin/lab/outputs"))
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    save_spectrum(args.out)
    save_horizon(args.out)
    save_phase_map(args.out)
    save_scheme(args.out)
    print(f"Wrote visuals to {args.out}")


if __name__ == "__main__":
    main()
