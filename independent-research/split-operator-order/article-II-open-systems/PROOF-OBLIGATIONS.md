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
- Strong finite-channel no-go: complete closed-loop holonomy data can fail to identify a UCP channel (depolarizing sign ambiguity).
- Full bilinear `Gamma_L` determines a bounded generator on `M_d` modulo Hamiltonian derivations.
- General finite-dimensional rank criterion: a first-order contextual-loop design is universally dissipatively identifiable iff its real measurement map has rank `(d^2-1)^2`.
- If the rank is deficient, two distinct positive-definite Kossakowski matrices can be chosen in the same measurement fibre; rank deficiency is therefore physical, not merely algebraic, non-identifiability.
- Complete qubit theorem: the Article-I braid plus two backtracking loops identify all nine real dissipative parameters modulo Hamiltonian derivations; an exact `9 x 9` minor has determinant `3932160 = 2^18*3*5`.
- Exact qutrit theorem: four declared Coxeter faces give full rank `64` and are information-theoretically minimal.
- Exact minimal Coxeter-face designs for `d=3,4,5`, each saturating the matrix-valued face-count lower bound.
- Generic open-dense full-rank consequence for the certified `d=3,4,5` face templates.
- All-d Weyl generator-defect theorem: two generator-direction defect families determine every bounded unital *-preserving generator on `M_d(C)` modulo Hamiltonian derivations.
- All-d generalized flat-loop tomography upper bound: at most `3d^2-1` matrix-valued closed-loop coefficients suffice.
- All-d engineered Coxeter-square lemma: arbitrary target edge transports `U,V in SU(d)` can be realized as the first two contextual transports of an Article-I commuting-transposition square face.
- All-d backtracking-as-degenerate-braid lemma: every target `U in SU(d)` can be realized as the nontrivial edge transport of an adjacent-swap braid face with the remaining gate equal to the identity, using Gotô commutator surjectivity.
- Anchored-square quotient-invariance theorem: vanishing backtracking and square defects for two dense anchors makes the generator class modulo derivations invariant under `PSU(d)`.
- Representation-theoretic reduction theorem: the only `PSU(d)`-fixed quotient direction is the isotropic depolarizing direction; Weyl backtracking removes it.
- All-d Coxeter tomography upper bound: at most `3d^2-1` adjacent-transposition braid/square face coefficients identify every bounded dissipative generator on `M_d(C)` modulo Hamiltonian derivations.
- Combined with the dimension lower bound `ceil((d^2-1)^2/(2d^2))`, matrix-valued Coxeter tomography has optimal asymptotic order `Theta(d^2)` for every finite `d`.

## Immediate open obligations

1. Integrate the all-d Coxeter theorem into the main LaTeX manuscript with stable theorem numbering and explicit citations for Gotô commutator surjectivity and dense two-generation of semisimple Lie groups.
2. Prove or refute the sharper all-d Coxeter conjecture:
   `L_d^Cox = ceil((d^2-1)^2/(2d^2))`
   for every `d>=3`.
3. Close the constant-factor gap between the proved all-d Coxeter upper bound `3d^2-1` and the universal matrix-valued lower bound `~d^2/2`.
4. Determine whether the exact lower bound can be achieved by square-only designs, braid-only designs, or necessarily mixed Coxeter designs in arbitrary dimension.
5. Establish explicit conditioning bounds for the all-d anchored construction; identifiability and numerical stability remain distinct claims.
6. Replace existence-only dense anchors by an explicit deterministic family `S_1(d),S_2(d)` with proved dense generation or an equally strong finite spanning property.
7. Characterize the kernel of first-order holonomy measurement maps for deficient designs.
8. Determine which anchored/open-path observables remove finite-channel ambiguities such as the depolarizing sign obstruction.
9. Construct the smallest explicit example of finite-loop cancellation with nonzero individual multiplicativity defects.
10. Audit the loop-defect/context-reduction construction against operator-algebra, Lindbladian-learning, process-tomography, noiseless-subsystem, quantum-error-correction, and channel-holonomy literature.

## Longer-range analytical obligations

1. Universal monotonicity of reduced curvature under successive CP reductions is **not proved** and should not be assumed.
2. Infinite-dimensional extension with unbounded GKSL generators requires explicit common invariant domains and differentiation hypotheses.
3. Equality between reduced order curvature and any standard decoherence or information-loss monotone is not established.
4. A general operational interpretation in terms of channel capacity, entropy production, or recoverability is not established.
5. No universal relation to physical gauge curvature or spacetime curvature is claimed.
6. No theorem states that every dissipative semigroup produces nonzero order curvature.
7. Non-Markovian/process-tensor generalization is deferred until the Markovian bounded theory is closed.

## Falsification / weakening criteria

The stronger sharp-count programme must be weakened if:

- the lower-bound-saturating Coxeter conjecture fails in some dimension;
- all-d full-rank designs exist but require increasingly poor conditioning;
- the anchored construction cannot be made deterministic without substantial extra structure;
- literature audit finds the same Coxeter-holonomy inverse problem and its all-d solution already established in equivalent form.

The bounded all-d `Theta(d^2)` Coxeter theorem itself is no longer contingent on the sharp-count conjecture.

## Claim firewall

Do not state without proof that:

- finite closed-loop holonomies identify an arbitrary UCP channel;
- the finite-time channel no-go is contradicted by local Lindblad identifiability;
- `||H||`, `||H-I||`, or `||Delta||` is monotone under further UCP reductions;
- nonunitarity alone destroys contextual flatness;
- reduced order holonomy is a decoherence monotone;
- the Stinespring complement is a physical environment observable without specifying the dilation model;
- the qubit/qutrit rank theorems are already experimental tomography protocols;
- the exact information-theoretic Coxeter lower-bound count is proved for all dimensions;
- the upper bound `3d^2-1` is sharp;
- the construction defines physical gauge or spacetime curvature.
