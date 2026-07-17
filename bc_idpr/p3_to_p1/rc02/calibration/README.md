# RC02 Calibration Preregistration and Unseal Package

**Status:** `CALIBRATION_EXECUTION_AUTHORIZED / CONFIRMATORY_SEALED`  
**Contract:** `BC-IDPR-P3-P1-RC02`  
**Date:** 2026-07-17

This package records the prospective calibration rule before any of the 12 calibration families are evaluated.

## Authorized

- exactly 12 calibration families;
- exactly 113 ordered carriers;
- all nine frozen q-curvature modes and paired controls;
- one deterministic primary-observable mode selection after the complete table exists.

## Still forbidden

- using pilot results in mode selection;
- changing the frozen pairing;
- selecting a mode from a partial calibration run;
- reading any of the eight confirmatory families;
- making a confirmatory or physical claim.

## Files

- `CALIBRATION_PREREGISTRATION_v0.1.0.json` — machine-readable prospective record;
- `CALIBRATION_PROTOCOL.md` — human-readable computation and selection rule;
- `CALIBRATION_RESULT_SCHEMA.json` — required post-run result shape;
- `CALIBRATION_CHANGE_CONTROL.md` — frozen-change and contamination rules;
- `validate_calibration_preregistration.py` —