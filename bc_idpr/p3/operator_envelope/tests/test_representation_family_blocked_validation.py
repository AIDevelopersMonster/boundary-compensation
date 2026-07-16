import importlib.util
from pathlib import Path

P = Path(__file__).resolve().parents[1] / 'src' / 'representation_family_blocked_validation.py'
S = importlib.util.spec_from_file_location('m8', P)
M = importlib.util.module_from_spec(S)
assert S.loader is not None
S.loader.exec_module(M)
R = M.build()


def test_status():
    assert R['status'] == 'REPRESENTATION_FAMILY_BLOCKED_GENERALIZATION_NOT_CERTIFIED'


def test_carrier_and_family_counts():
    assert R['validation']['ordered_carrier_count'] == 75
    assert R['validation']['unordered_representation_family_count'] == 9


def test_family_holdout_is_grouped():
    assert sum(R['validation']['family_sizes'].values()) == 75
    assert max(R['validation']['family_sizes'].values()) == 24


def test_dimensions_are_corrected_m7_dimensions():
    assert R['descriptors']['baseline_dimension'] == 10
    assert R['descriptors']['matrix_augmented_dimension'] == 14


def test_no_derivative_leakage():
    assert R['descriptors']['derivatives_excluded_from_predictors']


def test_blocked_errors_exceed_ordinary_errors():
    ordinary = R['ordinary_leave_one_carrier_out']['matrix_augmented_nrmse']
    blocked = R['leave_one_representation_family_out']['matrix_augmented_nrmse']
    assert all(b > a for a, b in zip(ordinary, blocked))


def test_blocked_threshold_fails():
    assert not all(R['leave_one_representation_family_out']['matrix_threshold_pass_each_target'])


def test_uniform_improvement_fails():
    assert not all(R['leave_one_representation_family_out']['improvement_pass_each_target'])


def test_cross_carrier_gate_remains_blocked():
    assert R['decision']['new_cross_carrier_pilot'].startswith('BLOCKED')


def test_evidence_rule():
    assert R['evidence_rule'] == 'No statement from the Gemini advisory report is used as evidence.'
