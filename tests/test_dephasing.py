import numpy as np

from bc_gateway.models import gamma_abs_two_spin_bath, lambda_minus_from_gamma_abs


def test_gamma_abs_at_zero_is_one():
    assert np.isclose(gamma_abs_two_spin_bath(0.0), 1.0)


def test_lambda_minus_formula():
    gamma_abs = np.array([1.0, 0.9, 0.0])
    expected = np.array([0.0, 0.05, 0.5])
    assert np.allclose(lambda_minus_from_gamma_abs(gamma_abs), expected)
