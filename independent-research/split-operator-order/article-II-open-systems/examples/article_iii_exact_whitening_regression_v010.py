#!/usr/bin/env python3
"""Regression test for the Article III exact closed-form whitening theorem.

Reconstructs the published/archived Article-II baseline designs for d=3,4,5
using real/complex arithmetic, applies the theorem-level projector whitener,
and checks the normalized singular data against independently reproduced
full-double-precision reference values.

This script is metric/reproducibility code. It does not turn the small-d
conditioning values into an asymptotic theorem.
"""

import numpy as np

from article_iii_conditioning_common_v010 import (
    closed_form_whitener,
    conditioning_stats,
    coxeter_loop,
    d4_gates,
    engineered_square,
    from_ops_real,
    measurement_block,
    normalize_design,
    qutrit_gates,
    traceless_hermitian_basis,
)
from exact_face_rank_certificate_d5_v010 import OPS as D5_OPS


EXPECTED = {
    3: {
        "sigma_min": 0.12173880409571293,
        "sigma_max": 4.59941043232095,
        "kappa": 37.780972685626374,
        "A": 0.014820336422654371,
    },
    4: {
        "sigma_min": 0.0535512399868459,
        "sigma_max": 4.3512436874946685,
        "kappa": 81.25383629890717,
        "A": 0.002867735304128763,
    },
    5: {
        "sigma_min": 0.03978665131344871,
        "sigma_max": 4.843628225780513,
        "kappa": 121.74003254562082,
        "A": 0.00158297762273795,
    },
}


def d3_blocks(fs):
    u = qutrit_gates()
    specs = [
        ((0, 1, 2, 3), [0, 1] * 3),
        ((0, 1, 2, 3), [1, 2] * 3),
        ((0, 1, 2, 3), [0, 2, 0, 2]),
        ((0, 1, 3, 2), [0, 1] * 3),
    ]
    return [measurement_block(coxeter_loop(u, p, g), fs) for p, g in specs]


def d4_blocks(fs):
    u = d4_gates()
    b01 = [0, 1] * 3
    b12 = [1, 2] * 3
    specs = [
        ((0, 1, 2, 3), b01),
        ((0, 1, 2, 3), b12),
        ((0, 1, 3, 2), b01),
        ((0, 2, 3, 1), b01),
        ((1, 0, 2, 3), b12),
        ((1, 2, 3, 0), b01),
        ((2, 0, 1, 3), b12),
        ((3, 0, 1, 2), b12),
    ]
    return [measurement_block(coxeter_loop(u, p, g), fs) for p, g in specs]


def d5_blocks(fs):
    blocks = []
    for ou, ov in D5_OPS:
        u = from_ops_real(5, ou)
        v = from_ops_real(5, ov)
        blocks.append(measurement_block(engineered_square(u, v), fs))
    return blocks


def close(a, b, atol=5e-11, rtol=5e-10):
    return abs(a - b) <= atol + rtol * abs(b)


def run_dimension(d, block_builder):
    fs = traceless_hermitian_basis(d)
    w, diag = closed_form_whitener(d, fs)

    assert diag["theorem_error"] < 1e-10
    assert diag["projector_error"] < 1e-10
    assert diag["whitening_error"] < 1e-10

    blocks = block_builder(fs)
    m = normalize_design(blocks, d, w)
    stats = conditioning_stats(m)

    q = d * d - 1
    assert stats["cols"] == q * q
    assert stats["rank"] == q * q

    exp = EXPECTED[d]
    assert close(stats["sigma_min"], exp["sigma_min"])
    assert close(stats["sigma_max"], exp["sigma_max"])
    assert close(stats["kappa"], exp["kappa"])
    assert close(stats["A"], exp["A"])

    print(
        f"d={d} faces={len(blocks)} shape={stats['rows']}x{stats['cols']} "
        f"rank={stats['rank']} sigma_min={stats['sigma_min']:.15g} "
        f"sigma_max={stats['sigma_max']:.15g} kappa={stats['kappa']:.15g} "
        f"A={stats['A']:.15g} theorem_err={diag['theorem_error']:.3e} "
        f"white_err={diag['whitening_error']:.3e}"
    )


if __name__ == "__main__":
    run_dimension(3, d3_blocks)
    run_dimension(4, d4_blocks)
    run_dimension(5, d5_blocks)
    print("ARTICLE_III_EXACT_WHITENING_REGRESSION_OK")
