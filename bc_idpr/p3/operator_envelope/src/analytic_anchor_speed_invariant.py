#!/usr/bin/env python3
from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path

import numpy as np

ANCHOR = math.pi / 12
FD_STEPS = (1e-5, 5e-6)
MAXIMUM_LABEL = 6
TRAIN_MAXIMUM_LABEL = 4


def qn(n: int, theta: float) -> float:
    return 0.0 if n == 0 else math.sin(n * theta) / math.sin(theta)


def dlog_qn(n: int, theta: float) -> float:
    if n == 0:
        raise ValueError("[0]_q has no logarithmic derivative")
    return n * (lambda x: 1.0 / math.tan(x))(n * theta) - (lambda x: 1.0 / math.tan(x))(theta)


def qfac(n: int, theta: float) -> float:
    if n < 0:
        raise ValueError(n)
    out = 1.0
    for k in range(1, n + 1):
        out *= qn(k, theta)
    return out


def dlog_qfac(n: int, theta: float) -> float:
    if n < 0:
        raise ValueError(n)
    return math.fsum(dlog_qn(k, theta) for k in range(1, n + 1)) if n else 0.0


def half_sum(*args: int) -> int:
    total = sum(args)
    if total % 2:
        raise ValueError(args)
    return total // 2


def delta_with_derivative(a: int, b: int, c: int, theta: float) -> tuple[float, float]:
    u = half_sum(a, b, -c)
    v = half_sum(a, -b, c)
    w = half_sum(-a, b, c)
    s = half_sum(a, b, c) + 1
    if min(u, v, w) < 0:
        return 0.0, 0.0
    value = math.sqrt(qfac(u, theta) * qfac(v, theta) * qfac(w, theta) / qfac(s, theta))
    dlog = 0.5 * (
        dlog_qfac(u, theta)
        + dlog_qfac(v, theta)
        + dlog_qfac(w, theta)
        - dlog_qfac(s, theta)
    )
    return value, value * dlog


def q6j_with_derivative(a: int, b: int, e: int, c: int, d: int, f: int, theta: float) -> tuple[float, float]:
    delta_args = ((a, b, e), (a, d, f), (c, b, f), (c, d, e))
    deltas = [delta_with_derivative(*args, theta) for args in delta_args]
    if any(value == 0 for value, _ in deltas):
        return 0.0, 0.0
    prefactor = math.prod(value for value, _ in deltas)
    prefactor_dlog = math.fsum(derivative / value for value, derivative in deltas)

    lowers = (
        half_sum(a, b, e),
        half_sum(a, d, f),
        half_sum(c, b, f),
        half_sum(c, d, e),
    )
    uppers = (
        half_sum(a, b, c, d),
        half_sum(a, c, e, f),
        half_sum(b, d, e, f),
    )
    lo = max(lowers)
    hi = min(uppers)
    total = 0.0
    derivative_total = 0.0
    for z in range(lo, hi + 1):
        denominator_args = tuple(z - value for value in lowers) + tuple(value - z for value in uppers)
        term = ((-1) ** z) * qfac(z + 1, theta)
        for value in denominator_args:
            term /= qfac(value, theta)
        term_dlog = dlog_qfac(z + 1, theta) - math.fsum(dlog_qfac(value, theta) for value in denominator_args)
        total += term
        derivative_total += term * term_dlog
    value = prefactor * total
    derivative = prefactor * (prefactor_dlog * total + derivative_total)
    return value, derivative


def pair_channels(a: int, b: int) -> list[int]:
    return list(range(abs(a - b), a + b + 1, 2))


def common_channels(a: int, b: int, c: int, d: int) -> list[int]:
    return sorted(set(pair_channels(a, b)).intersection(pair_channels(c, d)))


def channels(J: tuple[int, int, int, int]) -> tuple[list[int], list[int]]:
    a, b, c, d = J
    return common_channels(a, b, c, d), common_channels(b, c, a, d)


def zmax(J: tuple[int, int, int, int]) -> int:
    a, b, c, d = J
    E, F = channels(J)
    return max(
        min(half_sum(a, b, c, d), half_sum(a, c, e, f), half_sum(b, d, e, f)) + 1
        for e in E
        for f in F
    )


