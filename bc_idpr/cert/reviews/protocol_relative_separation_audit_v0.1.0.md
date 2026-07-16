# BC-IDPR-CERT-01 — Protocol-Relative Observable Separation Audit

**Status:** internal mathematical and computational review, v0.1.0  
**Date:** 2026-07-16  
**Verdict:** `SEPARATION_NOT_CERTIFIED`; P1 remains blocked.

## 1. Question

The upstream P3-B chain establishes a nonzero intrinsic operator tangent, exact external-geometry fixation and a coherent lower-symbol protocol. CERT-01 asks a stricter question: does the induced observable displacement exceed the declared model and protocol uncertainty budget?

The decision statistic on the preregistered 33-point interval grid is

\[
M_{\rm net}(\theta)=R_q(\theta)-E_{\rm hold}(\theta)-E_{\rm protocol}(\theta).
\]

A positive certificate requires `max M_net > 0`.

## 2. Calibration stress test

Four frozen additive calibrations were declared before evaluating the decision:

1. regular-anchor calibration;
2. zero offset;
3. midpoint of regular and holdout anchor offsets;
4. holdout-anchor calibration.

These alternatives preserve the q-dependent operator family and coherent states. They test how much the lower-symbol conclusion depends on the arbitrary additive calibration convention already identified in M4.

## 3. Findings

For the anisotropic equifacial holdout,

\[
\max R_q=0.04984235930414149.
\]

The minimum holdout symbol mismatch over the grid is

\[
\min E_{\rm hold}=0.07819043294294023,
\]

and the maximum calibration-family radius is

\[
\max E_{\rm protocol}=0.10211910127354819.
\]

The best net margin is therefore

\[
\max M_{\rm net}=-0.15346173497377\ldots<0.
\]

The negative margin is not caused by wall proximity: the compact interval retains wall distance at least `pi/20`. External geometry leakage is exactly zero by M3. Numerical differentiation is not used in the decision statistic.

## 4. Interpretation

The result does not refute the independent-q operator direction. It separates three statements that must not be conflated:

- operator deformation exists;
- a declared lower symbol responds;
- observable separation exceeds the complete error budget.

The first two are supported. The third is not.

The positive nuisance-quotient margin from M2/M3 cannot rescue CERT-01 because it lives in operator Hilbert--Schmidt or dual operator-norm units. No certified Lipschitz lower bridge from those operator distances to the chosen two-coordinate lower symbol has yet been constructed.

## 5. Verdict

Assign

`SEPARATION_NOT_CERTIFIED`.

Consequences:

- P3-B remains a successful independent-deformation construction;
- M4 remains a valid protocol-relative semantic bridge;
- the present observable package is not sufficiently discriminating;
- confirmatory P1 analysis is not authorized.

This is a legitimate negative certificate rather than a failed computation.

## 6. Claim firewall

Do not infer:

- absence of all q-observable effects;
- failure of the q-Racah envelope;
- uniqueness of the chosen uncertainty budget;
- continuum non-separation beyond the declared grid;
- physical dynamics of q;
- a phase-residual law.

No statement from the Gemini advisory report is used as evidence.

## 7. Required next step

Proceed to `BC-IDPR-CERT-02 / Observable Package Enrichment and Calibration-Robust Separation`.

It must enlarge the observable package beyond two Gram coordinates, construct a calibration quotient or calibration-invariant statistic, and seek a certified lower bridge from operator quotient distance to observable distance. A nonuniform-spin carrier is preferred because it permits a genuine unequal-area scalene holdout. P1 stays blocked until a positive net margin is obtained under preregistered rules.
