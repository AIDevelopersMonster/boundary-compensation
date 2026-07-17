# BC-IDPR P5-UA01 Obligation Graph

## Spine

```text
RC02 frozen finite-atlas phase law
  -> UA01-WP0 chamber and wall registry
  -> UA01-WP1 coherent-state measurement matrix
  -> UA01-WP2 E-optimal design certificate
  -> UA01-WP3 jet-to-Lipschitz and basis-conditioning bounds
  -> UA01-WP4 local frame lower bound
  -> UA01-WP5 certified cover and uniform frame bound
  -> UA01-WP6 phase/amplitude/energy transfer
  -> UA01-WP7 independent external check
  -> UA01-WP8 P2 handoff certificate
  -> P2 eligibility decision
```

## Immutable upstream node

`BC-IDPR-P3-P1-RC02` is closed with outcome `A_UNIVERSAL_PHASE_LOCK`. It is an evidence node, not an optimization dataset. No edge in this graph permits a return to RC02 mode selection, threshold selection, control selection or confirmatory rerun.

## Work packages

### UA01-WP0 — Chamber and wall registry

**Inputs**

- independent deformation coordinates;
- normalized geometry variables;
- representation level/label typing;
- residual-protocol branch conventions.

**Outputs**

- compact target domain or an explicit finite union of compact chambers;
- geometric margin functional and threshold \(\nu\);
- wall set \(\mathcal W\) and certified margin \(\mu\);
- reset rules at every rank, spectral, phase or chart wall.

**Failure states**

- `UA01_EMPTY_ADMISSIBLE_CHAMBER`;
- `UA01_WALL_SET_INCOMPLETE`;
- `UA01_WALL_DISTANCE_UNCERTIFIED`.

### UA01-WP1 — Operator-adapted measurement matrix

**Outputs**

- residual basis \(B_\alpha(\theta)\);
- coherent-state lower-symbol evaluator;
- complex measurement matrix \(M(\theta)\);
- independent anchor evaluator;
- normalization and phase-gauge registry.

**Gate**

`UA01-G1A MATRIX_DEFINED` requires evaluator agreement within a declared certified tolerance and constant residual-channel rank.

**Failure states**

- `UA01_RESIDUAL_RANK_CHANGE`;
- `UA01_PHASE_GAUGE_AMBIGUOUS`;
- `UA01_MEASUREMENT_EVALUATOR_DISAGREEMENT`.

### UA01-WP2 — E-optimal coherent-state design

For a frozen candidate pool, solve

\[
\max_{w,t}\ t
\quad\text{subject to}\quad
\sum_a w_av_av_a^*\succeq tI,
\quad w\in\Delta_M.
\]

**Outputs**

- optimal or certified near-optimal weights;
- positive lower-frame value \(t_*\);
- dual matrix witness;
- KKT/contact set;
- primal-dual gap and residual audit;
- support sparsity and uniqueness/nonuniqueness report.

**Gate**

`UA01-G1 DESIGN` requires a certified \(t_*>0\).

**Failure states**

- `UA01_CANDIDATE_POOL_NOT_SPANNING`;
- `UA01_OPTIMAL_FRAME_CONSTANT_ZERO`;
- `UA01_DUAL_CERTIFICATE_MISSING`;
- `UA01_DESIGN_NONUNIQUE_UNCONTROLLED`.

### UA01-WP3 — Geometry/wall regularity bounds

**Outputs**

- derivative or jet bounds for residual operators and lower symbols;
- explicit dependence on \(\mu\), \(\nu\), level and labels;
- basis-conditioning bounds;
- a certified matrix perturbation constant \(L_j\) at each anchor.

Existing recursive jet calculus is admissible here as upstream machinery, but every imported constant must be specialized to the UA01 matrix and chamber.

**Failure states**

- `UA01_JET_BOUND_NOT_SPECIALIZED`;
- `UA01_BASIS_CONDITIONING_DIVERGES`;
- `UA01_LABEL_DEPENDENCE_UNBOUNDED`;
- `UA01_REGULARITY_LOST_BEFORE_WALL`.

### UA01-WP4 — Local frame theorem/certificate

At each anchor \(\theta_j\), certify

\[
\sigma_{\min}(M(\theta_j))=\sigma_j>0
\]

and a radius \(r_j>0\) such that

\[
\sigma_j-L_jr_j>0.
\]

**Output**

\[
\inf_{\theta\in B(\theta_j,r_j)}c_{\mathrm{fr}}(\theta)
\ge(\sigma_j-L_jr_j)^2>0.
\]

**Gate**

`UA01-G2 LOCAL_FRAME` requires at least one nonzero certified radius.

**Failure states**

