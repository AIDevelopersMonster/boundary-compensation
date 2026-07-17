# P3-B-M8 Research Audit v0.1.0

**Verdict:** negative family-level generalization certificate with a preserved exploratory signal.

## Validation integrity

The module reuses the frozen M7 predictors and ridge parameter. It changes only the validation split: all ordered carriers with the same sorted doubled-spin quadruple are held out together. This prevents permutation-related representation relatives from appearing on both sides of a fold.

The 75 ordered carriers form 9 families. Fold sizes range from 1 to 24. Held-out data are excluded from both standardization and regression.

## Findings

Matrix-augmented NRMSE increases from ordinary LOOCV

`(0.304711, 0.406176, 0.466017)`

to family-blocked values

`(0.385927, 0.566899, 0.673174)`.

Against the family-blocked scalar baseline, the matrix descriptor improves the first target by about 31.7 percent, but the second and third by only about 1.5 and 0.6 percent. The frozen requirements of NRMSE at most `0.35` and at least ten-percent improvement for every target are not met.

## Meaning

M7's ordinary LOOCV was informative but not an independent unseen-family transfer certificate. The result identifies representation-family dependence rather than proving absence of a richer equivariant law.

## Next obligation

A further module must either derive an independently motivated permutation-equivariant descriptor before evaluation or construct a genuinely new label-range atlas reserved for validation. Arbitrary feature search on the same nine families is exploratory only.

No statement from the Gemini advisory report is used as evidence.
