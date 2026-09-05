# Native tilt closure and all-odd extension-ready existence

**Article I post-publication research note — v0.1**  
**Author:** Malachevsky, A.A.  
**ORCID:** 0009-0008-6009-3196  
**Status:** `PROVED_NATIVE_TILT_NONZERO / PROVED_ALL_ODD_ER / SHARP_ALL_D_COXETER_RESEARCH_THEOREM`

## 1. Purpose

The centered-tangent programme had one remaining native-rank obstruction after the compressed embedded determinant `det D_n` was closed.

For odd `n>=3`, with

`L=(n^2-1)/2`,

the tangent regular measurement family with last anchor perturbed by

`H -> H+tS`

has full embedded regular row rank for suitable finite complete `H`-anchor compressions, but its unique non-derivation kernel line is the cycle-holonomy Schur multiplier `h_q`, which satisfies

`h_q(I)=0`.

The previous native-tilt audit proved that the old one-parameter path has zero tilt at every order, and that a transverse reverse-cycle perturbation

`Y_* -> Y_*+s Z_r`, `Z_r=E_(r-1,r)`,

produces an explicit first-order holonomy spike.

The remaining question was whether the finite reconstruction operator `R_t` could annihilate every such spike.

This note proves that it cannot. The proof uses three ingredients already available in the branch:

1. the exact description of the row-dependency space of a finite complete `H`-anchor compression;
2. the fact that every diagonal output block is a square basis of the quotient `Q=M_n/C H`;
3. a singular block-Schur-complement lemma controlled by the already-proved invertibility of `D_n`.

The result closes the native tilt for every odd `n>=3`.

## 2. Setup

Let

`H=diag(h_0,...,h_(n-1))`

have simple spectrum and trace zero, and let

`S=sum_i E_(i+1,i)`.

Choose a finite complete `H`-anchor compression

`Y_1,...,Y_L`

on the good locus supplied by the centered-tangent transversality theorem. Thus:

- the finite `H`-anchor measurement matrix `M_0` has rank

  `r_H=n^4-2n^2+2n`;

- the positive-cycle edge matrix has rank `n`;

- the compressed binder determinant `D_n` is invertible;

- the last sample `Y_L=Y_*` is chosen in the binder-compatible reverse-cycle-zero subspace before the final transverse perturbation.

Write

`M(t)=M_0+tN`,

where `N` changes only the last paired face and replaces its `H` anchor by the cyclic binder `S`.

For sufficiently small nonzero `t`, the already-proved `det D_n!=0` theorem gives

`rank M(t)=(n^2-1)n^2`,

and

`ker M(t)=Der(M_n) direct-sum C h_q`,

where `q=sum_j a_j!=0` is the cycle-holonomy coordinate.

Let

`E(F)=F(I)`.

Because `E` vanishes on this kernel, there is a unique reconstruction map

`R_t: im M(t)=W -> M_n`

such that

`E=R_t M(t)`.

The transverse perturbation `Y_* -> Y_*+sZ_r`, with

`Z_r=E_(r-1,r)`,

has derivative on `h_q`

`A_(t,r) h_q = -t q d_r`,

where `d_r in W` is the data vector supported only in the last paired face, with

- first orientation: `E_(r,r)`;
- reversed orientation: `E_(r-1,r-1)`.

Thus

`kappa_(n,r)(t)=R_t A_(t,r)h_q=-tq R_t d_r`.

The task is to prove `R_t d_r!=0` for at least one `r`.

## 3. Every reverse-cycle diagonal spike belongs to `im M_0`

The finite complete `H`-anchor row-dependency theorem gives exactly

`n(n-2)`

global left dependencies.

They are obtained from the one-dimensional local dependencies of the off-diagonal output blocks `(a,b)`, `a!=b`, after the `F(H)` residual edge rows are cancelled by the edge matrix `R`.

There are no left dependencies supported on a diagonal output block `(a,a)`.

Consequently every data vector supported only on diagonal output blocks is orthogonal to the full left-nullspace of `M_0`, and hence lies in `im M_0`.

In particular,

`d_r in im M_0`

for every `r`.

Choose any preimage

`F_r^(0)`

with

`M_0 F_r^(0)=d_r`.

