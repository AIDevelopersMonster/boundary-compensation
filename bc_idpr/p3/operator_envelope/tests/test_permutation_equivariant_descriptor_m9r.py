import importlib.util
from pathlib import Path

P = Path(__file__).resolve().parents[1] / "src" / "permutation_equivariant_descriptor_m9r.py"
S = importlib.util.spec_from_file_location("m9r", P)
M = importlib.util.module_from_spec(S)
S.loader.exec_module(M)
R = M.build()


def test_status():
    assert R["status"] == "PERMUTATION_EQUIVARIANT_NEW_LABEL_GENERALIZATION_NOT_CERTIFIED"


def test_train_atlas():
    assert R["atlas"]["train_ordered_carriers"] == 75
    assert R["atlas"]["train_representation_families"] == 9


def test_independent_test_atlas():
    assert R["atlas"]["test_ordered_carriers"] == 208
    assert R["atlas"]["test_representation_families"] == 15
    assert all(max(key) >= 5 for key in R["atlas"]["test_family_keys"])


def test_all_targets_improved():
    assert all(value >= 0.10 for value in R["models"]["relative_improvement"])


def test_absolute_threshold_fails():
    assert not all(value <= 0.40 for value in R["models"]["permutation_equivariant_descriptor_test_nrmse"])


def test_anchor_amplitude_near_but_above_threshold():
    value = R["models"]["permutation_equivariant_descriptor_test_nrmse"][0]
    assert 0.40 < value < 0.60


def test_higher_jets_not_certified():
    assert R["decision"]["higher_jet_transfer"] == "NOT_CERTIFIED"


def test_cross_carrier_gate_blocked():
    assert R["decision"]["new_cross_carrier_pilot"] == "BLOCKED"


def test_numerical_stability():
    assert R["criteria"]["actual_maximum_numerical_jet_instability"] < 1e-4


def test_evidence_rule():
    assert R["evidence_rule"] == "No statement from the Gemini advisory report is used as evidence."
