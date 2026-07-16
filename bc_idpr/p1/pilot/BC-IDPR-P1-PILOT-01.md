# BC-IDPR-P1-PILOT-01 — Preregistered Signed Differential Residual Pilot

**Status:** `PREREGISTERED_PHASE_MODEL_CRITERIA_NOT_MET`  
**Date:** 2026-07-16  
**Preregistration commit:** `3991d90fae3872384438749441b90e4495188c85`

## 1. Purpose

Test whether the frozen four-channel differential observable from CERT-02 is more specifically described by the preregistered odd-frequency phase basis than by a generic smooth cubic null model.

## 2. Frozen observable

The active complex signed residual is

\[
Z(\theta)=Q^{\rm reg}_{23}(\theta)+iQ^{\rm hold}_{23}(\theta),
\qquad
Q(\theta)=S(\theta)-S(\pi/8).
\]

The two `G12` channels are negative controls.

## 3. Frozen models

The phase model uses

\[
e^{ik\theta}-e^{ik\theta_0},\qquad k\in\{1,3,5\}.
\]

The smooth null uses

\[
x,\ x^2,\ x^3,\qquad x=\theta-\theta_0.
\]

Both are fitted without intercept by complex least squares and assessed by eight-fold contiguous blocked cross-validation.

## 4. Preregistered criteria

Success required all of:

1. negative-control maximum at most `1e-12`;
2. maximum signed excursion at least `0.001`;
3. phase normalized CV RMSE at most `0.05`;
4. phase advantage over the cubic null at least `0.10`;
5. phase coefficient instability at most `0.25`.

No criterion was changed after evaluation.

## 5. Result

The controls and signal-size criteria passed. The phase model also had a low normalized CV error, but the cubic null performed slightly better. The preregistered phase-specific advantage criterion therefore failed.

## 6. Claim status

The result supports smooth nonzero differential response, but not a phase-specific residual law. P1 confirmatory status and all physical interpretations remain blocked.
