# BC-IDPR-P1 — Phase-Resolved Response

## Entry condition

P1 execution begins only after the P3 handoff passes the independence gate. Protocol design may proceed earlier, but predictors, exclusions, tolerances, and model-selection rules must be frozen before final data inspection.

## Objective

Measure branch-resolved signed and complex residual response under a certified independent deformation, and determine whether any phase structure is robust, identifiable, and analytically motivated.

## Required outputs

1. `P1-PREREGISTRATION` — frozen grid, predictors, null models, exclusions, and tests.
2. `P1-OBSERVABLE-REGISTRY` — signed, complex, branch, projector, and sector-weight observables.
3. `P1-RUN-MANIFEST` — code, environment, input hashes, and parameter ranges.
4. `P1-RESULTS` — machine-readable results and figures.
5. `P1-DEVIATION-LOG` — every departure from preregistration.
6. `P1-ROBUSTNESS-AUDIT` — resolution, branch, frame, scale, geometry, and wall checks.
7. `P1-CLASSIFICATION` — robust structure, inconclusive result, or valid null result.

## Model hierarchy

Test in declared order:

1. null or constant residual;
2. power or asymptotic baseline;
3. trigonometric modulation;
4. mixed power-trigonometric form;
5. symmetry-constrained or analytically derived phase law.

A fitted sinusoid is evidence of modulation, not an explanation.

## Failure and null statuses

- `PHASE_SIGNAL_NOT_ROBUST`
- `MODEL_SELECTION_INCONCLUSIVE`
- `BRANCH_IDENTITY_FAILURE`
- `CERTIFICATE_RESET`
- `NULL_RESULT_WITH_VALID_PROTOCOL`

## Claim ceiling

P1 may report phase-sensitive response within the certified model family. It may not infer fundamental physics from modulation without an additional derivation and independent validation layer.
