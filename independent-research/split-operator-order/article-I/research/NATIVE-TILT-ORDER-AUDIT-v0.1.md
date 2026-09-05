# Native tilt order audit: exact no-go for the old one-parameter binder and a transverse first-order detector

**Article I post-publication research note — v0.1**  
**Author:** Malachevsky, A.A.  
**ORCID:** 0009-0008-6009-3196  
**Status:** `PROVED_OLD_TILT_DIRECTION_IDENTICALLY_ZERO / PROVED_TRANSVERSE_FIRST_ORDER_HOLONOMY_DETECTOR / FINITE_NATIVE_PROJECTION_SCALAR_OPEN`

## 1. Purpose

The previous centered-tangent compression audit left one final native-rank question after the embedded regular determinant `det D_n` was closed: does the unique non-derivation kernel line tilt out of

`N={F:M_n->M_n : F(I)=0}`

under the same perturbation

`H -> H+tS`

used to lift the compressed row dependencies?

This note answers that question exactly.

The answer is negative: **the old one-parameter perturbation has zero native tilt at every order**. The cycle-holonomy Schur multiplier remains an exact kernel vector for every `t`.

A minimal transverse modification of the binder sample, however, detects the holonomy line already at first order. This reduces the true final problem to one explicit finite-compression reconstruction coefficient.

Throughout `n>=3` is odd,

`L=(n^2-1)/2`,

`H=diag(h_0,...,h_(n-1))`

has simple spectrum,

`S=sum_i E_(i+1,i)`

is the positive cyclic shift, and indices are modulo `n`.

## 2. The surviving cycle-holonomy line

Inside the complete `H`-anchor kernel, modulo off-diagonal derivations, write a Schur multiplier as

`F(E_(r,s))=c_(r,s) E_(r,s)`, `r!=s`,

with `F` zero on the diagonal algebra.

The binder equations for the special sample `Y_*` used in the centered-tangent construction impose path additivity

`c_(r,s)=a_s+a_(s+1)+...+a_(r-1)`,

where

`a_j=c_(j+1,j)`.

The gradient/diagonal-derivation subspace is characterized by

`q:=sum_j a_j=0`.

Thus modulo inner derivations the unique surviving non-derivation line is represented by any path-additive Schur multiplier `h_q` with

`q!=0`.

Because every such Schur multiplier vanishes on the diagonal algebra,

`h_q(I)=0`.

## 3. Exact no-go for the old `H+tS` perturbation

Let

`Y_1,...,Y_(L-1),Y_*`

be a finite complete compression of the `H` anchor, with `Y_*` binder-generic and with the reverse-cycle positions

`(Y_*)_(i,i+1)=0`

as in the path-additivity construction.

Consider the one-parameter family of paired faces

`(H,Y_i)`, `i<L`,

and

`(H+tS,Y_*)`.

### Theorem 3.1 — the old native tilt is identically zero

For every complex `t`, the path-additive holonomy representative `h_q` satisfies every regular tangent face equation of this family exactly.

Hence whenever the compressed dependency determinant is nonzero and the full regular row rank is maximal, the kernel is exactly

`Der(M_n) direct-sum C h_q`,

and the unique non-derivation kernel line is constant in `t` and remains inside `N`.

In particular, all coefficients of the previously proposed native tilt series vanish:

`tau_n^(1)=tau_n^(2)=...=0`

along this one-parameter deformation.

#### Proof

For every traceless `Y`, membership of `h_q` in the complete `H`-anchor kernel gives

`delta_(h_q)(H,Y)=0`,

`delta_(h_q)(Y,H)=0`.

The path-additivity binder theorem gives

`delta_(h_q)(S,Y_*)=0`,

`delta_(h_q)(Y_*,S)=0`.

By bilinearity of the tangent Leibniz defect,

`delta_(h_q)(H+tS,Y_*)`

`=delta_(h_q)(H,Y_*)+t delta_(h_q)(S,Y_*)=0`,

and similarly

`delta_(h_q)(Y_*,H+tS)=0`.

All other faces remain `H`-anchored and therefore also annihilate `h_q`.

Thus `h_q` is an exact kernel vector for every `t`, not merely a formal limiting vector. Since `h_q(I)=0`, no native tilt can appear at any order along this deformation. QED.

### Corollary 3.2 — exact native rank deficit on the old path

On any value of `t` for which the embedded regular row rank is

`(n^2-1)n^2`,

the kernel has dimension `n^2` and equals

`Der(M_n) direct-sum C h_q`.

Its intersection with `N` is the whole kernel. Therefore the native rank is exactly

`(n^2-1)^2-1`.

So the old one-parameter path can never by itself produce an extension-ready odd design.

## 4. Minimal transverse perturbation

The absence of tilt comes from one deliberate feature of the binder sample: all reverse-cycle entries vanish.

Fix an index `r` and put

`Z_r=E_(r-1,r)`.

This is one of the forbidden reverse-cycle positions. Replace the binder sample by

`Y_*(s)=Y_*+s Z_r`.

Keep the anchor

`H+tS`.

The last face is therefore

`(H+tS, Y_*+sZ_r)`.

## 5. Exact holonomy detector

For a path-additive Schur multiplier, the reverse edge coefficient is

`c_(r-1,r)=q-a_(r-1)`.

A direct diagonal calculation gives

`[delta_(h_q)(S,Z_r)]_(r,r)`

`= -(a_(r-1)+c_(r-1,r))`

`= -q`.

The reversed orientation gives

`[delta_(h_q)(Z_r,S)]_(r-1,r-1)=-q`.

### Theorem 5.1 — transverse activation is first order

