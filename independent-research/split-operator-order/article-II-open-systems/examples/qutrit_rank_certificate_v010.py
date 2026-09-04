#!/usr/bin/env python3
"""Exact qutrit full-rank certificate for Article II v0.1.

Builds the 72 x 64 first-order holonomy measurement matrix over Q(i)
for the four-face qutrit design declared in GENERAL-RANK-CRITERION-v0.1.md,
projects to real/imaginary rational coordinates, and certifies full column
rank by row reduction modulo p=1000003.

A full-rank reduction modulo a prime not dividing any denominator proves
that a 64 x 64 rational minor is nonzero, hence rank_Q = 64.
"""

from fractions import Fraction as F

P = 1000003


def z(a=0, b=0):
    return (F(a), F(b))


def za(x, y):
    return (x[0] + y[0], x[1] + y[1])


def zn(x):
    return (-x[0], -x[1])


def zm(x, y):
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def zc(x):
    return (x[0], -x[1])


def zz(x):
    return x[0] == 0 and x[1] == 0


def mat0(n=3):
    return [[z() for _ in range(n)] for __ in range(n)]


def eye(n=3):
    m = mat0(n)
    for i in range(n):
        m[i][i] = z(1)
    return m


def madd(a, b):
    return [[za(a[i][j], b[i][j]) for j in range(len(a[0]))] for i in range(len(a))]


def mneg(a):
    return [[zn(v) for v in row] for row in a]


def msub(a, b):
    return madd(a, mneg(b))


def mmul(a, b):
    n, p, m = len(a), len(b), len(b[0])
    c = [[z() for _ in range(m)] for __ in range(n)]
    for i in range(n):
        for k in range(p):
            aik = a[i][k]
            if zz(aik):
                continue
            for j in range(m):
                if not zz(b[k][j]):
                    c[i][j] = za(c[i][j], zm(aik, b[k][j]))
    return c


def dag(a):
    return [[zc(a[j][i]) for j in range(len(a))] for i in range(len(a[0]))]


def mscale(c, a):
    return [[zm(c, v) for v in row] for row in a]


def comm(a, b):
    return msub(mmul(a, b), mmul(b, a))


def word(u, perm):
    w = eye()
    for idx in perm:
        w = mmul(w, u[idx])
    return w


def swap_pos(perm, i):
    q = list(perm)
    q[i], q[i + 1] = q[i + 1], q[i]
    return tuple(q)


def edge(u, perm, i):
    q = swap_pos(perm, i)
    return mmul(word(u, q), dag(word(u, perm))), q


def loop(u, perm, generators):
    t = []
    cur = perm
    for g in generators:
        e, cur = edge(u, cur, g)
        t.append(e)
    assert cur == perm
    return t


def gamma(cmat, fs, x, y):
    out = mat0()
    ax = [comm(fa, x) for fa in fs]
    yb = [comm(y, fb) for fb in fs]
    for a in range(len(fs)):
        for b in range(len(fs)):
            cab = cmat[a][b]
            if not zz(cab):
                out = madd(out, mscale(cab, mmul(ax[a], yb[b])))
    return out


def loop_coeff(cmat, fs, t):
    m = len(t)
    pref = [eye()]
    for k in range(1, m + 1):
        pref.append(mmul(t[k - 1], pref[k - 1]))
    out = mat0()
    for k in range(2, m + 1):
        left = eye()
        for j in range(m, k, -1):
            left = mmul(left, t[j - 1])
        out = madd(out, mneg(mmul(left, gamma(cmat, fs, t[k - 1], pref[k - 1]))))
    return out


def hermitian_kossakowski_basis(q=8):
    basis = []
    for a in range(q):
        c = [[z() for _ in range(q)] for __ in range(q)]
        c[a][a] = z(1)
        basis.append(c)
    for a in range(q):
        for b in range(a + 1, q):
            c = [[z() for _ in range(q)] for __ in range(q)]
            c[a][b] = c[b][a] = z(1)
            basis.append(c)
            c = [[z() for _ in range(q)] for __ in range(q)]
            c[a][b], c[b][a] = z(0, 1), z(0, -1)
            basis.append(c)
    return basis


def traceless_hermitian_basis():
    fs = []
    for j in range(3):
        for k in range(j + 1, 3):
            m = mat0(); m[j][k] = m[k][j] = z(1); fs.append(m)
            m = mat0(); m[j][k] = z(0, -1); m[k][j] = z(0, 1); fs.append(m)
    m = mat0(); m[0][0], m[1][1] = z(1), z(-1); fs.append(m)
    m = mat0(); m[1][1], m[2][2] = z(1), z(-1); fs.append(m)
    return fs


def qutrit_gates():
    x = mat0(); x[1][0] = x[2][1] = x[0][2] = z(1)
    d = mat0(); d[0][0], d[1][1], d[2][2] = z(1), z(0, 1), z(-1)
    r12 = mat0(); r12[0][0], r12[0][1] = z(F(3, 5)), z(F(4, 5))
    r12[1][0], r12[1][1], r12[2][2] = z(F(-4, 5)), z(F(3, 5)), z(1)
    r23 = mat0(); r23[0][0] = z(1)
    r23[1][1], r23[1][2] = z(F(3, 5)), z(F(4, 5))
    r23[2][1], r23[2][2] = z(F(-4, 5)), z(F(3, 5))
    return [x, d, r12, r23]


def rank_mod(matrix, p):
    m = [row[:] for row in matrix]
    nr, nc, r = len(m), len(m[0]), 0
    for c in range(nc):
        pivot = next((i for i in range(r, nr) if m[i][c] % p), None)
        if pivot is None:
            continue
        m[r], m[pivot] = m[pivot], m[r]
        inv = pow(m[r][c], p - 2, p)
        m[r] = [(v * inv) % p for v in m[r]]
        for i in range(nr):
            if i != r and m[i][c] % p:
                f = m[i][c] % p
                m[i] = [(m[i][j] - f * m[r][j]) % p for j in range(nc)]
        r += 1
        if r == nc:
            break
    return r


def main():
    fs = traceless_hermitian_basis()
    u = qutrit_gates()
    specs = [
        ((0, 1, 2, 3), [0, 1] * 3),
        ((0, 1, 2, 3), [1, 2] * 3),
        ((0, 1, 2, 3), [0, 2, 0, 2]),
        ((0, 1, 3, 2), [0, 1] * 3),
    ]
    loops = [loop(u, perm, gens) for perm, gens in specs]
    cols = []
    for cmat in hermitian_kossakowski_basis():
        vals = []
        for t in loops:
            k = loop_coeff(cmat, fs, t)
            vals += [k[i][j][0] for i in range(3) for j in range(3)]
            vals += [k[i][j][1] for i in range(3) for j in range(3)]
        cols.append(vals)
    a = [[cols[c][r] for c in range(64)] for r in range(72)]
    a_mod = [
        [(v.numerator % P) * pow(v.denominator % P, P - 2, P) % P for v in row]
        for row in a
    ]
    rank = rank_mod(a_mod, P)
    print(f"rows=72 cols=64 prime={P} rank_mod_p={rank}")
    assert rank == 64
    print("CERTIFIED_FULL_COLUMN_RANK_OVER_Q")


if __name__ == "__main__":
    main()
