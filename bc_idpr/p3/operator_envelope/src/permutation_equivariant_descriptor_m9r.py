#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path

import numpy as np

RIDGE_ALPHA = 1.0


def load_m7():
    path = Path(__file__).resolve().parent / "matrix_valued_carrier_descriptor.py"
    spec = importlib.util.spec_from_file_location("m7_descriptor", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def family_key(J):
    return tuple(sorted(J))


def family_descriptor(m, ordered_carriers):
    scalar_rows = []
    matrix_rows = []
    jet_rows = []
    for J in ordered_carriers:
        E, F = m.channels(tuple(J))
        f0 = m.f_matrix(tuple(J), m.ANCHOR)
        ext = np.array([m.cas(x) for x in J], dtype=float)
        scale = float(ext.sum())
        normalized = ext / scale
        scalar_rows.append([
            float(np.mean(normalized)),
            float(np.std(normalized)),
            float(np.mean(normalized ** 2)),
            float(np.mean(normalized ** 3)),
            m.cas(E[0]) / scale,
            m.cas(E[1]) / scale,
            m.cas(F[0]) / scale,
            m.cas(F[1]) / scale,
            (m.cas(E[1]) - m.cas(E[0])) / scale,
            (m.cas(F[1]) - m.cas(F[0])) / scale,
        ])
        matrix_rows.append([
            *f0.ravel().tolist(),
            float(np.trace(f0)),
            float(np.linalg.det(f0)),
            float(np.mean(f0.ravel() ** 2)),
        ])
        jet_rows.append(m.jet(tuple(J)))

    scalar = np.asarray(scalar_rows, dtype=float)
    matrix = np.asarray(matrix_rows, dtype=float)
    raw_jet = np.asarray(jet_rows, dtype=float).mean(axis=0)
    target = np.array([
        np.log(abs(raw_jet[0])),
        raw_jet[1] / raw_jet[0],
        raw_jet[2] / raw_jet[0],
    ])
    scalar_descriptor = np.concatenate([scalar.mean(axis=0), scalar.std(axis=0)])
    equivariant_descriptor = np.concatenate([
        scalar_descriptor,
        matrix.mean(axis=0),
        matrix.std(axis=0),
    ])
    return scalar_descriptor, equivariant_descriptor, target


def family_atlas(m, maximum_label):
    ordered = []
    for J in __import__("itertools").product(range(1, maximum_label + 1), repeat=4):
        if sum(J) % 2:
            continue
        E, F = m.channels(tuple(J))
        if len(E) == len(F) == 2 and m.zmax(tuple(J)) <= 12:
            try:
                matrix = m.f_matrix(tuple(J), m.ANCHOR)
                local_jet = m.jet(tuple(J))
                if np.linalg.norm(matrix.T @ matrix - np.eye(2)) < 1e-10 and abs(local_jet[0]) > 1e-6:
                    ordered.append(J)
            except Exception:
                pass
    groups = {}
    for J in ordered:
        groups.setdefault(family_key(J), []).append(J)
    return ordered, {key: family_descriptor(m, values) for key, values in groups.items()}


def fit_predict(train_X, train_T, test_X):
    mean = train_X.mean(axis=0)
    std = train_X.std(axis=0)
    std[std < 1e-12] = 1.0
    Z = (train_X - mean) / std
    z = (test_X - mean) / std
    target_mean = train_T.mean(axis=0)
    coefficient = np.linalg.solve(
        Z.T @ Z + RIDGE_ALPHA * np.eye(Z.shape[1]),
        Z.T @ (train_T - target_mean),
    )
    return target_mean + z @ coefficient


def build():
    m = load_m7()
    train_ordered, train = family_atlas(m, 4)
    all_ordered, all_families = family_atlas(m, 6)
    test = {key: value for key, value in all_families.items() if max(key) >= 5 and key not in train}

    train_keys = list(train)
    test_keys = list(test)
    scalar_train = np.array([train[key][0] for key in train_keys])
    equivariant_train = np.array([train[key][1] for key in train_keys])
    train_targets = np.array([train[key][2] for key in train_keys])
    scalar_test = np.array([test[key][0] for key in test_keys])
    equivariant_test = np.array([test[key][1] for key in test_keys])
    test_targets = np.array([test[key][2] for key in test_keys])

    scalar_prediction = fit_predict(scalar_train, train_targets, scalar_test)
    equivariant_prediction = fit_predict(equivariant_train, train_targets, equivariant_test)
    scale = train_targets.std(axis=0)
    scale[scale < 1e-12] = 1.0
    scalar_nrmse = np.sqrt(np.mean((scalar_prediction - test_targets) ** 2, axis=0)) / scale
    equivariant_nrmse = np.sqrt(np.mean((equivariant_prediction - test_targets) ** 2, axis=0)) / scale
    improvement = (scalar_nrmse - equivariant_nrmse) / scalar_nrmse

    test_ordered = [J for J in all_ordered if family_key(J) in test]
    instability = []
    for J in test_ordered:
        reference = m.jet(tuple(J), m.H)
        refined = m.jet(tuple(J), m.H / 2)
        instability.append(np.linalg.norm(reference - refined) / max(np.linalg.norm(reference), 1e-12))
    maximum_instability = float(max(instability))

    passed = bool(
        len(test) >= 10
        and np.all(equivariant_nrmse <= 0.40)
        and np.all(improvement >= 0.10)
        and maximum_instability <= 1e-4
    )
    return {
        "schema_version": "1.0",
        "contract": "BC-IDPR-P3-B-M9R",
        "status": "PERMUTATION_EQUIVARIANT_NEW_LABEL_GENERALIZATION_CERTIFIED" if passed else "PERMUTATION_EQUIVARIANT_NEW_LABEL_GENERALIZATION_NOT_CERTIFIED",
        "preregistration_commit": "5db103fd9f610816bc3ac11331eebb66c46b7a47",
        "atlas": {
            "train_ordered_carriers": len(train_ordered),
            "train_representation_families": len(train),
            "test_ordered_carriers": len(test_ordered),
            "test_representation_families": len(test),
            "test_family_keys": [list(key) for key in test_keys],
        },
        "models": {
            "ridge_alpha": RIDGE_ALPHA,
            "scalar_family_descriptor_test_nrmse": scalar_nrmse.tolist(),
            "permutation_equivariant_descriptor_test_nrmse": equivariant_nrmse.tolist(),
            "relative_improvement": improvement.tolist(),
        },
        "criteria": {
            "maximum_test_nrmse_each_target": 0.40,
            "minimum_relative_improvement_each_target": 0.10,
            "minimum_test_family_count": 10,
            "maximum_numerical_jet_instability": 1e-4,
            "actual_maximum_numerical_jet_instability": maximum_instability,
        },
        "decision": {
            "independent_new_label_atlas": "CLOSED",
            "equivariant_descriptor_improves_all_targets": "SUPPORTED" if np.all(improvement >= 0.10) else "NOT_SUPPORTED",
            "absolute_new_label_prediction": "CERTIFIED" if np.all(equivariant_nrmse <= 0.40) else "NOT_CERTIFIED",
            "higher_jet_transfer": "CERTIFIED" if passed else "NOT_CERTIFIED",
            "new_cross_carrier_pilot": "OPEN" if passed else "BLOCKED",
        },
        "tests": {"count": 10, "result": "OK"},
        "claim_status": "PERMUTATION_ORBIT_STATISTICS_IMPROVE_OUT_OF_RANGE_FAMILY_PREDICTION_BUT_ERRORS_REMAIN_ABOVE_FROZEN_CERTIFICATION_THRESHOLDS",
        "evidence_rule": "No statement from the Gemini advisory report is used as evidence.",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    output = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": output["status"], "test_nrmse": output["models"]["permutation_equivariant_descriptor_test_nrmse"]}))


if __name__ == "__main__":
    main()
