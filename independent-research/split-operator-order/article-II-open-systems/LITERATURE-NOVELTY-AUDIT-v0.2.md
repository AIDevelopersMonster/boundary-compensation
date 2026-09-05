# Article II — literature and novelty audit v0.2

**Date:** 2026-09-05  
**Author:** Malachevsky, A.A.  
**ORCID:** 0009-0008-6009-3196  
**Status:** `TARGETED_PRIORITY_AUDIT_COMPLETE / BROAD_PRIORITY_CLAIMS_FORBIDDEN`

## 1. Scope of this audit

This audit supports the publication candidate

*Context Reduction in Open Quantum Systems: Multiplicativity Defects, Lindblad Order Holonomy, and Sharp Coxeter Tomography*.

It does not claim an exhaustive priority search over all operator-algebra, quantum-information, control, and open-system literature. Its purpose is narrower:

1. verify the standard mathematical infrastructure used by the manuscript;
2. identify nearby uses of the word *holonomy* that must not be conflated with the present construction;
3. place the first-order generator-identifiability results against modern Lindblad/Liouvillian tomography and learning;
4. define publication-safe novelty language.

The publication claim ceiling remains the mathematics proved in the manuscript. No priority statement such as “first”, “unique”, or “new invariant” is licensed by this audit.

## 2. Verified classical infrastructure

### 2.1 Stinespring dilation

W. F. Stinespring, *Positive Functions on C*-Algebras*, Proceedings of the American Mathematical Society 6 (1955), 211–216. DOI: `10.1090/S0002-9939-1955-0069403-4`.

Use in Article II: a UCP map is written

`Phi(X)=V* pi(X)V`,

and the manuscript derives

`Delta_Phi(X,Y)=V* pi(X)(I-VV*)pi(Y)V`.

The dilation theorem is classical; only its insertion into the declared operator-order loop calculus is part of the manuscript synthesis.

### 2.2 Schwarz inequality and multiplicative domain

M.-D. Choi, *A Schwarz Inequality for Positive Linear Maps on C*-Algebras*, Illinois Journal of Mathematics 18 (1974), 565–574. DOI: `10.1215/ijm/1256051007`.

Use in Article II: two-sided backtracking defects for a unitary are the two Schwarz defects, and simultaneous vanishing is the standard multiplicative-domain equality condition.

The manuscript must not present the multiplicative domain itself as new.

### 2.3 GKSL/Lindblad generators

G. Lindblad, *On the Generators of Quantum Dynamical Semigroups*, Communications in Mathematical Physics 48 (1976), 119–130. DOI: `10.1007/BF01608499`.

V. Gorini, A. Kossakowski, E. C. G. Sudarshan, *Completely Positive Dynamical Semigroups of N-Level Systems*, Journal of Mathematical Physics 17 (1976), 821–825. DOI: `10.1063/1.522979`.

Use in Article II: the bounded Heisenberg-picture generator representation and its dissipative Kossakowski parametrization are standard. The identity

`Gamma_L(X,Y)=sum_alpha [V_alpha*,X][Y,V_alpha]`

is an elementary expansion of the standard generator and is not claimed as an independent new GKSL theorem.

### 2.4 Multiplicative properties of quantum channels

M. Rahaman, *Multiplicative Properties of Quantum Channels*, Journal of Physics A: Mathematical and Theoretical 50 (2017), 345302. DOI: `10.1088/1751-8121/aa7b57`; arXiv:`1701.06205`.

Use in Article II: modern multiplicative-domain structure and channel multiplicativity are established independent literature.

### 2.5 Noncommutative carré du champ

M. Wirth and H. Zhang, *Curvature-Dimension Conditions for Symmetric Quantum Markov Semigroups*, Annales Henri Poincaré 24 (2023), 717–750. DOI: `10.1007/s00023-022-01220-x`.

Article II uses a Leibniz-defect sign convention adapted to multiplicativity loss. For `X=A*`, `Y=A`, the resulting form is positive in the GKSL setting. This must be described as related to established noncommutative carré-du-champ machinery, not as a new curvature-dimension theory.

## 3. Existing channel holonomy is mathematically different

D. Kult, J. Åberg, and E. Sjöqvist, *Holonomy for Quantum Channels*, Physical Review A 77 (2008), 012114. DOI: `10.1103/PhysRevA.77.012114`; arXiv:`0711.2140`.

That work develops a holonomy for smoothly parametrized families of quantum channels using the Jamiołkowski representation, Uhlmann-type parallel transport, and an associated gauge structure.

Article II uses the term **reduced order holonomy** for a different object:

`H_Phi=Phi(T_m)...Phi(T_1)`

obtained by applying a declared UCP reduction edgewise to an exactly flat operator-order transport loop

`T_m...T_1=I`.

The two notions must be separated explicitly in the manuscript. Article II does not claim to reproduce, generalize, or supersede the Kult–Åberg–Sjöqvist channel holonomy. In particular, no Jamiołkowski/Uhlmann parallel-transport structure is assumed in the present definition.

