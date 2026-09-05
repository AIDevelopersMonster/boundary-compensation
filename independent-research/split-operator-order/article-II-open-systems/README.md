# Article II — Open Systems / Context Reduction

**Working title:** *Context Reduction in Open Quantum Systems: Multiplicativity Defects, Lindblad Order Holonomy, and Sharp Coxeter Tomography*  
**Current milestone:** `v0.2.0 / REVIEWED_CLEAN / RENDER_AUDIT_PENDING`  
**Author:** Malachevsky, A.A.  
**ORCID:** 0009-0008-6009-3196

Article II develops the open-system continuation of the split-operator-order programme. The central mechanism is not nonunitarity by itself, but loss of the multiplicative context required by the exactly flat contextual transport of Article I.

## Publication-consolidation manuscript

Current manuscript:

`manuscript-v0.2.0-en.md`

It consolidates the bounded analytical core, the finite-dimensional inverse problem, and the audited sharp Coxeter theorem.

## Exact open-system core

For a UCP map `Phi:A->B`,

`Delta_Phi(X,Y)=Phi(XY)-Phi(X)Phi(Y)`.

For a flat contextual loop

`T_m...T_1=I`,

with reduced product

`H_Phi=Phi(T_m)...Phi(T_1)`, 

the exact loop decomposition is

`H_Phi-I`

`= -sum_(k=2)^m Phi(T_m)...Phi(T_(k+1)) Delta_Phi(T_k,P_(k-1))`.

The developed core also contains:

- the UCP norm certificate and multiplicative-domain flatness criterion;
- exact composition of multiplicativity defects under nested reductions;
- layer-resolved context-loss decomposition;
- two-sided backtracking/Schwarz defects;
- Stinespring leakage formula;
- exact semigroup evolution and Duhamel representation;
- bounded GKSL Leibniz defect

  `Gamma_L(X,Y)=sum_alpha [V_alpha^*,X][Y,V_alpha]`;

- exact integral representation of reduced Lindblad loop holonomy;
- explicit dephasing, depolarizing, and amplitude-damping braid-loop formulas.

## Inverse problem

Closed-loop finite-time holonomy does not identify an arbitrary UCP channel in general. At first order, however, the full bilinear `Gamma_L` determines a bounded finite-dimensional unital *-preserving generator modulo Hamiltonian derivations.

For `M_d(C)` the quotient dimension is

`N_d=(d^2-1)^2`.

A matrix-valued Coxeter face supplies at most `2d^2` real coordinates, giving

`L_d^Cox>=floor(d^2/2)`.

## Sharp Coxeter theorem

After adversarial proof audit and two explicit repairs, the lower bound is attained.

Within the declared bounded finite-dimensional first-order matrix-valued Coxeter-face measurement model,

`L_d^Cox=floor(d^2/2)`

for every `d>=3`.

The proof chain uses:

1. the structural scalar-one restriction quotient and extension-ready criterion;
2. centered odd-dimensional tangent geometry;
3. finite complete `H`-anchor compression;
4. cycle factorization of the compressed dependency determinant;
5. binder-compatible restricted transversality;
6. the reverse-cycle transverse native-tilt detector and singular-lift reconstruction;
7. all-odd extension-ready existence;
8. the repaired odd-to-even transfer constructed directly in `SL_n(C)`;
9. `SU(n)` Zariski density and engineered contextual-square realization.

The `d=2` obstruction concerns only minimal **extension-readiness** under scalar-one embedding and does not assert failure of native two-face tomography.

## Audit repairs

The publication audit found and repaired two genuine proof issues:

- ambient Zariski openness did not by itself imply intersection with the reverse-cycle-zero binder subspace;
- post hoc scalar determinant normalization is not rank-invariant after scalar-one embedding because `diag(cA,1)` is not a scalar multiple of `diag(A,1)`.

Repair notes:

- `../article-I/research/BINDER-COMPATIBLE-TRANSVERSALITY-REPAIR-v0.1.md`;
- `../article-I/research/ODD-TO-EVEN-TRANSFER-AUDIT-REPAIR-v0.1.md`.

Publication audit:

- `../article-I/research/SHARP-COXETER-PUBLICATION-AUDIT-2026-09-05.md`.

## Literature / novelty boundary

Current targeted audit:

`LITERATURE-NOVELTY-AUDIT-v0.2.md`.

Classical infrastructure is separated explicitly from the programme contribution: Stinespring dilation, Choi Schwarz/multiplicative-domain theory, GKSL/Lindblad generators, noncommutative carre-du-champ methods, and general Lindbladian/Liouvillian tomography are not novelty claims.

The reduced product defect used here is also distinguished from the Jamiołkowski/Uhlmann-type *holonomy for quantum channels* literature.

Publication language remains deliberately narrow: `we derive`, `we prove in the present operator-order setting`, and `the contribution is the coupling of these structures`.

## Reproducibility

The `examples/` directory contains deterministic builders/checks for:

- braid-loop channel formulas;
- qubit first-order identifiability;
- exact qutrit rank certification;
- exact `d=4` finite-field rank certification;
- exact `d=5` finite-field rank certification.

The `d=5` builder reconstructs the full `600 x 576` matrix modulo `1000033` and certifies rank `576`. The all-dimensional theorem itself is algebraic and does not depend on extrapolating low-dimensional numerical evidence.

## Historical notes

The earlier constructive bounds

`L_d^Cox<=3d^2-1`

and

`L_d^Cox<=2d^2`

remain valid constructions but are no longer the best face-count theorem. Earlier notes describing the sharp count as a conjecture are retained as historical research checkpoints and are superseded by the audited proof chain.

See `LEGACY-STATUS-v0.2.md`.

## Claim firewall

Do not infer from the current results:

- finite-time channel identifiability from closed loops;
- conditioning or statistical efficiency;
- robustness to SPAM/noise;
- universal monotonicity under further CP reductions;
- equivalence with entropy production, recoverability, capacity loss, or a standard decoherence monotone;
- infinite-dimensional unbounded-generator results;
- physical spacetime or gauge curvature.

## Current publication gate

Mathematical existence blockers: none currently identified.

Targeted related-work/claim-boundary audit: complete.

Author and ORCID: verified.

Repository licence: MIT at repository level.

Article-specific Zenodo DOI: not yet assigned.

Final LaTeX/source compilation and PDF visual inspection: pending.

**Current release status:** `REVIEWED_CLEAN`.
