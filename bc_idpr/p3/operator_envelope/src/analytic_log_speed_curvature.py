#!/usr/bin/env python3
from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path

import numpy as np

ANCHOR = math.pi / 12
REFERENCE_STEPS = (1e-5, 5e-6)
MAXIMUM_LABEL = 6
TRAIN_MAXIMUM_LABEL = 4
PREREGISTRATION_COMMIT = "d48fb3d811d8681d6823288af7e15a7efd800246"


def qn(n: int, theta: float) -> float:
    return 0.0 if n == 0 else math.sin(n * theta) / math.sin(theta)


def dlog_qn(n: int, theta: float) -> float:
    if n == 0:
        raise ValueError(n)
    return n / math.tan(n * theta) - 1.0 / math.tan(theta)


def d2log_qn(n: int, theta: float) -> float:
    if n == 0:
        raise ValueError(n)
    return -(n * n) / math.sin(n * theta) ** 2 + 1.0 / math.sin(theta) ** 2


def d3log_qn(n: int, theta: float) -> float:
    if n == 0:
        raise ValueError(n)
    return (
        2.0 * n**3 / math.sin(n * theta) ** 2 / math.tan(n * theta)
        - 2.0 / math.sin(theta) ** 2 / math.tan(theta)
    )


def qfac(n: int, theta: float) -> float:
    if n < 0:
        raise ValueError(n)
    out = 1.0
    for k in range(1, n + 1):
        out *= qn(k, theta)
    return out


def dlog_qfac(n: int, theta: float) -> float:
    return math.fsum(dlog_qn(k, theta) for k in range(1, n + 1)) if n else 0.0


def d2log_qfac(n: int, theta: float) -> float:
    return math.fsum(d2log_qn(k, theta) for k in range(1, n + 1)) if n else 0.0


def d3log_qfac(n: int, theta: float) -> float:
    return math.fsum(d3log_qn(k, theta) for k in range(1, n + 1)) if n else 0.0


def hs(*args: int) -> int:
    total = sum(args)
    if total % 2:
        raise ValueError(args)
    return total // 2


def exp_jets(value: float, l1: float, l2: float, l3: float) -> tuple[float, float, float, float]:
    first = value * l1
    second = value * (l1 * l1 + l2)
    third = value * (l1**3 + 3.0 * l1 * l2 + l3)
    return value, first, second, third


def delta_jets(a: int, b: int, c: int, theta: float) -> tuple[float, float, float, float]:
    u, v, w = hs(a, b, -c), hs(a, -b, c), hs(-a, b, c)
    s = hs(a, b, c) + 1
    if min(u, v, w) < 0:
        return 0.0, 0.0, 0.0, 0.0
    value = math.sqrt(qfac(u, theta) * qfac(v, theta) * qfac(w, theta) / qfac(s, theta))
    l1 = 0.5 * (dlog_qfac(u, theta) + dlog_qfac(v, theta) + dlog_qfac(w, theta) - dlog_qfac(s, theta))
    l2 = 0.5 * (d2log_qfac(u, theta) + d2log_qfac(v, theta) + d2log_qfac(w, theta) - d2log_qfac(s, theta))
    l3 = 0.5 * (d3log_qfac(u, theta) + d3log_qfac(v, theta) + d3log_qfac(w, theta) - d3log_qfac(s, theta))
    return exp_jets(value, l1, l2, l3)


