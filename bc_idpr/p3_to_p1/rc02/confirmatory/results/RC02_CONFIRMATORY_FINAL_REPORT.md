# RC02 Confirmatory Final Report

**Contract:** `BC-IDPR-P3-P1-RC02`  
**Stage:** `CONFIRMATORY`  
**Date:** 2026-07-17  
**Status:** `CONFIRMATORY_COMPLETE_OUTCOME_FROZEN`  
**Frozen outcome:** `A_UNIVERSAL_PHASE_LOCK`

## Execution

One complete confirmatory run was performed on the eight preregistered families and all 106 ordered carriers. The immutable parameters were integer mode `5`, paired control `9.5`, the 1101-point phase grid on `[0.60,1.15]`, cubic baseline projection, the anchored complex-column primary observable and the signed-angular-speed replication observable.

Pilot and calibration families were not reevaluated. There was no interim inspection, early stopping, mode reselection or rerun.

## Primary result

\[
N_+=8/8,
\qquad
\operatorname{median}_f\Delta_f=0.12716387712459315,
\]

\[
p_{\mathrm{sign}}=0.00390625=\frac1{256},
\qquad
R_1=0.9967284980027259,
\qquad
R_2=0.9869553189520441.
\]

All preregistered energy criteria passed and `R1 >= 0.60`. The frozen decision precedence therefore assigns

\[
\boxed{\texttt{A\_UNIVERSAL\_PHASE\_LOCK}}.
\]

The primary median exceeds the frozen `0.02` threshold by a factor of `6.358194`. The smallest family median is `0.071275181920`, still `3.563759` times the threshold.

## Family results

| Family | Carriers | Primary median | Primary phase | Replication median |
|---|---:|---:|---:|---:|
| `1,1,4,4` | 6 | 0.176303139003 | -1.262774395 | 0.158357895116 |
| `1,2,2,3` | 12 | 0.195598367112 | -1.172415249 | 0.181050386796 |
| `1,2,5,6` | 24 | 0.115286013457 | -1.189143058 | 0.084686623977 |
| `1,3,3,5` | 12 | 0.152933607458 | -1.152768975 | 0.130141377839 |
| `1,3,5,5` | 12 | 0.127163877125 | -1.078305169 | 0.092405538454 |
| `1,4,5,6` | 24 | 0.071275181920 | -1.036865839 | 0.016483949948 |
| `1,5,5,5` | 4 | 0.075762397330 | -1.005729173 | 0.017432680123 |
| `2,2,4,6` | 12 | 0.127163877125 | -1.078305169 | 0.092405538450 |

## Replication

The replication endpoint was computed independently of the primary decision and could not change the assigned outcome. It produced `8/8` positive families, median advantage `0.09240553845217536`, sign-test p-value `1/256`, `R1=1.0` and `R2=1.0`.

This is supporting reproducibility within the same finite recoupling atlas, not an independent external replication.

## Numerical audit

```text
max transpose-orthogonality residual: 2.3678475198021344e-15
max column-norm deviation:            8.8817841970012523e-16
max anchor evaluator disagreement:    2.0591569550578068e-15
anchor speed sign failures:            0
primary residual degeneracies:         0
replication residual degeneracies:     0
undefined primary family phases:       0
undefined replication family phases:   0
nonfinite values:                      0
hard failures:                         0
```

## Interpretation boundary

The result establishes a preregistered finite-class, local-in-deformation-coordinate directional phase concentration for the frozen mode/control pair. It does not establish arbitrary-level or arbitrary-label universality, full category coherence, global gluing, a continuum limit, or a physical time/dynamics, mass, matter or gravity interpretation.

## Freeze state

```text
RC02_CONFIRMATORY_RUN: COMPLETE
RC02_CONFIRMATORY_OUTCOME: A_UNIVERSAL_PHASE_LOCK
RC02_CONFIRMATORY_OUTCOME_STATUS: FROZEN
RC02_CONFIRMATORY_RERUN: NOT_AUTHORIZED
RC02_P1_FINITE_ATLAS_RESULT: CONFIRMED
```

Canonical SHA-256 of the full local result artifact:

```text
d1cfa470cb6a9a8989c573a11be7a705c875c37f3ae101e35fb9544a602ee3c0
```

No statement from the Gemini advisory report is used as evidence.
