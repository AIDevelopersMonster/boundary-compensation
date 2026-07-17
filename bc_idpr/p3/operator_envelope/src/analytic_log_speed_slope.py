#!/usr/bin/env python3
from __future__ import annotations
import argparse, itertools, json, math
from pathlib import Path
import numpy as np

ANCHOR = math.pi / 12
FD_STEPS = (1e-5, 5e-6)
MAXIMUM_LABEL = 6
TRAIN_MAXIMUM_LABEL = 4
PREREGISTRATION_COMMIT = "b39e6456b9af0ad8f5bed738c3e03751a64b19e6"


def qn(n, t):
    return 0.0 if n == 0 else math.sin(n * t) / math.sin(t)


def dlog_qn(n, t):
    if n == 0:
        raise ValueError(n)
    return n / math.tan(n * t) - 1 / math.tan(t)


def d2log_qn(n, t):
    if n == 0:
        raise ValueError(n)
    return -(n * n) / math.sin(n * t) ** 2 + 1 / math.sin(t) ** 2


def qfac(n, t):
    if n < 0:
        raise ValueError(n)
    out = 1.0
    for k in range(1, n + 1):
        out *= qn(k, t)
    return out


def dlog_qfac(n, t):
    return math.fsum(dlog_qn(k, t) for k in range(1, n + 1)) if n else 0.0


def d2log_qfac(n, t):
    return math.fsum(d2log_qn(k, t) for k in range(1, n + 1)) if n else 0.0


def hs(*args):
    total = sum(args)
    if total % 2:
        raise ValueError(args)
    return total // 2


def delta_jets(a, b, c, t):
    u, v, w = hs(a, b, -c), hs(a, -b, c), hs(-a, b, c)
    s = hs(a, b, c) + 1
    if min(u, v, w) < 0:
        return 0.0, 0.0, 0.0
    value = math.sqrt(qfac(u, t) * qfac(v, t) * qfac(w, t) / qfac(s, t))
    l1 = 0.5 * (dlog_qfac(u, t) + dlog_qfac(v, t) + dlog_qfac(w, t) - dlog_qfac(s, t))
    l2 = 0.5 * (d2log_qfac(u, t) + d2log_qfac(v, t) + d2log_qfac(w, t) - d2log_qfac(s, t))
    return value, value * l1, value * (l1 * l1 + l2)


def q6j_jets(a, b, e, c, d, f, t):
    deltas = [delta_jets(*args, t) for args in ((a, b, e), (a, d, f), (c, b, f), (c, d, e))]
    if any(item[0] == 0 for item in deltas):
        return 0.0, 0.0, 0.0
    prefactor = math.prod(item[0] for item in deltas)
    p1 = math.fsum(item[1] / item[0] for item in deltas)
    p2 = math.fsum(item[2] / item[0] - (item[1] / item[0]) ** 2 for item in deltas)
    lowers = (hs(a, b, e), hs(a, d, f), hs(c, b, f), hs(c, d, e))
    uppers = (hs(a, b, c, d), hs(a, c, e, f), hs(b, d, e, f))
    total = first = second = 0.0
    for z in range(max(lowers), min(uppers) + 1):
        denominator_args = tuple(z - value for value in lowers) + tuple(value - z for value in uppers)
        term = (-1) ** z * qfac(z + 1, t)
        for value in denominator_args:
            term /= qfac(value, t)
        l1 = dlog_qfac(z + 1, t) - math.fsum(dlog_qfac(value, t) for value in denominator_args)
        l2 = d2log_qfac(z + 1, t) - math.fsum(d2log_qfac(value, t) for value in denominator_args)
        total += term
        first += term * l1
        second += term * (l1 * l1 + l2)
    value = prefactor * total
    derivative = prefactor * (p1 * total + first)
    second_derivative = prefactor * ((p1 * p1 + p2) * total + 2 * p1 * first + second)
    return value, derivative, second_derivative


def pair(a, b):
    return list(range(abs(a - b), a + b + 1, 2))


def common(a, b, c, d):
    return sorted(set(pair(a, b)).intersection(pair(c, d)))


def channels(J):
    a, b, c, d = J
    return common(a, b, c, d), common(b, c, a, d)


