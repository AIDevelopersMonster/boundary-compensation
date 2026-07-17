import importlib.util
from pathlib import Path

MODULE = Path(__file__).resolve().parents[1] / "src" / "p1_pilot_01.py"
spec = importlib.util.spec_from_file_location("pilot", MODULE)
pilot = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(pilot)
RESULT = pilot.build(257)

def test_preregistration_commit_is_frozen():
    assert RESULT["preregistration_commit"] == "3991d90fae3872384438749441b90e4495188c85"

def test_dense_grid_is_frozen():
    assert RESULT["domain"]["sample_count"] == 257

def test_negative_controls_pass():
    assert RESULT["controls"]["passed"]

def test_signed_excursion_passes():
    assert RESULT["signal"]["passed"]

def test_phase_fit_is_numerically_good():
    assert RESULT["phase_model"]["cv_normalized_rmse"] < 0.05

def test_phase_specific_advantage_fails():
    assert not RESULT["comparison"]["passed"]

def test_final_status_is_negative():
    assert RESULT["status"] == "PREREGISTERED_PHASE_MODEL_CRITERIA_NOT_MET"

def test_confirmatory_gate_remains_blocked():
    assert RESULT["claim_gate"]["confirmatory_phase_law"] == "BLOCKED"
