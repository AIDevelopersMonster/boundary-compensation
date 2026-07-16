# Audit — BC-IDPR-CERT-03 Nonuniform Affine-Quotient Separation

**Review status:** complete  
**Date:** 2026-07-16  
**Verdict:** restricted positive certificate.

## 1. Scope reviewed

The audit checks whether the M5 nonuniform-spin lower-symbol response can be converted into a calibration-robust differential coordinate without importing the positive conclusion from CERT-02 by analogy.

The tested nuisance group is the constant positive affine action

\[
y(\theta)\mapsto a y(\theta)+b,\qquad a>0.
\]

The endpoint-normalized coordinate

\[
u(\theta)=\frac{y(\theta)-y(\theta_{\rm lo})}{y(\theta_{\rm hi})-y(\theta_{\rm lo})}
\]

is exactly invariant under this action in exact arithmetic.

## 2. Preregistration integrity

The decision protocol was committed before the numerical evaluation at

`be415393641808a84759de04293ee5ae9e1a9e87`.

It froze:

- the M5 carrier and unequal-area geometry;
- interval `[pi/15, pi/10]`;
- 129-point grid;
- anchor `pi/12`;
- affine nuisance group;
- decision thresholds;
- finite-difference steps;
- one-evaluation stopping rule.

No post-result model or threshold modification was used.

## 3. Numerical findings

The G12 channel acts as the declared negative control. Its maximum numerical derivative is

`3.552713678800501e-15`,

below the preregistered `1e-12` threshold.

The varying G23 channel has endpoint span

`0.008715842540636967`,

comfortably above the minimum denominator threshold `1e-4`.

Three frozen positive affine transformations produced maximum quotient discrepancy

`1.0974554598419672e-13`,

below the required `1e-12`.

The derivative audit over the full grid gives:

- minimum reference derivative: `0.016523871375351273`;
- maximum finite-difference step radius: `1.583662367909966e-07`;
- uncertainty-adjusted monotonicity margin: `0.01652385241081851 > 0`.

For adjacent quotient values:

- minimum separation: `0.0015734158353453054`;
- propagated uncertainty bound: `3.0328813549488765e-08`;
- net minimum margin: `0.0015733855065317558 > 0`.

## 4. Interpretation

The certificate establishes distinguishability and ordering of the declared q-deformation parameter modulo constant positive affine calibration. It is stronger than additive-offset cancellation because both offset and positive scale are removed.

It is not an absolute-symbol certificate. Endpoint normalization uses the observed endpoint span and therefore cannot validate agreement with an external classical target.

The restriction `a>0` is essential: a negative scale reverses ordering. Nonlinear or theta-dependent calibrations are outside the quotient and remain open.

## 5. Relation to earlier results

CERT-01 remains negative for absolute observable separation.

CERT-02 remains positive for additive-offset differential separation on the equal-spin carrier.

P1-PILOT-01 remains negative for phase-specific model advantage on that equal-spin dataset.

CERT-03 does not overwrite any of those results. It opens a new, independent P1 preregistration on the nonuniform M5 carrier.

## 6. Claim firewall

Allowed:

`AFFINE_CALIBRATION_INVARIANT_ORDERING_AND_GRID_SEPARATION_ON_DECLARED_NONUNIFORM_CARRIER`.

Forbidden:

- absolute semiclassical accuracy;
- universal carrier-independent response;
- invariance under nonlinear or theta-dependent calibration;
- confirmatory phase law;
- physical interpretation of q.

No statement from the Gemini advisory report is used as evidence.

## 7. Verdict

Assign

`NONUNIFORM_AFFINE_QUOTIENT_SEPARATION_CERTIFIED`.

Open only the gate

`nonuniform_affine_quotient_differential_pilot = OPEN`.

Keep

`confirmatory_phase_law = BLOCKED`

until a new predictor family, null model, blocked validation protocol and stopping rule are committed before inspecting the dense-grid pilot result.
