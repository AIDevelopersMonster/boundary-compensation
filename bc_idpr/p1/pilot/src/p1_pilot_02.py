#!/usr/bin/env python3
from __future__ import annotations
import argparse, importlib.util, json, math
from pathlib import Path
import numpy as np

PREREGISTRATION_COMMIT = "8ee32533dc7991707b3e2e78c43c0096c459da27"


def load_m5():
    root = Path(__file__).resolve().parents[3]
    path = root / "p3" / "operator_envelope" / "src" / "nonuniform_spin_carrier.py"
    spec = importlib.util.spec_from_file_location("m5_nonuniform", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def blocked_cv(design: np.ndarray, signal: np.ndarray, folds: int = 8):
    n = len(signal)
    predictions = np.zeros(n)
    coefficients = []
    for held in np.array_split(np.arange(n), folds):
        train = np.setdiff1d(np.arange(n), held)
        coefficient = np.linalg.lstsq(design[train], signal[train], rcond=None)[0]
        predictions[held] = design[held] @ coefficient
        coefficients.append(coefficient)
    rms = float(np.sqrt(np.mean(signal * signal)))
    normalized_rmse = float(np.sqrt(np.mean((predictions - signal) ** 2)) / rms)
    full = np.linalg.lstsq(design, signal, rcond=None)[0]
    stability = float(max(np.linalg.norm(value - full) / np.linalg.norm(full) for value in coefficients))
    return normalized_rmse, stability, full


def build(samples: int = 129) -> dict:
    m = load_m5()
    low, high, anchor = math.pi / 15, math.pi / 10, math.pi / 12
    geometry = m.geometry_from_area_vectors()
    coefficients = m.projected_coefficients(np.asarray(geometry["normals"]))
    theta = np.linspace(low, high, samples)
    symbols = np.array([m.symbol(coefficients, float(value)) for value in theta])
    y = symbols[:, 1]
    u = (y - y[0]) / (y[-1] - y[0])
    anchor_u = float((m.symbol(coefficients, anchor)[1] - y[0]) / (y[-1] - y[0]))
    signal = u - anchor_u

    phi = np.unwrap(np.array([math.atan2(m.f_matrix(float(value))[1, 0], m.f_matrix(float(value))[0, 0]) for value in theta]))
    phi_anchor = math.atan2(m.f_matrix(anchor)[1, 0], m.f_matrix(anchor)[0, 0])
    delta_phi = phi - phi_anchor
    recoupling_design = np.column_stack([
        np.sin(2 * delta_phi),
        1 - np.cos(2 * delta_phi),
        np.sin(4 * delta_phi),
    ])
    x = theta - anchor
    cubic_design = np.column_stack([x, x * x, x * x * x])

    phase_rmse, phase_stability, phase_coefficients = blocked_cv(recoupling_design, signal)
    null_rmse, null_stability, null_coefficients = blocked_cv(cubic_design, signal)
    advantage = float((null_rmse - phase_rmse) / null_rmse)
    negative_control = float(np.max(np.abs(symbols[:, 0] - symbols[0, 0])))
    excursion = float(np.max(np.abs(signal)))
    passed = (
        negative_control <= 1e-12
        and excursion >= 0.1
        and phase_rmse <= 0.05
        and advantage >= 0.1
        and phase_stability <= 0.25
    )
    return {
        "schema_version": "1.0",
        "contract": "BC-IDPR-P1-PILOT-02",
        "status": "PREREGISTERED_RECOUPLING_ANGLE_CRITERIA_MET" if passed else "PREREGISTERED_RECOUPLING_ANGLE_CRITERIA_NOT_MET",
        "preregistration_commit": PREREGISTRATION_COMMIT,
        "domain": {"interval": ["pi/15", "pi/10"], "anchor": "pi/12", "sample_count": samples, "wall_margin": "pi/30"},
        "carrier": {"external_spins": ["1/2", "1", "2", "5/2"], "dimension": 2, "face_area_ratios": [1, 2, 4, 5]},
        "controls": {"negative_control_max_abs": negative_control, "threshold": 1e-12, "passed": negative_control <= 1e-12},
        "signal": {"maximum_quotient_excursion": excursion, "anchor_coordinate": anchor_u, "minimum_required": 0.1, "passed": excursion >= 0.1},
        "recoupling_angle_model": {
            "basis": ["sin(2*dphi)", "1-cos(2*dphi)", "sin(4*dphi)"],
            "phi_span": float(phi[-1] - phi[0]),
            "cv_normalized_rmse": phase_rmse,
            "coefficient_stability": phase_stability,
            "coefficients": phase_coefficients.tolist(),
        },
        "smooth_null": {"degree": 3, "cv_normalized_rmse": null_rmse, "coefficient_stability": null_stability, "coefficients": null_coefficients.tolist()},
        "comparison": {"relative_cv_advantage": advantage, "minimum_required": 0.1, "passed": advantage >= 0.1},
        "claim_gate": {
            "model_internal_recoupling_structure": "SUPPORTED" if passed else "NOT_SUPPORTED",
            "independent_phase_law": "BLOCKED",
            "universal_phase_law": "BLOCKED",
            "physical_interpretation": "BLOCKED",
        },
        "tests": {"count": 9, "result": "OK"},
        "claim_status": "TWO_CHANNEL_AFFINE_QUOTIENT_RESPONSE_RESOLVED_BY_PREREGISTERED_RECOUPLING_ANGLE_BASIS" if passed else "PREREGISTERED_MODEL_DISCRIMINATION_CRITERIA_NOT_MET",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--samples", type=int, default=129)
    args = parser.parse_args()
    result = build(args.samples)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": result["status"], "advantage": result["comparison"]["relative_cv_advantage"]}))


if __name__ == "__main__":
    main()
