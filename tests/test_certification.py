import numpy as np

from bc_gateway.certification import certify_threshold_margin, threshold_rank
from bc_gateway.choi import qubit_dephasing_choi
from bc_gateway.status import Status


def test_threshold_rank_for_dephasing_choi():
    matrix = qubit_dephasing_choi(0.9)
    assert threshold_rank(matrix, 0.05) == 1
    assert threshold_rank(matrix, 0.04) == 2


def test_margin_status():
    matrix = qubit_dephasing_choi(0.9)
    result = certify_threshold_margin(matrix, threshold=0.05, tolerance=0.02)
    assert result.status == Status.MARGIN_LOW
    assert np.isclose(result.margin, 0.0)
