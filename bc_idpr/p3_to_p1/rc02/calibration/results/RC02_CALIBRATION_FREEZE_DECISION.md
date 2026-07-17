# RC02 Calibration Freeze Decision

**Status:** `MODE_5_FROZEN / CONFIRMATORY_EXECUTION_NOT_AUTHORIZED`  
**Date:** 2026-07-17

The complete preregistered calibration table contains all 12 families, all 113 ordered carriers and all 9 integer modes. The frozen primary selection rule returns

\[
n_*=5.
\]

The result is now immutable inside RC02. Mode 5 may not be replaced because of pilot values, replication values, later preferences or partial confirmatory inspection.

## State transition

```text
CALIBRATION_PREREGISTRATION: SATISFIED
CALIBRATION_EXECUTION: COMPLETE
SELECTED_MODE: 5
SELECTED_MODE_MUTABILITY: FROZEN
CONFIRMATORY_RESULTS_PRESENT: false
CONFIRMATORY_EXECUTION_AUTHORIZED: false
```

A separate confirmatory preregistration and unseal certificate is required before any of the eight confirmatory families may be evaluated.

No statement from the Gemini advisory report is used as evidence.
