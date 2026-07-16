# BC-IDPR-P3-A-01 — Gauge Quotient Research Audit

**Status:** internal mathematical and computational review, v0.1.0  
**Date:** 2026-07-16  
**Scope:** final P3-A-M1 gauge-quotient stage for the declared `SU(2)_2 / Ising` coordinate complex.

## 1. Reviewed claim

The reviewed claim is deliberately relative:

> For the fixed Ising fusion datum, the declared standard real associator baseline, strict unit normalization, the complete enumerated pentagon system, and the declared trivalent-basis gauge action, the linearized deformation quotient is zero.

Equivalently,

\[
\ker D\mathcal P_{F^{(0)}}=\operatorname{im}D\mathcal G_{F^{(0)}},
\qquad
\dim H^3_{\mathrm{lin}}(F^{(0)})=0.
\]

This is not presented as a new proof of generalized Ocneanu rigidity and is not automatically identified with a standard Davydov–Yetter cohomology group.

## 2. Exact computation

The coordinate dimensions and ranks are:

\[
\dim C^2=14,
\qquad
\dim C^1_{\mathrm{unit\ normalized}}=5,
\]

\[
\operatorname{rank}D\mathcal P=11,
\qquad
\dim\ker D\mathcal P=3,
\]

\[
\operatorname{rank}D\mathcal G=3,
\qquad
\dim\ker D\mathcal G=2.
\]

The exact complex condition holds:

\[
D\mathcal P\,D\mathcal G=0.
\]

The combined matrix formed from a basis of `ker(DP)` and the columns of `DG` has rank three. Since `rank(DG)=3`, this proves

\[
\operatorname{im}D\mathcal G=\ker D\mathcal P.
\]

Therefore

\[
\dim\left(\ker D\mathcal P/\operatorname{im}D\mathcal G\right)=0.
\]

All ranks and identities are computed exactly over `Q(sqrt(2))`; no floating-point rank threshold is used.

## 3. Gauge-parameter audit

Strict unit normalization fixes all trivalent basis changes with the tensor unit in an input position. The five surviving gauge parameters are

1. `chi[sigma,sigma->1]`;
2. `chi[sigma,sigma->psi]`;
3. `chi[sigma,psi->sigma]`;
4. `chi[psi,sigma->sigma]`;
5. `chi[psi,psi->1]`.

Their action on the fourteen associator variables has rank three. The two-dimensional kernel of `DG` is a stabilizer of the selected F-coordinate presentation: two independent combinations of trivalent rescalings act trivially on every retained associator coordinate.

This stabilizer is recorded rather than quotiented away silently. It must not be called a categorical deformation direction.

## 4. Independent verification channels

### 4.1 Full nonlinear symbolic gauge check

The baseline was transformed by arbitrary nonzero symbolic multiplicative parameters `u0,...,u4` using the declared finite gauge rule. All 136 scalar pentagon residuals were recomputed as rational functions of these parameters.

Result:

\[
136/136
\]

residuals vanish identically. This verifies the convention and signs of the gauge action independently of the linearized matrix identity.

### 4.2 First-order finite-gauge check

For the preregistered direction

\[
(2,-1,3,-2,1),
\]

the finite exponential gauge transformation was differentiated directly at `t=0`. The resulting fourteen-component variation agrees exactly with `DG` applied to the same direction.

### 4.3 Explicit kernel lifts

Every vector in the stored basis of `ker(DP)` has an explicit exact preimage under `DG`. Canonical representatives obtained by setting stabilizer parameters to zero are stored in the certificate. This is stronger than a rank-only comparison and directly demonstrates that each raw pentagon-preserving tangent is gauge.

## 5. Literature consultation

The result is consistent with the generalized Ocneanu rigidity theorem of Etingof, Nikshych and Ostrik, which states undeformability of fusion categories and tensor functors over characteristic zero at fixed fusion data. Bartlett provides a graphical proof route to Ocneanu rigidity.

Primary references:

1. P. Etingof, D. Nikshych, V. Ostrik, *On fusion categories*, Annals of Mathematics 162 (2005), arXiv:math/0203060.
2. B. Bartlett, *Fusion categories via string diagrams*, Communications in Contemporary Mathematics 18 (2016), arXiv:1502.02882.

The literature is used as an expectation and consistency check, not as a substitute for the finite certificate.

## 6. Reviewer concerns and resolutions

### Concern A — sign or inverse error in the gauge formula

**Resolution:** the arbitrary symbolic finite-gauge pentagon audit passes for all 136 residuals. A convention error would generically violate this test.

### Concern B — accidental equality from rank counting alone

**Resolution:** `DP DG=0` is checked entrywise, the combined span rank is checked, and explicit gauge lifts are produced for every stored kernel vector.

### Concern C — hidden floating-point rank ambiguity

**Resolution:** all matrices live in exact algebraic arithmetic over `Q(sqrt(2))`.

### Concern D — unit normalization may conceal degrees of freedom

**Resolution:** the certificate is explicitly relative to strict unit normalization. Unit-related basis changes are not counted as variables or gauges. A comparison with a fully unnormalized monoidal complex would be useful as a later robustness audit, but it is not required for the declared relative claim.

### Concern E — overclaiming categorical cohomology

**Resolution:** the notation `H^3_lin` remains operational. No identification with Davydov–Yetter cohomology is asserted without a separate convention theorem.

## 7. Verdict

**Accept P3-A-M1.**

The finite Ising anchor receives status

`LOCALLY_RIGID_IN_DECLARED_COMPLEX`.

The zero quotient is certified by exact arithmetic and three independent structural checks. P3-A can now serve as the negative-control channel for P3-B.

## 8. Publication firewall

The accepted result does not imply:

- global rigidity of every `SU(2)_k` realization;
- rigidity under changes of fusion rules, object set, pivotal structure, braiding, or modular data;
- impossibility of a nontrivial generic-q operator derivative;
- identification of q-variation with a deformation inside the fixed Ising fusion category;
- any direct physical conclusion.

## 9. Recommended next operation

Begin `BC-IDPR-P3-B-01`: construct a finite generic-q operator family near the `k=2` anchor and compute the intrinsic derivative margin after projection away from normalization, basis and representation-scale nuisance directions.

The central comparison is now well posed:

\[
H^3_{\mathrm{lin}}(F^{(0)})=0
\quad\text{while testing whether}\quad
P_{\mathcal N^\perp}\,\partial_qD_J(q_2)\neq0.
\]
