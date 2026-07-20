# P2-RC01 Handoff — Typed Global Carrier and Coefficient-Analysis Map Reconstruction

P2-OR02 proved that U3 and U4 occupy disjoint ordered-boundary character
sectors. The five-edge same-index cycle is therefore reset at its carrier layer.

## Required construction

1. Define the global object `H_glob` as a typed sector decomposition or another
   explicitly justified common carrier.
2. Specify restriction maps from `H_glob` to every registered local support.
3. Construct the P5-required maps `Pi_a : S_a -> V_a` with declared domains,
   kernels, norms, and frame dependence.
4. Define compatibility only between type-correct sectors. If inter-family
   morphisms are intended, construct them algebraically; do not infer them from
   equality of grid indices.
5. Certify a positive lower singular-value bound for the assembled analysis
   map and bound the compatibility defect.
6. Rebuild any cycle from the new typed morphisms. P2-E02 transitions may be
   retained only as proxy diagnostics, not reused as physical edges.

## Execution constraints

- absence of historical caches triggers local computation, never an absence
  certificate;
- full 32768- or 65536-dimensional family bases remain prohibited;
- raw arrays are RAM-only and are scrubbed after contraction;
- no post-hoc sign, axis, or side permutation is allowed.

## Terminal outcomes

- `TYPED_GLOBAL_CARRIER_CERTIFIED`;
- `GLOBAL_ANALYSIS_NOT_INJECTIVE`;
- `COMPATIBILITY_DEFECT_TOO_LARGE`;
- `WALL_RESET_REQUIRED`;
- `NO_TYPE_CORRECT_CYCLE`.