Because `ker M_0` is the complete `H`-anchor kernel and every element of that kernel has `F(I)=0`, the value

`F_r^(0)(I)`

is independent of the chosen preimage.

## 4. Gauge reduction for diagonal data

The data `d_r` vanish on every off-diagonal output block.

Let

`z=diag F_r^(0)(H)`.

For each off-diagonal block, applying its unique local row dependency to the zero data gives the corresponding edge equation

`rho_(a,b)(z)=0`.

Since the edge matrix has rank `n`,

`z=0`.

The off-diagonal part of `F_r^(0)(H)` can be removed by subtracting an inner derivation, because `H` has simple spectrum. This does not change any defect data and does not change `F(I)`.

Hence we may and do choose the preimage so that

`F_r^(0)(H)=0`.

For a diagonal output block `(a,a)`, define the scalar functional

`f_a(X)=[F_r^(0)(X)]_(a,a)`.

Then `f_a(H)=0`, so it descends to

`Q=M_n(C)/C H`.

The two rows contributed by one sample `Y_i` are represented by

`T_a(Y_i)=[(H-h_a I)Y_i]`,

`R_a(Y_i)=[Y_i(H-h_a I)]`.

Because the compression is complete and

`2L=n^2-1=dim Q`,

the list

`{T_a(Y_i),R_a(Y_i)}_(i=1)^L`

is a basis of `Q` for every diagonal output block `a`.

## 5. Dual identity coefficient

Fix a diagonal block `a`. Expand the identity class in its finite block basis:

`[I] = sum_i c_(a,i,+) T_a(Y_i) + sum_i c_(a,i,-) R_a(Y_i)`.

For the spike `d_a`, the block `a` has exactly one unit datum on the `+` row of the last sample. Therefore the corresponding dual functional satisfies

`[F_a^(0)(I)]_(a,a)=c_(a,L,+)`.

Similarly the second spike component contributes

`[F_a^(0)(I)]_(a-1,a-1)=c_(a-1,L,-)`.

In particular,

`F_a^(0)(I)!=0`

whenever

`c_(a,L,+)!=0`.

So it remains only to prove that the complete-compression / `det D_n` good locus can be chosen so that at least one last-face dual identity coefficient is nonzero.

## 6. The nonzero dual-coefficient condition is a genuine open condition

For fixed `a`, the condition

`c_(a,L,+)!=0`

is the nonvanishing of the determinant obtained by replacing the basis vector `T_a(Y_L)` by `[I]` in the diagonal-block basis matrix. Therefore it is Zariski open on the block-basis locus.

It is not the zero polynomial.

### Lemma 6.1 — reserved-two-directions witness

For every odd `n>=3` and every fixed `a`, there exists an `L`-tuple in the reverse-cycle-zero affine subspace for the last sample such that

1. the diagonal block `(a,a)` is a basis of `Q`;
2. `c_(a,L,+)!=0`.

#### Proof

On the traceless diagonal subspace `D_0`, the map

`D -> [(H-h_a I)D]`

is an isomorphism onto the diagonal part of `Q`. Therefore choose traceless diagonal `D_a` with

`T_a(D_a)=[I]`.

Choose indices `p,q` with

`p!=q`, `p!=a`, `q!=a`,

and choose the orientation so that `E_(p,q)` is not one of the forbidden reverse-cycle entries of the binder constraint.

Put

`Y_L=D_a+E_(p,q)`.

Then

`T_a(Y_L)=[I]+alpha E_(p,q)`,

`R_a(Y_L)=[I]+beta E_(p,q)`,

where

`alpha=h_p-h_a`, `beta=h_q-h_a`.

Simple spectrum and `p,q!=a`, `p!=q` give

`alpha!=0`, `beta!=0`, `alpha!=beta`.

Hence the last two vectors are independent and span both `[I]` and `E_(p,q)`:

`[I]=(beta T_a(Y_L)-alpha R_a(Y_L))/(beta-alpha)`.

The coefficient of `T_a(Y_L)` is therefore nonzero.

It remains to choose the first `L-1` samples so that their `n^2-3` row vectors form a complement of this two-plane.

