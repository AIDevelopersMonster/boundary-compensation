# BC-IDPR-P1-PILOT-01 — Research Audit

**Status:** internal mathematical and computational review, v0.1.0  
**Date:** 2026-07-16  
**Verdict:** preregistered phase-specific criterion not met.

## 1. Provenance discipline

The preregistration was committed before the 257-point evaluation. The model bases, folds, thresholds, channels and stopping rule were not changed after the result was observed.

## 2. Numerical findings

The negative-control maximum is exactly zero at displayed precision. The maximum signed excursion is

\[
0.05169452570488938.
\]

The odd-frequency phase model has normalized blocked-CV RMSE

\[
0.015038365888071567,
\]

with coefficient instability

\[
0.1820407828956029.
\]

The generic cubic smooth null has lower normalized blocked-CV RMSE

\[
0.01389762354938252.
\]

Thus the preregistered relative phase advantage is

\[
-0.08208182748911279,
\]

where success required at least `0.10`.

## 3. Interpretation

The phase basis fits well in an absolute approximation sense, but this is insufficient. On a short regular interval, a smooth cubic model captures the same response at least as well under the frozen validation protocol. Therefore the pilot does not identify a phase-specific law.

## 4. Verdict

Assign

`PREREGISTERED_PHASE_MODEL_CRITERIA_NOT_MET`.

This does not reverse CERT-02. Differential parameter separation remains certified. What fails is the stronger model-selection claim that the response has demonstrated the preregistered odd-frequency phase structure.

## 5. Claim firewall

Do not infer:

- absence of q-dependent response;
- falsity of the q-Racah operator construction;
- a continuum no-phase theorem;
- physical dynamics of q;
- permission to replace the null model after observing the result.

No statement from the Gemini advisory report is used as evidence.

## 6. Next step

Do not rerun P1 with altered predictors on the same data. Return to construction: proceed to `P3-B-M5`, a nonuniform-spin carrier with a genuine unequal-area scalene holdout and a richer independently defined observable package. A later P1 pilot must use newly generated data and a new preregistration.