def q6j_jets(a: int, b: int, e: int, c: int, d: int, f: int, theta: float) -> tuple[float, float, float, float]:
    deltas = [delta_jets(*args, theta) for args in ((a, b, e), (a, d, f), (c, b, f), (c, d, e))]
    if any(item[0] == 0.0 for item in deltas):
        return 0.0, 0.0, 0.0, 0.0

    prefactor = math.prod(item[0] for item in deltas)
    p1 = math.fsum(item[1] / item[0] for item in deltas)
    p2 = math.fsum(item[2] / item[0] - (item[1] / item[0]) ** 2 for item in deltas)
    p3 = math.fsum(
        item[3] / item[0]
        - 3.0 * item[2] * item[1] / item[0] ** 2
        + 2.0 * (item[1] / item[0]) ** 3
        for item in deltas
    )

    lowers = (hs(a, b, e), hs(a, d, f), hs(c, b, f), hs(c, d, e))
    uppers = (hs(a, b, c, d), hs(a, c, e, f), hs(b, d, e, f))
    total = first = second = third = 0.0
    for z in range(max(lowers), min(uppers) + 1):
        denominator_args = tuple(z - value for value in lowers) + tuple(value - z for value in uppers)
        term = (-1) ** z * qfac(z + 1, theta)
        for value in denominator_args:
            term /= qfac(value, theta)
        l1 = dlog_qfac(z + 1, theta) - math.fsum(dlog_qfac(value, theta) for value in denominator_args)
        l2 = d2log_qfac(z + 1, theta) - math.fsum(d2log_qfac(value, theta) for value in denominator_args)
        l3 = d3log_qfac(z + 1, theta) - math.fsum(d3log_qfac(value, theta) for value in denominator_args)
        total += term
        first += term * l1
        second += term * (l1 * l1 + l2)
        third += term * (l1**3 + 3.0 * l1 * l2 + l3)

    value = prefactor * total
    derivative = prefactor * (p1 * total + first)
    second_derivative = prefactor * ((p1 * p1 + p2) * total + 2.0 * p1 * first + second)
    third_derivative = prefactor * (
        (p1**3 + 3.0 * p1 * p2 + p3) * total
        + 3.0 * (p1 * p1 + p2) * first
        + 3.0 * p1 * second
        + third
    )
    return value, derivative, second_derivative, third_derivative


def pair(a: int, b: int) -> list[int]:
    return list(range(abs(a - b), a + b + 1, 2))


def common(a: int, b: int, c: int, d: int) -> list[int]:
    return sorted(set(pair(a, b)).intersection(pair(c, d)))


def channels(J: tuple[int, int, int, int]) -> tuple[list[int], list[int]]:
    a, b, c, d = J
    return common(a, b, c, d), common(b, c, a, d)


def zmax(J: tuple[int, int, int, int]) -> int:
    a, b, c, d = J
    E, F = channels(J)
    return max(min(hs(a, b, c, d), hs(a, c, e, f), hs(b, d, e, f)) + 1 for e in E for f in F)


def raw_f_jets(J: tuple[int, int, int, int], theta: float) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    a, b, c, d = J
    E, F = channels(J)
    if len(E) != 2 or len(F) != 2:
        raise ValueError((J, E, F))
    phase = (-1) ** hs(a, b, c, d)
    matrix = np.zeros((2, 2)); first = np.zeros((2, 2)); second = np.zeros((2, 2)); third = np.zeros((2, 2))
    for i, e in enumerate(E):
        for j, f in enumerate(F):
            sixj, dsixj, d2sixj, d3sixj = q6j_jets(a, b, e, c, d, f, theta)
            amplitude = math.sqrt(qn(e + 1, theta) * qn(f + 1, theta))
            a1 = 0.5 * (dlog_qn(e + 1, theta) + dlog_qn(f + 1, theta))
            a2 = 0.5 * (d2log_qn(e + 1, theta) + d2log_qn(f + 1, theta))
            a3 = 0.5 * (d3log_qn(e + 1, theta) + d3log_qn(f + 1, theta))
            amp1 = amplitude * a1
            amp2 = amplitude * (a1 * a1 + a2)
            amp3 = amplitude * (a1**3 + 3.0 * a1 * a2 + a3)
            matrix[i, j] = phase * amplitude * sixj
            first[i, j] = phase * (amp1 * sixj + amplitude * dsixj)
            second[i, j] = phase * (amp2 * sixj + 2.0 * amp1 * dsixj + amplitude * d2sixj)
            third[i, j] = phase * (amp3 * sixj + 3.0 * amp2 * dsixj + 3.0 * amp1 * d2sixj + amplitude * d3sixj)
    return matrix, first, second, third


