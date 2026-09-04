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
- Exact dephasing calculation on the six-edge contextual braid loop inherited from Article I.
- Closed benchmark formulas for dephasing, depolarization, and amplitude damping.
- Transport-operator-system restriction ceiling for channel identifiability.
- Strong finite-channel no-go: complete closed-loop holonomy data can fail to identify a UCP channel (depolarizing sign ambiguity).
- Full bilinear `Gamma_L` determines a bounded generator on `M_d` modulo Hamiltonian derivations.
- Finite qubit reconstruction theorem: six first-order backtracking/braid scalars recover the six real symmetric Kossakowski parameters with determinant `8192`.
- For the Article-I braid design, all local right/left backtracking coefficients have rank `5`, while adding braid information raises the rank to `6`.

## Immediate open obligations

1. Derive the explicit inverse reconstruction formulas `c=M^{-1}m` in publication notation and audit numerical conditioning.
2. Determine the minimal subset of contextual edges/face coefficients needed for full-rank qubit dissipator identification.
3. Optimize the transport tuple for the smallest singular value of the holonomy measurement map.
4. Characterize the kernel of the first-order holonomy measurement operator for a fixed transport design.
5. Find sufficient conditions for full dissipative identifiability in `M_d`, `d>2`, in terms of the span of sampled `Gamma_L(X,Y)` pairs.
6. Determine which anchored/open-path observables remove finite-channel ambiguities such as the depolarizing sign obstruction.
7. Construct the smallest explicit example of loop-defect cancellation with nonzero individual multiplicativity defects.
8. Determine sufficient conditions under which vanishing of all elementary Coxeter-face reduced holonomies forces multiplicativity on the generated transport algebra.
9. Audit the loop-defect/context-reduction construction against operator-algebra, Lindbladian-learning, process-tomography, noiseless-subsystem, quantum-error-correction, and channel-holonomy literature.

## Longer-range analytical obligations

1. Universal monotonicity of reduced curvature under successive CP reductions is **not proved** and should not be assumed.
2. Infinite-dimensional extension with unbounded GKSL generators requires explicit common invariant domains and differentiation hypotheses.
3. Equality between reduced order curvature and any standard decoherence or information-loss monotone is not established.
4. A general operational interpretation in terms of channel capacity, entropy production, or recoverability is not established.
5. No universal relation to physical gauge curvature or spacetime curvature is claimed.
6. No theorem states that every dissipative semigroup produces nonzero order curvature.
7. Non-Markovian/process-tensor generalization is deferred until the Markovian bounded theory is closed.

## Falsification criteria

The partial-context programme must be weakened or closed if:

- proposed curvature quantities depend primarily on arbitrary representation choices rather than the declared reduction;
- the exact semigroup defect calculus gives no information beyond standard Schwarz defects once applied to nontrivial Coxeter loops;
- no stable full-rank measurement design exists beyond the current qubit example;
- identifiability disappears under small perturbations because the measurement matrix is generically ill-conditioned;
- no invariant or operationally interpretable quantity survives changes of minimal Stinespring realization;
- a literature audit finds the complete loop-defect/context-reduction construction already known in an equivalent form, leaving no substantive operator-order specialization.

## Claim firewall

Do not state without proof that:

- finite closed-loop holonomies identify an arbitrary UCP channel;
- `||H||`, `||H-I||`, or `||Delta||` is monotone under further UCP reductions;
- nonunitarity alone destroys contextual flatness;
- reduced order holonomy is a decoherence monotone;
- the Stinespring complement is a physical environment observable without specifying the dilation model;
- the qubit rank-6 theorem is already an experimental tomography protocol;
- the construction defines physical gauge or spacetime curvature.
