#!/usr/bin/env python3
"""Exact finite-field builder for Article-II Coxeter rank certificates.

Matrices are represented simultaneously under the two embeddings i -> +/-r
of Q(i) into F_p.  Real/imaginary output coordinates are reconstructed from
those two evaluations.  This module contains no stored rank labels.
"""
import numpy as np

P = 1000033
IROOT = 350504
assert (IROOT * IROOT + 1) % P == 0
INV2 = pow(2, -1, P)
INV2I = INV2 * pow(IROOT, -1, P) % P


def scalar(a=0, b=0, den=1):
    inv = pow(den % P, -1, P)
    return ((a + b * IROOT) * inv % P, (a - b * IROOT) * inv % P)


def eye(d):
    a = np.eye(d, dtype=np.int64) % P
    return a.copy(), a.copy()


def zero(d):
    a = np.zeros((d, d), dtype=np.int64)
    return a.copy(), a.copy()


def mat(d, entries):
    ap = np.zeros((d, d), dtype=np.int64)
    am = np.zeros((d, d), dtype=np.int64)
    for (i, j), v in entries.items():
        if len(v) == 2:
            a, b = v; den = 1
        else:
            a, b, den = v
        ap[i, j], am[i, j] = scalar(a, b, den)
    return ap, am


def add(a, b): return ((a[0] + b[0]) % P, (a[1] + b[1]) % P)
def neg(a): return ((-a[0]) % P, (-a[1]) % P)
def sub(a, b): return add(a, neg(b))
def mul(a, b): return ((a[0] @ b[0]) % P, (a[1] @ b[1]) % P)
def dag(a): return (a[1].T.copy(), a[0].T.copy())
def comm(a, b): return sub(mul(a, b), mul(b, a))


def scale(c, a):
    return ((c[0] * a[0]) % P, (c[1] * a[1]) % P)


def traceless_hermitian_basis(d):
    fs = []
    for j in range(d):
        for k in range(j + 1, d):
            fs.append(mat(d, {(j,k):(1,0), (k,j):(1,0)}))
            fs.append(mat(d, {(j,k):(0,-1), (k,j):(0,1)}))
    for j in range(d - 1):
        fs.append(mat(d, {(j,j):(1,0), (j+1,j+1):(-1,0)}))
    assert len(fs) == d*d - 1
    return fs


def word(u, perm):
    w = eye(u[0][0].shape[0])
    for idx in perm: w = mul(w, u[idx])
    return w


def swap_pos(perm, i):
    q = list(perm); q[i], q[i+1] = q[i+1], q[i]
    return tuple(q)


def edge(u, perm, i):
    q = swap_pos(perm, i)
    return mul(word(u, q), dag(word(u, perm))), q


def loop(u, perm, generators):
    out = []; cur = tuple(perm)
    for g in generators:
        e, cur = edge(u, cur, g); out.append(e)
    assert cur == tuple(perm)
    return out


def engineered_square(u, v):
    return [u, v, dag(u), mul(mul(dag(u), dag(v)), u)]


def measurement_block(transports, fs):
    d = transports[0][0].shape[0]; q = len(fs); m = len(transports)
    pref = [eye(d)]
    for t in transports: pref.append(mul(t, pref[-1]))
    op = np.zeros((q,q,d,d), dtype=np.int64)
    om = np.zeros_like(op)
    for kk in range(1, m):
        left = eye(d)
        for j in range(m - 1, kk, -1): left = mul(left, transports[j])
        x, y = transports[kk], pref[kk]
        ax = [comm(f, x) for f in fs]
        yb = [comm(y, f) for f in fs]
        for a in range(q):
            for b in range(q):
                z = mul(left, mul(ax[a], yb[b]))
                op[a,b] = (op[a,b] - z[0]) % P
                om[a,b] = (om[a,b] - z[1]) % P
    cols = []
    def output(kp, km):
        re = (kp + km) * INV2 % P
        im = (kp - km) * INV2I % P
        return np.r_[re.ravel(), im.ravel()]
    for a in range(q): cols.append(output(op[a,a], om[a,a]))
    for a in range(q):
        for b in range(a + 1, q):
            cols.append(output((op[a,b]+op[b,a])%P, (om[a,b]+om[b,a])%P))
            cols.append(output(IROOT*(op[a,b]-op[b,a])%P,
                               (-IROOT)*(om[a,b]-om[b,a])%P))
    return np.array(cols, dtype=np.int64).T % P


def rank_mod(a):
    a = a.copy() % P
    m, n = a.shape; r = 0
    for c in range(n):
        nz = np.flatnonzero(a[r:, c])
        if not len(nz): continue
        piv = r + int(nz[0])
        if piv != r: a[[r,piv]] = a[[piv,r]]
        a[r] = a[r] * pow(int(a[r,c]), -1, P) % P
        for i in np.flatnonzero(a[r+1:,c]) + r + 1:
            f = int(a[i,c]); a[i] = (a[i] - f*a[r]) % P
        r += 1
        if r == n: break
    return r


def from_ops(d, ops):
    u = eye(d)
    for op in ops:
        typ, j, k = op[:3]
        if typ == 'r':
            _, j, k, a, b, c = op
            e = {(x,x):(1,0) for x in range(d)}
            e[(j,j)] = (a,0,c); e[(j,k)] = (b,0,c)
            e[(k,j)] = (-b,0,c); e[(k,k)] = (a,0,c)
        else:
            _, j, k, s = op
            e = {(x,x):(1,0) for x in range(d)}
            e[(j,j)] = (0,s); e[(k,k)] = (0,-s)
        u = mul(mat(d,e), u)
    return u