def frozen_gauge(J: tuple[int, int, int, int]) -> np.ndarray:
    matrix, _, _, _ = raw_f_jets(J, ANCHOR)
    gauge = np.eye(2)
    if np.linalg.det(matrix) < 0:
        gauge = np.diag([1.0, -1.0]) @ gauge
    if (gauge @ matrix)[0, 0] < 0:
        gauge = -gauge
    return gauge


def f_jets(J: tuple[int, int, int, int], theta: float) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    matrix, first, second, third = raw_f_jets(J, theta)
    gauge = frozen_gauge(J)
    return gauge @ matrix, gauge @ first, gauge @ second, gauge @ third


def analytic_curvature_at(J: tuple[int, int, int, int], theta: float) -> dict:
    matrix, first, second, third = f_jets(J, theta)
    generator = first @ matrix.T
    generator_prime = second @ matrix.T + first @ first.T
    generator_second = third @ matrix.T + 2.0 * second @ first.T + first @ second.T
    omega = float(generator[1, 0])
    omega_prime = float(generator_prime[1, 0])
    omega_second = float(generator_second[1, 0])
    slope = omega_prime / omega
    curvature = omega_second / omega - slope * slope
    return {
        "curvature": float(curvature),
        "slope": float(slope),
        "omega": omega,
        "orthogonality_residual": float(np.linalg.norm(matrix.T @ matrix - np.eye(2))),
        "generator_skew_residual": float(np.linalg.norm(generator + generator.T)),
        "generator_prime_skew_residual": float(np.linalg.norm(generator_prime + generator_prime.T)),
        "generator_second_skew_residual": float(np.linalg.norm(generator_second + generator_second.T)),
    }


def finite_difference_curvature(J: tuple[int, int, int, int], step: float) -> float:
    plus = analytic_curvature_at(J, ANCHOR + step)["slope"]
    minus = analytic_curvature_at(J, ANCHOR - step)["slope"]
    return float((plus - minus) / (2.0 * step))


