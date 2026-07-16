# RC01 pilot execution report

**Pipeline:** `BC-IDPR-P3-P1-RC01-PILOT-PIPELINE`  
**Version:** `v0.1.0`  
**Date:** 2026-07-17  
**Status:** `PILOT_COMPLETED / PROTOCOL_REVISION_REQUIRED / CALIBRATION_BLOCKED`

## 1. Execution scope

Only the four preregistered pilot families were evaluated:

- `(1,2,3,4)`;
- `(1,3,3,3)`;
- `(1,3,4,6)`;
- `(2,2,3,5)`.

They contain 64 ordered carriers. No calibration or confirmatory carrier was passed to the evaluator.

```text
calibration_families_evaluated=0
confirmatory_families_evaluated=0
calibration_results_present=false
confirmatory_results_present=false
selected_mode=null
outcome=null
```

## 2. Software and numerical checks

- phase grid: 1101 points on `[0.60,1.15]`;
- certified-local grid: 401 points on `[0.99,1.01]`;
- pilot carriers: 64;
- pilot families: 4;
- unit tests: `6 passed`;
- wall time: approximately 25 seconds;
- maximum dense-grid orthogonality residual: `2.0790184679485825e-15`;
- maximum column-norm deviation: `8.881784197001252e-16`;
- maximum disagreement between the vectorized evaluator and the published coefficient evaluator at the anchor: `1.2021721300496787e-15`;
- anchor-speed sign failures: 0;
- degenerate primary residuals: 0;
- degenerate signed-speed residuals: 0;
- nonfinite certified-local values: 0;
- integrity hard failures: 0.

The implementation and contamination guard passed.

## 3. Non-inferential pilot diagnostics

All registered modes were computed for software validation only. No frequency was selected, ranked for future use or frozen as `n_star`.

The observed pilot advantages were small and cannot be interpreted inferentially. More importantly, a response-independent audit of the frozen predictor dictionary proved that the preregistered threshold `0.02` is unreachable: the exact maximum permitted by the paired projector geometry is at most `0.003670726619615724`.

The full proof is recorded in `PREDICTOR_IDENTIFIABILITY_AUDIT.md`.

## 4. Pilot decision

The pilot succeeded as software, but RC01 failed as an identifiable confirmatory design.

```text
PILOT_PIPELINE_VALIDATED=true
PREDICTOR_COMPARISON_IDENTIFIABLE=false
FROZEN_CONFIRMATORY_THRESHOLD_REACHABLE=false
CALIBRATION_AUTHORIZED=false
CONFIRMATORY_REMAINS_SEALED=true
```

No RC01 outcome A--D is assigned because the confirmatory stage was not opened.

## 5. Required next step

A new preregistration identifier is required before further scientific execution. The next contract must redesign the null/control comparison and include a response-independent reachability audit before any carrier observable is evaluated.

No statement from the Gemini advisory report is used as evidence.