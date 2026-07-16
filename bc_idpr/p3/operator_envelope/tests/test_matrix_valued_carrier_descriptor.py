import importlib.util
from pathlib import Path

P=Path(__file__).resolve().parents[1]/'src'/'matrix_valued_carrier_descriptor.py'
S=importlib.util.spec_from_file_location('m7',P); M=importlib.util.module_from_spec(S); S.loader.exec_module(M)
R=M.build()


def test_status(): assert R['status']=='REPRESENTATION_DESCRIPTOR_LOOCV_NOT_CERTIFIED'
def test_atlas(): assert R['domain']['atlas_size']==75
def test_dimensions(): assert R['descriptors']['baseline_dimension']==10 and R['descriptors']['matrix_augmented_dimension']==14
def test_dimensions_match_feature_vectors():
    J=M.build_atlas()[0]
    assert R['descriptors']['baseline_dimension']==M.descriptor(J,False).shape[0]
    assert R['descriptors']['matrix_augmented_dimension']==M.descriptor(J,True).shape[0]
def test_no_derivative_leakage(): assert R['descriptors']['derivatives_excluded_from_predictors']
def test_matrix_improves_all(): assert R['loocv']['all_targets_improved']
def test_threshold_fails(): assert not R['loocv']['all_targets_below_threshold']
def test_omega_not_certified(): assert R['gates']['omega_prediction']=='NOT_CERTIFIED'
def test_higher_jet_not_certified(): assert R['gates']['higher_jet_prediction']=='NOT_CERTIFIED'
def test_numerical_stability(): assert R['numerical_stability']['maximum_relative_jet_change_h_to_h_over_2']<2e-5
def test_evidence_rule(): assert 'Gemini advisory report' in R['evidence_rule']
