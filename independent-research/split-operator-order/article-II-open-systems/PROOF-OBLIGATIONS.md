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
- If the rank is deficient, two distinct positive-definite Kossakowski matrices can be chosen in the same measurement fibre; thus rank deficiency is a physical, not merely algebraic, non-identifiability.
- Complete qubit theorem: the Article-I braid plus two backtracking loops identify all nine real dissipative parameters modulo Hamiltonian derivations; an exact `9 x 9` minor has determinant `3932160 = 2^18*3*5`.
- The older six-parameter real-symmetric Kossakowski theorem remains valid only as a restricted bistochastic/unital subclass result.
- Exact qutrit theorem: four declared Coxeter faces give a `72 x 64` rational measurement matrix of rank `64`, hence identify the complete qutrit dissipative generator modulo Hamiltonian derivations.
- The qutrit four-face design is information-theoretically minimal among general matrix-valued face designs because `3*18<64`.
- Exact modular certificate: reduction modulo prime `1000003` has rank `64`, proving full rational column rank.
- Generic qutrit consequence: for the same four-face template, full rank holds on a nonempty open dense subset of `U(3)^4`.

## Immediate open obligations

1. Integrate the complete qubit and qutrit rank theorems into the main LaTeX manuscript with stable theorem numbering and exact proof appendices.
2. Determine whether, for every `d`, there exists a universal Coxeter-face template with `O(d^2)` loops attaining full rank `(d^2-1)^2`.
3. Determine the sharp asymptotic minimum number of face/backtracking loop families needed for generic dissipative identification in `M_d`.
4. Characterize the kernel of the first-order holonomy measurement operator for a fixed transport design when rank is deficient.
5. Optimize transport tuples for the smallest singular value of the measurement map; identifiability and numerical conditioning must remain separate claims.
6. Determine which anchored/open-path observables remove finite-channel ambiguities such as the depolarizing sign obstruction.
7. Construct the smallest explicit example of loop-defect cancellation with nonzero individual multiplicativity defects.
8. Determine sufficient conditions under which vanishing of all elementary Coxeter-face reduced holonomies forces multiplicativity on the generated transport algebra.
9. Audit the loop-defect/context-reduction construction against operator-algebra, Lindbladian-learning, process-tomography, noiseless-subsystem, quantum-error-correction, and channel-holonomy literature.
10. Decide whether backtracking-only designs have a general rank ceiling; current low-dimensional evidence is dimension-dependent and does not support a universal `d^2-1 backtracks suffice` theorem.

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
- no stable full-rank measurement design exists beyond dimensions `d=2,3`;
- higher-dimensional full-rank designs require factorially many contextual loops or become generically singular;
- identifiability disappears under small perturbations because the measurement matrix is generically ill-conditioned;
- no invariant or operationally interpretable quantity survives changes of minimal Stinespring realization;
- a literature audit finds the complete loop-defect/context-reduction construction already known in an equivalent form, leaving no substantive operator-order specialization.

## Claim firewall

Do not state without proof that:

- finite closed-loop holonomies identify an arbitrary UCP channel;
- the finite-time channel no-go is contradicted by local Lindblad identifiability;
- `||H||`, `||H-I||`, or `||Delta||` is monotone under further UCP reductions;
- nonunitarity alone destroys contextual flatness;
- reduced order holonomy is a decoherence monotone;
- the Stinespring complement is a physical environment observable without specifying the dilation model;
- the qubit/qutrit rank theorems are already experimental tomography protocols;
- four faces suffice for all dimensions;
- `d^2-1` backtracking loops universally suffice;
- the construction defines physical gauge or spacetime curvature.