- `UA01_CERTIFIED_RADIUS_ZERO`;
- `UA01_ANCHOR_FRAME_CONSTANT_TOO_SMALL`;
- `UA01_PERTURBATION_BOUND_DOMINATES`.

### UA01-WP5 — Uniformization by certified cover

**Outputs**

- certified finite cover of the full declared chamber;
- overlap audit and no-wall-crossing certificate;
- explicit global lower bound

\[
\underline c_{\mathrm{fr}}
\ge
\min_j(\sigma_j-L_jr_j)^2>0.
\]

Adaptive subdivision is permitted only under a deterministic stopping rule independent of RC02 confirmatory outcomes.

**Gate**

`UA01-G3 UNIFORM_FRAME` requires complete coverage and a strictly positive minimum.

**Failure states**

- `UA01_DOMAIN_NOT_COVERED`;
- `UA01_SUBDIVISION_DOES_NOT_TERMINATE`;
- `UA01_UNIFORM_FRAME_BOUND_COLLAPSES`;
- `UA01_ONLY_GRID_EVIDENCE_AVAILABLE`.

### UA01-WP6 — Phase and energy transfer

**Outputs**

- uniform amplitude floor \(a_0>0\) for the complex family statistic;
- angular perturbation bound \(\delta\);
- explicit \(R_1\) and \(R_2\) lower bounds;
- explicit energy-advantage lower bound \(\underline\Delta_E\);
- comparison with the frozen RC02 benchmarks \(R_1\ge0.60\) and \(\Delta_E\ge0.02\).

**Gate**

`UA01-G4 PHASE` requires nonvanishing statistics and positive certified concentration and energy margins.

**Failure states**

- `UA01_PHASE_STATISTIC_CAN_VANISH`;
- `UA01_PHASE_BRANCH_NONUNIQUE`;
- `UA01_R1_BOUND_BELOW_TARGET`;
- `UA01_ENERGY_MARGIN_NONPOSITIVE`.

### UA01-WP7 — Independent external check

The primary purpose is falsification, not parameter selection.

Admissible routes:

1. newly sealed families unused by RC02 and by design selection;
2. exact exhaustive enumeration of a declared finite class;
3. certified interval evaluation over the complete target chamber.

**Gate**

`UA01-G5 EXTERNAL` requires a route independent of RC02 confirmatory tuning.

**Failure states**

- `UA01_EXTERNAL_SET_CONTAMINATED`;
- `UA01_ONLY_POST_HOC_VALIDATION`;
- `UA01_CERTIFIED_BOUND_VIOLATED`.

### UA01-WP8 — P2 handoff

**Outputs**

- local constants with sector and normalization metadata;
- compatibility-space definitions;
- lower singular-value bounds for gluing restrictions;
- phase-gauge compatibility bounds;
- explicit size dependence;
- proof that the proposed global lower bound remains positive in the declared finite gluing class.

**Gate**

`UA01-G6 P2_HANDOFF` is governed by `P2_HANDOFF_CONTRACT.md`.

**Failure states**

- `UA01_SECTOR_COMPATIBILITY_UNDEFINED`;
- `UA01_GLUING_SINGULAR_VALUE_ZERO`;
- `UA01_GLOBAL_BOUND_DECAYS_WITHOUT_CONTROL`;
- `UA01_PHASE_COCYCLE_UNCONTROLLED`;
- `UA01_P2_HANDOFF_INCOMPLETE`.

## Dependency matrix

| Work package | Requires | Opens |
|---|---|---|
| `WP0` | RC02 closure, P3/CERT typing | `WP1`, `WP3` |
| `WP1` | `WP0` | `WP2`, `WP3` |
| `WP2` | `WP1` | `WP4` |
| `WP3` | `WP0`, `WP1` | `WP4` |
| `WP4` | `WP2`, `WP3` | `WP5`, local `WP6` |
| `WP5` | `WP4` | uniform `WP6` |
| `WP6` | `WP4` or `WP5` | `WP7`, qualified local result |
| `WP7` | frozen `WP2`--`WP6` outputs | `WP8` |
| `WP8` | `WP5`, `WP6`, `WP7` | P2 eligibility decision |

## Allowed terminal states

```text
P5_A_UNIFORM_PHASE_FRAME_BOUND
P5_B_LOCAL_BOUND_ONLY
P5_C_NUMERICAL_CERTIFICATE_ONLY
P5_D_ANALYTICAL_OBSTRUCTION
```

Every terminal state must preserve unresolved holes and downstream restrictions. A negative or local-only outcome must not be converted into P2 eligibility by adding a new empirical prefactor.

No statement from the Gemini advisory report is used as evidence.
