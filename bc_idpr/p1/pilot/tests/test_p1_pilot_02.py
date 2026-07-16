from __future__ import annotations
import importlib.util
from pathlib import Path


def load_module():
    path = Path(__file__).resolve().parents[1] / "src" / "p1_pilot_02.py"
    spec = importlib.util.spec_from_file_location("p1_pilot_02", path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def result():
    return load_module().build(129)


def test_status():
    assert result()["status"] == "PREREGISTERED_RECOUPLING_ANGLE_CRITERIA_MET"


def test_preregistration_commit_frozen():
    assert result()["preregistration_commit"] == "8ee32533dc7991707b3e2e78c43c0096c459da27"


def test_negative_control():
    r = result()
    assert r["controls"]["negative_control_max_abs"] <= r["controls"]["threshold"]


def test_signal_excursion():
    r = result()
    assert r["signal"]["maximum_quotient_excursion"] >= r["signal"]["minimum_required"]


def test_phase_cv_error():
    assert result()["recoupling_angle_model"]["cv_normalized_rmse"] <= 0.05


def test_phase_advantage():
    r = result()
    assert r["comparison"]["relative_cv_advantage"] >= r["comparison"]["minimum_required"]


def test_phase_stability():
    assert result()["recoupling_angle_model"]["coefficient_stability"] <= 0.25


def test_equal_model_dimension():
    r = result()
    assert len(r["recoupling_angle_model"]["basis"]) == 3
    assert r["smooth_null"]["degree"] == 3


def test_claim_firewall():
    gate = result()["claim_gate"]
    assert gate["model_internal_recoupling_structure"] == "SUPPORTED"
    assert gate["independent_phase_law"] == "BLOCKED"
    assert gate["universal_phase_law"] == "BLOCKED"
    assert gate["physical_interpretation"] == "BLOCKED"
