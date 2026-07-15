# BC-IDPR-P3 — Independent Deformation

## Objective

Construct a family `D(q, rho, xi; vartheta)` and at least one admissible path along which `q` changes while normalized geometry `xi`, representation scale `rho`, and declared protocol variables `vartheta` remain fixed exactly or within certified tolerances.

## Required outputs

1. `P3-CONTRACT` — typed object definitions and admissible domain.
2. `P3-EXACT-BENCHMARK` — minimal family with exact parameter separation.
3. `P3-CONFOUNDED-CONTROL` — family with deliberate geometry or scale leakage.
4. `P3-CERTIFICATE` — analytic and numerical leakage diagnostics.
5. `P3-OBSTRUCTION-GRAPH` — existence, obstruction, and no-go obligations.
6. `P3-HANDOFF` — frozen interface to P1.

## Core identity

For an observable `O`, audit the decomposition

`dO/ds = partial_q O * q_dot + partial_rho O * rho_dot + D_xi O[xi_dot] + D_vartheta O[vartheta_dot]`.

A P3 path is accepted only when contaminating terms vanish or admit bounds below preregistered tolerances.

## Minimum certificate fields

- `q_variation_margin`
- `geometry_leakage`
- `scale_leakage`
- `protocol_leakage`
- `branch_identity_margin`
- `wall_distance`
- `certificate_status`

## Claim ceiling

P3 certifies a mathematical parameter-separation construction. It does not establish physical causation, dynamics, time, RG flow, or a fundamental deformation law.
