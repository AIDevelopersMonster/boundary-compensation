# BC-IDPR P5 Uniform Analysis Contract 01

**Title:** A Priori Phase/Frame Lower Bounds from Geometry, Wall Margin, and Coherent-State Design  
**Contract ID:** `BC-IDPR-P5-UA01`  
**Document class:** solver-neutral analytical research contract  
**Status:** `OPEN_OBLIGATION_GRAPH / NO_UNIFORM_THEOREM_CLAIMED / P2_BLOCKED`  
**Date:** 2026-07-17

## Research question

For a declared finite quantum-6j operator class and a wall-safe independent-deformation chamber, can one prove a nonzero lower bound

```text
c_frame >= B_frame(geometry margin, wall margin, coherent-state design) > 0
```

and use it to certify stable phase concentration and positive predictor-versus-control energy advantage without reusing RC02 confirmatory data for tuning?

## Mathematical spine

```text
geometric nondegeneracy
  -> wall-safe derivative and basis bounds
  -> coherent-state measurement matrix M(theta)
  -> lower singular-value / frame bound
  -> nonvanishing complex phase statistic
  -> phase-concentration and energy-margin transfer
  -> P2 gluing handoff eligibility
```

## Frozen upstream evidence

RC02 is immutable. Its confirmatory outcome `A_UNIVERSAL_PHASE_LOCK` is accepted only on the frozen atlas of eight families and 106 ordered carriers. It motivates the analytical target but does not prove any P5 bound.

## Contract artifacts

- [`CONTRACT.md`](CONTRACT.md) — definitions, target inequalities, typed holes, evidence rules and outcome map.
- [`OBLIGATION_GRAPH.md`](OBLIGATION_GRAPH.md) — work packages, gates, dependencies and accepted failure states.
- [`P2_HANDOFF_CONTRACT.md`](P2_HANDOFF_CONTRACT.md) — exact conditions required before global gluing work may begin.
- [`UA01_CONTRACT.json`](UA01_CONTRACT.json) — machine-readable contract summary.

## Immediate first work package

`UA01-WP1` must construct the operator-adapted coherent-state measurement matrix and solve the fixed-candidate E-optimal design problem

```text
maximize t
subject to sum_a w_a v_a v_a^* >= t I,
           w_a >= 0,
           sum_a w_a = 1.
```

The resulting primal weights and dual/KKT certificate will determine whether the observed frame strength has an extremal structure rather than being merely a numerical accident.

## Claim firewall

No positive P5 result may be promoted beyond the explicitly certified chamber, level/label class, residual subspace and coherent-state protocol. P2 remains closed until the handoff contract is satisfied.

No statement from the Gemini advisory report is used as evidence.
