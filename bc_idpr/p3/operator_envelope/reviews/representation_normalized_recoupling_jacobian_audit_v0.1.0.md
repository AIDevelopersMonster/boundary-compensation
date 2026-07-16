# BC-IDPR-P3-B-M6 — Research Audit v0.1.0

**Date:** 2026-07-16  
**Verdict:** construction-level positive factorization certificate with a negative normalization result.

## 1. Scope reviewed

The module was reviewed for:

1. validity of the five declared two-channel carriers;
2. orthogonality of every q-Racah recoupling matrix on the frozen interval;
3. skewness of `K(theta)=F'(theta)F(theta)^T`;
4. the operator identity
   `||d_theta(F D F^T)||_HS = sqrt(2)|d2-d1||omega|`;
5. whether two elementary Casimir-gap normalizations collapse anchor speeds;
6. whether anchor normalization collapses the full speed curves.

## 2. Positive result

All five carriers retain exactly two channels in both pairings. The maximum orthogonality residual is below `3.17e-16`. The largest skew-generator residual is below `2.24e-10` and the largest relative residual in the operator factorization is below `1.88e-10`.

The representation-Jacobian factorization is therefore numerically certified at a margin far inside the declared `2e-7` tolerance. This is the strongest reusable output of M6.

## 3. Negative normalization result

Raw anchor angular speed varies substantially across the atlas, with coefficient of variation `0.5485453421`.

Dividing by `sqrt(Delta C_E Delta C_F)` reduces the CV only to `0.3612386192`. Dividing by `Delta C_E Delta C_F` reduces it to `0.1147239322`, still above the frozen collapse threshold `0.10`.

The latter near miss must not be rounded into a positive result. No alternative exponent or fitted scalar normalization was searched after seeing the result.

## 4. Shape result

The normalized curves

`rho_C(theta)=|omega_C(theta)|/|omega_C(theta0)|`

also fail to collapse. Their maximum pairwise absolute difference is `0.3348046725`, above the threshold `0.10`. Carrier dependence therefore includes shape, not merely an anchor amplitude.

## 5. Interpretation

M6 explains part of the failure of P1-PILOT-03R. Observable derivatives inherit an exact channel-gap factor, but the remaining recoupling speed `omega_C(theta)` is itself representation dependent. A single transferred coefficient vector cannot be expected to become carrier neutral merely by dividing by one elementary Casimir scale.

This does not prove that no representation-aware normalization exists. It only rejects the two declared scalar candidates and anchor-only shape normalization on the five-carrier atlas.

## 6. Claim firewall

Supported:

- two-channel skew-generator reduction;
- exact operator-response factorization through the channel gap and angular speed;
- insufficiency of the two frozen scalar normalizations;
- insufficiency of anchor-only curve normalization.

Not supported:

- universal recoupling-speed law;
- impossibility of richer matrix-valued normalization;
- universal q-number transfer;
- physical interpretation of q;
- semiclassical or continuum conclusions.

## 7. Gate decision

Assign:

`RECOUPLING_JACOBIAN_FACTORIZATION_CERTIFIED_SCALAR_NORMALIZATION_INSUFFICIENT`.

Keep the next cross-carrier pilot blocked. The next construction should use a richer carrier descriptor containing at least `F(theta0)`, `F'(theta0)`, both channel Casimir gaps, and external-spin invariants, with any reduction rule frozen before transfer evaluation.

No statement from the Gemini advisory report is used as evidence.
