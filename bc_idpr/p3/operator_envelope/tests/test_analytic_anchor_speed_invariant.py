import importlib.util
from pathlib import Path

P = Path(__file__).resolve().parents[1] / "src" / "analytic_anchor_speed_invariant.py"
S = importlib.util.spec_from_file_location("m10", P)
M = importlib.util.module_from_spec(S)
S.loader.exec_module(M)
R = M.build()


def test_status():
    assert R["status"] == "ANALYTIC_Q6J_ANCHOR_SPEED_INVARIANT_CERTIFIED"


def test_no_fit():
    assert R["analytic_identity"]["fitted_parameter_count"] == 0


def test_atlas():
    assert R["atlas"]["test_ordered_carriers"] == 208
    assert R["atlas"]["test_family_count"] == 15


def test_relative_residual():
    assert R["validation"]["maximum_relative_analytic_vs_refined_fd_residual"] <= 1e-7


def test_step_stability():
    assert R["validation"]["maximum_fd_step_disagreement_relative"] <= 1e-7


def test_orthogonality():
    assert R["validation"]["maximum_orthogonality_residual"] <= 1e-10


def test_skew():
    assert R["validation"]["maximum_generator_skew_residual"] <= 1e-7


def test_formula_closed():
    assert R["decision"]["explicit_anchor_speed_formula"] == "CLOSED"


def test_higher_jet_open():
    assert R["decision"]["higher_jet_formula"] == "OPEN_SEPARATE_OBLIGATION"


def test_evidence_rule():
    assert "Gemini advisory report" in R["evidence_rule"]
