"""
BC-Origin II kernel core
Structural Coupling Kernels and Multi-Shadow Spectral Geometry
"""

import numpy as np
from dataclasses import dataclass

# -----------------------------
# utilities
# -----------------------------

def sign(x):
    return 1 if x > 0 else -1 if x < 0 else 0

# -----------------------------
# kernels
# -----------------------------

def lorentz_kernel(di):
    return 1.0 / (1.0 + di * di)


def exp_kernel(di, a=0.5):
    return np.exp(-a * abs(di))

# -----------------------------
# core structures
# -----------------------------

def closure_d(q, n, theta=0.0):
    return 2*np.pi*abs(n) - theta


def build_D(n_list, q_list, gamma=0.0, eta=1.0, kind="lorentz"):
    N = len(n_list)
    D = np.zeros((N, N))

    def K(i, j):
        d = n_list[i] - n_list[j]
        if kind == "lorentz":
            return lorentz_kernel(d)
        else:
            return exp_kernel(d)

    for i in range(N):
        di = closure_d(q_list[i], n_list[i])

        for j in range(N):
            Kij = K(i, j)
            sij = sign(n_list[i]) * sign(n_list[j])

            if i == j:
                D[i, i] = di + gamma * sij * Kij
            else:
                D[i, j] = eta * Kij

    return D


def spectrum(D):
    return np.linalg.eigvalsh(D)


def horizon(D):
    return np.min(spectrum(D))


def run_demo():
    n = [1, 2, -3, 4]
    q = [1, 1, 2, 2]

    D = build_D(n, q, gamma=0.8, eta=1.0)

    print("eigenvalues:", spectrum(D))
    print("horizon:", horizon(D))


if __name__ == "__main__":
    run_demo()
