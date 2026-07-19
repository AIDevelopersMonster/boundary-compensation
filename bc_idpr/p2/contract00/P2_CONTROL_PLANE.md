# BC-IDPR P2 Global Gluing Control Plane

## Canonical object

- Code: `BC-IDPR-P2-CONTRACT00`
- Title: `Typed Coefficient Gluing on a Finite Registered Atlas`
- Document class: technical research contract and baseline theorem note
- Branch: BC-IDPR / P2 Global Gluing
- State: `ACTIVE_BASELINE_CONSTRUCTION`
- Upstream: published P5, DOI `10.5281/zenodo.21444321`
- Downstream: data-derived transition registry, singular-value certificate, compatibility-defect certificate, later finite-complex or manifold-level extension

## Claim ceiling

The contract is finite-dimensional and coefficient-level. It constructs a type-correct abstract baseline for gluing the five P5 coefficient channels. It does not yet derive transition maps from quantum-6j support data, prove a nonzero global section for the registered atlas, certify a manifold-level frame constant, or identify gluing with physical geometry or dynamics.

## Frozen P5 input

- Registered vertices: `U1@65536`, `U2@32768`, `U3@65536`, `U4@32768`, `EQ@65536`.
- Local coefficient spaces: `V_a ~= R^2`.
- Local normalized defects: `Dtilde_a(eta) >= mu_a I`.
- Uniform interval: `eta in [0.995,1.005]`.
- Common lower resource: `mu_star = 0.02059662265710331`.

## P2 work packages

### P2-WP0 - typing, graph, and normalization

Declare the global domain, the finite overlap graph, local coefficient spaces, edge orientation, transition-map direction, weight normalization, and reset walls. No transition may be inferred from numerical convenience alone.

### P2-WP1 - support-to-coefficient interfaces

When an edge comparison starts from selected support spaces, construct typed maps

`Pi_a: S_a -> V_a`

and certify their normalization, rank, and stability. The high-rank supports are never identified with the two-dimensional coefficient channels.

### P2-WP2 - edge transition registry

Construct candidate edge maps

`T_ab(eta): V_b -> V_a`

from declared overlap data. Record whether each map is orthogonal/unitary, contractive, or general bounded; record its conditioning and validity chamber.

### P2-WP3 - cycle compatibility and exact gluing domain

Build the twisted incidence operator

`(B_T x)_(a,b) = x_a - T_ab x_b`

and determine the exact consistency space `K_T = ker B_T`. For a connected graph, certify the fixed space of all fundamental cycle products. Accepted outputs include dimensions 0, 1, or 2; zero is a legitimate obstruction result.

### P2-WP4 - singular-value and compatibility budget

Construct a global analysis map

`Gamma: H_glob -> direct_sum_a V_a`

or use the normalized inclusion/transport parametrization of `K_T`. Certify

`sigma_min(Gamma) >= s_star > 0`

on the declared domain and decompose the self-adjoint defect

`E_compat = E_type + E_overlap + E_cycle + E_numeric`

with an operator-norm budget `delta_compat`.

### P2-WP5 - uniform eta continuation and reset protocol

Prove the edge maps, cycle products, gluing dimension, singular-value bound, and defect budget remain valid on the full eta interval. Any rank, threshold, branch, orientation, or transition-conditioning wall triggers `P2_CERTIFICATE_RESET`.

### P2-WP6 - finite-complex and manifold-level promotion

This work package remains blocked until at least one nontrivial finite registered-atlas gluing certificate passes. Promotion requires a family of complexes/refinements and lower constants uniform in the declared complexity parameter. One finite graph is not a manifold theorem.

## Gates

### Gate P2-G1 - typed baseline

Pass only when the graph, edge directions, coefficient maps, and global domain are type correct and reproducible.

### Gate P2-G2 - nontrivial gluing

Pass only when the exact or declared approximate gluing domain is nonzero and its dimension is certified. Failure status: `NO_NONZERO_GLOBAL_SECTION`.

### Gate P2-G3 - quantitative positivity

Pass only when

`delta_compat < mu_star * s_star^2`.

### Gate P2-G4 - eta uniformity

Pass only when P2-G1 through P2-G3 hold throughout `[0.995,1.005]` without silent continuation across walls.

### Gate P2-G5 - manifold-level claim

Blocked until a refinement family and complexity-uniform constants are proved.

## Accepted failure states

- `TYPE_MISMATCH`
- `EDGE_MAP_UNDEFINED`
- `EDGE_MAP_ILL_CONDITIONED`
- `NO_NONZERO_GLOBAL_SECTION`
- `GLOBAL_SECTION_DIMENSION_REDUCED`
- `GLOBAL_ANALYSIS_NOT_INJECTIVE`
- `SINGULAR_VALUE_MARGIN_LOW`
- `CYCLE_COMPATIBILITY_FAILED`
- `COMPATIBILITY_DEFECT_TOO_LARGE`
- `P2_CERTIFICATE_RESET`
- `INCONCLUSIVE_GLUING`

## Immediate next computational obligation

Construct the first data-derived transition registry on a preregistered sparse graph. The recommended first graph is a spanning tree plus one declared chord: it is the smallest topology with one nontrivial fundamental cycle and therefore the smallest model capable of detecting a genuine cycle-compatibility obstruction.
