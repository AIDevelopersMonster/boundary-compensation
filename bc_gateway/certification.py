"""Threshold-rank certification utilities."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .status import Status


@dataclass(frozen=True)
class CertificationResult:
    """Result of a threshold-margin certification check."""

    threshold: float
    tolerance: float
    margin: float
    effective_rank: int
    status: Status


def _eigvals_hermitian(matrix: np.ndarray) -> np.ndarray:
    """Return eigenvalues of a Hermitian matrix as a real NumPy array."""
    values = np.linalg.eigvalsh(np.asarray(matrix, dtype=complex))
    return np.real_if_close(values).astype(float)


def threshold_rank(matrix: np.ndarray, threshold: float) -> int:
    """Count eigenvalues strictly above the declared threshold."""
    if threshold < 0:
        raise ValueError("threshold must be non-negative")
    eigvals = _eigvals_hermitian(matrix)
    return int(np.count_nonzero(eigvals > threshold))


def threshold_margin(matrix: np.ndarray, threshold: float) -> float:
    """Distance from the declared threshold to the spectrum."""
    if threshold < 0:
        raise ValueError("threshold must be non-negative")
    eigvals = _eigvals_hermitian(matrix)
    return float(np.min(np.abs(eigvals - threshold)))


def certify_threshold_margin(matrix: np.ndarray, threshold: float, tolerance: float) -> CertificationResult:
    """Certify threshold-rank stability under deterministic operator-norm tolerance.

    If the spectral margin is larger than the tolerance, the threshold rank is stable
    under all positive operator perturbations of norm at most ``tolerance``. Otherwise
    the margin is low and a pathwise continuation must reset before proceeding.
    """
    if tolerance < 0:
        raise ValueError("tolerance must be non-negative")
    margin = threshold_margin(matrix, threshold)
    rank = threshold_rank(matrix, threshold)
    status = Status.CERTIFIED_STABLE if margin > tolerance else Status.MARGIN_LOW
    return CertificationResult(
        threshold=float(threshold),
        tolerance=float(tolerance),
        margin=margin,
        effective_rank=rank,
        status=status,
    )
