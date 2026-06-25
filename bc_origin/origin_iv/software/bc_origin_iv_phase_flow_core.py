"""
BC-Origin IV phase-flow core, v0.1.1 software patch.

Finite-dimensional toy-model utilities for lifted phase flow, structural-overlap
avoided crossings, closure-lift reindexing, and admissibility-horizon diagnostics
in BC-Origin shadow operators.

Claim boundary:
- This is not a physical-time simulator.
- This is not a Landau-Zener transition-probability model.
- This is not a physical Thouless-pump simulation.
- The lifted-phase reindexing identity is a closure-denominator identity on the
  lifted phase cover unless an additional sheet-transition rule is declared.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Iterable, Sequence
import math
import numpy as np

TAU = 2.0 * math.pi


def validate_nonzero_winding(n: int, name: str = "n") -> int:
    """Validate a BC-Origin winding label and return it as an int."""
    n_int = int(n)
    if n_int == 0:
        raise ValueError(f"{name} must be nonzero in the BC-Origin winding-index model.")
    return n_int


@dataclass(frozen=True)
class PhaseFlowBranch:
    """One lifted-phase shadow denominator branch.

    Parameters
    ----------
    n_abs:
        Positive winding magnitude |n|.
    theta0:
        Initial lifted residual phase. This is not reduced modulo 2*pi.
    phase_lift_coefficient:
        Coefficient of the declared path on the lifted phase cover:
        Theta(lambda) = theta0 + lambda * phase_lift_coefficient.
        It is not a physical velocity or a time derivative.
    """

    n_abs: int
    theta0: float = 0.0
    phase_lift_coefficient: float = TAU

    def __post_init__(self) -> None:
        if int(self.n_abs) <= 0:
            raise ValueError("n_abs must be a positive winding magnitude |n|.")

    def theta_lift(self, lam: float) -> float:
        """Lifted phase Theta(lambda), not reduced modulo 2*pi."""
        return float(self.theta0 + lam * self.phase_lift_coefficient)

    def theta_mod(self, lam: float) -> float:
        """Circle phase theta(lambda) = Theta(lambda) mod 2*pi."""
        return float(self.theta_lift(lam) % TAU)

    def denominator(self, lam: float) -> float:
        """Closure denominator d(lambda) = 2*pi*|n| - Theta(lambda)."""
        return float(TAU * int(self.n_abs) - self.theta_lift(lam))


def lorentz_kernel(n_i: int, n_j: int) -> float:
    """Declared index-space Lorentzian kernel K_ij = 1/(1+(n_i-n_j)^2)."""
    n_i = validate_nonzero_winding(n_i, "n_i")
    n_j = validate_nonzero_winding(n_j, "n_j")
    m = n_i - n_j
    return 1.0 / (1.0 + float(m * m))


def exponential_kernel(n_i: int, n_j: int, alpha: float = 1.0) -> float:
    """Declared index-space exponential kernel exp(-alpha*|n_i-n_j|)."""
    n_i = validate_nonzero_winding(n_i, "n_i")
    n_j = validate_nonzero_winding(n_j, "n_j")
    if alpha < 0:
        raise ValueError("alpha must be nonnegative for the exponential kernel.")
    return float(math.exp(-float(alpha) * abs(n_i - n_j)))


def kernel_value(n_i: int, n_j: int, kind: str = "lorentz", alpha: float = 1.0) -> float:
    """Evaluate a declared structural kernel on hidden winding-index labels."""
    if kind in {"lorentz", "lorentzian"}:
        return lorentz_kernel(n_i, n_j)
    if kind in {"exp", "exponential"}:
        return exponential_kernel(n_i, n_j, alpha=alpha)
    raise ValueError(f"unknown kernel kind: {kind}")


@dataclass(frozen=True)
class TwoShadowInvariants:
    """Trace/determinant/eigenvalue diagnostics for a two-shadow operator."""

    d1: float
    d2: float
    structural_overlap: float
    trace: float
    determinant: float
    lambda_minus: float
    lambda_plus: float
    gap: float


def build_two_shadow_operator(
    branch1: PhaseFlowBranch,
    branch2: PhaseFlowBranch,
    lam: float,
    structural_overlap: float,
) -> np.ndarray:
    """Build the minimal two-shadow lifted phase-flow operator."""
    k = float(structural_overlap)
    d1 = branch1.denominator(lam)
    d2 = branch2.denominator(lam)
    return np.array([[d1, k], [k, d2]], dtype=float)


def two_shadow_invariants(
    branch1: PhaseFlowBranch,
    branch2: PhaseFlowBranch,
    lam: float,
    structural_overlap: float,
) -> TwoShadowInvariants:
    """Return trace, determinant and ordered eigen-denominator diagnostics."""
    D = build_two_shadow_operator(branch1, branch2, lam, structural_overlap)
    ev = np.linalg.eigvalsh(D)
    d1 = float(D[0, 0])
    d2 = float(D[1, 1])
    tr = d1 + d2
    det = d1 * d2 - float(structural_overlap) ** 2
    return TwoShadowInvariants(
        d1=d1,
        d2=d2,
        structural_overlap=float(structural_overlap),
        trace=float(tr),
        determinant=float(det),
        lambda_minus=float(ev[0]),
        lambda_plus=float(ev[1]),
        gap=float(ev[1] - ev[0]),
    )


def two_shadow_eigenvalues(
    branch1: PhaseFlowBranch,
    branch2: PhaseFlowBranch,
    lam: float,
    structural_overlap: float,
) -> np.ndarray:
    """Return ordered eigen-denominators of the two-shadow operator."""
    return np.linalg.eigvalsh(build_two_shadow_operator(branch1, branch2, lam, structural_overlap))


def two_shadow_gap(
    branch1: PhaseFlowBranch,
    branch2: PhaseFlowBranch,
    lam: float,
    structural_overlap: float,
) -> float:
    """Return lambda_plus - lambda_minus for the two-shadow operator."""
    ev = two_shadow_eigenvalues(branch1, branch2, lam, structural_overlap)
    return float(ev[-1] - ev[0])


def horizon_value(D: np.ndarray) -> float:
    """Return lambda_min(D), the local admissibility-horizon diagnostic."""
    return float(np.linalg.eigvalsh(np.asarray(D, dtype=float))[0])


def localized_count(D: np.ndarray, threshold: float = 0.0) -> int:
    """Count eigen-denominators above a declared localization threshold."""
    return int(np.sum(np.linalg.eigvalsh(np.asarray(D, dtype=float)) > threshold))


def find_zero_crossings_linear(x: Sequence[float], y: Sequence[float]) -> list[float]:
    """Estimate zero crossings by linear interpolation over a sampled curve."""
    x_arr = np.asarray(x, dtype=float)
    y_arr = np.asarray(y, dtype=float)
    if x_arr.shape != y_arr.shape:
        raise ValueError("x and y must have the same shape")
    roots: list[float] = []
    for i in range(len(x_arr) - 1):
        y0 = y_arr[i]
        y1 = y_arr[i + 1]
        if y0 == 0.0:
            roots.append(float(x_arr[i]))
        elif y0 * y1 < 0.0:
            t = -y0 / (y1 - y0)
            roots.append(float(x_arr[i] + t * (x_arr[i + 1] - x_arr[i])))
    if len(y_arr) and y_arr[-1] == 0.0:
        roots.append(float(x_arr[-1]))
    return roots


def lifted_phase_reindex_denominator(n_abs: int, theta: float, periods: int = 1) -> tuple[float, float]:
    """Return both sides of the closure-lift reindexing identity.

        d(|n|, Theta + 2*pi*m) = d(|n|-m, Theta)

    This is an identity on the lifted phase cover. It is not, by itself, a
    physical transition rule between winding sectors.
    """
    n_abs = int(n_abs)
    periods = int(periods)
    if n_abs <= 0:
        raise ValueError("n_abs must be positive")
    if periods < 0:
        raise ValueError("periods must be nonnegative")
    if n_abs - periods < 0:
        raise ValueError("n_abs - periods must be nonnegative for this toy identity")
    lhs = TAU * n_abs - (float(theta) + periods * TAU)
    rhs = TAU * (n_abs - periods) - float(theta)
    return float(lhs), float(rhs)


def build_multi_shadow_operator(
    n_values: Sequence[int],
    branches: Sequence[PhaseFlowBranch],
    lam: float,
    global_kernel_normalization: float = 1.0,
    edge_holonomy: np.ndarray | None = None,
    kernel_kind: str = "lorentz",
) -> np.ndarray:
    """Build an N-shadow lifted phase-flow operator.

    Baseline convention:
        D_ii(lambda) = d_i(lambda)
        D_ij(lambda) = eta * epsilon_ij * K(n_i,n_j), i != j

    eta is a global visualization/model normalization, not a pairwise fitted
    coupling. epsilon is a symmetric +/-1 edge-holonomy matrix. If omitted,
    epsilon_ij=1.
    """
    n_values = [validate_nonzero_winding(n, f"n_values[{i}]") for i, n in enumerate(n_values)]
    branches = list(branches)
    N = len(n_values)
    if len(branches) != N:
        raise ValueError("n_values and branches must have the same length")
    if edge_holonomy is None:
        edge_holonomy = np.ones((N, N), dtype=float)
    edge_holonomy = np.asarray(edge_holonomy, dtype=float)
    if edge_holonomy.shape != (N, N):
        raise ValueError("edge_holonomy must be an N x N matrix")
    if not np.allclose(edge_holonomy, edge_holonomy.T):
        raise ValueError("edge_holonomy must be symmetric for a real self-adjoint operator")

    D = np.zeros((N, N), dtype=float)
    for i in range(N):
        D[i, i] = branches[i].denominator(lam)
    for i in range(N):
        for j in range(i + 1, N):
            kij = kernel_value(n_values[i], n_values[j], kind=kernel_kind)
            val = float(global_kernel_normalization) * edge_holonomy[i, j] * kij
            D[i, j] = D[j, i] = val
    return D


def scan_spectrum(D_of_lam: Callable[[float], np.ndarray], lam_grid: Iterable[float]) -> np.ndarray:
    """Evaluate eigvalsh(D(lambda)) on a grid."""
    return np.asarray([np.linalg.eigvalsh(D_of_lam(float(lam))) for lam in lam_grid])
