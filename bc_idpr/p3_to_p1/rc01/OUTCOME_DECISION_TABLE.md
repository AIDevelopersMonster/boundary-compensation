# RC01 Outcome Decision Table

**Contract:** `BC-IDPR-P3-P1-RC01`  
**Version:** `v0.1.0`  
**Status:** `FROZEN_BEFORE_PILOT`  

The decision unit is the family, not the ordered carrier. Only the calibration-selected and commit-frozen `n_star` enters the confirmatory decision.

| Outcome | Energy advantage | Directional phase | Axial phase | Integrity gates | Permitted claim |
|---|---|---|---|---|---|
| `A_UNIVERSAL_PHASE_LOCK` | at least 7/8 positive; median at least 0.02; exact one-sided sign p at most 0.03515625 | `R1 >= 0.60` | reported, not required | all pass | finite-class integer-q phase locking for the primary complex observable |
| `B_PHASE_CLASSES` | same energy criteria as A | `R1 < 0.60` | `R2 >= 0.75` | all pass | finite-class axial or multi-class q-phase structure; no universal directional phase |
| `C_PHASE_HYPOTHESIS_REJECTED` | primary energy criteria fail | any | any | all pass | preregistered integer-q phase hypothesis not supported against matched controls |
| `D_INCONCLUSIVE` | not interpreted | not interpreted | not interpreted | one or more hard failures | no positive or negative phase conclusion |

## Precedence

1. Any hard failure gives `D_INCONCLUSIVE`.
2. If no hard failure and A criteria pass, assign A.
3. Otherwise, if B criteria pass, assign B.
4. Otherwise assign C.

## Replication observable

The signed-speed endpoint is reported under the same frozen `n_star`. Agreement strengthens interpretation; disagreement must be reported. It cannot change C into A and cannot rescue a failed primary complex-observable criterion.

## Local logarithmic observables

Local log-slope and log-curvature results on `[0.99,1.01]` are consistency diagnostics. They do not enter A/B/C assignment.

## Non-claims

None of A, B, C or D establishes physical time oscillation, matter, mass, defects, gravity, global gluing, a continuum exponent or universality outside the frozen finite class.

No statement from the Gemini advisory report is used as evidence.
