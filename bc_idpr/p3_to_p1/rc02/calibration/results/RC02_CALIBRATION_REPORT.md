# RC02 Calibration Report

**Contract:** `BC-IDPR-P3-P1-RC02`  
**Status:** `CALIBRATION_COMPLETE_MODE_FROZEN / CONFIRMATORY_STILL_SEALED`  
**Date:** 2026-07-17

## Execution scope

- evaluated calibration families: `12`;
- evaluated ordered carriers: `113`;
- evaluated integer modes: `2,...,10`;
- pilot families evaluated: `0`;
- confirmatory families evaluated: `0`;
- pilot data used for selection: `false`;
- replication data used for selection: `false`.

## Frozen primary scores

| mode | primary calibration score | replication score |
|---:|---:|---:|
| 2 | -0.0092637971682950904 | -0.018542007457330784 |
| 3 | 0.036984629831185722 | 0.01928521623278423 |
| 4 | 0.0090498366890381654 | -0.0011865831089133971 |
| 5 | 0.1511086183308894 | 0.12873749220570929 |
| 6 | 0.012896984462036715 | 0.02113486196047068 |
| 7 | -0.00066015479318545789 | 0.0082739594134948746 |
| 8 | -0.014635106078941584 | 0.00063140247953571982 |
| 9 | -0.08027037017259267 | -0.063651921411068513 |
| 10 | -0.32005332674675924 | -0.29274717001212924 |

The deterministic primary rule selects

\[
n_*=5.
\]

The primary score gap to the runner-up is `0.11412398849970368`. No tie rule was needed.

## Descriptive consistency only

At the selected mode, `11/12` primary family advantages and `11/12` replication family advantages are positive. The replication channel also has its largest median score at mode `5`.

These are calibration diagnostics, not confirmatory evidence. They cannot be used to alter the frozen threshold, family split, predictor/control pairing or outcome logic.

## Numerical gate

- maximum transpose-orthogonality residual: `2.4515184678427659e-15`;
- maximum column-norm deviation: `9.9920072216264089e-16`;
- maximum anchor evaluator disagreement: `2.7240086067659812e-15`;
- anchor-speed sign failures: `0`;
- residual degeneracies: `0`;
- nonfinite values: `0`;
- hard failures: `0`.

## Gate decision

```text
RC02_CALIBRATION: COMPLETE
RC02_SELECTED_MODE: 5
RC02_MODE_STATUS: FROZEN
RC02_CONFIRMATORY: SEALED_AND_UNTOUCHED
NEXT_REQUIRED_ARTIFACT: RC02_CONFIRMATORY_PREREGISTRATION_AND_UNSEAL_CERTIFICATE
```

No statement from the Gemini advisory report is used as evidence.
