"""
BC-Origin II figure generator

Boundary Compensation Origin II:
Structural Coupling Kernels and Multi-Shadow Spectral Geometry

Run from repository root:

    python bc_origin/origin_ii/software/generate_bc_origin_ii_figures.py --out bc_origin/origin_ii/figures

Expected outputs:

    kernel_decay_profile.png
    kernel_matrix_heatmap.png
    n_body_spectrum.png
    lambda_min_horizon_map.png
    constant_vs_structural_coupling.png
    balanced_sign_graph_check.png
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

try:
    from bc_origin_ii_kernel_core import build_D, spectrum, horizon, sign
except ImportError as exc:
    raise SystemExit(
        "Could not import bc_origin_ii_kernel_core.py. "
        "Run this script from the repository root and keep "
        "bc_origin_ii_kernel_core.py in the same software folder."
    ) from exc


def lorentz_kernel_distance(m: np.ndarray | float) -> np.ndarray | float:
    return 1.0 / (1.0 + np.asarray(m) ** 2)


def build_kernel_matrix(n_values: list[int]) -> np.ndarray:
    n = np.asarray(n_values)
    diff = n[:, None] - n[None, :]
    return 1.0 / (1.0 + diff**2)


def build_sign_matrix(n_values: list[int]) -> np.ndarray:
    sigma = np.asarray([sign(x) for x in n_values])
    return sigma[:, None] * sigma[None, :]


def save_kernel_decay_profile(out: Path) -> None:
    m = np.arange(-12, 13)
    k = lorentz_kernel_distance(m)

    plt.figure(figsize=(7.5, 4.5))
    plt.plot(m, k, marker="o")
    plt.xlabel("winding-index separation m = n_i - n_j")
    plt.ylabel("K(m)")
    plt.title("BC-Origin II structural kernel decay")
    plt.tight_layout()
    plt.savefig(out / "kernel_decay_profile.png", dpi=180)
    plt.close()


def save_kernel_matrix_heatmap(out: Path) -> None:
    n_values = [-5, -3, -1, 1, 2, 4, 7]
    K = build_kernel_matrix(n_values)

    plt.figure(figsize=(6.2, 5.4))
    im = plt.imshow(K, origin="lower", aspect="auto")
    plt.colorbar(im, label="K_ij")
    plt.xticks(range(len(n_values)), n_values)
    plt.yticks(range(len(n_values)), n_values)
    plt.xlabel("n_j")
    plt.ylabel("n_i")
    plt.title("Structural kernel matrix K_ij")
    plt.tight_layout()
    plt.savefig(out / "kernel_matrix_heatmap.png", dpi=180)
    plt.close()


def save_n_body_spectrum(out: Path) -> None:
    n_values = [-5, -3, -1, 1, 2, 4, 7]
    q_values = [1, 1, 2, 1, 2, 2, 3]

    eta_values = np.linspace(0.0, 4.0, 160)
    eig_table = []

    for eta in eta_values:
        D = build_D(n_values, q_values, gamma=0.8, eta=eta, kind="lorentz")
        eig_table.append(spectrum(D))

    eig_table = np.asarray(eig_table)

    plt.figure(figsize=(8.0, 5.0))
    for a in range(eig_table.shape[1]):
        plt.plot(eta_values, eig_table[:, a])
    plt.axhline(0, linewidth=1)
    plt.xlabel("global off-diagonal scale eta")
    plt.ylabel("eigen-denominators lambda_a(D_N)")
    plt.title("N-shadow spectrum under structural kernel coupling")
    plt.tight_layout()
    plt.savefig(out / "n_body_spectrum.png", dpi=180)
    plt.close()


def save_lambda_min_horizon_map(out: Path) -> None:
    n_values = [-5, -3, -1, 1, 2, 4, 7]
    q_values = [1, 1, 2, 1, 2, 2, 3]

    gamma_values = np.linspace(-8.0, 2.0, 180)
    eta_values = np.linspace(0.0, 5.0, 160)

    z = np.zeros((len(eta_values), len(gamma_values)))

    for i, eta in enumerate(eta_values):
        for j, gamma in enumerate(gamma_values):
            D = build_D(n_values, q_values, gamma=gamma, eta=eta, kind="lorentz")
            z[i, j] = horizon(D)

    plt.figure(figsize=(8.2, 5.2))
    im = plt.imshow(
        z,
        origin="lower",
        aspect="auto",
        extent=[
            gamma_values.min(),
            gamma_values.max(),
            eta_values.min(),
            eta_values.max(),
        ],
    )
    plt.contour(gamma_values, eta_values, z, levels=[0], linewidths=2)
    plt.colorbar(im, label="lambda_min(D_N)")
    plt.xlabel("gamma")
    plt.ylabel("eta")
    plt.title("Admissibility horizon map: lambda_min(D_N) = 0")
    plt.tight_layout()
    plt.savefig(out / "lambda_min_horizon_map.png", dpi=180)
    plt.close()


def constant_coupling_matrix(n_values: list[int], q_values: list[int], gamma: float, eta: float) -> np.ndarray:
    N = len(n_values)
    D = np.zeros((N, N))

    for i in range(N):
        d_i = 2.0 * np.pi * abs(n_values[i])
        D[i, i] = d_i + gamma

        for j in range(N):
            if i != j:
                D[i, j] = eta

    return D


def save_constant_vs_structural_coupling(out: Path) -> None:
    n_values = [-5, -3, -1, 1, 2, 4, 7]
    q_values = [1, 1, 2, 1, 2, 2, 3]

    eta_values = np.linspace(0.0, 5.0, 180)

    structural = []
    constant = []

    for eta in eta_values:
        D_struct = build_D(n_values, q_values, gamma=-3.0, eta=eta, kind="lorentz")
        D_const = constant_coupling_matrix(n_values, q_values, gamma=-3.0, eta=eta)
        structural.append(horizon(D_struct))
        constant.append(np.min(np.linalg.eigvalsh(D_const)))

    plt.figure(figsize=(8.0, 4.8))
    plt.plot(eta_values, structural, label="structural kernel coupling")
    plt.plot(eta_values, constant, linestyle="--", label="constant pair coupling")
    plt.axhline(0, linewidth=1)
    plt.xlabel("eta")
    plt.ylabel("lambda_min")
    plt.title("Constant vs structural coupling: horizon diagnostic")
    plt.legend()
    plt.tight_layout()
    plt.savefig(out / "constant_vs_structural_coupling.png", dpi=180)
    plt.close()


def save_balanced_sign_graph_check(out: Path) -> None:
    n_values = [-5, -3, -1, 1, 2, 4, 7]
    S = build_sign_matrix(n_values)

    triangle_products = []
    N = len(n_values)

    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                triangle_products.append(S[i, j] * S[j, k] * S[k, i])

    unique_products = sorted(set(int(x) for x in triangle_products))

    plt.figure(figsize=(6.4, 5.2))
    im = plt.imshow(S, origin="lower", aspect="auto", vmin=-1, vmax=1)
    plt.colorbar(im, label="s_ij = sign(n_i n_j)")
    plt.xticks(range(len(n_values)), n_values)
    plt.yticks(range(len(n_values)), n_values)
    plt.xlabel("n_j")
    plt.ylabel("n_i")
    plt.title(
        "Balanced sign matrix\n"
        f"triangle cycle products: {unique_products}"
    )
    plt.tight_layout()
    plt.savefig(out / "balanced_sign_graph_check.png", dpi=180)
    plt.close()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--out",
        type=Path,
        default=Path("bc_origin/origin_ii/figures"),
        help="Output directory for generated figures.",
    )
    args = parser.parse_args()

    args.out.mkdir(parents=True, exist_ok=True)

    save_kernel_decay_profile(args.out)
    save_kernel_matrix_heatmap(args.out)
    save_n_body_spectrum(args.out)
    save_lambda_min_horizon_map(args.out)
    save_constant_vs_structural_coupling(args.out)
    save_balanced_sign_graph_check(args.out)

    print(f"Wrote BC-Origin II figures to: {args.out}")
    for name in [
        "kernel_decay_profile.png",
        "kernel_matrix_heatmap.png",
        "n_body_spectrum.png",
        "lambda_min_horizon_map.png",
        "constant_vs_structural_coupling.png",
        "balanced_sign_graph_check.png",
    ]:
        print(f"  - {args.out / name}")


if __name__ == "__main__":
    main()