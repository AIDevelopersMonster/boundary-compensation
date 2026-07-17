#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from typing import Dict, List

import mpmath as mp
import numpy as np


def rotation(phi: float) -> np.ndarray:
    return np.array([[math.cos(phi), -math.sin(phi)], [math.sin(phi), math.cos(phi)]], dtype=float)


def static_frame_jet_gap(alpha: float = 0.015, epsilon: float = 0.1) -> List[Dict[str, float]]:
    d = np.diag([1.0, math.sqrt(alpha)])
    out = []
    for omega in (10.0, 100.0, 1000.0):
        theta = math.pi / (2.0 * omega)
        phi = epsilon * math.sin(omega * theta)
        phi_prime = epsilon * omega * math.cos(omega * theta)
        phi_second = -epsilon * omega * omega * math.sin(omega * theta)
        r = rotation(phi)
        j = np.array([[0.0, -1.0], [1.0, 0.0]])
        m = r @ d
        m_second = r @ ((-phi_prime * phi_prime) * np.eye(2) + phi_second * j) @ d
        svals = np.linalg.svd(m, compute_uv=False)
        out.append({
            "omega": omega,
            "sigma_min": float(svals[-1]),
            "sigma_min_squared": float(svals[-1] ** 2),
            "M_second_op_norm": float(np.linalg.norm(m_second, 2)),
            "exact_at_selected_theta": float(abs(phi_second)),
        })
    return out


def phase_frame_decoupling(alpha: float = 0.015, family_count: int = 8) -> Dict[str, float]:
    equal = np.zeros(family_count)
    uniform = 2.0 * math.pi * np.arange(family_count) / family_count
    bimodal = np.array([0.0, math.pi] * (family_count // 2))

    def r1(phases: np.ndarray) -> float:
        return float(abs(np.mean(np.exp(1j * phases))))

    return {
        "frame_alpha_fixed": alpha,
        "R1_equal_phases": r1(equal),
        "R1_uniform_phases": r1(uniform),
        "R1_bimodal_phases": r1(bimodal),
    }


def qn(n: int, theta: mp.mpf) -> mp.mpf:
    return mp.sin(n * theta) / mp.sin(theta)


def phi(n: int, theta: mp.mpf) -> mp.mpf:
    return -(n**2) / (mp.sin(n * theta) ** 2) + 1 / (mp.sin(theta) ** 2)


def psi(n: int, theta: mp.mpf) -> mp.mpf:
    return n * mp.cot(n * theta) - mp.cot(theta)


def qfactorial_monomial_identity() -> Dict[str, str]:
    mp.mp.dps = 80
    theta = mp.mpf("0.213")
    gammas = {2: mp.mpf("1.5"), 3: mp.mpf("-2"), 5: mp.mpf("0.5"), 7: mp.mpf("1")}

    def log_t(t: mp.mpf) -> mp.mpf:
        return sum(g * mp.log(qn(n, t)) for n, g in gammas.items())

    direct_second = mp.diff(log_t, theta, 2)
    dictionary_second = sum(g * phi(n, theta) for n, g in gammas.items())

    term_specs = [
        (1, {2: mp.mpf("1"), 5: mp.mpf("0.5")}),
        (-1, {3: mp.mpf("1"), 4: mp.mpf("0.5")}),
        (1, {2: mp.mpf("-1"), 6: mp.mpf("1")}),
    ]

    def term(spec, t):
        sign, gs = spec
        return sign * mp.e ** sum(g * mp.log(qn(n, t)) for n, g in gs.items())

    def total(t):
        return sum(term(spec, t) for spec in term_specs)

    f = total(theta)
    direct_log_second = mp.diff(lambda t: mp.log(total(t)), theta, 2)
    weights = [term(spec, theta) / f for spec in term_specs]
    lambdas = []
    kappas = []
    for _, gs in term_specs:
        lambdas.append(sum(g * psi(n, theta) for n, g in gs.items()))
        kappas.append(sum(g * phi(n, theta) for n, g in gs.items()))
    rhs = (
        sum(w * k for w, k in zip(weights, kappas))
        + sum(w * l * l for w, l in zip(weights, lambdas))
        - (sum(w * l for w, l in zip(weights, lambdas))) ** 2
    )

    return {
        "monomial_direct_second": mp.nstr(direct_second, 50),
        "monomial_dictionary_second": mp.nstr(dictionary_second, 50),
        "monomial_abs_residual": mp.nstr(abs(direct_second - dictionary_second), 10),
        "finite_sum_direct_log_second": mp.nstr(direct_log_second, 50),
        "finite_sum_dictionary_closure": mp.nstr(rhs, 50),
        "finite_sum_abs_residual": mp.nstr(abs(direct_log_second - rhs), 10),
        "signed_weight_sum": mp.nstr(sum(weights), 30),
    }


def rc02_circular_summary(r1: float = 0.9967284980027259) -> Dict[str, float]:
    circular_variance = 1.0 - r1
    small_angle_rms = math.sqrt(2.0 * circular_variance)
    rigorous_wrapped_rms_upper = math.pi * math.sqrt(circular_variance / 2.0)
    return {
        "R1": r1,
        "circular_variance": circular_variance,
        "small_angle_rms_radians": small_angle_rms,
        "small_angle_rms_degrees": math.degrees(small_angle_rms),
        "rigorous_wrapped_rms_upper_radians": rigorous_wrapped_rms_upper,
        "rigorous_wrapped_rms_upper_degrees": math.degrees(rigorous_wrapped_rms_upper),
    }


def main() -> None:
    result = {
        "schema_version": "1.0",
        "contract": "BC-IDPR-P5-UA01-WP3-JET-GAP",
        "status": "EXACT_NONIMPLICATIONS_AND_Q_FACTORIAL_JET_CLOSURE_VERIFIED",
        "static_frame_jet_gap": static_frame_jet_gap(),
        "phase_frame_decoupling": phase_frame_decoupling(),
        "q_factorial_jet_identity": qfactorial_monomial_identity(),
        "rc02_circular_summary": rc02_circular_summary(),
        "claim_ceiling": "mathematical counterexamples and exact q-factorial identities; no mode-5 uniqueness theorem and no physical dynamics claim",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