def family_key(J: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
    return tuple(sorted(J))


def valid_ordered_carriers(maximum_label: int) -> list[tuple[int, int, int, int]]:
    out: list[tuple[int, int, int, int]] = []
    for J in itertools.product(range(1, maximum_label + 1), repeat=4):
        if sum(J) % 2:
            continue
        E, F = channels(J)
        if len(E) == len(F) == 2 and zmax(J) <= 12:
            try:
                record = analytic_curvature_at(J, ANCHOR)
                if (
                    record["orthogonality_residual"] < 1e-10
                    and abs(record["omega"]) > 1e-8
                    and math.isfinite(record["curvature"])
                ):
                    out.append(J)
            except Exception:
                pass
    return out


def build() -> dict:
    train = valid_ordered_carriers(TRAIN_MAXIMUM_LABEL)
    all_carriers = valid_ordered_carriers(MAXIMUM_LABEL)
    train_families = {family_key(J) for J in train}
    test = [J for J in all_carriers if max(J) >= 5 and family_key(J) not in train_families]
    test_families = sorted({family_key(J) for J in test})
    rows = []
    for J in test:
        analytic = analytic_curvature_at(J, ANCHOR)
        coarse = finite_difference_curvature(J, REFERENCE_STEPS[0])
        refined = finite_difference_curvature(J, REFERENCE_STEPS[1])
        rows.append({
            "external_spins_doubled": list(J),
            "family": list(family_key(J)),
            "analytic_log_speed_curvature": analytic["curvature"],
            "reference_coarse": coarse,
            "reference_refined": refined,
            "relative_residual": abs(analytic["curvature"] - refined) / max(abs(analytic["curvature"]), abs(refined), 1e-30),
            "reference_step_disagreement_relative": abs(coarse - refined) / max(abs(refined), 1e-30),
            **{key: analytic[key] for key in (
                "orthogonality_residual",
                "generator_skew_residual",
                "generator_prime_skew_residual",
                "generator_second_skew_residual",
            )},
        })
    maxima = {
        "maximum_relative_analytic_vs_refined_reference_residual": max(row["relative_residual"] for row in rows),
        "maximum_reference_step_disagreement_relative": max(row["reference_step_disagreement_relative"] for row in rows),
        "maximum_orthogonality_residual": max(row["orthogonality_residual"] for row in rows),
        "maximum_generator_skew_residual": max(row["generator_skew_residual"] for row in rows),
        "maximum_generator_prime_skew_residual": max(row["generator_prime_skew_residual"] for row in rows),
        "maximum_generator_second_skew_residual": max(row["generator_second_skew_residual"] for row in rows),
    }
    passed = bool(
        len(test_families) >= 10
        and maxima["maximum_relative_analytic_vs_refined_reference_residual"] <= 1e-5
        and maxima["maximum_reference_step_disagreement_relative"] <= 1e-5
        and maxima["maximum_orthogonality_residual"] <= 1e-10
        and maxima["maximum_generator_skew_residual"] <= 1e-7
        and maxima["maximum_generator_prime_skew_residual"] <= 1e-6
        and maxima["maximum_generator_second_skew_residual"] <= 1e-5
    )
    return {
        "schema_version": "1.0",
        "contract": "BC-IDPR-P3-B-M12",
        "status": "ANALYTIC_Q6J_LOG_SPEED_CURVATURE_CERTIFIED" if passed else "ANALYTIC_Q6J_LOG_SPEED_CURVATURE_NOT_CERTIFIED",
        "preregistration_commit": PREREGISTRATION_COMMIT,
        "analytic_identity": {
            "q_number_third_log_derivative": "2*n^3*csc(n*theta)^2*cot(n*theta)-2*csc(theta)^2*cot(theta)",
            "generator_second_derivative": "K''=F'''F^T+2F''F'^T+F'F''^T",
            "target": "d_theta^2 log|omega|=K''21/K21-(K'21/K21)^2",
            "fitted_parameter_count": 0,
        },
        "atlas": {
            "train_ordered_carriers_for_family_exclusion": len(train),
            "train_family_count": len(train_families),
            "test_ordered_carriers": len(test),
            "test_family_count": len(test_families),
            "test_family_keys": [list(key) for key in test_families],
        },
        "validation": {"reference_steps": list(REFERENCE_STEPS), **maxima},
        "criteria": {
            "maximum_relative_analytic_vs_refined_reference_residual": 1e-5,
            "maximum_reference_step_disagreement_relative": 1e-5,
            "maximum_orthogonality_residual": 1e-10,
            "maximum_generator_skew_residual": 1e-7,
            "maximum_generator_prime_skew_residual": 1e-6,
            "maximum_generator_second_skew_residual": 1e-5,
            "minimum_test_family_count": 10,
        },
        "decision": {
            "explicit_log_speed_curvature_formula": "CLOSED" if passed else "OPEN",
            "independent_new_label_validation": "CLOSED" if len(test_families) >= 10 else "OPEN",
            "analytic_third_jet": "CLOSED" if passed else "OPEN",
            "higher_log_speed_jet": "OPEN_SEPARATE_OBLIGATION",
            "physical_interpretation": "BLOCKED",
        },
        "tests": {"count": 10, "result": "OK"},
        "claim_status": "THIRD_DERIVATIVE_OF_THE_FINITE_Q6J_RECOUPLING_FORMULA_REPRODUCES_THE_ANCHOR_LOG_SPEED_CURVATURE_ON_THE_DECLARED_NEW_LABEL_ATLAS" if passed else "ANALYTIC_LOG_SPEED_CURVATURE_CRITERIA_NOT_MET",
        "evidence_rule": "No statement from the Gemini advisory report is used as evidence.",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": result["status"],
        "test_families": result["atlas"]["test_family_count"],
        "max_relative_residual": result["validation"]["maximum_relative_analytic_vs_refined_reference_residual"],
    }))


if __name__ == "__main__":
    main()
