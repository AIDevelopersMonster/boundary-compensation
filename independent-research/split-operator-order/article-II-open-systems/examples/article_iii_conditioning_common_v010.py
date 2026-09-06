#!/usr/bin/env python3
"""Common real/complex builders for Article III conditioning experiments.

This module implements the exact domain whitening proved in
ARTICLE-III-GRAM-SPECTRUM-THEOREM-v0.1.md:

    G^{-1/2} = P_r + (sqrt(2)/d) P_a + (1/d) P_s.

All Kossakowski coordinates are Frobenius-orthonormal and all traceless
Hermitian operator coordinates are orthonormal for tau(X*Y)=Tr(X*Y)/d.
No singular-value information is inferred from finite-field residues.
"""

from __future__ import annotations

import itertools
import math
import numpy as np


def tau_inner(a: np.ndarray, b: np.ndarray) -> complex:
    d = a.shape[0]
    return np.trace(a.conj().T @ b) / d


def traceless_hermitian_basis(d: int) -> list[np.ndarray]:
    """tau-orthonormal Hermitian traceless basis of M_d."""
    fs: list[np.ndarray] = []
    s = math.sqrt(d / 2.0)
    for j in range(d):
        for k in range(j + 1, d):
            m = np.zeros((d, d), dtype=complex)
            m[j, k] = m[k, j] = s
            fs.append(m)

            m = np.zeros((d, d), dtype=complex)
            m[j, k] = -1j * s
            m[k, j] = 1j * s
            fs.append(m)

    for ell in range(1, d):
        m = np.zeros((d, d), dtype=complex)
        c = math.sqrt(d / (ell * (ell + 1.0)))
        for j in range(ell):
            m[j, j] = c
        m[ell, ell] = -ell * c
        fs.append(m)

    assert len(fs) == d * d - 1
    gram = np.array([[tau_inner(a, b) for b in fs] for a in fs])
    assert np.allclose(gram, np.eye(len(fs)), atol=1e-12)
    return fs


def hermitian_coordinate_columns(q: int):
    """Sparse Frobenius-orthonormal basis of Herm(q).

    Each column is returned as a list of triples (a,b,coefficient).
    Ordering: diagonal, real-symmetric, imaginary-antisymmetric.
    """
    cols = []
    for a in range(q):
        cols.append([(a, a, 1.0)])

    r = 1.0 / math.sqrt(2.0)
    for a in range(q):
        for b in range(a + 1, q):
            cols.append([(a, b, r), (b, a, r)])
            cols.append([(a, b, -1j * r), (b, a, 1j * r)])

    assert len(cols) == q * q
    return cols


def word(gates: list[np.ndarray], perm) -> np.ndarray:
    w = np.eye(gates[0].shape[0], dtype=complex)
    for idx in perm:
        w = w @ gates[idx]
    return w


def swap_pos(perm, i: int):
    q = list(perm)
    q[i], q[i + 1] = q[i + 1], q[i]
    return tuple(q)


def edge(gates: list[np.ndarray], perm, i: int):
    q = swap_pos(perm, i)
    return word(gates, q) @ word(gates, perm).conj().T, q


def coxeter_loop(gates: list[np.ndarray], perm, generators) -> list[np.ndarray]:
    cur = tuple(perm)
    out = []
    for g in generators:
        e, cur = edge(gates, cur, g)
        out.append(e)
    assert cur == tuple(perm)
    return out


def engineered_square(u: np.ndarray, v: np.ndarray) -> list[np.ndarray]:
    """Flat four-edge square with product T4 T3 T2 T1 = I."""
    return [u, v, u.conj().T, u.conj().T @ v.conj().T @ u]


def measurement_block(transports: list[np.ndarray], fs: list[np.ndarray]) -> np.ndarray:
    """Build one real matrix-valued first-order face block.

    Columns are Frobenius-orthonormal Hermitian Kossakowski coordinates.
    Rows are Re/Im matrix entries before the final 1/sqrt(d L) output scaling.
    """
    d = transports[0].shape[0]
    q = len(fs)
    m = len(transports)

    pref = [np.eye(d, dtype=complex)]
    for t in transports:
        pref.append(t @ pref[-1])

    op = np.zeros((q, q, d, d), dtype=complex)
    for kk in range(1, m):
        left = np.eye(d, dtype=complex)
        for j in range(m - 1, kk, -1):
            left = left @ transports[j]

        x = transports[kk]
        y = pref[kk]
        ax = [f @ x - x @ f for f in fs]
        yb = [y @ f - f @ y for f in fs]
        for a in range(q):
            for b in range(q):
                op[a, b] -= left @ ax[a] @ yb[b]

    mats = []
    for a in range(q):
        mats.append(op[a, a])

    r = 1.0 / math.sqrt(2.0)
    for a in range(q):
        for b in range(a + 1, q):
            mats.append(r * (op[a, b] + op[b, a]))
            mats.append(1j * r * (op[b, a] - op[a, b]))

    cols = [np.r_[k.real.ravel(), k.imag.ravel()] for k in mats]
    return np.array(cols, dtype=float).T


