# RC02 Calibration Preregistration

**Artifact:** `BC-IDPR-P3-P1-RC02-CALIBRATION-PREREGISTRATION`  
**Version:** `v0.1.0`  
**Date:** 2026-07-17  
**Status:** `CALIBRATION_PREREGISTERED / EXECUTION_AUTHORIZED / CONFIRMATORY_SEALED`

## 1. Purpose

This document authorizes one calibration execution after the successful RC02 pilot. Calibration has one inferential function: choose a single integer q-curvature mode for later confirmation. It does not test the final confirmatory claim.

## 2. Authorized calibration scope

Exactly these 12 unordered families are unsealed:

| family | ordered carriers |
|---|---:|
| `(1, 1, 1, 1)` | 1 |
| `(1, 1, 2, 2)` | 6 |
| `(1, 1, 3, 3)` | 6 |
| `(1, 1, 5, 5)` | 6 |
| `(1, 1, 6, 6)` | 6 |
| `(1, 2, 4, 5)` | 24 |
| `(1, 3, 4, 4)` | 12 |
| `(1, 3, 6, 6)` | 12 |
| `(1, 4, 4, 5)` | 12 |
| `(1, 5, 6, 6)` | 12 |
| `(2, 2, 2, 4)` | 4 |
| `(2, 3, 3, 6)` | 12 |

Total: **12 families and 113 ordered carriers**.

The four pilot families are excluded from mode selection. The eight confirmatory families remain sealed:

```text
(1, 1, 4, 4)
(1, 2, 2, 3)
(1, 2, 5, 6)
(1, 3, 3, 5)
(1, 3, 5, 5)
(1, 4, 5, 6)
(1, 5, 5, 5)
(2, 2, 4, 6)
```

## 3. Frozen computation

The phase grid, cubic baseline, observables, q-curvature atoms and predictor/control pairing remain conceptually identical to RC02 v0.1.0. No pairing may be changed after viewing calibration values.

For ordered carrier `J` and integer mode `n`, define

\[
\Delta_{J,n}
=|\langle r_J,\psi_n\rangle|^2
-|\langle r_J,\chi_n\rangle|^2.
\]

For family `f`, compute

\[
\Delta_{f,n}=\operatorname{median}_{J\in f}\Delta_{J,n}.
\]

For each mode, the calibration score is

\[
S_n=\operatorname{median}_{f\in\mathcal F_{cal}}\Delta_{f,n}.
\]

The selected mode is

\[
n_*=\arg\max_{n\in\{2,\ldots,10\}} S_n,
\]

with ties within `1e-12` resolved by the smallest integer `n`.

The signed-speed replication table is computed and stored for every mode but cannot alter `n_*`.

## 4. Completion rule

Mode selection is forbidden until all 12 families, all 113 carriers and all 9 modes have completed. All family-by-mode values must be retained. Pilot results cannot be pooled with calibration results.

The confirmatory threshold `0.02` is not a calibration filter. Calibration selects the maximum frozen score even when the score is small or negative; interpretation occurs only in the later confirmatory stage.

## 5. Numerical gate

Calibration is invalid if any of the following occurs:

- transpose-orthogonality residual exceeds `1e-10`;
- column-norm deviation exceeds `1e-10`;
- anchor evaluator disagreement exceeds `1e-12`;
- any sign failure, residual degeneracy or nonfinite value occurs;
- fewer than 12 families or 113 ordered carriers are processed;
- any confirmatory family is accessed.

On failure, `selected_mode` must remain `null`.

## 6. Exit and next gate

A valid completion produces `RC02_CALIBRATION_RESULTS.json` and freezes one `selected_mode`. Confirmatory execution remains forbidden until a separate `RC02_CALIBRATION_FREEZE_CERTIFICATE` is committed and a confirmatory unseal artifact is issued.

No statement from the Gemini advisory report is used as evidence.
