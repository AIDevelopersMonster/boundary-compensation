# Binder-compatible transversality repair for the odd ER construction

**Article I post-publication research note — v0.1**  
**Author:** Malachevsky, A.A.  
**ORCID:** 0009-0008-6009-3196  
**Status:** `PROVED_RESTRICTED_GOOD_LOCUS_NONEMPTY / REPAIRS_NATIVE-TILT-INTERSECTION_STEP`

## 1. Audit issue repaired

The full-space transversality note proved that the conditions

- complete finite `H`-anchor compression;
- invertible odd-cycle pivot;
- `theta_e != 0` for every non-cycle directed edge;

can be attained simultaneously in

`X=(sl_n(C))^L`, `L=(n^2-1)/2`,

for every odd `n>=3`.

The later native-tilt proof additionally requires the last sample `Y_L=Y_*` to lie in the binder-compatible affine subspace

`V_0={Y in sl_n(C): Y_(i,i+1)=0 for every i mod n}`,

because the path-additivity binder deliberately suppresses the reverse-cycle entries.

A nonempty Zariski-open subset of the full space need not automatically meet this proper linear subspace. The native-tilt proof therefore required a restricted transversality lemma. This note supplies it.

Put

`X_0=(sl_n(C))^(L-1) x V_0`.

This is an irreducible affine space.

Throughout `H=diag(h_0,...,h_(n-1))` has simple spectrum and trace zero. Since the construction is existential, `H` may be chosen in the additional nonempty Zariski-open locus where the finitely many pair-sum/projective-ratio degeneracies used below are absent.

## 2. Complete compression remains nonempty on `X_0`

For an output block `(a,b)`, after deleting the `F(H)` columns the paired rows are

`T_a(Y)=[(H-h_a I)Y]`,

`R_b(Y)=[Y(H-h_b I)]`

in

`Q=M_n(C)/C H`.

The maximal block dimensions are `n^2-1` for `a=b` and `n^2-2` for `a!=b`.

### Lemma 2.1 — diagonal blocks

For every `a`, the maximal diagonal-block rank `n^2-1` is attained by some tuple in `X_0`.

#### Proof

Use the reserved-two-directions construction from the native-tilt note. Choose traceless diagonal `D_a` with

`T_a(D_a)=[I]`.

Choose distinct `p,q`, both different from `a`, and orient them so that `E_(p,q)` is not a forbidden reverse-cycle entry. Set

`Y_L=D_a+E_(p,q) in V_0`.

Then

`T_a(Y_L)=[I]+alpha E_(p,q)`,

`R_a(Y_L)=[I]+beta E_(p,q)`,

with `alpha,beta` nonzero and distinct. Hence the two last rows span `[I]` and `E_(p,q)`.

The remaining `n^2-3` directions are filled by the same mixed-diagonal and unequal-projective-ratio pairing argument used in the finite-compression theorem. Exactly `L-1` samples suffice. Thus all `2L=n^2-1` rows form a basis of `Q`. QED.

### Lemma 2.2 — off-diagonal blocks

For every `a!=b`, the maximal off-diagonal block rank `n^2-2` is attained by some tuple in `X_0`.

#### Proof

The complete visible block is `Q` with the single invisible direction `E_(a,b)` removed. Choose one visible off-diagonal unit `E_(p,q)` which is not a reverse-cycle entry and is not `E_(a,b)`. Such a unit exists for every `n>=3`.

Use the `L-1`-sample maximal-compression construction with this one visible direction reserved. Equivalently, in the pairing proof omit `E_(p,q)` from the first `n^2-3` independent rows; the counting and projective-ratio matching are unchanged after reserving one visible pivot. The case `n=3` is a direct four-unit check.

Set `Y_L=E_(p,q) in V_0`. Its two rows lie on the same visible matrix-unit line and add precisely the reserved direction. Hence the total block rank is `n^2-2`. QED.

For each fixed block, maximal rank is a nonvanishing-minor condition, hence Zariski open in `X_0`. Lemmas 2.1 and 2.2 prove nonemptiness. By irreducibility and finite intersection, there is a nonempty Zariski-open set

`U_comp^0 subset X_0`

on which every block is maximal and the full finite `H`-anchor compression has rank

`r_H=n^4-2n^2+2n`.

As in the original compression theorem, the additional connected-support condition forcing the remaining diagonal `F(H)` coordinates is open and may be imposed simultaneously.

## 3. Odd-cycle pivot remains nonempty on `X_0`

For every unordered pair `{p,q}` use the symmetric sample

`U_pq=E_pq+E_qp`,

and add `(n-1)/2` diagonal samples. Order one diagonal sample last, so the tuple lies in `X_0`.