Reserve the one diagonal direction `[I]` and the one off-diagonal direction `E_(p,q)` for the last sample. There remain

- `n-2` diagonal quotient directions;
- `n(n-1)-1` off-diagonal directions.

Use `n-2` mixed samples, each combining one remaining traceless diagonal direction with a distinct unit `E_(a,j)`, to produce one diagonal and one off-diagonal pivot. After that the number of remaining off-diagonal directions is

`(n(n-1)-1)-(n-2)=(n-1)^2`.

Pair those remaining units so that the projective coefficient ratios

`[h_u-h_a : h_v-h_a]`

are different inside every pair. As in the finite-compression theorem, every ratio fiber has size at most `n-1`; for `n>=5` this is at most half of `(n-1)^2`, and `n=3` is checked directly. Hence such a perfect pairing exists.

The number of samples used is

`(n-2)+(n-1)^2/2=(n^2-3)/2=L-1`.

Their two rows form a basis of the complement. Together with the last two rows they form a basis of `Q`, and the displayed coefficient of `T_a(Y_L)` remains nonzero. QED.

Therefore the polynomial condition `c_(a,L,+)!=0` is nonempty on the same irreducible reverse-cycle-zero parameter space used by the binder construction.

The already-proved conditions

- complete finite `H`-anchor compression;
- cycle-pivot nonvanishing;
- all `theta_e!=0`, hence `det D_n!=0`;
- binder genericity;

are nonempty Zariski-open conditions on that parameter space.

Their intersection with

`c_(a,L,+)!=0`

is therefore nonempty.

Fix such a tuple from now on.

## 7. Singular-lift lemma

We now compare the reconstruction at `t!=0` with the complete `H`-anchor preimage at `t=0`.

Let

`K_H=ker M_0`.

The `det D_n!=0` theorem gives a decomposition

`K_H=K_t direct-sum K_c`,

where

`K_t=Der(M_n) direct-sum C h_q`

and

`dim K_c=n(n-2)`.

Choose a complement `X` of `K_H` in the full map space, so

`M_0|_X : X -> im M_0`

is an isomorphism.

Choose a complement `C` of `im M_0` in `W`. The compressed dependency theorem is exactly the statement that the projected map

`pi_C N|_(K_c) : K_c -> C`

is an isomorphism.

### Lemma 7.1 — bounded reconstruction of old-image data

For every `d in im M_0`, there is, for sufficiently small nonzero `t`, a solution

`F(t)`

of

`M(t)F(t)=d`

such that

`F(t)=F^(0)+K_0+O(t)`,

where

`M_0F^(0)=d`

and

`K_0 in K_c`.

Consequently

`lim_(t->0) E(F(t))=E(F^(0))`.

#### Proof

With respect to

`V/K_t = X direct-sum K_c`

and

`W=im M_0 direct-sum C`,

the matrix of `M(t)` has block form

`[ A+O(t)      t B+O(t^2) ]`

`[ t C_1       t D+O(t^2) ]`,

where `A=M_0|_X` and `D=pi_C N|_(K_c)` are invertible.

For data `(d,0)`, the second block equation determines a bounded leading value of the `K_c` coordinate,

`k_0=-D^(-1) C_1 A^(-1)d`,

and the first block equation then gives

`x(t)=A^(-1)d+O(t)`.

Thus a bounded solution exists and converges modulo `K_H` to the old preimage class.

Since every element of `K_H` satisfies `F(I)=0`, adding `K_0` does not change `E`. Hence the displayed limit follows. QED.

Because `E` vanishes on `ker M(t)=K_t`, the value `E(F(t))` is exactly `R_t d`. Therefore

`lim_(t->0) R_t d = E(F^(0))`

for every `d in im M_0`.

## 8. Native tilt is nonzero

Choose the good tuple from Section 6 and set `r=a`. Then

`d_a in im M_0`

and its old-image preimage satisfies

`[F_a^(0)(I)]_(a,a)=c_(a,L,+)!=0`.

By Lemma 7.1,

`R_t d_a -> F_a^(0)(I) !=0`

as `t->0`.

Therefore for every sufficiently small nonzero `t`,

`R_t d_a !=0`.

Since

`A_(t,a) h_q=-t q d_a`

