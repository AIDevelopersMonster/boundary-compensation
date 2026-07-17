# BC-IDPR-CERT-01

## Protocol-Relative Observable Separation Certificate

**Programme:** Boundary Compensation — Independent Deformation and Phase-Resolved Response  
**Layer:** CERT  
**Status:** `SEPARATION_NOT_CERTIFIED`  
**Date:** 2026-07-16  
**Upstream:** `BC-IDPR-P3-B-02`, `BC-IDPR-P3-B-03`, `BC-IDPR-P3-B-04`

---

## 1. Purpose

P3-B established four distinct facts:

1. a nonzero intrinsic generic-q operator tangent;
2. persistence under a direct three-channel q-Racah implementation;
3. exact fixation of a complete external tetrahedral geometry;
4. a protocol-relative coherent lower-symbol bridge.

CERT asks the next and stricter question:

> Is the observable q-response separated from the declared symbol mismatch, calibration-protocol variation, arithmetic uncertainty, nuisance equivalence and wall uncertainty by a positive net margin?

A nonzero derivative is not sufficient. The relevant condition is

\[
m_{\rm sep}
=
R_q-E_{\rm model}-E_{\rm protocol}-E_{\rm num}-E_{\rm wall}>0.
\]

---

## 2. Frozen observable protocol

The primary protocol is inherited from M4:

- carrier: four external spin-one representations;
- invariant carrier dimension: three;
- observables: \(g_{12}=n_1\cdot n_2\) and \(g_{23}=n_2\cdot n_3\);
- coherent state: normalized invariant projection of four SU(2) coherent states;
- q-dependent second-channel operator: \(F(\theta)G_{12}F(\theta)^T\);
- anchor: \(\theta_0=\pi/8\);
- compact interval: \([\pi/10,3\pi/20]\);
- primary calibration: additive offsets fitted only on the regular tetrahedron at the anchor.

The first observable is a q-independent negative control. Observable separation is therefore tested on the complete two-coordinate symbol, with the response carried by the second coordinate.

---

## 3. Response quantity

For a fixed geometry \(g\), frozen calibration \(p\), and symbol \(S_p^g(\theta)\), define the finite-excursion response

\[
R_p^g(\theta)
=
\|S_p^g(\theta)-S_p^g(\theta_0)\|_2.
\]

On the preregistered 33-point grid, the primary regular-anchor protocol gives

\[
\max_{\theta}R_{\rm reg}^{\rm regular}(\theta)
=0.013713613923774015,
\]

\[
\max_{\theta}R_{\rm reg}^{\rm holdout}(\theta)
=0.04984235930414149.
\]

The nonzero derivative from M4 is therefore confirmed, but CERT evaluates whether this finite response is distinguishable from the error budget.

---

## 4. Model mismatch

For the independent anisotropic equifacial holdout, the primary frozen protocol has

\[
0.07819043294294023
\le
E_{\rm hold}(\theta)
\le
0.1491999657742081.
\]

At the anchor,

\[
E_{\rm hold}(\theta_0)=0.10211910127354808.
\]

Thus even the smallest recorded holdout mismatch exceeds the largest recorded holdout response:

\[
0.07819043294294023
>
0.04984235930414149.
\]

This alone prevents a positive conservative separation margin.

---

## 5. Calibration-protocol stress test

Four frozen additive calibration policies were preregistered for CERT:

1. regular-anchor offset;
2. zero offset;
3. midpoint of regular and holdout anchor offsets;
4. holdout-anchor offset.

These policies do not change the q-response excursion because they differ by theta-independent offsets, but they change the absolute symbol mismatch.

The maximum displacement of an alternative frozen calibration from the primary protocol is

\[
E_{\rm protocol}^{\max}
=0.10211910127354819.
\]

This is not treated as a statistical standard deviation. It is a deterministic protocol envelope.

---

## 6. Numerical, wall and nuisance terms

The following inherited controls remain valid:

- q-Racah arithmetic: 80 decimal digits;
- coherent-carrier computation: double precision;
- carrier basis Gram residual: below \(6.0\times10^{-16}\);
- q-Racah orthogonality residual: below \(2.2\times10^{-16}\) in the M4 bridge implementation;
- external geometry leakage: exactly zero by M3;
- compact interval wall distance: at least \(\pi/20\);
- operator nuisance-quotient margin: positive by M2/M3.

These terms are too small, or independently controlled, to reverse the dominant failure caused by finite-j symbol mismatch and calibration dependence.

---

## 7. Conservative net margin

CERT uses the holdout geometry and defines

\[
m_{\rm sep}(\theta)
=
R_{m hold}(\theta)
-E_{m hold}(\theta)
-E_{m protocol}(\theta).
\]

On the declared grid,

\[
\max_{\theta}m_{\rm sep}(\theta)
=-0.1534617349737727,
\]

and

\[
\min_{\theta}m_{\rm sep}(\theta)
=-0.20423820254709618.
\]

Therefore no sampled point has a positive net separation margin.

Even under the weaker budget that omits protocol variation,

\[
R_{m hold}^{\max}-E_{m hold}^{\min}
=
-0.02834807363879874<0.
\]

The failure is therefore not created solely by the alternative-calibration stress test.

---

## 8. Decision

Assign status

`SEPARATION_NOT_CERTIFIED`.

The controlled statement is:

> The declared coherent-state protocol exhibits a reproducible nonzero q-response at fixed external geometry, but the response is not separated from finite-spin symbol mismatch and frozen-calibration uncertainty by a positive margin.

Consequently:

- P3 remains successful as an operator-level independent-deformation result;
- M4 remains successful as a nonempty semantic bridge;
- the present observable protocol fails CERT;
- confirmatory P1 is not authorized;
- no phase-residual law may be claimed from this protocol.

---

## 9. Scientific interpretation

This is not a falsification of independent q-deformation. It is a falsification of the stronger claim that the present spin-one, two-coordinate, additive-calibration coherent-symbol protocol already makes that deformation observably distinguishable.

The failure localizes the bottleneck:

\[
\text{operator nontriviality}
\quad\checkmark,
\qquad
\text{external-geometry control}
\quad\checkmark,
\qquad
\text{semantic bridge}
\quad\checkmark,
\qquad
\text{observable separation}
\quad\times.
\]

---

## 10. Required next step

Proceed to `BC-IDPR-CERT-02 / Resolution-and-Protocol Lift`.

It must improve separation without post hoc tuning by at least one of the following preregistered routes:

1. increase representation scale \(j\) and test finite-j convergence;
2. enlarge the Gram-observable package beyond two coordinates;
3. use nonuniform external spins and an unequal-area scalene holdout;
4. replace additive calibration by a theoretically constrained symbol normalization;
5. construct a multi-geometry calibration/validation split;
6. prove a uniform response lower bound and a symbol-error upper bound on a compact chamber.

P1 remains blocked until a positive net margin is certified on independent holdout data.
