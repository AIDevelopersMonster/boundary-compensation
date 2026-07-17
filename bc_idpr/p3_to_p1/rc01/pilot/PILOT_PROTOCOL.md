# RC01 pilot pipeline protocol

**Pipeline:** `BC-IDPR-P3-P1-RC01-PILOT-PIPELINE`  
**Version:** `v0.1.0`  
**Status:** `PILOT_ONLY / NON_INFERENTIAL`

The executable evaluates exactly the four preregistered pilot families. It refuses every stage name other than `pilot`.

## Permitted operations

- reconstruct the two frozen grids;
- evaluate the primary anchored complex-column observable;
- evaluate the signed-speed replication observable;
- evaluate the two certified-local logarithmic-speed consistency observables;
- remove the frozen cubic baseline;
- compute all preregistered integer and half-integer-control diagnostics;
- test data layout, orientation, orthogonality gates, degeneracy handling and reproducibility.

## Forbidden operations

- evaluating any calibration or confirmatory carrier;
- selecting `n_star`;
- ranking or recommending a primary frequency for later stages;
- modifying grids, modes, baseline degree or thresholds;
- assigning outcomes A--D;
- importing the deferred review proposals into RC01.

## Hermitian convention

The implementation uses the standard mathematical convention in which the Hermitian inner product is conjugate-linear in its first argument. Thus `numpy.vdot(r, psi)` implements the preregistered coefficient `c=<r,psi>/||r||`.

## Contamination guard

Every evaluator call is preceded by a family-key assertion. The result certificate must state:

```text
calibration_results_present=false
confirmatory_results_present=false
selected_mode=null
outcome=null
```

No statement from the Gemini advisory report is used as evidence.