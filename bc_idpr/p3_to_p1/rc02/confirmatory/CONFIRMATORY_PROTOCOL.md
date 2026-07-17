# RC02 Confirmatory Protocol

**Contract:** `BC-IDPR-P3-P1-RC02`  
**Version:** `v0.1.0`  
**Status:** `FROZEN_BEFORE_CONFIRMATORY_EXECUTION`

## Scope

Exactly eight preassigned families and all 106 ordered carriers derived from the pinned 283-carrier supplement are evaluated. Pilot and calibration families are not reevaluated. The only admissible integer mode is

\[
n_*=5,
\]

with the frozen paired control frequency `9.5`.

## Primary endpoint

For every ordered carrier, residualize the anchored complex-column observable against the frozen cubic baseline. With normalized predictor `psi_5` and control `chi_5`, compute

\[
\Delta_J=|\langle r_J,\psi_5\rangle|^2-|\langle r_J,\chi_5\rangle|^2.
\]

The family energy endpoint is the median over every ordered permutation in that family. A family is positive only when its median is strictly greater than zero.

The family phase is the argument of the amplitude-weighted resultant of the predictor coefficients. Equal family weights are then used for `R1` and `R2`. All eight phases must exist.

## Primary decision

The energy gate requires all three:

1. at least seven of eight positive families;
2. median family advantage at least `0.02`;
3. one-sided exact sign-test p-value at most `9/256 = 0.03515625`.

Outcome precedence is frozen:

1. any hard failure gives `D_INCONCLUSIVE`;
2. energy gate plus `R1 >= 0.60` gives `A_UNIVERSAL_PHASE_LOCK`;
3. energy gate plus `R1 < 0.60` and `R2 >= 0.75` gives `B_PHASE_CLASSES`;
4. every other valid result gives `C_PHASE_HYPOTHESIS_REJECTED`.

## Replication endpoint

The signed-angular-speed residual is evaluated under exactly the same predictor and control. Its energy, sign-test, `R1` and `R2` values are reported. It never changes the primary A/B/C/D assignment and cannot rescue a failed primary endpoint.

## Sequential firewall

No partial outcome, early stopping, mode change, control change, threshold change, family exclusion or selective rerun is permitted. A numerical failure produces D or a protocol-failure state; it is not repaired after inspecting effects.

## Non-claims

The outcome is restricted to the declared finite recoupling class and the frozen deformation interval. It is not a claim about physical oscillations, dynamics, full modular categories, continuum physics, gravity, matter or defects.

No statement from the Gemini advisory report is used as evidence.