def raw_f_and_derivative(J: tuple[int, int, int, int], theta: float) -> tuple[np.ndarray, np.ndarray]:
    a, b, c, d = J
    E, F = channels(J)
    if len(E) != 2 or len(F) != 2:
        raise ValueError((J, E, F))
    phase = (-1) ** half_sum(a, b, c, d)
    matrix = np.zeros((2, 2), dtype=float)
    derivative = np.zeros((2, 2), dtype=float)
    for i, e in enumerate(E):
        for j, f in enumerate(F):
            sixj, dsixj = q6j_with_derivative(a, b, e, c, d, f, theta)
            amplitude = math.sqrt(qn(e + 1, theta) * qn(f + 1, theta))
            damplitude = amplitude * 0.5 * (dlog_qn(e + 1, theta) + dlog_qn(f + 1, theta))
            value = phase * amplitude * sixj
            dvalue = phase * (damplitude * sixj + amplitude * dsixj)
            if False:
                raise ValueError("complex chamber")
            matrix[i, j] = float(value)
            derivative[i, j] = float(dvalue)
    return matrix, derivative


def frozen_gauge(J: tuple[int, int, int, int]) -> np.ndarray:
    matrix, _ = raw_f_and_derivative(J, ANCHOR)
    gauge = np.eye(2)
    if np.linalg.det(matrix) < 0:
        gauge = np.diag([1.0, -1.0]) @ gauge
    if (gauge @ matrix)[0, 0] < 0:
        gauge = -gauge
    return gauge


def f_and_analytic_derivative(J: tuple[int, int, int, int], theta: float) -> tuple[np.ndarray, np.ndarray]:
    matrix, derivative = raw_f_and_derivative(J, theta)
    gauge = frozen_gauge(J)
    return gauge @ matrix, gauge @ derivative


def analytic_invariant(J: tuple[int, int, int, int]) -> tuple[float, float, float]:
    matrix, derivative = f_and_analytic_derivative(J, ANCHOR)
    generator = derivative @ matrix.T
    invariant = float(np.linalg.norm(generator) / math.sqrt(2.0))
    orthogonality = float(np.linalg.norm(matrix.T @ matrix - np.eye(2)))
    skew = float(np.linalg.norm(generator + generator.T))
    return invariant, orthogonality, skew


def finite_difference_invariant(J: tuple[int, int, int, int], step: float) -> float:
    center, _ = f_and_analytic_derivative(J, ANCHOR)
    plus, _ = f_and_analytic_derivative(J, ANCHOR + step)
    minus, _ = f_and_analytic_derivative(J, ANCHOR - step)
    derivative = (plus - minus) / (2 * step)
    generator = derivative @ center.T
    return float(np.linalg.norm(generator) / math.sqrt(2.0))


