import importlib.util
from pathlib import Path

P=Path(__file__).resolve().parents[1]/'src'/'finite_q6j_jet_calculus.py'
S=importlib.util.spec_from_file_location('jet',P); M=importlib.util.module_from_spec(S); S.loader.exec_module(M)
R=M.build()

def test_status(): assert R['status']=='FINITE_Q6J_RECURSIVE_JET_CALCULUS_CERTIFIED_THROUGH_LOG_ORDER_2'
def test_atlas(): assert R['atlas']['test_ordered_carriers']==208 and R['atlas']['test_family_count']==15
def test_speed_gate(): assert R['validation']['speed_relative_residual']<1e-7
def test_slope_gate(): assert R['validation']['log_speed_slope_relative_residual']<1e-6
def test_curvature_gate(): assert R['validation']['log_speed_curvature_relative_residual']<1e-5
def test_reference_stability(): assert R['validation']['curvature_reference_step_disagreement']<1e-5
def test_orthogonality(): assert R['validation']['orthogonality_residual']<1e-10
def test_skew_orders(): assert all(R['validation'][f'generator_skew_residual_order_{k}']<10**(-7+k) for k in range(3))
def test_no_fit(): assert R['general_lemma']['fitted_parameter_count']==0
def test_general_recurrence(): assert 'sum_' in R['general_lemma']['generator_recurrence']
def test_validation_ceiling(): assert R['implementation_validation_ceiling']['log_speed_derivative_order']==2
def test_evidence_rule(): assert 'Gemini advisory report' in R['evidence_rule']
