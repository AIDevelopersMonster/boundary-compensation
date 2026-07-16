# BC-IDPR-CERT-01

## Protocol-Relative Observable Separation Certificate

**Programme:** Boundary Compensation — Independent Deformation and Phase-Resolved Response (BC-IDPR)  
**Layer:** CERT — observable separation  
**Status:** `Q_RESPONSE_DETECTED_BUT_SYMBOL_SEPARATION_NOT_CERTIFIED`  
**Date:** 2026-07-16  
**Upstream:** `BC-IDPR-P3-B-02`, `BC-IDPR-P3-B-03`, `BC-IDPR-P3-B-04`

---

## 1. Purpose

P3-B established three different facts:

1. the finite generic-q operator package has a nonzero nuisance-quotient derivative;
2. the complete external tetrahedral geometry can be held exactly fixed with zero external leakage;
3. a declared coherent-state lower-symbol protocol transfers the operator response to two normal-Gram observables.

CERT asks the stronger question:

> Is the observable q-response separated from the complete finite-spin symbol-error and protocol-variation budget by a positive declared margin?

A nonzero derivative is not sufficient. The result must survive an independent holdout geometry and the declared calibration family.

---

## 2. Upstream gates

The inherited gates are satisfied:

\[
E_{\mathrm{ext}}=0,
\]

\[
\min_I m_{\mathrm{int}}=1.229236658459239\ldots>0,
\]

\[
\min_I m_{\mathrm{op}}^{\mathrm{dual}}
=0.5322970424764865\ldots>0.
\]

The compact path remains

\[
I=\left[\frac{\pi}{10},\frac{3\pi}{20}\right],
\qquad
\theta_0=\frac{\pi}{8},
\]

with wall margin at least

\[
\frac{\pi}{20}.
\]

Thus any failure at CERT-01 is not attributed to geometry leakage, a vanishing operator tangent, or a wall event.

---

## 3. Observable contrast

For a fixed geometry and frozen protocol, define the full-path differential contrast

\[
R_g
=
\left\|
\widetilde S_g\!\left(\frac{3\pi}{20}\right)
-
\widetilde S_g\!\left(\frac{\pi}{10}\right)
\right\|_2.
\]

The finite-spin symbol-error budget is

\[
E_{\mathrm{sym},g}
=
\max_{\theta\in I_{33}}
\left\|
\widetilde S_g(\theta)-T_g
\right\|_2,
\]

where `I_33` is the preregistered 33-point grid and `T_g` is the fixed classical normal-Gram target.

The conservative per-case margin is

\[
M_g
=
R_g-E_{\mathrm{sym},g}
-E_{\mathrm{num}}-E_{\mathrm{ext}}-E_{\mathrm{wall}}.
\]

The numerical allowance is fixed at

\[
E_{\mathrm{num}}=10^{-10}.
\]

The global certificate margin is

\[
M_{\mathrm{global}}
=
\min_{\text{geometry, protocol}}M_g.
\]

P1 pilot authorization requires

\[
M_{\mathrm{global}}>0.
\]

This is a sufficient-condition protocol. Failure does not prove that no other estimator or quantization could separate the response.

---

## 4. Admissible protocol family

Three calibration classes are audited.

### 4.1 Raw protocol

No calibration:

\[
\widetilde S=S_{\mathrm{raw}}.
\]

### 4.2 M4 frozen additive calibration

Per-channel offsets are fitted only on the regular tetrahedron at the anchor and then frozen.

### 4.3 Near-identity diagonal affine family

\[
\widetilde S_i=a_iS_{\mathrm{raw},i}+b_i,
\qquad
0.9\le a_i\le1.1,
\]

with offsets chosen so that the regular anchor target is preserved. All four slope-box corners are evaluated. Since the grid mismatch is a norm of an affine function of the slopes, the corner audit supplies the declared finite-family stress test.

The holdout is excluded from all calibration fits.

---

## 5. Numerical audit

The maximum discrepancy between the double-precision bridge and an independent 100-decimal q-Racah symbol evaluation at the endpoints and anchor is

\[
1.2413\times10^{-16}.
\]

The maximum discrepancy between two five-point derivative estimates under step halving is

\[
1.299\times10^{-12}.
\]

Both are dominated by the declared allowance `1e-10`.

---

## 6. Baseline M4 result

### 6.1 Regular calibration geometry

\[
R_{\mathrm{reg}}=0.01921494191009726,
\]

\[
E_{\mathrm{sym,reg}}=0.013713613923774015,
\]

so

\[
M_{\mathrm{reg}}=0.005501327886323246>0.
\]

The regular geometry passes the baseline separation test.

### 6.2 Independent holdout

\[
R_{\mathrm{hold}}=0.07669015854685712,
\]

\[
E_{\mathrm{sym,hold}}=0.1491999657742081,
\]

so

\[
M_{\mathrm{hold}}=-0.07250980732735098<0.
\]

The holdout fails the baseline separation test even though its differential q-response is clearly detected numerically.

---

## 7. Protocol stress test

Under the raw protocol, the minimum geometry margin is

\[
-0.06446994819945216.
\]

Under the near-identity affine calibration box, the worst case occurs at

\[
(a_1,a_2)=(0.9,0.9)
\]

on the holdout geometry. There,

\[
R=0.06902114269217141,
\]

\[
E_{\mathrm{sym}}=0.19777222958851792,
\]

and

\[
M_{\mathrm{global}}
=-0.12875108699634652<0.
\]

All declared protocol-geometry cases have response contrast above the numerical allowance, but not all have positive separation margin.

---

## 8. Certified decision

The CERT-01 status is

`Q_RESPONSE_DETECTED_BUT_SYMBOL_SEPARATION_NOT_CERTIFIED`.

The precise conclusion is:

> The declared coherent-state observable package exhibits a stable nonzero differential q-response at fixed external geometry, but the response is not uniformly separated from finite-spin symbol mismatch on the independent holdout under the declared calibration family.

Therefore:

`P1_CONFIRMATORY_AND_PREREGISTERED_PILOT_BLOCKED_SYMBOL_ERROR_REDUCTION_REQUIRED`.

Exploratory P1 diagnostics remain allowed only when explicitly labeled exploratory and excluded from confirmatory claims.

---

## 9. Claim firewall

CERT-01 does not establish:

- absence of q-response;
- impossibility of observable separation under every protocol;
- failure of the operator-level P3 result;
- invalidity of coherent intertwiners;
- a no-go theorem for larger spins;
- a physical interpretation of q;
- permission for confirmatory P1 analysis.

The negative margin identifies the current bottleneck: finite-spin semantic accuracy on independent geometry.

---

## 10. Required remediation

Proceed to

`P3-B-M5 / Spin-Scaling and Holdout Symbol-Error Reduction`.

M5 must:

1. repeat the bridge at larger external spins while preserving normalized geometry;
2. test whether holdout symbol mismatch decreases relative to differential response;
3. include at least one nonuniform-spin carrier for an unequal-area scalene tetrahedron;
4. enlarge the normal-Gram observable package beyond two coordinates;
5. separate coherent-state preparation error from operator functional-calculus error;
6. rerun CERT with the same frozen decision rule before any P1 pilot is authorized.