def multiplication_matrix(d: int, fs: list[np.ndarray]) -> np.ndarray:
    """Matrix of T(C)=sum C_ab F_a F_b - Tr(C) I in ON coordinates."""
    q = d * d - 1
    cols = hermitian_coordinate_columns(q)
    tmat = np.zeros((q, q * q), dtype=float)

    for j, entries in enumerate(cols):
        k = np.zeros((d, d), dtype=complex)
        trc = 0.0
        for a, b, coeff in entries:
            k += coeff * (fs[a] @ fs[b])
            if a == b:
                trc += float(np.real(coeff))
        k0 = k - trc * np.eye(d)
        for r, f in enumerate(fs):
            tmat[r, j] = float(np.real(tau_inner(f, k0)))

    return tmat


def closed_form_whitener(d: int, fs: list[np.ndarray]):
    """Return W=G^{-1/2} and theorem diagnostics."""
    q = d * d - 1
    n = q * q
    tmat = multiplication_matrix(d, fs)

    pa = (tmat.T @ tmat) / (d * d - 2.0)
    s = np.zeros(n, dtype=float)
    s[:q] = 1.0 / math.sqrt(q)
    ps = np.outer(s, s)
    pr = np.eye(n) - pa - ps

    w = pr + (math.sqrt(2.0) / d) * pa + (1.0 / d) * ps

    theorem_error = np.linalg.norm(
        tmat @ tmat.T - (d * d - 2.0) * np.eye(q), ord=2
    )
    projector_error = max(
        np.linalg.norm(pa @ pa - pa, ord=2),
        np.linalg.norm(ps @ ps - ps, ord=2),
        np.linalg.norm(pa @ ps, ord=2),
    )

    # Independent formula G=I+J+(1/2)T*T, used only as a regression check.
    trace_vec = np.zeros(n, dtype=float)
    trace_vec[:q] = 1.0
    gram = np.eye(n) + np.outer(trace_vec, trace_vec) + 0.5 * (tmat.T @ tmat)
    whitening_error = np.linalg.norm(w.T @ gram @ w - np.eye(n), ord=2)

    return w, {
        "T": tmat,
        "P_adj": pa,
        "P_scalar": ps,
        "P_residual": pr,
        "gram": gram,
        "theorem_error": theorem_error,
        "projector_error": projector_error,
        "whitening_error": whitening_error,
    }


def normalize_design(blocks: list[np.ndarray], d: int, w: np.ndarray) -> np.ndarray:
    """Stack, exact-whiten, and apply averaged normalized HS output metric."""
    l = len(blocks)
    return (np.vstack(blocks) @ w) / math.sqrt(d * l)


def conditioning_stats(m: np.ndarray) -> dict:
    sv = np.linalg.svd(m, compute_uv=False)
    smax = float(sv[0])
    smin = float(sv[-1])
    return {
        "rows": int(m.shape[0]),
        "cols": int(m.shape[1]),
        "rank": int(np.linalg.matrix_rank(m)),
        "sigma_min": smin,
        "sigma_max": smax,
        "kappa": smax / smin,
        "A": smin * smin,
        "B": smax * smax,
    }


def qutrit_gates() -> list[np.ndarray]:
    x = np.zeros((3, 3), dtype=complex)
    x[1, 0] = x[2, 1] = x[0, 2] = 1.0
    dph = np.diag([1.0, 1j, -1.0]).astype(complex)
    r12 = np.eye(3, dtype=complex)
    r12[:2, :2] = [[3.0 / 5.0, 4.0 / 5.0], [-4.0 / 5.0, 3.0 / 5.0]]
    r23 = np.eye(3, dtype=complex)
    r23[1:, 1:] = [[3.0 / 5.0, 4.0 / 5.0], [-4.0 / 5.0, 3.0 / 5.0]]
    return [x, dph, r12, r23]


def d4_gates() -> list[np.ndarray]:
    x = np.zeros((4, 4), dtype=complex)
    x[1, 0] = x[2, 1] = x[3, 2] = x[0, 3] = 1.0
    dph = np.diag([1.0, 1j, -1.0, -1j]).astype(complex)
    r12 = np.eye(4, dtype=complex)
    r12[:2, :2] = [[3.0 / 5.0, 4.0 / 5.0], [-4.0 / 5.0, 3.0 / 5.0]]
    r23 = np.eye(4, dtype=complex)
    r23[1:3, 1:3] = [[3.0 / 5.0, 4.0 / 5.0], [-4.0 / 5.0, 3.0 / 5.0]]
    return [x, dph, r12, r23]


def from_ops_real(d: int, ops) -> np.ndarray:
    """Real/complex analogue of finite_field_rank_common_v010.from_ops."""
    u = np.eye(d, dtype=complex)
    for op in ops:
        typ, j, k = op[:3]
        e = np.eye(d, dtype=complex)
        if typ == "r":
            _, j, k, a, b, c = op
            e[j, j] = a / c
            e[j, k] = b / c
            e[k, j] = -b / c
            e[k, k] = a / c
        elif typ == "p":
            _, j, k, s = op
            e[j, j] = 1j * s
            e[k, k] = -1j * s
        else:
            raise ValueError(f"unknown op type: {typ}")
        u = e @ u
    return u


def coxeter_pool(gates: list[np.ndarray]):
    """The 72-face pool used in the first d=3/d=4 conditioning study."""
    loop_types = ([0, 1] * 3, [1, 2] * 3, [0, 2, 0, 2])
    for perm in itertools.permutations(range(4)):
        for gens in loop_types:
            yield tuple(perm), tuple(gens), coxeter_loop(gates, perm, gens)