Choose `H` generically so that for every unordered pair distinct from `{a,b}` the two coefficient vectors contributed by `U_pq` to an off-diagonal block `(a,b)` are independent. Their determinant is

`(h_p-h_q)(h_p+h_q-h_a-h_b)`,

so this is a finite nonempty open condition on the simple-spectrum trace-zero diagonal `H`.

Choose the diagonal samples generically so that their `n-1` rows span the diagonal part of `Q` in every cycle block. Then every positive-cycle block has exactly its single local dependency, supported on

`U_(s+1,s)`,

and that dependency is

`T_(s+1)(U_(s+1,s))+R_s(U_(s+1,s))=0`.

After restoring `diag F(H)=z`, its edge row is therefore, up to nonzero scaling,

`z_(s+1)+z_s`.

The `n x n` cycle matrix is the unsigned incidence matrix of an odd cycle and is invertible; in unit row normalization its determinant has absolute value `2`.

Thus the cycle-pivot condition is a nonempty Zariski-open condition on `X_0`. Intersecting with the dense set `U_comp^0` gives a nonempty restricted complete-compression/cycle-pivot locus.

## 4. Every `theta_e` is nontrivial on `X_0`

Fix a non-cycle directed edge

`e=(r,s)`, `r!=s`, `r!=s+1 mod n`.

The reverse unit

`E_(s,r)`

belongs to `V_0`: it would be forbidden only if `r=s+1`, precisely the excluded cycle case.

Choose the first `L-1` samples so that, in the local block `(r,s)`, they span the complete visible space except the direction `E_(s,r)`. Set

`Y_L=E_(s,r)`.

Then the unique local dependency is supported on the last sample and has

`lambda_(e,+,L)=lambda_(e,-,L)=1`

up to common scale, because

`T_r(E_(s,r))+R_s(E_(s,r))=0`.

Now perturb inside `V_0` by

`Y_L(epsilon)=E_(s,r)+epsilon E_(r-1,s)`.

The new entry is allowed because `r-1!=s`, and it is not a forbidden reverse-cycle position: that would require `s=r`, impossible.

At `epsilon=0` the second neighboring entry in the formula for `theta_e` vanishes, while the first coefficient is nonzero. Hence

`theta_e(epsilon)=epsilon+O(epsilon^2)`

in the normalization above. Therefore `theta_e` is not the zero regular function on `X_0`.

So for every non-cycle edge `e`,

`U_e^0={theta_e!=0}`

is a nonempty Zariski-open subset of `X_0`.

## 5. Binder genericity and the dual identity coefficient

Inside `V_0`, the binder-generic condition is simply the nonvanishing of the finitely many off-diagonal entries not belonging to the forbidden reverse cycle, together with the already-proved maximal binder minor. It is a nonempty Zariski-open condition.

The native-tilt note separately constructed, for every fixed diagonal block `a`, a point of `X_0` for which the diagonal block is a basis and the last-face dual identity coefficient

`c_(a,L,+)`

is nonzero. Thus

`U_dual^0={c_(a,L,+)!=0}`

is also a nonempty Zariski-open subset of `X_0`.

## 6. Restricted simultaneous-intersection theorem

### Theorem 6.1 — binder-compatible good locus

For every odd `n>=3`, there exists one tuple

`(Y_1,...,Y_L) in X_0`

such that simultaneously:

1. it is a complete finite `H`-anchor compression;
2. the positive-cycle edge pivot is invertible;
3. `theta_e!=0` for every non-cycle directed edge;
4. the last sample is binder-generic with all reverse-cycle entries exactly zero;
5. for a prescribed diagonal block `a`, the dual identity coefficient `c_(a,L,+)` is nonzero.

#### Proof

Each condition is a nonempty Zariski-open subset of the irreducible affine space `X_0`, by Sections 2-5. Their finite intersection is therefore nonempty. QED.

### Corollary 6.2

On this restricted good locus the compressed dependency operator `D_n` is invertible, the old one-parameter kernel is exactly

`Der(M_n) direct-sum C h_q`,

and the native-tilt reconstruction argument may be applied without any parameter-space mismatch.

## 7. Audit consequence

This note repairs the only missing intersection step identified in Sections 2 and 6 of `NATIVE-TILT-CLOSURE-ALL-ODD-ER-v0.1.md`: the full-space theorem `det D_n!=0` is now strengthened to the binder-compatible reverse-cycle-zero subspace actually required by the native-tilt proof.

The all-odd extension-ready conclusion is therefore not blocked by that parameter-space issue.

This repair does **not** audit or repair the separate odd-to-even transfer theorem. In particular, it makes no statement about the centered scalar-one formulas or determinant-one/unitary realization used in `ODD-TO-EVEN-EXTENSION-READY-v0.1.md`.
