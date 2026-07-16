import importlib.util
from pathlib import Path
P=Path(__file__).resolve().parents[1]/'src'/'finite_q6j_uniform_conditioning.py'
S=importlib.util.spec_from_file_location('conditioning',P);M=importlib.util.module_from_spec(S);S.loader.exec_module(M);R=M.build()
def test_status(): assert R['status']=='UNIFORM_FINITE_Q6J_JET_CONDITIONING_CERTIFIED_ON_DECLARED_DISK'
def test_radius_ratio(): assert abs(R['radii']['certified_to_wall_ratio']-1/16)<1e-15
def test_q_lower(): assert R['q_number_bounds']['minimum_lower_bound']>0.25
def test_omega_lower(): assert R['complex_boundary_validation']['certified_abs_omega_lower_bound']>0.09
def test_majorant(): assert R['cauchy_majorant_check']['all_checked_coefficients_below_majorant']
def test_class(): assert R['declared_class']['ordered_carriers']==283 and R['declared_class']['representation_families']==24
def test_gates(): assert R['decision']['uniform_log_speed_domain']=='CLOSED_ON_DECLARED_DISK'
def test_evidence_rule(): assert 'Gemini advisory report' in R['evidence_rule']