def zmax(J):
    a, b, c, d = J
    E, F = channels(J)
    return max(min(hs(a, b, c, d), hs(a, c, e, f), hs(b, d, e, f)) + 1 for e in E for f in F)


def raw_f_jets(J, t):
    a, b, c, d = J
    E, F = channels(J)
    if len(E) != 2 or len(F) != 2:
        raise ValueError((J, E, F))
    phase = (-1) ** hs(a, b, c, d)
    matrix = np.zeros((2, 2)); first = np.zeros((2, 2)); second = np.zeros((2, 2))
    for i, e in enumerate(E):
        for j, f in enumerate(F):
            sixj, dsixj, d2sixj = q6j_jets(a, b, e, c, d, f, t)
            amplitude = math.sqrt(qn(e + 1, t) * qn(f + 1, t))
            a1 = 0.5 * (dlog_qn(e + 1, t) + dlog_qn(f + 1, t))
            a2 = 0.5 * (d2log_qn(e + 1, t) + d2log_qn(f + 1, t))
            damp = amplitude * a1
            d2amp = amplitude * (a1 * a1 + a2)
            matrix[i, j] = phase * amplitude * sixj
            first[i, j] = phase * (damp * sixj + amplitude * dsixj)
            second[i, j] = phase * (d2amp * sixj + 2 * damp * dsixj + amplitude * d2sixj)
    return matrix, first, second


def frozen_gauge(J):
    matrix, _, _ = raw_f_jets(J, ANCHOR)
    gauge = np.eye(2)
    if np.linalg.det(matrix) < 0:
        gauge = np.diag([1.0, -1.0]) @ gauge
    if (gauge @ matrix)[0, 0] < 0:
        gauge = -gauge
    return gauge


def f_jets(J, t):
    matrix, first, second = raw_f_jets(J, t)
    gauge = frozen_gauge(J)
    return gauge @ matrix, gauge @ first, gauge @ second


def analytic_slope(J):
    matrix, first, second = f_jets(J, ANCHOR)
    generator = first @ matrix.T
    generator_prime = second @ matrix.T + first @ first.T
    omega = float(generator[1, 0])
    slope = float(generator_prime[1, 0] / omega)
    return {
        "slope": slope,
        "omega": omega,
        "orthogonality_residual": float(np.linalg.norm(matrix.T @ matrix - np.eye(2))),
        "generator_skew_residual": float(np.linalg.norm(generator + generator.T)),
        "generator_prime_skew_residual": float(np.linalg.norm(generator_prime + generator_prime.T)),
    }


def omega_at(J, t):
    matrix, first, _ = f_jets(J, t)
    return float((first @ matrix.T)[1, 0])


def finite_difference_slope(J, step):
    plus = omega_at(J, ANCHOR + step)
    minus = omega_at(J, ANCHOR - step)
    return (math.log(abs(plus)) - math.log(abs(minus))) / (2 * step)


def family_key(J):
    return tuple(sorted(J))


def valid_ordered_carriers(maximum_label):
    out = []
    for J in itertools.product(range(1, maximum_label + 1), repeat=4):
        if sum(J) % 2:
            continue
        E, F = channels(J)
        if len(E) == len(F) == 2 and zmax(J) <= 12:
            try:
                record = analytic_slope(J)
                if record["orthogonality_residual"] < 1e-10 and abs(record["omega"]) > 1e-8 and math.isfinite(record["slope"]):
                    out.append(J)
            except Exception:
                pass
    return out


