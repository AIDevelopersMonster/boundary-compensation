# BC-IDPR-P3-B-M7 — Matrix-Valued Carrier Descriptor and Recoupling Jet Atlas

**Status:** `REPRESENTATION_DESCRIPTOR_LOOCV_NOT_CERTIFIED`  
**Date:** 2026-07-16  
**Type:** construction module with exploratory leave-one-carrier-out validation

## 1. Objective

M6 proved the exact two-channel factorization

\[
\|\partial_\theta(FDF^T)\|_{HS}=\sqrt{2}\,|d_2-d_1|\,|\omega(\theta)|.
\]

M7 asks whether representation data available at the anchor predict the local recoupling jet

\[
\bigl(\omega,\omega',\omega''\bigr)_{\theta_0}
\]

across an expanded carrier atlas.

## 2. Anti-leakage rule

The predictive descriptor contains normalized external and channel Casimirs and the four entries of \(F(\theta_0)\). Derivatives of \(F\) are excluded from predictors and are used only to construct targets.

The transformed targets are

\[
\log|\omega|,\qquad \omega'/\omega,\qquad \omega''/\omega.
\]

## 3. Atlas and validation

The deterministic wall-safe atlas contains 75 ordered two-channel carriers with doubled spins in \(\{1,2,3,4\}\). Validation is leave-one-carrier-out ridge regression with frozen regularization \(\alpha=1\).

The baseline descriptor has dimension 11. The matrix-augmented descriptor has dimension 15.

## 4. Results

Baseline LOOCV NRMSE:

\[
(0.509846,\;0.491628,\;0.569295).
\]

Matrix-augmented LOOCV NRMSE:

\[
(0.304711,\;0.406176,\;0.466017).
\]

The matrix descriptor improves all three targets, but none reaches the certification threshold \(0.25\). Therefore the representation map is informative but not predictive enough to certify carrier-neutral jet transfer.

Numerical stability under halving the finite-difference scale has maximum relative jet change \(1.08\times10^{-5}\).

## 5. Decision

- expanded two-channel atlas: `CLOSED`;
- matrix descriptor relevance: `SUPPORTED_EXPLORATORILY`;
- anchor angular-speed prediction: `NOT_CERTIFIED`;
- higher-jet prediction: `NOT_CERTIFIED`;
- new cross-carrier pilot: `BLOCKED`.

## 6. Claim firewall

Allowed claim:

> Adding \(F(\theta_0)\) to normalized representation invariants improves leave-one-carrier-out prediction of all three transformed jet targets on the declared atlas, but the remaining errors exceed the frozen certification threshold.

Forbidden claims include a universal representation law, certified prediction of \(\omega\), transfer beyond the declared atlas, physical \(q\)-dynamics, and post-hoc descriptor enlargement.

No statement from the Gemini advisory report is used as evidence.
