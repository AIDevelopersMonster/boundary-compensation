import importlib.util
from pathlib import Path
P=Path(__file__).resolve().parents[1]/'src'/'g2r_interval_conditioning.py'
S=importlib.util.spec_from_file_location('g2r',P);M=importlib.util.module_from_spec(S);S.loader.exec_module(M);R=M.build()
def test_status(): assert R['status']=='RIGOROUS_ARB_UNIFORM_CONDITIONING_CERTIFIED'
def test_backend(): assert R['arithmetic']['backend']=='python-flint Arb' and R['arithmetic']['outward_rounding']
def test_class(): assert R['primary_run']['ordered_carriers_covered_by_symmetry']==283
def test_families(): assert R['primary_run']['representation_families']==24 and R['primary_run']['canonical_family_representatives_evaluated']==24
def test_primary_positive(): assert R['primary_run']['minimum_lower_bound']>0.16
def test_control_positive(): assert R['control_run']['minimum_lower_bound']>0.16
def test_precision_stability(): assert R['primary_run']['worst_carrier']==R['control_run']['worst_carrier']==[1,1,1,1]
def test_frozen_radius(): assert R['proof_family']['confirmatory_radius']=='pi/1200'
def test_gate(): assert R['decision']['G2_overall']=='PASS'
def test_evidence(): assert 'Gemini advisory report' in R['evidence_rule']
