# RC02 pilot execution report

**Contract:** `BC-IDPR-P3-P1-RC02`  
**Stage:** `pilot`  
**Status:** `PILOT_COMPLETED_PASS / CALIBRATION_DESIGN_ALLOWED / CALIBRATION_EXECUTION_SEALED`  
**Date:** 2026-07-17

## Scope

The executable evaluated exactly the four carried-forward pilot families:

- `(1,2,3,4)`;
- `(1,3,3,3)`;
- `(1,3,4,6)`;
- `(2,2,3,5)`.

These contain 64 ordered carriers. No calibration or confirmatory family was evaluated. The frozen RC02 predictor/control pairing was not changed and no final mode was selected.

## Pipeline checks

- predictor-geometry tests: `3 passed`;
- pilot grid: 1101 points on `[0.60,1.15]`;
- maximum paired predictor/control overlap: `0.9909657558650774`;
- minimum projector-difference norm: `0.1341151397223887`;
- calibration results present: `false`;
- confirmatory results present: `false`;
- selected mode: `null`.

## Numerical quality control

- maximum transpose-orthogonality residual: `2.7832392358026496e-15`;
- maximum column-norm deviation: `1.9984014443252818e-15`;
- maximum anchor evaluator disagreement: `4.440892098500626e-16`;
- anchor speed sign failures: `0`;
- primary residual degeneracies: `0`;
- signed-speed residual degeneracies: `0`;
- hard failures: `0`.

## Descriptive pilot diagnostics

The pilot is non-inferential. Per-mode diagnostics were retained for code validation only and are not used to rank or select a final mode.

Primary complex-observable median family advantages ranged from

```text
-0.05002181422201787 to 0.07584627527883348
```

Signed-speed replication median family advantages ranged from

```text
-0.08430450441128065 to 0.10210516287055891
```

These ranges show that the redesigned geometry is numerically active on the pilot set. They do not establish phase locking, choose a mode, or authorize confirmatory inference.

## Gate decision

```text
RC02_PILOT: COMPLETED_PASS
RC02_FINAL_MODE_SELECTION: FORBIDDEN_AND_NOT_PERFORMED
RC02_CALIBRATION_DESIGN: ALLOWED
RC02_CALIBRATION_EXECUTION: SEALED
RC02_CONFIRMATORY: SEALED_AND_UNTOUCHED
NEXT_REQUIRED_ARTIFACT: RC02_CALIBRATION_PREREGISTRATION_AND_UNSEAL_CERTIFICATE
```

No statement from the Gemini advisory report is used as evidence.
