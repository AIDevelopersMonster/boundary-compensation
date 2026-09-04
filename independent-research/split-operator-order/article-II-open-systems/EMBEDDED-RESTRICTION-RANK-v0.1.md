# Structural embedded-rank ceiling for minimal Coxeter designs

**Article II research note — v0.1**  
**Author:** Malachevsky, A.A.  
**ORCID:** 0009-0008-6009-3196  
**Status:** `PROVED_RESTRICTION_QUOTIENT_CEILING / ATTAINABILITY_SEPARATE`

## 1. Purpose

The block-extension experiments revealed a stable parity pattern for the rank of a lower-dimensional Coxeter design after the embedding

`M_d(C) -> M_(d+1)(C),  X -> X direct-sum 1`.

The purpose of this note is to prove the structural ceiling behind that pattern. This separates two questions that had previously been mixed together:

1. **How much information can any embedded old-face family possibly carry?**
2. **Does there exist a minimal design that actually attains that ceiling?**

The first question is answered completely here. The second is the remaining extension-ready existence problem.

Throughout, put

`n=d+1`,

`A_n=M_n(C)`,

and let

`B=M_d(C) direct-sum C`

be the block-diagonal subalgebra of `A_n`.

## 2. Old embedded faces factor through the block-diagonal restriction

Every old contextual transport embedded from dimension `d` has the form

`T -> T direct-sum 1`

and therefore belongs to `B`.

Let `D:A_n->A_n` be a complex-linear unital `*`-preserving infinitesimal generator difference. Every first-order old-face coefficient is built only from values of `D` on products of those embedded transports. Since `B` is a subalgebra, all such products remain in `B`.

Hence the entire embedded old-face measurement map factors through

`D |-> D|_B`.

Consequently, the embedded rank is bounded by the dimension of the quotient of normalized `*`-preserving maps `B->A_n` modulo restricted Hamiltonian derivations.

## 3. Dimension of the restriction quotient

### Theorem 3.1 — restriction-quotient dimension

Let `C(B,A_n)` be the real vector space of complex-linear `*`-preserving maps

`D:B->A_n`

with `D(I)=0`. Let `Der_*(B,A_n)` be the subspace obtained by restricting Hamiltonian derivations of `A_n` to `B`. Then

`dim_R C(B,A_n) / Der_*(B,A_n)`

is exactly

`R_res(d)=(d^2-1)n^2+2`.

#### Proof

The Hermitian part of `B=M_d(C) direct-sum C` has real dimension

`d^2+1`.

A complex-linear `*`-preserving map is determined by its values on Hermitian inputs, and those values are arbitrary Hermitian `n x n` matrices. Imposing `D(I)=0` removes one Hermitian input direction. Therefore

`dim_R C(B,A_n)=d^2 n^2`.

Every `*`-derivation from the finite-dimensional C*-algebra `B` into `A_n`, with the bimodule structure induced by the block embedding, is inner. Thus it has the form

`delta_H(b)=i[H,b]`,

with `H=H^* in A_n`.

The kernel of

`H |-> i[H, . ]|_B`

is the Hermitian commutant of `B`. Since

`B'={lambda I_d direct-sum mu : lambda,mu in C}`,

its Hermitian part has real dimension `2`. Hence

`dim_R Der_*(B,A_n)=n^2-2`.

Subtracting gives

`d^2 n^2-(n^2-2)=(d^2-1)n^2+2`.

QED.

## 4. The full-to-restricted quotient map is surjective

### Lemma 4.1 — restriction surjectivity modulo derivations

The restriction map from the full dissipative quotient on `A_n` onto the quotient in Theorem 3.1 is surjective.

#### Proof

Take any normalized `*`-preserving map `D_B:B->A_n`. On Hermitian parts this is a real-linear map from `Herm(B)` to `Herm(A_n)` vanishing on `I`. Extend it arbitrarily to a real-linear map on `Herm(A_n)`, still vanishing on `I`, and then complexify. This gives a complex-linear `*`-preserving extension `D:A_n->A_n`.

Restriction sends full Hamiltonian derivations to restricted Hamiltonian derivations, so the same argument descends to the quotient. QED.

### Corollary 4.2 — invisible kernel dimension

The kernel of the quotient restriction has dimension

`K_B(d)=2 d n^2-1`.

Indeed, the full dissipative quotient in dimension `n` has dimension

`N_n=(n^2-1)^2`,

so

`K_B(d)=N_n-R_res(d)=2 d n^2-1`.

This number is the exact amount of new quotient information that no old embedded face can see once the restriction quotient itself has been completely resolved.

## 5. Structural parity ceiling

A minimal dimension-`d` design has

`L_d=floor(d^2/2)`

matrix-valued faces. After embedding into dimension `n=d+1`, one face supplies at most `2n^2` real scalar coordinates. Therefore every embedded minimal design satisfies

