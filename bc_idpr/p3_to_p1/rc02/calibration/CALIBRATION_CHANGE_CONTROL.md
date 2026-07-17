# RC02 Calibration Change Control

## Frozen after commit

The calibration family set, 113-carrier census, phase grid, cubic baseline, observables, q-curvature formula, control pairing, family aggregation, primary mode score, tie rule and numerical thresholds are frozen.

## Permitted before execution

Only non-scientific corrections that leave numerical output unchanged: comments, spelling, path fixes and clearer error messages. Every correction requires a new checksum ledger and validator run.

## Requires a new contract version

Any change to a family, predictor, control, pairing, aggregation statistic, tie tolerance, quality threshold, use of pilot data or confirmatory gate requires RC02 v0.2.0 or RC03 before computation.

## Contamination

Reading any confirmatory response before a calibration freeze certificate permanently contaminates the confirmatory stage. Partial calibration inspection cannot be used to change or stop the mode-selection rule.

No statement from the Gemini advisory report is used as evidence.
