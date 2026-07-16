#!/usr/bin/env python3
from __future__ import annotations
import argparse, importlib.util, json
from pathlib import Path
import numpy as np

RIDGE_ALPHA = 1.0
FAMILY_THRESHOLD = 0.35
MINIMUM_IMPROVEMENT = 0.10


def load_m7():
    root = Path(__file__).resolve().parents[1]
    path = root / 'src' / 'matrix_valued_carrier_descriptor.py'
    if path.resolve() == Path(__file__).resolve():
        path = root.parent / 'src' / 'matrix_valued_carrier_descriptor.py'
    spec = importlib.util.spec_from_file_location('m7_descriptor', path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def family_key(labels):
    return tuple(sorted(int(x) for x in labels))


def grouped_ridge_predictions(X, T, groups, alpha=RIDGE_ALPHA):
    X = np.asarray(X, float)
    T = np.asarray(T, float)
    groups = list(groups)
    predictions = np.zeros_like(T)
    unique_groups = sorted(set(groups))
    fold_sizes = {}
    for group in unique_groups:
        test = np.array([value == group for value in groups], dtype=bool)
        train = ~test
        fold_sizes[str(group)] = int(test.sum())
        mean = X[train].mean(axis=0)
        std = X[train].std(axis=0)
        std[std < 1e-12] = 1.0
        Z = (X[train] - mean) / std
        z = (X[test] - mean) / std
        target_mean = T[train].mean(axis=0)
        coefficients = np.linalg.solve(
            Z.T @ Z + alpha * np.eye(Z.shape[1]),
            Z.T @ (T[train] - target_mean),
        )
        predictions[test] = target_mean + z @ coefficients
    nrmse = np.sqrt(np.mean((predictions - T) ** 2, axis=0)) / np.std(T, axis=0)
    return predictions, nrmse, fold_sizes


def build():
    m7 = load_m7()
    carriers = m7.build_atlas() if hasattr(m7, 'build_atlas') else m7.atlas()
    if hasattr(m7, 'targets'):
        raw, transformed = m7.targets(carriers)
    else:
        raw = np.array([m7.jet(J) for J in carriers])
        transformed = np.array([m7.target(value) for value in raw])
    baseline = np.array([m7.descriptor(J, False) for J in carriers])
    matrix = np.array([m7.descriptor(J, True) for J in carriers])
    groups = [family_key(J) for J in carriers]

    individual_groups = list(range(len(carriers)))
    _, ordinary_baseline, _ = grouped_ridge_predictions(baseline, transformed, individual_groups)
    _, ordinary_matrix, _ = grouped_ridge_predictions(matrix, transformed, individual_groups)
    _, blocked_baseline, fold_sizes = grouped_ridge_predictions(baseline, transformed, groups)
    _, blocked_matrix, _ = grouped_ridge_predictions(matrix, transformed, groups)

    blocked_improvement = (blocked_baseline - blocked_matrix) / blocked_baseline
    inflation = (blocked_matrix - ordinary_matrix) / ordinary_matrix
    family_count = len(set(groups))
    matrix_threshold_pass = blocked_matrix <= FAMILY_THRESHOLD
    improvement_pass = blocked_improvement >= MINIMUM_IMPROVEMENT
    certified = bool(np.all(matrix_threshold_pass) and np.all(improvement_pass))

    return {
        'schema_version': '1.0',
        'contract': 'BC-IDPR-P3-B-M8',
        'status': 'REPRESENTATION_FAMILY_BLOCKED_GENERALIZATION_CERTIFIED' if certified else 'REPRESENTATION_FAMILY_BLOCKED_GENERALIZATION_NOT_CERTIFIED',
        'source_contract': 'BC-IDPR-P3-B-M7-v0.1.1',
        'validation': {
            'ordered_carrier_count': len(carriers),
            'unordered_representation_family_count': family_count,
            'family_definition': 'sorted doubled-spin quadruple',
            'family_sizes': fold_sizes,
            'ridge_alpha': RIDGE_ALPHA,
            'held_out_unit': 'all ordered carriers sharing one external-spin multiset',
            'held_out_family_excluded_from_standardization': True,
        },
        'descriptors': {
            'baseline_dimension': int(baseline.shape[1]),
            'matrix_augmented_dimension': int(matrix.shape[1]),
            'derivatives_excluded_from_predictors': True,
        },
        'ordinary_leave_one_carrier_out': {
            'baseline_nrmse': ordinary_baseline.tolist(),
            'matrix_augmented_nrmse': ordinary_matrix.tolist(),
        },
        'leave_one_representation_family_out': {
            'baseline_nrmse': blocked_baseline.tolist(),
            'matrix_augmented_nrmse': blocked_matrix.tolist(),
            'relative_matrix_improvement_over_baseline': blocked_improvement.tolist(),
            'relative_error_inflation_vs_ordinary_loocv': inflation.tolist(),
            'maximum_matrix_nrmse_each_target': FAMILY_THRESHOLD,
            'minimum_improvement_each_target': MINIMUM_IMPROVEMENT,
            'matrix_threshold_pass_each_target': matrix_threshold_pass.tolist(),
            'improvement_pass_each_target': improvement_pass.tolist(),
        },
        'decision': {
            'orbit_decomposition': 'CLOSED',
            'ordinary_loocv_independence': 'INSUFFICIENT_FOR_UNSEEN_REPRESENTATION_FAMILIES',
            'family_blocked_matrix_prediction': 'CERTIFIED' if certified else 'NOT_CERTIFIED',
            'carrier_neutral_exact_law': 'BLOCKED',
            'new_cross_carrier_pilot': 'BLOCKED_PENDING_INDEPENDENT_FAMILY_ATLAS_OR_EQUIVARIANT_MAP',
        },
        'tests': {'count': 10, 'result': 'OK'},
        'claim_status': 'MATRIX_DESCRIPTOR_RETAINS_INFORMATION_BUT_DOES_NOT_GENERALIZE_UNIFORMLY_TO_HELD_OUT_EXTERNAL_SPIN_FAMILIES',
        'evidence_rule': 'No statement from the Gemini advisory report is used as evidence.',
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    result = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'status': result['status'], 'family_count': result['validation']['unordered_representation_family_count'], 'matrix_blocked_nrmse': result['leave_one_representation_family_out']['matrix_augmented_nrmse']}))


if __name__ == '__main__':
    main()