`rank M_d^uparrow <= min(2n^2 L_d, R_res(d))`.

Substituting `L_d=floor(d^2/2)` yields the exact structural ceiling

`R_d^max <= (d^2-1)(d+1)^2 + 2 * 1_(d even)`.

Equivalently:

### Odd `d`

`2n^2 L_d=(d^2-1)n^2=R_res(d)-2`.

Thus an embedded lower-bound-saturating family is two real coordinates short of complete restriction tomography even if every available row is independent.

### Even `d`

`2n^2 L_d=d^2 n^2 > R_res(d)`.

The structural bottleneck is the restriction quotient itself, and the unavoidable row redundancy is

`d^2 n^2-R_res(d)=n^2-2`,

exactly the dimension of the restricted inner-derivation image.

Hence the experimentally observed formula is not a numerical coincidence. It is the unique rank ceiling imposed by block-diagonal restriction and Hamiltonian gauge.

## 6. Exact deficiency to the next full quotient

If the structural ceiling is attained, the remaining dimension after the old-face embedding is

- for even `d`:

  `Delta_d=2 d (d+1)^2-1`;

- for odd `d`:

  `Delta_d=2 d (d+1)^2+1`.

In one formula,

`Delta_d=2 d (d+1)^2-(-1)^d`.

This proves the parity-dependent deficiency formula that had previously appeared only as a stable computational pattern.

## 7. Block-module decomposition of the restriction quotient

The same result has a useful representation-theoretic refinement. Complexify the real problem. A normalized map on

`B=M_d direct-sum C`

may be represented by an arbitrary complex-linear map

`F:M_d->M_n`,

using the normalized coordinate `A-a I_d` for `diag(A,a)`.

Decompose the output into the four `d+1` block sectors. Modulo the corresponding restricted inner derivations, the quotient dimensions are:

1. top-left regular sector:

   `dim = d^4-d^2+1`;

2. top-right left-module sector:

   `dim = d^3-d`;

3. bottom-left right-module sector:

   `dim = d^3-d`;

4. bottom-right scalar sector:

   `dim = d^2`.

Their sum is

`d^4+2d^3-2d+1=(d^2-1)(d+1)^2+2=R_res(d)`.

For infinitesimal square probes with ordered pair `(A,B)`, the four normalized coboundary forms are respectively

`F(AB)-F(A)B-AF(B)`,

`F(AB)-AF(B)`,

`F(AB)-F(A)B`,

and

`F(AB)`.

This decomposition makes the parity defect transparent. If `d` is odd, then `2L_d=d^2-1`; maximal row rank means:

- the regular sector is one coordinate short of its full quotient;
- each cross-module sector is exactly saturated;
- the scalar sector is one coordinate short;

for a total deficit of exactly `2` inside the restriction quotient.

For even `d`, all four quotient sectors can in principle be fully identified.

## 8. Definition — extension-ready minimal design

A dimension-`d` design is called **extension-ready minimal** if

1. it has exactly `L_d=floor(d^2/2)` faces;
2. its native measurement rank is `(d^2-1)^2`;
3. after block embedding into `M_(d+1)`, its rank attains the structural ceiling of Section 5.

The counterexample in the block-extension audit shows that condition 2 does not imply condition 3.

## 9. Generic-intersection lemma

### Lemma 9.1 — simultaneous native and embedded genericity

Fix a connected real-analytic face-parameter family. Assume:

- at least one parameter choice has native full rank `(d^2-1)^2`;
- at least one parameter choice attains the structural embedded ceiling of Section 5.

Then extension-ready minimal designs exist in that family, and in fact form an open dense subset of the intersection of the two corresponding nonvanishing-minor loci.

#### Proof

Each rank condition is the nonvanishing of at least one maximal minor of a matrix whose entries depend real-analytically, and algebraically in the usual rational/complex parameterizations, on the face parameters. If a maximal minor is nonzero at one point, it is not the zero analytic function. Its nonvanishing locus is therefore open and dense on the connected analytic component. The intersection of two open dense subsets is nonempty and open dense. QED.

This lemma is deliberately conditional: it does not replace the missing all-`d` embedded-ceiling witness. It shows exactly what kind of witness is sufficient.

## 10. Consequence for the sharp programme

The old numerical pattern can now be split into a proved theorem and a remaining existence statement.

### Proved

For every finite `d`, no embedded minimal design can exceed

`(d^2-1)(d+1)^2 + 2 * 1_(d even)`,

and the corresponding next-step deficiency is exactly

`2d(d+1)^2-(-1)^d`

whenever that ceiling is attained.

### Still to prove for the all-d sharp theorem

Construct, for every `d`, a lower-bound-saturating native design that attains this ceiling, or prove a parity-controlled induction that produces such designs at the stages where the next sharp extension requires them.

The target is therefore no longer a guessed rank formula. It is a concrete **attainability / transversality theorem on the restriction quotient**.
