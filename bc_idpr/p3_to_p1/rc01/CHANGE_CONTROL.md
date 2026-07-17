# RC01 Change-Control Protocol

**Contract:** `BC-IDPR-P3-P1-RC01`  
**Status:** `ACTIVE_FROM_PREREGISTRATION_COMMIT`  

## 1. Before pilot execution

Typographical corrections that do not alter semantics may be committed as patch versions. Any change to a grid, observable, predictor, split, threshold, endpoint or outcome rule requires preregistration version `v0.2.0` or higher.

## 2. During pilot

Only the four pilot families may be evaluated. Permitted changes are limited to parser and serialization fixes, deterministic ordering fixes, matrix-orientation implementation fixes needed to realize the already frozen formula, precision increases, error-message and failure-report improvements, and performance improvements that preserve canonical output.

The following are forbidden without invalidating RC01:

- inspecting calibration or confirmatory outcomes;
- adding frequencies;
- changing the cubic residual baseline;
- tuning thresholds from pilot effect sizes;
- replacing the primary observable;
- moving families between stages.

Pilot closure requires `PILOT_FREEZE_CERTIFICATE.json` with code hashes, dependency versions and a statement that no calibration or confirmatory family was evaluated.

## 3. Calibration

Calibration begins only after pilot closure. The twelve calibration families may be used solely to execute the frozen mode-selection rule and diagnostics declared in the contract.

Calibration closure requires `CALIBRATION_FREEZE_CERTIFICATE.json` containing selected `n_star`, all nine calibration median energy advantages, tie-resolution record, code and data hashes, environment versions, and a statement that confirmatory outcomes were not computed.

The certificate must be committed before confirmatory unsealing.

## 4. Confirmatory run

The confirmatory run is one-shot. A rerun is permitted only for byte-identical reproducibility confirmation, a documented hardware or dependency failure before complete output existed, or a demonstrated implementation defect that invalidates the whole run.

A defect discovered after outcome inspection invalidates RC01. The corrected analysis must receive a new contract identifier and disclose the invalidated run.

## 5. Contamination rule

Any computation of a primary confirmatory statistic before the calibration freeze commit triggers `CONFIRMATORY_CONTAMINATION` and outcome `D_INCONCLUSIVE` for RC01.

No statement from the Gemini advisory report is used as evidence.