Publication-safe wording:

> “Our reduced order holonomy is a product defect associated with edgewise reduction of an exactly flat operator-order loop. It should not be confused with geometric holonomies defined for smoothly parametrized families of quantum channels.”

## 4. Lindblad/Liouvillian learning and tomography boundary

The first-order inverse problem in Article II is one instance of a much broader active literature on learning open-system generators. The following nearby works were checked as boundary references.

### 4.1 Weakly dissipative many-body Liouvillian learning

T. Olsacher, T. Kraft, C. Kokail, B. Kraus, and P. Zoller, *Hamiltonian and Liouvillian learning in weakly-dissipative quantum many-body systems*, Quantum Science and Technology 10 (2025), 015065. DOI: `10.1088/2058-9565/ad9ed5`.

This work studies reconstruction of Hamiltonian and Liouvillian operator content from nonequilibrium quench dynamics in weakly dissipative many-body systems.

### 4.2 Non-Markovian Lindblad-like tomography

S. Varona, M. Müller, and A. Bermudez, *Lindblad-like quantum tomography for non-Markovian quantum dynamical maps*, npj Quantum Information 11 (2025), 96. DOI: `10.1038/s41534-025-01044-7`.

This is a time-local master-equation tomography framework allowing non-Markovian behavior. Article II does not claim comparable non-Markovian scope.

### 4.3 Shadow Lindblad tomography

R. T. Birke et al., *Demonstrating and Benchmarking Classical Shadows for Lindblad Tomography*, arXiv:`2602.14694` (2026).

This work concerns randomized/shadow measurement efficiency for Lindblad-parameter recovery on superconducting hardware. Article II contains no sample-complexity or hardware-efficiency theorem.

### 4.4 Ansatz-free arbitrary Lindbladian learning

N. Romanov, P. Ivashkov, W. Gong, I. Kannan, A. Gu, H.-Y. Hu, and S. F. Yelin, *Learning Arbitrary Lindbladians with Quantum Error Correction*, arXiv:`2606.18188` (2026).

This is an ansatz-free Lindbladian-learning framework with precision/scaling results and quantum-error-correction primitives. Article II does not compete with that task formulation.

## 5. Publication-safe novelty boundary

The manuscript may claim that, **in the declared operator-order setting**, it derives and proves the following combined structure:

1. an exact telescoping decomposition of reduced loop defect into transported multiplicativity defects;
2. an exact composition law that resolves multiplicativity loss layer by layer under nested reductions;
3. an exact Stinespring representation of the same defect and a backtracking leakage interpretation;
4. an exact Duhamel insertion of the GKSL Leibniz defect into reduced loop holonomy for uniformly continuous UCP semigroups;
5. explicit exact Coxeter-loop channel fingerprints for dephasing, depolarization, and amplitude damping;
6. a separation between finite-channel loop-only non-identifiability and infinitesimal generator identifiability modulo Hamiltonian derivations;
7. a finite-dimensional Coxeter-loop measurement theory with quotient dimension `(d^2-1)^2`;
8. information-theoretically minimal first-order Coxeter designs in every dimension `d>=3`, with sharp face count

   `L_d^Cox=floor(d^2/2)`.

The last item is a theorem of the present programme, not a claim that general Lindbladian tomography requires this number of experiments. It applies only to the declared matrix-valued first-order Coxeter-face measurement model.

## 6. Claims that remain forbidden

Do not state that:

- the multiplicativity defect, multiplicative domain, Stinespring dilation, GKSL form, or carré-du-champ construction is new;
- reduced order holonomy is the same as the established channel holonomy of Kult–Åberg–Sjöqvist;
- reduced order holonomy is a physical spacetime or gauge curvature;
- the sharp Coxeter face count is a universal lower bound for arbitrary quantum process tomography or arbitrary Lindbladian learning protocols;
- algebraic identifiability implies good conditioning, sample efficiency, or robustness to SPAM/noise;
- the finite-time channel no-go contradicts generator tomography;
- the construction supersedes recent Lindblad/Liouvillian learning algorithms.

## 7. Remaining source work

A broader specialist search could still find prior appearances of individual algebraic identities, especially the loop telescoping identity or semigroup defect Duhamel formula. Therefore priority language remains conservative even after this targeted audit.

Recommended manuscript wording is `we derive`, `we prove in the present operator-order setting`, and `the contribution here is the coupling of these structures`, rather than `we introduce the first` or `we discover a new invariant`.

## 8. Audit conclusion

The enlarged Article-II claim set is compatible with the checked literature provided the manuscript preserves the boundaries above.

No searched source was identified as stating the same sharp finite-dimensional Coxeter-face theorem in the present operator-order measurement model. This is **not** an exhaustive priority proof and must not be converted into a universal novelty claim.

**Literature-audit status:** `REVIEWED_CLEAN` for citation boundary and claim discipline, subject to final bibliography formatting and DOI/link checks in the compiled source.