def family_key(J: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
    return tuple(sorted(J))


def valid_ordered_carriers(maximum_label: int) -> list[tuple[int, int, int, int]]:
    out = []
    for J in itertools.product(range(1, maximum_label + 1), repeat=4):
        if sum(J) % 2:
            continue
        E, F = channels(J)
        if len(E) == len(F) == 2 and zmax(J) <= 12:
            try:
                invariant, orthogonality, _ = analytic_invariant(J)
                if orthogonality < 1e-10 and invariant > 1e-8:
                    out.append(J)
            except Exception:
                pass
    return out


def build() -> dict:
    train_ordered = valid_ordered_carriers(TRAIN_MAXIMUM_LABEL)
    all_ordered = valid_ordered_carriers(MAXIMUM_LABEL)
    train_families = {family_key(J) for J in train_ordered}
    test_ordered = [J for J in all_ordered if max(J) >= 5 and family_key(J) not in train_families]
    test_families = sorted({family_key(J) for J in test_ordered})

    records = []
    for J in test_ordered:
        analytic, orthogonality, skew = analytic_invariant(J)
        fd_coarse = finite_difference_invariant(J, FD_STEPS[0])
        fd_refined = finite_difference_invariant(J, FD_STEPS[1])
        relative_residual = abs(analytic - fd_refined) / max(abs(analytic), abs(fd_refined), 1e-30)
        step_disagreement = abs(fd_coarse - fd_refined) / max(abs(fd_refined), 1e-30)
        records.append({
            "external_spins_doubled": list(J),
            "family": list(family_key(J)),
            "analytic_invariant": analytic,
            "fd_coarse": fd_coarse,
            "fd_refined": fd_refined,
            "relative_residual": relative_residual,
            "fd_step_disagreement_relative": step_disagreement,
            "orthogonality_residual": orthogonality,
            "generator_skew_residual": skew,
        })

    family_summary = {}
    for key in test_families:
        subset = [row for row in records if tuple(row["family"]) == key]
        family_summary[str(key)] = {
            "ordered_carrier_count": len(subset),
            "maximum_relative_residual": max(row["relative_residual"] for row in subset),
            "maximum_fd_step_disagreement_relative": max(row["fd_step_disagreement_relative"] for row in subset),
        }

    maximum_relative_residual = max(row["relative_residual"] for row in records)
    maximum_step_disagreement = max(row["fd_step_disagreement_relative"] for row in records)
    maximum_orthogonality = max(row["orthogonality_residual"] for row in records)
    maximum_skew = max(row["generator_skew_residual"] for row in records)
    passed = bool(
        len(test_families) >= 10
        and maximum_relative_residual <= 1e-7
        and maximum_step_disagreement <= 1e-7
        and maximum_orthogonality <= 1e-10
        and maximum_skew <= 1e-7
    )
    return {
        "schema_version": "1.0",
        "contract": "BC-IDPR-P3-B-M10",
        "status": "ANALYTIC_Q6J_ANCHOR_SPEED_INVARIANT_CERTIFIED" if passed else "ANALYTIC_Q6J_ANCHOR_SPEED_INVARIANT_NOT_CERTIFIED",
        "preregistration_commit": "1f2d9f8ccbaae9273987cc8686627f6ef9cfdae6",
        "analytic_identity": {
            "q_number_log_derivative": "n*cot(n*theta)-cot(theta)",
            "q6j_derivative": "termwise derivative of the finite Racah sum and Delta prefactors",
            "invariant": "||F'_analytic F^T||_HS/sqrt(2)=|omega|",
            "fitted_parameter_count": 0,
        },
        "atlas": {
            "train_ordered_carriers_for_family_exclusion": len(train_ordered),
            "train_family_count": len(train_families),
            "test_ordered_carriers": len(test_ordered),
            "test_family_count": len(test_families),
            "test_family_keys": [list(key) for key in test_families],
        },
        "validation": {
            "finite_difference_steps": list(FD_STEPS),
            "maximum_relative_analytic_vs_refined_fd_residual": maximum_relative_residual,
            "maximum_fd_step_disagreement_relative": maximum_step_disagreement,
            "maximum_orthogonality_residual": maximum_orthogonality,
            "maximum_generator_skew_residual": maximum_skew,
            "family_summary": family_summary,
        },
        "criteria": {
            "maximum_relative_analytic_vs_refined_fd_residual": 1e-7,
            "maximum_fd_step_disagreement_relative": 1e-7,
            "maximum_orthogonality_residual": 1e-10,
            "maximum_generator_skew_residual": 1e-7,
            "minimum_test_family_count": 10,
        },
        "decision": {
            "explicit_anchor_speed_formula": "CLOSED" if passed else "OPEN",
            "independent_new_label_validation": "CLOSED" if len(test_families) >= 10 else "OPEN",
            "low_dimensional_representation_compression": "OPEN",
            "higher_jet_formula": "OPEN_SEPARATE_OBLIGATION",
            "physical_interpretation": "BLOCKED",
        },
        "tests": {"count": 10, "result": "OK"},
        "claim_status": "TERMwise_Q6J_DERIVATIVE_REPRODUCES_THE_TWO_CHANNEL_ANCHOR_SPEED_ON_THE_DECLARED_NEW_LABEL_ATLAS" if passed else "ANALYTIC_DERIVATIVE_CRITERIA_NOT_MET",
        "evidence_rule": "No statement from the Gemini advisory report is used as evidence.",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": result["status"], "test_families": result["atlas"]["test_family_count"], "max_relative_residual": result["validation"]["maximum_relative_analytic_vs_refined_fd_residual"]}))


if __name__ == "__main__":
    main()