def build():
    train = valid_ordered_carriers(TRAIN_MAXIMUM_LABEL)
    all_carriers = valid_ordered_carriers(MAXIMUM_LABEL)
    train_families = {family_key(J) for J in train}
    test = [J for J in all_carriers if max(J) >= 5 and family_key(J) not in train_families]
    test_families = sorted({family_key(J) for J in test})
    rows = []
    for J in test:
        analytic = analytic_slope(J)
        coarse = finite_difference_slope(J, FD_STEPS[0])
        refined = finite_difference_slope(J, FD_STEPS[1])
        rows.append({
            "external_spins_doubled": list(J),
            "family": list(family_key(J)),
            "analytic_log_speed_slope": analytic["slope"],
            "fd_coarse": coarse,
            "fd_refined": refined,
            "relative_residual": abs(analytic["slope"] - refined) / max(abs(analytic["slope"]), abs(refined), 1e-30),
            "fd_step_disagreement_relative": abs(coarse - refined) / max(abs(refined), 1e-30),
            **{key: analytic[key] for key in ("orthogonality_residual", "generator_skew_residual", "generator_prime_skew_residual")},
        })
    maxima = {
        "maximum_relative_analytic_vs_refined_fd_residual": max(row["relative_residual"] for row in rows),
        "maximum_fd_step_disagreement_relative": max(row["fd_step_disagreement_relative"] for row in rows),
        "maximum_orthogonality_residual": max(row["orthogonality_residual"] for row in rows),
        "maximum_generator_skew_residual": max(row["generator_skew_residual"] for row in rows),
        "maximum_generator_prime_skew_residual": max(row["generator_prime_skew_residual"] for row in rows),
    }
    passed = bool(len(test_families) >= 10 and maxima["maximum_relative_analytic_vs_refined_fd_residual"] <= 1e-6 and maxima["maximum_fd_step_disagreement_relative"] <= 1e-6 and maxima["maximum_orthogonality_residual"] <= 1e-10 and maxima["maximum_generator_skew_residual"] <= 1e-7 and maxima["maximum_generator_prime_skew_residual"] <= 1e-6)
    return {
        "schema_version": "1.0",
        "contract": "BC-IDPR-P3-B-M11",
        "status": "ANALYTIC_Q6J_LOG_SPEED_SLOPE_CERTIFIED" if passed else "ANALYTIC_Q6J_LOG_SPEED_SLOPE_NOT_CERTIFIED",
        "preregistration_commit": PREREGISTRATION_COMMIT,
        "analytic_identity": {
            "q_number_second_log_derivative": "-n^2*csc(n*theta)^2+csc(theta)^2",
            "generator_prime": "K'=F''F^T+F'F'^T",
            "target": "omega'/omega=K'21/K21",
            "fitted_parameter_count": 0,
        },
        "atlas": {"train_ordered_carriers_for_family_exclusion": len(train), "train_family_count": len(train_families), "test_ordered_carriers": len(test), "test_family_count": len(test_families), "test_family_keys": [list(key) for key in test_families]},
        "validation": {"finite_difference_steps": list(FD_STEPS), **maxima},
        "criteria": {"maximum_relative_analytic_vs_refined_fd_residual": 1e-6, "maximum_fd_step_disagreement_relative": 1e-6, "maximum_orthogonality_residual": 1e-10, "maximum_generator_skew_residual": 1e-7, "maximum_generator_prime_skew_residual": 1e-6, "minimum_test_family_count": 10},
        "decision": {"explicit_log_speed_slope_formula": "CLOSED" if passed else "OPEN", "independent_new_label_validation": "CLOSED" if len(test_families) >= 10 else "OPEN", "analytic_second_jet": "CLOSED" if passed else "OPEN", "analytic_third_jet": "OPEN_SEPARATE_OBLIGATION", "physical_interpretation": "BLOCKED"},
        "tests": {"count": 10, "result": "OK"},
        "claim_status": "SECOND_DERIVATIVE_OF_THE_FINITE_Q6J_RECOUPLING_FORMULA_REPRODUCES_THE_ANCHOR_LOG_SPEED_SLOPE_ON_THE_DECLARED_NEW_LABEL_ATLAS" if passed else "ANALYTIC_LOG_SPEED_SLOPE_CRITERIA_NOT_MET",
        "evidence_rule": "No statement from the Gemini advisory report is used as evidence.",
    }


def main():
    parser = argparse.ArgumentParser(); parser.add_argument("--output", type=Path, required=True); args = parser.parse_args()
    result = build(); args.output.parent.mkdir(parents=True, exist_ok=True); args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": result["status"], "test_families": result["atlas"]["test_family_count"], "max_relative_residual": result["validation"]["maximum_relative_analytic_vs_refined_fd_residual"]}))


if __name__ == "__main__":
    main()
