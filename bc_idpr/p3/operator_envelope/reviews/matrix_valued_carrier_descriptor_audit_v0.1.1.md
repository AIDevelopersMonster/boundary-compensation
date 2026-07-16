# P3-B-M7 Research Audit v0.1.1 — Metadata Correction

**Verdict:** the negative M7 certification result is unchanged.

## Defect found

The v0.1.0 document and certificate reported descriptor dimensions `11` and `15`. Direct inspection of the implemented feature vectors gives:

- baseline: four external Casimirs + four channel Casimirs + two channel gaps = `10`;
- matrix augmented: baseline + four entries of `F(theta0)` = `14`.

The regression code always operated on the actual NumPy arrays. Therefore no fit, prediction, NRMSE value or gate decision was affected.

## Corrective action

The source now derives dimensions from `X0.shape[1]` and `X1.shape[1]`. A regression test compares the declared metadata with the actual feature-vector lengths. The test count increases from 10 to 11.

## Preserved result

Matrix augmentation still improves all three LOOCV targets, but the errors

`(0.304711, 0.406176, 0.466017)`

remain above the frozen threshold `0.25`. The status remains

`REPRESENTATION_DESCRIPTOR_LOOCV_NOT_CERTIFIED`.

No statement from the Gemini advisory report is used as evidence.