with `q!=0`, we obtain

`kappa_(n,a)(t)=-tq R_t d_a !=0`.

This proves the missing finite native-projection coefficient.

### Theorem 8.1 — all-odd native tilt

For every odd `n>=3`, there exists a minimal centered tangent face tuple with

1. full embedded regular row rank `(n^2-1)n^2`;
2. a unique non-derivation kernel line modulo inner derivations;
3. a transverse reverse-cycle perturbation for which that line satisfies

   `d/ds|_(s=0) h(s)(I) !=0`.

Hence for sufficiently small nonzero transverse parameter `s`, the surviving non-derivation line leaves

`N={F:F(I)=0}`,

and the native normalized regular rank is exactly

`(n^2-1)^2`.

#### Proof

The embedded rank is open in `s` and remains maximal for sufficiently small `s`. The one-dimensional kernel quotient therefore varies analytically. The derivative formula from the previous native-tilt audit gives

`h_1(I)=-kappa_(n,a)(t)`.

The right side is nonzero by the argument above. Therefore `h(s)(I)!=0` for all sufficiently small nonzero `s` outside an isolated exceptional set. The only normalized kernel then consists of inner derivations, so the native quotient rank is full. QED.

## 9. All-odd extension-ready theorem

The centered tangent framework had already proved that, for every odd `n>=3`, the scalar, left-module and right-module embedded sector maxima are each attained on nonempty Zariski-open loci.

Theorem 8.1 proves that the simultaneous regular embedded maximum and native full-rank condition is also attained on a nonempty open locus.

The tangent face parameter space is irreducible. Therefore the finite intersection of these nonempty open loci is nonempty.

### Theorem 9.1 — extension-ready minimal designs in every odd dimension

For every odd `n>=3`, there exists an extension-ready minimal Coxeter design with exactly

`L_n=(n^2-1)/2`

faces.

The embedded design attains the structural scalar-one restriction ceiling, and the native design has full dissipative quotient rank

`(n^2-1)^2`.

The analytic exponential lifting from tangent pairs to genuine determinant-one transports preserves the selected nonzero minors for sufficiently small nonzero transport scale. Hence the theorem is not merely formal-tangent: it gives genuine finite Coxeter-square designs.

## 10. Sharp all-dimensional consequence

The branch already contains the conditional odd-to-even transfer theorem

`ER_d -> ER_(d+1)`

for every odd `d>=3`, using exactly `d+1` new faces and preserving the lower-bound count.

Theorem 9.1 supplies `ER_d` for every odd `d>=3`. Hence extension-ready minimal designs exist in every dimension `d>=3`.

The structural scalar-count lower bound is

`L_d^Cox >= floor(d^2/2)`.

The extension-ready constructions give the matching upper bound.

### Corollary 10.1 — sharp Coxeter face count

For every integer `d>=3`,

`L_d^Cox = floor(d^2/2)`.

This is now a theorem at the research-note level of the branch.

The `d=2` extension-ready obstruction remains valid and is a separate low-dimensional phenomenon; it does not affect the statement above.

## 11. Numerical sanity check — not used in the proof

For random good compressions in `n=3` and `n=5`, the asymptotic prediction from Lemma 7.1 was checked directly.

If `F_r^(0)` solves

`M_0 F_r^(0)=d_r`,

then numerically

`kappa_(n,r)(t)/t -> -q F_r^(0)(I)`

as `t->0`.

The relative agreement reached approximately `10^(-3)` at `t=10^(-3)` in the direct dense checks. These calculations are only consistency checks and are not used in any theorem above.

## 12. Claim firewall and next publication obligation

The sharp face-count equality is proved here inside the bounded finite-dimensional first-order Coxeter tomography model of this branch.

It does **not** imply:

- conditioning or numerical stability;
- finite-time channel identifiability;
- monotonicity of reduced curvature under arbitrary CP reductions;
- any physical gauge, spacetime, or gravitational curvature claim.

The research gate is closed, but publication status is not automatic. Before upgrading the main manuscript, run the branch publication audit: theorem numbering, proof dependency audit, exact relation between tangent and finite Coxeter faces, low-dimensional exception wording, bibliography/related-work boundary, and reproducibility notes.
