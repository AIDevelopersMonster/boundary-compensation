# BC-IDPR-CERT-02 — Calibration-Quotient Differential Separation Audit

**Status:** internal mathematical and computational review, v0.1.0  
**Date:** 2026-07-16  
**Verdict:** restricted positive certificate.

## 1. Reviewed claim

For the fixed M4 carrier and two fixed coherent preparations, distinct theta values on the preregistered grid are separated by the differential lower-symbol signature after quotienting all constant additive calibration offsets.

This is not an absolute-symbol accuracy claim.

## 2. Why CERT-01 remains valid

CERT-01 compared absolute observable displacement with static holdout mismatch and calibration radius. Its negative verdict is unchanged. CERT-02 asks a different, narrower question. Constant offsets act as a nuisance group and cancel exactly in

`Q(theta)=S(theta)-S(theta0)`.

Thus static bias is not reclassified as small; it is removed only for differential parameter comparison.

## 3. Enriched package

The signature is four-dimensional and contains the two lower-symbol channels for both the regular calibration geometry and the independent anisotropic equifacial holdout. The first channel is a theta-independent negative control. The two second-channel components respond with opposite signs near the anchor.

At theta=pi/8 the derivative is approximately

`(0, -0.1072982943, 0, 0.4463919039)`,

with Euclidean norm `0.4591063666`.

## 4. Separation result

On the 33-point grid:

- minimum adjacent separation: `0.0013122984675`;
- maximum adjacent separation: `0.0044885546569`;
- endpoint separation: `0.0790607007972`.

The derivative was recomputed with four central-difference steps. The resulting step radius is below `6.61e-8`. After propagation over one grid step and addition of a conservative arithmetic allowance, the uncertainty bound is below `3.15e-10`. Hence the minimum uncertainty-adjusted adjacent margin is

`0.0013122981529 > 0`.

## 5. Calibration audit

Two nontrivial synthetic offset vectors were applied to the complete four-channel signature. Differential signatures before and after the offsets agree to machine precision. This verifies the declared quotient action but does not establish invariance under multiplicative, nonlinear or theta-dependent recalibrations.

## 6. Limitation discovered during implementation

The planned nonuniform-spin carrier was not imported into CERT-02. Unequal external spins change the invariant carrier, admissible channels and q-Racah recoupling matrix. That is a new P3 construction, not a harmless certification-layer substitution. The scientifically correct route is a separate `P3-B-M5` module followed by a new holdout certificate.

## 7. Literature boundary

Coherent intertwiners, closure data and q-6j recoupling have established mathematical precedents in the primary literature. Those sources motivate the construction but do not prove the BC quotient, grid margin or pilot gate. No Gemini advisory statement is used as evidence.

## 8. Verdict

Assign

`CALIBRATION_QUOTIENT_DIFFERENTIAL_SEPARATION_CERTIFIED`.

Gate split:

- differential additive-offset-quotient P1 pilot: `OPEN`;
- static absolute-symbol P1 claim: `BLOCKED_BY_CERT_01`;
- unequal-area/nonuniform-spin claim: `OPEN_OBLIGATION`.

## 9. Next step

Proceed to a preregistered `P1-PILOT-01` using only signed differential residuals and the exact four-channel protocol frozen here. In parallel, start `P3-B-M5` for a nonuniform-spin carrier. The pilot must remain exploratory until phase predictors, grid, exclusions and stopping rules are frozen before evaluation.
