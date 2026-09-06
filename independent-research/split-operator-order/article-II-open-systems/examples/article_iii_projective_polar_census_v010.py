#!/usr/bin/env python3
"""Projective/polar support-frame census for Article III.

Requires article_iii_conditioning_common_v010.py in the same directory.
The script removes face amplitude, then optionally removes within-face singular
weighting, and compares sharp/oversampled Coxeter designs in d=3 and d=4.

No asymptotic theorem is claimed from these low-dimensional calculations.
"""

from __future__ import annotations

import itertools
import math
import numpy as np

from article_iii_conditioning_common_v010 import (
    closed_form_whitener,
    coxeter_loop,
    d4_gates,
    measurement_block,
    qutrit_gates,
    traceless_hermitian_basis,
)

LOOPS = {
    "b01": tuple([0, 1] * 3),
    "b12": tuple([1, 2] * 3),
    "c02": (0, 2, 0, 2),
}


def build_pool(d, gates):
    fs = traceless_hermitian_basis(d)
    w, _ = closed_form_whitener(d, fs)
    pool = []
    for perm in itertools.permutations(range(4)):
        for name, gens in LOOPS.items():
            raw = measurement_block(coxeter_loop(gates, perm, gens), fs)
            one = (raw @ w) / math.sqrt(d)
            energy = float(np.linalg.norm(one, "fro") ** 2)
            b = one / math.sqrt(energy)
            q = b.T @ b

            u, s, vh = np.linalg.svd(b, full_matrices=False)
            rank = int(np.sum(s > 1e-10 * s[0]))
            p = vh[:rank].T @ vh[:rank]
            r = p / rank

            pool.append({
                "perm": tuple(perm),
                "type": name,
                "energy": energy,
                "rank": rank,
                "Q": q,
                "R": r,
                "purity": float(np.trace(q @ q)),
            })
    return pool


def find(pool, perm, typ):
    for i, x in enumerate(pool):
        if x["perm"] == tuple(perm) and x["type"] == typ:
            return i
    raise KeyError((perm, typ))


def stats(pool, inds, key):
    s = sum(pool[i][key] for i in inds) / len(inds)
    ev = np.linalg.eigvalsh(s)
    n = s.shape[0]
    a = float(ev[0])
    b = float(ev[-1])
    eta = n * a
    kappa = math.sqrt(b / a) if a > 1e-15 else float("inf")
    delta = float(np.linalg.norm(s - np.eye(n) / n, "fro") / ((1 / n) * math.sqrt(n)))
    return {
        "L": len(inds), "A": a, "B": b, "eta": eta,
        "kappa": kappa, "delta": delta, "trace": float(np.trace(s)),
    }


def greedy_add(pool, start, target, key="R"):
    inds = list(start)
    hist = [stats(pool, inds, key)]
    while len(inds) < target:
        used = set(inds)
        best = None
        for i in range(len(pool)):
            if i in used:
                continue
            st = stats(pool, inds + [i], key)
            score = st["A"]
            if best is None or score > best[0]:
                best = (score, i, st)
        inds.append(best[1])
        hist.append(best[2])
    return inds, hist


def random_sharp_search(pool, l, samples, seed, key="Q"):
    rng = np.random.default_rng(seed)
    best = None
    for _ in range(samples):
        inds = tuple(sorted(rng.choice(len(pool), size=l, replace=False).tolist()))
        st = stats(pool, inds, key)
        if best is None or st["A"] > best[0]:
            best = (st["A"], inds, st)
    return list(best[1]), best[2]


def show(label, pool, inds, key):
    st = stats(pool, inds, key)
    print(label, key, st)
    print("  faces:")
    for i in inds:
        x = pool[i]
        print("   ", x["perm"], x["type"], f"E={x['energy']:.12g}", f"rank={x['rank']}")


def main():
    p3 = build_pool(3, qutrit_gates())
    p4 = build_pool(4, d4_gates())

    print("POOL FACE-RANKS")
    for d, pool in ((3, p3), (4, p4)):
        ranks = sorted({x["rank"] for x in pool})
        print("d=", d, "ranks=", {r: sum(x["rank"] == r for x in pool) for r in ranks})

    # d=3 projective sharp search, then polar oversampling from the same seed.
    d3sharp, _ = random_sharp_search(p3, 4, 5000, 260906, key="Q")
    show("d3 projective sharp", p3, d3sharp, "Q")
    show("d3 polar sharp", p3, d3sharp, "R")
    d3over, d3hist = greedy_add(p3, d3sharp, 12, key="R")
    print("d3 polar greedy oversampling")
    for st in d3hist:
        print(st)

    # d=4 Article-II sharp witness with the known one-face replacement.
    d4_specs = [
        ((0, 1, 2, 3), "b01"),
        ((0, 1, 2, 3), "b12"),
        ((0, 1, 3, 2), "b01"),
        ((0, 2, 3, 1), "b01"),
        ((1, 2, 0, 3), "c02"),
        ((1, 2, 3, 0), "b01"),
        ((2, 0, 1, 3), "b12"),
        ((3, 0, 1, 2), "b12"),
    ]
    d4sharp = [find(p4, *s) for s in d4_specs]
    show("d4 projective sharp", p4, d4sharp, "Q")
    show("d4 polar sharp", p4, d4sharp, "R")
    d4over, d4hist = greedy_add(p4, d4sharp, 14, key="R")
    print("d4 polar greedy oversampling")
    for st in d4hist:
        print(st)

    print("ARTICLE_III_PROJECTIVE_POLAR_CENSUS_OK")


if __name__ == "__main__":
    main()
