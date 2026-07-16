import importlib.util
from pathlib import Path

P = Path(__file__).resolve().parents[1] / "src" / "analytic_log_speed_slope.py"
S = importlib.util.spec_from_file_location("m11", P)
M = importlib.util.module_from_spec(S)
S.loader.exec_module(M)
R = M.build()


def test_status():
    assert R["status"] == "ANALYTIC_Q6J_LOG_SPEED_SLOPE_CERTIFIED"


def test_atlas_counts():
    assert R["atlas"]["test_ordered_carriers"] == 208
    assert R["atlas"]["test_family_count"] == 15


def test_no_fitted_parameters():
    assert R["analytic_identity"]["fitted_parameter_count"] == 0


def test_analytic_residual():
    assert R["validation"]["maximum_relative_analytic_vs_refined_fd_residual"] <= 1e-6


def test_reference_step_agreement():
    assert R["validation"]["maximum_fd_step_disagreement_relative"] <= 1e-6


def test_orthogonality():
    assert R["validation"]["maximum_orthogonality_residual"] <= 1e-10


def test_generator_skew():
    assert R["validation"]["maximum_generator_skew_residual"] <= 1e-7


def test_generator_prime_skew():
    assert R["validation"]["maximum_generator_prime_skew_residual"] <= 1e-6


def test_gate_split():
    assert R["decision"]["analytic_second_jet"] == "CLOSED"
    assert R["decision"]["analytic_third_jet"] == "OPEN_SEPARATE_OBLIGATION"


def test_evidence_rule():
    assert "Gemini advisory report" in R["evidence_rule"]
