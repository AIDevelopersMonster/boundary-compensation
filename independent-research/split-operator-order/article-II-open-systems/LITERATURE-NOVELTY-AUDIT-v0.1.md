# Article II — literature and novelty audit v0.1

## Status

`PARTIAL / SPECIALIST PRIORITY AUDIT STILL REQUIRED`

This note separates classical infrastructure from the candidate contribution of the Split Operator Order Article II manuscript.

## Classical infrastructure — do not claim as new

### Stinespring dilation

W. F. Stinespring, *Positive Functions on C*-Algebras*, Proceedings of the American Mathematical Society 6 (1955), 211–216. DOI: `10.1090/S0002-9939-1955-0069403-4`.

Use: every CP map admits a dilation of the form `Phi(X)=V* pi(X)V`; the manuscript's leakage identity is a direct algebraic consequence of this representation.

### Schwarz inequality and multiplicative domain

M.-D. Choi, *A Schwarz Inequality for Positive Linear Maps on C*-Algebras*, Illinois Journal of Mathematics 18 (1974), 565–574. DOI: `10.1215/ijm/1256051007`.

Use: the multiplicative domain and equality cases of the Schwarz inequality are classical. The two-sided unitary backtracking test in the manuscript is a specialization/repackaging for the operator-order loop language, not a new multiplicative-domain theorem.

### GKSL/Lindblad generators

G. Lindblad, *On the Generators of Quantum Dynamical Semigroups*, Communications in Mathematical Physics 48 (1976), 119–130. DOI: `10.1007/BF01608499`.

V. Gorini, A. Kossakowski, E. C. G. Sudarshan, *Completely Positive Dynamical Semigroups of N-Level Systems*, Journal of Mathematical Physics 17 (1976), 821–825. DOI: `10.1063/1.522979`.

Use: the bounded generator form is standard.

### Quantum-channel multiplicative domains

M. Rahaman, *Multiplicative Properties of Quantum Channels*, arXiv:1701.06205.

Use: modern structure of multiplicative domains, multiplicative index, and channel applications is established literature.

### Carré du champ / quantum Markov semigroups

Noncommutative carré-du-champ forms for quantum Markov semigroups are established. One modern reference is *Curvature-Dimension Conditions for Symmetric Quantum Markov Semigroups*, Annales Henri Poincaré (2023), DOI `10.1007/s00023-022-01220-x`.

The manuscript uses

`Gamma_L(X,Y)=L(XY)-L(X)Y-X L(Y)`

with a sign convention adapted to multiplicativity defects. For `X=A*`, `Y=A`, this is the positive Schwarz-defect production form under the manuscript's generator convention. It should not be advertised as a new carré-du-champ construction.

## Candidate contribution — narrow claim

Subject to a deeper specialist search, the paper's candidate contribution is the following synthesis:

1. start with the exactly flat contextual operator-order transport from Article I;
2. reduce each edge by a declared UCP map;
3. express the resulting loop holonomy exactly as a sum of transported multiplicativity defects;
4. resolve multiplicativity loss exactly across a chain of context reductions using

   `Delta_{Psi o Phi}=Psi(Delta_Phi)+Delta_Psi(Phi(.),Phi(.))`;

5. for a uniformly continuous UCP semigroup, derive an exact Duhamel representation of the multiplicativity defect in terms of the GKSL Leibniz defect;
6. insert that exact integral into the loop decomposition, obtaining an exact reduced-order-holonomy formula;
7. evaluate the construction on contextual Coxeter loops inherited from Article I rather than on arbitrary unrelated products.

## Claims currently forbidden

- that the multiplicativity defect itself is new;
- that the multiplicative domain itself is new;
- that Stinespring leakage is a new dilation theorem;
- that the GKSL Leibniz/carré-du-champ identity is new;
- that reduced order holonomy equals entropy production, channel capacity loss, recoverability defect, or a standard decoherence monotone;
- that dissipation generically or necessarily creates nonzero curvature;
- that the construction is physical gauge or spacetime curvature.

## Priority questions still requiring search

1. Has an exact product-loop decomposition into multiplicativity defects been used previously in CP-map/operator-algebra literature?
2. Has the composition identity for multiplicativity defects been organized as a layer-resolved information-loss calculus?
3. Has the exact semigroup Duhamel identity for the Schwarz/multiplicativity defect been explicitly coupled to loop holonomy?
4. Are there existing notions of channel holonomy/path dependence that are mathematically equivalent to the present reduced product?
5. Does quantum error correction/noiseless-subsystem literature already identify the same loop criterion through multiplicative domains?

Until these are answered, publication language should use `we derive`, `in this operator-order setting`, and `candidate new synthesis`, not `first`, `new theory`, or `novel invariant` without qualification.
