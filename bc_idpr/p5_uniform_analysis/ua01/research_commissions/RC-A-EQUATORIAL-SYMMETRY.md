# P5-UA01 Research Commission A

## Exact equatorial and reflection structure of the mode family

**Commission ID:** `P5-UA01-RC-A`  
**Type:** exact symbolic / representation-theoretic analysis  
**Primary question:** What exact algebraic structure is created by the anchor `theta_0 = pi/12`, and which invariants distinguish the modes `m=5,6,7`?

## Frozen object

Use

\[
[m]_q(\theta)=\frac{\sin(m\theta)}{\sin\theta},
\qquad
\Phi_m(\theta)=\partial_\theta^2\log[m]_q(\theta)
=-m^2\csc^2(m\theta)+\csc^2\theta.
\]

The derivative order is fixed at two. The integer `m` is the q-number / predictor-mode index.

## Tasks

1. Prove the complete reflection identities at `theta_0=pi/12`, including
   \[
   [m]_q=[12-m]_q,
   \]
   with precise domains and sign conventions.
2. Characterize the equatorial triplet `m=5,6,7` and the reflected pair `5 <-> 7`.
3. Derive exact algebraic values for `[m]_q`, `Phi_m`, and the first required theta-jets at the anchor for all `m=2,...,10`.
4. Decompose the mode family into reflection-even and reflection-odd parts under `m -> 12-m`.
5. Determine exactly how the factor `m^2` in the second logarithmic derivative breaks q-dimension reflection symmetry.
6. Search for anchor-local invariants or extremal quantities that single out `m=5`, the pair `{5,7}`, or the triplet `{5,6,7}` without using RC02 response outcomes.
7. State which properties persist on a neighborhood of `theta_0` and which hold only at the exact anchor.

## Positive targets

Potential useful outputs include:

- an exact reflection theorem;
- an equatorial-mode normal form;
- a symmetry-breaking identity for `Phi_{12-m}-Phi_m`;
- a local invariant or monotone quantity whose extremum is attained at `m=5`;
- a proof that the natural invariant selects only a pair or triplet, requiring later carrier geometry to resolve the branch.

## Deliverables

- theorem and proof ledger;
- exact symbolic table for `m=2,...,10`;
- minimal-polynomial / algebraic-number representation of anchor values;
- local Taylor expansion around `theta_0` with certified remainder;
- list of candidate invariants ranked by mathematical naturalness;
- explicit handoff to Commissions B and C.

## Prohibitions

Do not use physical resonance, phase-space rotation, Kuramoto language, pentagon numerology, or fifth-derivative arguments. Do not use confirmatory outcomes to choose an invariant.

## Allowed terminal statuses

- `EXACT_EQUATORIAL_INVARIANT_FOUND`
- `REFLECTION_PAIR_ONLY`
- `TRIPLET_STRUCTURE_ONLY`
- `NO_ANCHOR_LOCAL_SELECTOR_FOR_M5`