For the two-parameter last face,

`delta_(h_q)(H+tS,Y_*+sZ_r)`

has diagonal entry

`-t s q`

at `(r,r)`, and the reversed branch has diagonal entry

`-t s q`

at `(r-1,r-1)`.

Thus, for every fixed `t!=0`, the cycle-holonomy line is detected **linearly in `s`**.

#### Proof

Expand bilinearly:

`delta(h_q;H+tS,Y_*+sZ_r)`

`=delta(h_q;H,Y_*)`

` + s delta(h_q;H,Z_r)`

` + t delta(h_q;S,Y_*)`

` + ts delta(h_q;S,Z_r)`.

The first and third terms vanish by the `H`-anchor and binder equations. The second term also vanishes because `h_q` belongs to the complete `H`-anchor kernel and `Z_r` is traceless. The remaining term is exactly

`ts delta(h_q;S,Z_r)`,

whose `(r,r)` entry is `-tsq` by the calculation above. The reversed branch is identical at the adjacent diagonal entry. QED.

## 6. Augmented path-defect form

For a general Schur multiplier define, as in the cycle-factor note,

`u_(r,s)=c_(r,s)-sum_(j=s)^(r-1) a_j`

on non-cycle edges, and retain the holonomy coordinate

`q=sum_j a_j`.

There are

`n(n-2)`

path-defect coordinates `u_e` and one holonomy coordinate `q`, for a total

`n(n-2)+1=(n-1)^2`,

which is exactly the Schur quotient dimension modulo diagonal derivations.

For the reverse-cycle edge `(r-1,r)`,

`c_(r-1,r)=q-a_(r-1)+u_(r-1,r)`.

Hence the new diagonal detector is

`-[q+u_(r-1,r)]`.

The old binder block is triangular in increasing cyclic distance with nonzero diagonal coefficients `theta_e` on the `u_e` coordinates. After eliminating the already-resolved path defects, the transverse reverse-cycle row leaves the scalar coefficient

`-q`.

Thus at the **complete-anchor Schur quotient level** the augmented binder is triangular with diagonal

`{theta_e}_{e noncycle}`

followed by

`-1`

on the holonomy coordinate.

This proves that the obstruction is not higher order in the intrinsic Schur/binder geometry: the missing direction is a genuine first-order transverse direction.

## 7. Exact finite-compression tilt formula

Fix `t!=0` in the embedded-full-rank locus supplied by the closed `det D_n` theorem, and write the resulting full regular measurement map as

`M_t: V -> W`,

where

`V=Hom(M_n,M_n)`

and

`dim W=(n^2-1)n^2`.

Then `M_t` is surjective and

`ker M_t=Der(M_n) direct-sum C h_q`.

Let

`E:V->M_n`, `E(F)=F(I)`.

Since `E` vanishes on `ker M_t`, it factors uniquely through the surjective map `M_t`:

`E=R_t M_t`

for a unique linear reconstruction operator

`R_t:W->M_n`.

Let `A_(t,r)` be the derivative of the measurement matrix with respect to `s` at `s=0` for the perturbation `Y_* -> Y_*+sZ_r`.

If

`h(s)=h_q+s h_1+O(s^2)`

is the surviving non-derivation kernel line modulo derivations, then differentiation of

`M_(t,s) h(s)=0`

gives

`M_t h_1=-A_(t,r) h_q`.

Applying `R_t` yields the exact first-order tilt formula

`h_1(I)=-R_t A_(t,r) h_q`.

Define the **finite native-projection coefficient**

`kappa_(n,r)(t):=R_t A_(t,r) h_q in M_n`.

Then

`native first-order tilt <=> kappa_(n,r)(t) != 0`.

Moreover `A_(t,r) h_q` is explicit: it is supported only in the last paired face and contains the two diagonal spikes of size `-tq` described in Theorem 5.1.

Thus the old vague scalar `tau_n` has been replaced by a concrete reconstruction problem:

> Does the finite complete compression reconstruct a nonzero `F(I)` response from this explicit two-row diagonal holonomy spike?

## 8. What is proved and what remains

### Proved

1. The old `H+tS` perturbation has **no native tilt at any order**.
2. Therefore the previous formulation “compute the first nonzero coefficient of the same one-parameter kernel line” was aimed at a coefficient that is identically zero.
3. Turning on one reverse-cycle entry of the binder sample detects cycle holonomy exactly at order `ts`.
4. At fixed embedded-lifting `t!=0`, the intrinsic holonomy detection is first order in the new transverse parameter `s`.
5. The finite native tilt is exactly the matrix coefficient

   `kappa_(n,r)(t)=R_t A_(t,r) h_q`.

### Still open

Prove that for every odd `n>=3` one can choose the complete compression / cycle-pivot data and an index `r` so that

`kappa_(n,r)(t) != 0`.

This is now the only remaining native-rank obligation in the centered-tangent route.

## 9. Numerical sanity check — not part of the proof

For random complete compressions satisfying the required ranks, the two-parameter perturbation was checked directly in dimensions `n=3` and `n=5`. At fixed nonzero `t`, the norm of the surviving kernel value `h(s)(I)` scaled linearly with `|s|` over several decades, while it was at numerical zero for `s=0`.

This agrees with the exact first-order detector derived above but is not used in any theorem.

## 10. Claim firewall

This note does **not** yet prove all-odd extension-ready existence.

It does prove that the former one-parameter native-tilt target was structurally impossible, and it replaces it by a genuinely transverse first-order coefficient `kappa_(n,r)(t)`.

Do not search for a second- or higher-order coefficient along the old `H+tS` path: every such coefficient is exactly zero.
