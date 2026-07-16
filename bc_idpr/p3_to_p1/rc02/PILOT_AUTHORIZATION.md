# RC02 Pilot Authorization

**Status:** `AUTHORIZED_WITH_SEALED_DOWNSTREAM_STAGES`

## Permitted

- evaluate only the four carried-forward pilot families;
- implement q-curvature predictors and the frozen control pairing;
- test numerical finiteness, normalization and contamination guards;
- report all pilot family energies and phase coefficients;
- diagnose residual degeneracy and effect scale;
- stop if any geometry or hash certificate drifts.

## Forbidden

- access any calibration or confirmatory family response;
- change the phase grid, cubic baseline, predictor formula, control pool or pairing;
- lower or reinterpret the `0.02` threshold;
- select the final mode from pilot results;
- make confirmatory or physical claims.

## Exit states

- `PILOT_PASS_CALIBRATION_DESIGN_ALLOWED`;
- `PILOT_NUMERICAL_FAILURE`;
- `PILOT_EFFECT_SCALE_WARNING`;
- `PILOT_PROTOCOL_CONTAMINATION`.

Calibration remains unauthorized until a pilot certificate is committed.

No statement from the Gemini advisory report is used as evidence.