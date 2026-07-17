# BC-IDPR P3→P1 Research Contract 02

**Title:** Identifiable q-Curvature Predictors for Phase-Resolved Residual Modulation  
**Status:** `CONFIRMATORY_PREREGISTERED / MODE_5_FROZEN / UNSEAL_CERTIFICATE_ISSUED / RESULTS_NOT_COMPUTED`  
**Date:** 2026-07-17

RC02 replaces the unreachable predictor/control geometry of RC01 without using calibration or confirmatory carrier responses.

## Current state

```text
RC02_PREDICTOR_GEOMETRY: CERTIFIED
RC02_PILOT: COMPLETED_PASS
RC02_CALIBRATION: COMPLETE_ON_12_FAMILIES
RC02_SELECTED_MODE: 5
RC02_SELECTED_MODE_STATUS: FROZEN
RC02_CONFIRMATORY_PREREGISTRATION: FROZEN
RC02_CONFIRMATORY_UNSEAL_CERTIFICATE: ISSUED
RC02_CONFIRMATORY_RESULTS: NOT_COMPUTED
```

The final test layer contains exactly eight previously sealed families and 106 ordered carriers. Only mode `5` and its matched control `9.5` are admissible. Pilot and calibration observations are excluded from final-test statistics.

The primary rule is fixed before computation: at least seven positive families, median family advantage at least `0.02`, exact one-sided sign-test p-value at most `0.03515625`, and phase concentration rules `R1 >= 0.60` for outcome A or `R1 < 0.60` with `R2 >= 0.75` for outcome B. Any hard failure has precedence and yields outcome D.

No partial reading, early stopping, family exclusion, mode change, threshold change or selective rerun is permitted. The signed-speed observable is replication-only and cannot alter the primary A/B/C/D result.

Calibration results: `bc_idpr/p3_to_p1/rc02/calibration/results/`.  
Confirmatory package: `bc_idpr/p3_to_p1/rc02/confirmatory/`.

No statement from the Gemini advisory report is used as evidence.
