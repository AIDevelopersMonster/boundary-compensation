# P3-B-M9R Research Audit v0.1.0

**Verdict:** negative certification result with a strong positive out-of-range structural signal.

## Scope

M9R evaluates a permutation-invariant family descriptor on representation families that were excluded from training and contain at least one previously unseen doubled-spin label `5` or `6`.

The predecessor M9 is correctly marked `FRONTIER_INVALIDATED`: its test class, with every label restricted to `{5,6}`, was empty under the exactly-two-channel condition. No model was fitted before that invalidation.

## Independence design

Training consists of nine families generated from doubled spins `{1,2,3,4}`. Testing consists of fifteen disjoint families from labels `{1,...,6}` that contain at least one `5` or `6`. The test set includes 208 valid ordered carriers.

All feature standardization and ridge fitting use training families only. Derivatives of `F` are excluded from predictors.

## Descriptor

The scalar baseline aggregates normalized external and channel Casimir features over each permutation orbit. The augmented descriptor additionally aggregates the entries, trace, determinant and entry second moment of `F(theta0)`.

This is an orbit-statistics construction, not an arbitrary post-result feature search.

## Findings

Scalar test NRMSE is

`(0.908351, 3.932189, 8.046650)`.

Permutation-equivariant test NRMSE is

`(0.491553, 1.584959, 5.179159)`.

Relative improvements are

`(0.458852, 0.596927, 0.356358)`.

Thus the augmented descriptor improves every target by more than the frozen ten-percent requirement. However, all absolute errors exceed the frozen `0.40` threshold. The first target, family-mean `log|omega|`, is closest but still fails at `0.491553`. The higher derivatives remain far from certification.

The maximum relative change under halving the jet-extraction step is `2.06e-7`, so numerical differentiation does not explain the failure.

## Claim firewall

Allowed:

> Permutation-orbit statistics of anchor recoupling data substantially improve prediction on fifteen independent representation families containing new doubled-spin labels, but they do not attain the preregistered absolute accuracy required for certification.

Not allowed:

- a universal permutation-equivariant law;
- exact prediction of the recoupling jet;
- all-spin or asymptotic transfer;
- a physical interpretation of `q`;
- retuning the same descriptor on the observed M9R test families and calling it confirmatory.

## Next obligation

The current evidence separates amplitude from shape. A next construction module may target only `log|omega|`, which is substantially closer to certification, but it must use an independently derived analytic invariant or a newly frozen family atlas. The observed M9R test families may not be reused for unrestricted feature selection.

No statement from the Gemini advisory report is used as evidence.
