from pathlib import Path
import importlib.util

P=Path(__file__).resolve().parents[1]/'src'/'calibration_quotient_differential.py'
S=importlib.util.spec_from_file_location('cert02',P)
M=importlib.util.module_from_spec(S); S.loader.exec_module(M)
R=M.build(33)

def test_status(): assert R['status']=='CALIBRATION_QUOTIENT_DIFFERENTIAL_SEPARATION_CERTIFIED'
def test_dimension(): assert R['observable_package']['dimension']==4
def test_offset_quotient(): assert R['calibration_quotient']['invariance_residual']<1e-12
def test_anchor_response(): assert R['anchor_response']['derivative_norm']>0.45
def test_adjacent_separation(): assert R['grid_summary']['minimum_adjacent_separation']>1e-3
def test_positive_net_margin(): assert R['uncertainty_ledger']['net_adjacent_margin']>1e-3
def test_gate_split():
    assert R['gate']['differential_p1_pilot']=='OPEN'
    assert R['gate']['static_absolute_symbol_gate']=='BLOCKED_BY_CERT_01'
