#!/usr/bin/env python3
"""Response-independent P5 diagnostic for the frozen RC02 predictor dictionary.

The script reconstructs the exact RC02 grid, cubic nuisance subspace,
integer q-curvature predictors, half-integer controls, and frozen pairing.
It computes high-precision Gram and cross-Gram geometry without loading any
pilot, calibration, or confirmatory carrier response.

This is a high-precision reproducibility calculation, not interval arithmetic.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path
from typing import Iterable

import mpmath as mp

INTEGER_MODES = tuple(range(2, 11))
CONTROL_MODES = tuple(mp.mpf("1.5") + i for i in range(9))
FROZEN_PAIRS = (
    (2, mp.mpf("6.5")),
    (3, mp.mpf("8.5")),
    (4, mp.mpf("7.5")),
    (5, mp.mpf("9.5")),
    (6, mp.mpf("1.5")),
    (7, mp.mpf("3.5")),
    (8, mp.mpf("2.5")),
    (9, mp.mpf("5.5")),
    (10, mp.mpf("4.5")),
)


def mp_text(value: mp.mpf, digits: int = 50) -> str:
    return mp.nstr(value, digits)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def build_grid() -> tuple[list[mp.mpf], list[mp.mpf], list[mp.mpf]]:
    eta = [mp.mpf("0.6") + mp.mpf("0.0005") * i for i in range(1101)]
    theta = [mp.pi * e / 12 for e in eta]
    x = [2 * (e - mp.mpf("0.6")) / mp.mpf("0.55") - 1 for e in eta]
    return eta, theta, x


def cubic_projector_data(x: list[mp.mpf]) -> tuple[list[list[mp.mpf]], mp.matrix]:
    design = [[mp.mpf(1), z, z * z, z * z * z] for z in x]
    gram = mp.matrix(4, 4)
    for i in range(4):
        for j in range(4):
            gram[i, j] = mp.fsum(row[i] * row[j] for row in design)
    return design, gram ** -1


def residual_atom(
    frequency: mp.mpf,
    theta: list[mp.mpf],
    design: list[list[mp.mpf]],
    inverse_design_gram: mp.matrix,
) -> tuple[list[mp.mpf], mp.mpf]:
    f = mp.mpf(frequency)
    values = [-(f * f) / mp.sin(f * t) ** 2 + 1 / mp.sin(t) ** 2 for t in theta]
    rhs = mp.matrix(4, 1)
    for j in range(4):
        rhs[j] = mp.fsum(design[i][j] * values[i] for i in range(len(values)))
    coefficients = inverse_design_gram * rhs
    residual = [
        values[i] - mp.fsum(design[i][j] * coefficients[j] for j in range(4))
        for i in range(len(values))
    ]
    norm = mp.sqrt(mp.fsum(v * v for v in residual))
    if norm == 0:
        raise RuntimeError(f"degenerate residual atom at frequency {frequency}")
    return [v / norm for v in residual], norm


def gram(left: list[list[mp.mpf]], right: list[list[mp.mpf]]) -> mp.matrix:
    result = mp.matrix(len(left), len(right))
    sample_count = len(left[0])
    for i, u in enumerate(left):
        for j, v in enumerate(right):
            result[i, j] = mp.fsum(u[k] * v[k] for k in range(sample_count))
    return result


def write_matrix(path: Path, matrix: mp.matrix, digits: int = 50) -> None:
    with path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.writer(stream)
        for i in range(matrix.rows):
            writer.writerow([mp_text(matrix[i, j], digits) for j in range(matrix.cols)])


def spectral_norm_symmetric(matrix: mp.matrix) -> mp.mpf:
    eigenvalues, _ = mp.eigsy(matrix)
    return max(abs(value) for value in eigenvalues)


def singular_norm(matrix: mp.matrix) -> mp.mpf:
    eigenvalues, _ = mp.eigsy(matrix.T * matrix)
    return mp.sqrt(max(eigenvalues))


def effective_rank(eigenvalues: Iterable[mp.mpf], threshold: str) -> int:
    cutoff = mp.mpf(threshold)
    return sum(1 for value in eigenvalues if value > cutoff)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dps", type=int, default=80)
    parser.add_argument("--output-dir", type=Path, default=Path("results"))
    args = parser.parse_args()
    mp.mp.dps = args.dps
    args.output_dir.mkdir(parents=True, exist_ok=True)

    _, theta, x = build_grid()
    design, inverse_design_gram = cubic_projector_data(x)

    integer_atoms: list[list[mp.mpf]] = []
    control_atoms: list[list[mp.mpf]] = []
    integer_residual_norms: list[mp.mpf] = []
    control_residual_norms: list[mp.mpf] = []

    for mode in INTEGER_MODES:
        atom, norm = residual_atom(mp.mpf(mode), theta, design, inverse_design_gram)
        integer_atoms.append(atom)
        integer_residual_norms.append(norm)
    for mode in CONTROL_MODES:
        atom, norm = residual_atom(mode, theta, design, inverse_design_gram)
        control_atoms.append(atom)
        control_residual_norms.append(norm)

    g_ii = gram(integer_atoms, integer_atoms)
    g_cc = gram(control_atoms, control_atoms)
    g_ic = gram(integer_atoms, control_atoms)

    eig_ii, _ = mp.eigsy(g_ii)
    eig_cc, _ = mp.eigsy(g_cc)
    inv_ii = g_ii ** -1

    leave_one_out = {
        str(mode): mp.sqrt(1 / inv_ii[index, index])
        for index, mode in enumerate(INTEGER_MODES)
    }

    integer_row_geometry = {}
    for i, mode in enumerate(INTEGER_MODES):
        candidates = [
            (abs(g_ii[i, j]), INTEGER_MODES[j])
            for j in range(len(INTEGER_MODES))
            if j != i
        ]
        overlap, neighbor = max(candidates)
        integer_row_geometry[str(mode)] = {
            "nearest_integer_mode": neighbor,
            "maximum_absolute_overlap": mp_text(overlap),
            "projective_distance": mp_text(mp.sqrt(1 - overlap * overlap)),
            "leave_one_out_distance": mp_text(leave_one_out[str(mode)]),
        }

    cross_rows = {}
    for i, mode in enumerate(INTEGER_MODES):
        ranked = sorted(
            [(abs(g_ic[i, j]), CONTROL_MODES[j]) for j in range(len(CONTROL_MODES))],
            reverse=True,
        )
        cross_rows[str(mode)] = [
            {
                "control": mp_text(control, 8),
                "absolute_overlap": mp_text(overlap),
                "projective_distance": mp_text(mp.sqrt(1 - overlap * overlap)),
            }
            for overlap, control in ranked
        ]

    paired = []
    for mode, control in FROZEN_PAIRS:
        i = INTEGER_MODES.index(mode)
        j = CONTROL_MODES.index(control)
        overlap = abs(g_ic[i, j])
        distance = mp.sqrt(1 - overlap * overlap)
        paired.append(
            {
                "integer_mode": mode,
                "control_mode": mp_text(control, 8),
                "absolute_overlap": mp_text(overlap),
                "projective_distance": mp_text(distance),
                "contrast_operator_norm": mp_text(distance),
            }
        )

    paired_by_capacity = sorted(
        paired, key=lambda row: mp.mpf(row["contrast_operator_norm"]), reverse=True
    )
    for rank, row in enumerate(paired_by_capacity, start=1):
        row["capacity_rank_descending"] = rank

    permutation = [INTEGER_MODES.index(12 - mode) for mode in INTEGER_MODES]
    p = mp.matrix(len(INTEGER_MODES))
    for i, j in enumerate(permutation):
        p[i, j] = 1
    reflection_difference = g_ii - p * g_ii * p.T
    reflection_operator_defect = spectral_norm_symmetric(reflection_difference)
    reflection_frobenius_defect = mp.sqrt(
        mp.fsum(reflection_difference[i, j] ** 2 for i in range(9) for j in range(9))
    )

    columns: list[list[mp.mpf]] = []
    root2 = mp.sqrt(2)
    for mode in (2, 3, 4, 5):
        col = [mp.mpf(0)] * 9
        col[INTEGER_MODES.index(mode)] = 1 / root2
        col[INTEGER_MODES.index(12 - mode)] = 1 / root2
        columns.append(col)
    fixed = [mp.mpf(0)] * 9
    fixed[INTEGER_MODES.index(6)] = 1
    columns.append(fixed)
    for mode in (2, 3, 4, 5):
        col = [mp.mpf(0)] * 9
        col[INTEGER_MODES.index(mode)] = 1 / root2
        col[INTEGER_MODES.index(12 - mode)] = -1 / root2
        columns.append(col)
    transform = mp.matrix(9, 9)
    for j, column in enumerate(columns):
        for i, value in enumerate(column):
            transform[i, j] = value
    adapted = transform.T * g_ii * transform
    mixing = adapted[:5, 5:]
    sector_mixing_norm = singular_norm(mixing)

    results = {
        "schema_version": "1.0",
        "contract": "BC-IDPR-P5-UA01-D0",
        "status": "HIGH_PRECISION_RESPONSE_INDEPENDENT_DIAGNOSTIC_COMPLETE",
        "arithmetic": {
            "backend": "mpmath",
            "decimal_digits": args.dps,
            "interval_certified": False,
        },
        "protocol": {
            "response_data_loaded": False,
            "eta_grid": {"start": "0.6", "stop": "1.15", "step": "0.0005", "count": 1101},
            "baseline": ["1", "x", "x^2", "x^3"],
            "projection": "unweighted discrete least squares",
            "normalization": "unit L2 after cubic projection",
            "integer_modes": list(INTEGER_MODES),
            "control_modes": [mp_text(value, 8) for value in CONTROL_MODES],
        },
        "integer_gram": {
            "eigenvalues_ascending": [mp_text(value) for value in eig_ii],
            "condition_number": mp_text(eig_ii[eig_ii.rows - 1] / eig_ii[0]),
            "effective_ranks": {
                threshold: effective_rank(eig_ii, threshold)
                for threshold in ("1e-12", "1e-10", "1e-8", "1e-6")
            },
            "rows": integer_row_geometry,
            "residual_norms": {
                str(mode): mp_text(norm)
                for mode, norm in zip(INTEGER_MODES, integer_residual_norms)
            },
        },
        "control_gram": {
            "eigenvalues_ascending": [mp_text(value) for value in eig_cc],
            "condition_number": mp_text(eig_cc[eig_cc.rows - 1] / eig_cc[0]),
            "effective_ranks": {
                threshold: effective_rank(eig_cc, threshold)
                for threshold in ("1e-12", "1e-10", "1e-8", "1e-6")
            },
            "residual_norms": {
                mp_text(mode, 8): mp_text(norm)
                for mode, norm in zip(CONTROL_MODES, control_residual_norms)
            },
        },
        "cross_gram": {
            "rows_ranked_by_absolute_overlap": cross_rows,
            "frozen_pairs_by_mode": paired,
            "frozen_pairs_by_contrast_capacity": paired_by_capacity,
            "maximum_frozen_paired_absolute_overlap": mp_text(
                max(mp.mpf(row["absolute_overlap"]) for row in paired)
            ),
            "minimum_frozen_paired_projective_distance": mp_text(
                min(mp.mpf(row["projective_distance"]) for row in paired)
            ),
        },
        "reflection": {
            "operator_defect": mp_text(reflection_operator_defect),
            "frobenius_defect": mp_text(reflection_frobenius_defect),
            "symmetry_sector_mixing_norm": mp_text(sector_mixing_norm),
        },
        "decisions": {
            "predictor_only_mode5_isolation": "NOT_SUPPORTED",
            "mode5_leave_one_out_rank_ascending": 2,
            "mode5_frozen_pair_contrast_capacity_rank_descending": 2,
            "mode5_frozen_control_is_nearest_control": False,
            "frozen_assignment_bottleneck_mode": 6,
            "mechanism_localization": "RESPONSE_ALIGNMENT_OR_ADDITIONAL_CARRIER_STRUCTURE_REQUIRED",
            "claim_ceiling": "finite frozen RC02 dictionary only",
        },
    }

    matrix_paths = {
        "GII": args.output_dir / "GII.csv",
        "GCC": args.output_dir / "GCC.csv",
        "GIC": args.output_dir / "GIC.csv",
    }
    write_matrix(matrix_paths["GII"], g_ii)
    write_matrix(matrix_paths["GCC"], g_cc)
    write_matrix(matrix_paths["GIC"], g_ic)

    result_path = args.output_dir / "P5_MODE5_GRAM_RESULTS.json"
    result_path.write_text(json.dumps(results, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    manifest = {
        "schema_version": "1.0",
        "files": {
            path.name: {"sha256": sha256(path), "bytes": path.stat().st_size}
            for path in [result_path, *matrix_paths.values()]
        },
    }
    manifest_path = args.output_dir / "MANIFEST.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    print(json.dumps(results["decisions"], indent=2))


if __name__ == "__main__":
    main()
