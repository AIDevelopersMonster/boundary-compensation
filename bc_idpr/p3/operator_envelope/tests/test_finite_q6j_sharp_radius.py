import importlib.util
from pathlib import Path
P=Path(__file__).resolve().parents[1]/'src'/'finite_q6j_sharp_radius.py'
S=importlib.util.spec_from_file_location('radius',P);M=importlib.util.module_from_spec(S);S.loader.exec_module(M);R=M.build()
def test_status(): assert R['status']=='TAYLOR_CAUCHY_UNIFORM_RADIUS_CERTIFIED'
def test_class(): assert R['declared_class']=={'ordered_carriers':283,'representation_families':24}
def test_ratio(): assert abs(R['radii']['confirmatory_to_wall_ratio']-.1)<1e-15
def test_improvement(): assert R['radii']['confirmatory_certified_radius']>0.001636246173744685
def test_margin(): assert R['margins']['confirmatory_minimum_abs_omega_lower_bound']>0.15
def test_extremal(): assert 0.1007<R['radii']['extremal_to_wall_ratio']<0.1009
def test_qmargin(): assert R['margins']['minimum_q_number_lower_bound_at_confirmatory_radius']>0.25
def test_readiness(): assert R['decision']['preprint_mathematical_core']=='READY'
def test_no_fit(): assert R['method']['fitted_parameter_count']==0
def test_evidence(): assert 'Gemini advisory report' in R['evidence_rule']
