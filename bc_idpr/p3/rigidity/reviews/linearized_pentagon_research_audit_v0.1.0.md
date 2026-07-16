# BC-IDPR-P3-A-01 — Linearized Pentagon Research Audit

**Status:** internal research consultation, v0.1.0  
**Scope:** exact Jacobian stage only; gauge quotient remains open.

## 1. Result under review

The declared Ising fusion datum and standard real baseline yield 136 scalar pentagon residuals in 14 unit-normalized associator-entry variables. Exact symbolic differentiation over `Q(sqrt(2))` gives

- 95 zero linearized rows;
- 41 nonzero linearized rows;
- 35 projectively distinct nonzero rows;
- exact rank 11;
- kernel dimension 3.

The rank is unchanged by removing zero rows and projective duplicates. A second directional coefficient extraction verifies the Jacobian action on a preregistered integer direction.

## 2. Literature consultation

Etingof–Nikshych–Ostrik prove generalized Ocneanu rigidity: fusion categories and tensor functors over characteristic zero are undeformable up to equivalence at fixed fusion datum. Bartlett gives a graphical route to Ocneanu rigidity. These results support the expectation that the three-dimensional raw pentagon kernel should be exhausted by gauge directions, but they do not replace the declared finite computation.

Primary references:

1. P. Etingof, D. Nikshych, V. Ostrik, *On fusion categories*, Annals of Mathematics 162 (2005), arXiv:math/0203060.
2. B. Bartlett, *Fusion categories via string diagrams*, Communications in Contemporary Mathematics 18 (2016), arXiv:1502.02882.

## 3. Reviewer assessment

### Strengths

- The residual list is generated from all admissible four-object fusion configurations rather than a hand-selected equation subset.
- Arithmetic is exact over the algebraic field required by the Ising `1/sqrt(2)` entries.
- Rank stability is checked against two deterministic row reductions.
- The Jacobian is independently spot-checked by extracting the coefficient of an auxiliary epsilon along a fixed integer direction.
- The raw kernel basis is explicitly machine-readable.

### Open obligations

1. Construct the trivalent-basis gauge map `DG` in the same variable ordering.
2. Verify exactly that `DP * DG = 0`.
3. Certify `rank(DG) = 3` and `im(DG) = ker(DP)`.
4. Audit whether the chosen unit normalization removes all unit-related gauge directions without overconstraining the complex.
5. Add a second implementation or manually derived basis comparison for the gauge image.

## 4. Claim firewall

The present computation establishes only

`dim ker(DP) = 3`

for the declared finite coordinate complex. It does not yet establish local rigidity because the quotient by gauge has not been computed. It also does not identify this coordinate kernel with Davydov–Yetter cohomology without an explicit convention comparison.

## 5. Decision

**Accept the Jacobian stage.** Proceed immediately to `build_gauge_tangent.py`. Do not publish a zero-dimensional deformation claim until image-kernel equality is certified.
