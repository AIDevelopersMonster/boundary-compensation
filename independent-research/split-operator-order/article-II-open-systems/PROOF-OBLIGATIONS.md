# Article II — proof obligations and claim firewall

## Proved in the current bounded core

- Exact reduced-loop decomposition into transported multiplicativity defects.
- UCP multiplicativity-defect norm certificate.
- Multiplicative-domain flatness criterion.
- Exact composition law for multiplicativity defects under nested reductions.
- Layer-resolved defect identity for finite context-reduction chains.
- Two-sided backtracking/Schwarz-defect characterization for unitary transports.
- Stinespring defect formula and squared-leakage form of backtracking defect.
- Exact semigroup evolution equation for `Delta_t`.
- Exact Duhamel representation of `Delta_t`.
- GKSL Leibniz-defect formula for bounded Lindblad operators.
- Exact positive evolution formula for the Schwarz defect.
- Exact integral representation of reduced loop holonomy for uniformly continuous UCP semigroups.
- First-order reduced-loop expansion as a corollary of the exact integral theorem.
- Exact benchmark channel calculations for dephasing, depolarization, and amplitude damping on the contextual braid/backtracking designs.
- Transport-operator-system restriction ceiling for finite-channel identifiability.
- Strong finite-channel no-go: complete closed-loop holonomy data can fail to identify a UCP channel.
- Full bilinear `Gamma_L` determines a bounded generator on `M_d` modulo Hamiltonian derivations.
- General finite-dimensional rank criterion: universal first-order contextual-loop identifiability iff the real measurement map has rank `(d^2-1)^2`.
- Complete qubit theorem: one Article-I braid plus two backtracking loops identify all nine real dissipative parameters modulo Hamiltonian derivations.
- Exact minimal Coxeter-face designs for `d=3,4,5`, each saturating the face-count lower bound.
- Generic open-dense full-rank consequence for the certified `d=3,4,5` templates.
- All-d Weyl generator-defect theorem and all-d generalized flat-loop tomography of order `Theta(d^2)`.
- Engineered Article-I Coxeter squares realizing arbitrary target first-two edge transports `U,V in SU(d)`.
- All-d Coxeter tomography theorem with upper bound `3d^2-1`.
- Improved all-d Coxeter tomography theorem: an order-three Clifford anchor propagates backtracking vanishing through the full Weyl orbit, eliminating the separate Weyl-backtrack family.
- Improved constructive bound:
  `L_d^Cox <= 2d^2`.
- Exact scalar-count lower bound:
  `L_d^Cox >= floor(d^2/2)`.
- Therefore the remaining universal constant-factor gap is at most `4`.
- Numerical lower-bound saturation evidence extends beyond the exact `d=3,4,5` certificates to generic square-only designs for `d=6` and `d=7`.

## Immediate open obligations

1. Integrate the `2d^2` theorem into the main LaTeX manuscript with stable numbering and explicit citations for Gotô commutator surjectivity and finite Heisenberg/Clifford implementation.
2. Prove or refute the sharp all-d Coxeter conjecture:
   `L_d^Cox = floor(d^2/2)`
   for every `d>=3`.
3. Prove the block-extension lemma suggested by the embedded-rank experiments: a lower-bound-saturating design in `M_d` should embed into `M_(d+1)` and be completable with exactly
   `floor((d+1)^2/2)-floor(d^2/2)`
   additional generic-mixing square faces.
4. Replace the current existential second-anchor construction by a publication-clean explicit deterministic family or a short standard theorem citation plus proof-specialized corollary.
5. Establish exact finite-field certificates for the current lower-bound-saturating `d=6,7` designs if they are retained as evidence.
6. Determine whether square-only lower-bound saturation holds for all `d`, or whether braid faces are required in some dimensions.
7. Establish conditioning bounds; identifiability and numerical stability remain separate claims.
8. Characterize kernels of deficient face designs.
9. Audit the full construction against Lindbladian learning/process tomography and channel-holonomy literature.

## Longer-range analytical obligations

1. Universal monotonicity of reduced curvature under successive CP reductions is not proved.
2. Infinite-dimensional extension with unbounded GKSL generators remains open.
3. Equality with any standard decoherence/information-loss monotone is not established.
4. A general operational interpretation in terms of channel capacity, entropy production, or recoverability is not established.
5. No physical gauge/spacetime curvature claim is made.
6. Non-Markovian/process-tensor generalization is deferred.

## Claim firewall

Do not state without proof that:

- finite closed-loop holonomies identify an arbitrary UCP channel;
- local Lindblad identifiability contradicts the finite-time channel no-go;
- `||H||`, `||H-I||`, or `||Delta||` is monotone under further UCP reductions;
- reduced order holonomy is a decoherence monotone;
- the exact lower-bound count `floor(d^2/2)` is proved for all dimensions;
- the `2d^2` upper bound is sharp;
- numerical full rank for `d=6,7` is already an exact theorem;
- the construction defines physical gauge or spacetime curvature.
