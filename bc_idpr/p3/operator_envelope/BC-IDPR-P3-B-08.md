# BC-IDPR-P3-B-M8 — Representation-Family Blocked Validation

**Status:** `REPRESENTATION_FAMILY_BLOCKED_GENERALIZATION_NOT_CERTIFIED`  
**Date:** 2026-07-16  
**Type:** validation-hardening module

## 1. Motivation

M7 used leave-one-carrier-out validation on 75 ordered carriers. Many carriers are permutations of the same unordered external-spin multiset. Thus the training set can contain close representation relatives of the held-out ordered carrier.

M8 strengthens independence by holding out an entire representation family at once.

## 2. Family definition

For an ordered doubled-spin quadruple

\[
J=(2j_1,2j_2,2j_3,2j_4),
\]

define its family key as the sorted quadruple

\[
\kappa(J)=\operatorname{sort}(J).
\]

The 75 ordered carriers collapse to 9 external-spin families. Each fold removes every ordered carrier sharing one key. The held-out family is excluded from standardization and coefficient estimation.

The descriptors and ridge parameter remain exactly those of corrected M7:

- baseline dimension 10;
- matrix-augmented dimension 14;
- \(\alpha=1\);
- no derivatives in predictors.

## 3. Results

Ordinary leave-one-carrier-out matrix NRMSE was

\[
(0.304711,\;0.406176,\;0.466017).
\]

Leave-one-representation-family-out matrix NRMSE is

\[
(0.385927,\;0.566899,\;0.673174).
\]

The corresponding family-blocked baseline errors are

\[
(0.565027,\;0.575465,\;0.677420).
\]

Matrix augmentation still helps the first target substantially, but its relative improvements over the baseline are approximately

\[
(31.70\%,\;1.49\%,\;0.63\%).
\]

Thus it does not provide uniform family-level improvement and fails the frozen maximum-NRMSE threshold \(0.35\) on all three targets.

## 4. Interpretation

The M7 descriptor contains real predictive information, but ordinary carrier-level LOOCV was not a sufficient independence test for unseen external-spin families. The higher-jet targets remain strongly family dependent.

This does not invalidate the M7 exploratory signal. It narrows it:

> anchor matrix data helps interpolate among ordered carriers inside a small representation box, but does not yet support uniform transfer to a completely held-out external-spin multiset.

## 5. Gates

- representation-family decomposition: `CLOSED`;
- ordinary LOOCV as unseen-family evidence: `INSUFFICIENT`;
- family-blocked matrix prediction: `NOT_CERTIFIED`;
- carrier-neutral exact law: `BLOCKED`;
- new cross-carrier pilot: `BLOCKED_PENDING_INDEPENDENT_FAMILY_ATLAS_OR_EQUIVARIANT_MAP`.

## 6. Claim firewall

Forbidden claims include universal non-transfer, physical q-dynamics, failure outside the declared label box, and post-hoc feature expansion on these same nine families as confirmatory evidence.

No statement from the Gemini advisory report is used as evidence.
