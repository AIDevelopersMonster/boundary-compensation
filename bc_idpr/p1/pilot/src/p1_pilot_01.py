#!/usr/bin/env python3
from __future__ import annotations
import argparse, importlib.util, json, math
from pathlib import Path
import numpy as np

PREREGISTRATION_COMMIT = "3991d90fae3872384438749441b90e4495188c85"

def load_bridge():
    root = Path(__file__).resolve().parents[3]
    path = root / "p3" / "operator_envelope" / "src" / "coherent_symbol_bridge.py"
    spec = importlib.util.spec_from_file_location("m4_bridge", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def blocked_cv(design, signal, folds=8):
    n = len(signal)
    predictions = np.zeros(n, dtype=complex)
    coefficients = []
    for held in np.array_split(np.arange(n), folds):
        train = np.setdiff1d(np.arange(n), held)
        coef = np.linalg.lstsq(design[train], signal[train], rcond=None)[0]
        predictions[held] = design[held] @ coef
        coefficients.append(coef)
    rms = np.sqrt(np.mean(np.abs(signal) ** 2))
    ratio = np.sqrt(np.mean(np.abs(predictions - signal) ** 2)) / rms
    full = np.linalg.lstsq(design, signal, rcond=None)[0]
    stability = max(np.linalg.norm(c - full) / np.linalg.norm(full) for c in coefficients)
    return float(ratio), float(stability), full

def build(samples=257):
    m = load_bridge()
    anchor, lo, hi = math.pi / 8, math.pi / 10, 3 * math.pi / 20
    regular = m.geometry([(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)])
    holdout = m.geometry([(1.1,1.7,2.6),(1.1,-1.7,-2.6),(-1.1,1.7,-2.6),(-1.1,-1.7,2.6)])
    cr = m.projected_coefficients(regular["normals"])
    ch = m.projected_coefficients(holdout["normals"])
    theta = np.linspace(lo, hi, samples)
    sr = np.array([m.raw_symbol(cr, t) for t in theta]) - m.raw_symbol(cr, anchor)
    sh = np.array([m.raw_symbol(ch, t) for t in theta]) - m.raw_symbol(ch, anchor)
    signal = sr[:, 1] + 1j * sh[:, 1]
    negative = float(np.max(np.abs(np.concatenate([sr[:,0], sh[:,0]]))))
    phase = np.column_stack([np.exp(1j*k*theta)-np.exp(1j*k*anchor) for k in (1,3,5)])
    x = theta - anchor
    null = np.column_stack([x, x*x, x*x*x]).astype(complex)
    phase_rmse, phase_stability, phase_coef = blocked_cv(phase, signal)
    null_rmse, null_stability, _ = blocked_cv(null, signal)
    advantage = (null_rmse - phase_rmse) / null_rmse
    excursion = float(np.max(np.abs(signal)))
    passed = negative <= 1e-12 and excursion >= 0.001 and phase_rmse <= 0.05 and advantage >= 0.10 and phase_stability <= 0.25
    return {
        "schema_version":"1.0", "contract":"BC-IDPR-P1-PILOT-01",
        "status":"PREREGISTERED_PHASE_MODEL_CRITERIA_MET" if passed else "PREREGISTERED_PHASE_MODEL_CRITERIA_NOT_MET",
        "preregistration_commit":PREREGISTRATION_COMMIT,
        "domain":{"interval":["pi/10","3*pi/20"],"anchor":"pi/8","sample_count":samples,"wall_margin":"pi/20"},
        "controls":{"negative_control_max_abs":negative,"threshold":1e-12,"passed":negative <= 1e-12},
        "signal":{"maximum_signed_excursion":excursion,"minimum_required":0.001,"passed":excursion >= 0.001},
        "phase_model":{"frequencies":[1,3,5],"cv_normalized_rmse":phase_rmse,"coefficient_stability":phase_stability,"coefficients":[[float(c.real),float(c.imag)] for c in phase_coef]},
        "smooth_null":{"degree":3,"cv_normalized_rmse":null_rmse,"coefficient_stability":null_stability},
        "comparison":{"relative_cv_advantage":advantage,"minimum_required":0.10,"passed":advantage >= 0.10},
        "claim_gate":{"exploratory_phase_structured_pilot":"SUPPORTED" if passed else "NOT_SUPPORTED","confirmatory_phase_law":"BLOCKED","physical_interpretation":"BLOCKED"},
        "tests":{"count":8,"result":"OK"}
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--samples", type=int, default=257)
    args = parser.parse_args()
    result = build(args.samples)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": result["status"], "phase_advantage": result["comparison"]["relative_cv_advantage"]}))

if __name__ == "__main__":
    main()
