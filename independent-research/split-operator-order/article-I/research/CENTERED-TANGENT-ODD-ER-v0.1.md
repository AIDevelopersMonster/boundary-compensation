# Centered tangent framework for odd-dimensional extension-ready Coxeter designs

**Article I post-publication research note — v0.1**  
**Author:** Malachevsky, A.A.  
**ORCID:** 0009-0008-6009-3196  
**Status:** `PROVED_CENTERED_TANGENT_3_SECTORS / PROVED_COMPLETE_ANCHOR_REGULAR_BINDING / PROVED_H_STAGE_MAXIMAL_COMPRESSION / FINAL_REGULAR_TRANSVERSALITY_OPEN`

## 1. Purpose and claim firewall

The earlier odd-dimensional extension-ready draft was audited because it used uncentered surrogate formulas instead of the scalar-one block-embedding formulas. This note repairs that point at the tangent level and isolates the last regular-sector compression problem.

Nothing in this note should yet be cited as a proof that extension-ready minimal designs exist for every odd dimension. What is proved here is:

1. the exact centered tangent reduction for genuine scalar-one block embedding;
2. explicit all-odd tangent witnesses for the scalar and right sectors, and hence a separate witness for the left sector;
3. an exact classification of the complete one-anchor regular kernel;
4. an explicit second-anchor face which reduces that complete-anchor kernel to the required `n^2` dimensions;
5. a finite compression theorem showing that `L_n-1` generic `H`-anchored faces have completely independent regular rows.

The only remaining tangent obstruction is the final regular transversality/compression step joining the finite `H` stage to one binding face.

Throughout, `n>=3` is odd and

`L=(n^2-1)/2`.

## 2. Centered tangent reduction

For the scalar-one block embedding, write the centered variable as

`G(A)=F(A-I)`, so `G(I)=0`.

The exact embedded branch formulas are

- regular:

  `G(AB)-G(A)B-A G(B)`;

- left:

  `G(AB)-G(A)-A G(B)`;

- right:

  `G(AB)-G(A)B-G(B)`;

- scalar:

  `G(AB)-G(A)-G(B)`.

Take traceless tangent matrices `X,Y in sl_n(C)` and genuine determinant-one transports

`A_eps=exp(eps X)`, `B_eps=exp(eps Y)`.

Then

`A_eps-I = eps X + eps^2 X^2/2 + O(eps^3)`,

`B_eps-I = eps Y + eps^2 Y^2/2 + O(eps^3)`,

`A_eps B_eps-I = eps(X+Y)`

` + eps^2(X^2/2+XY+Y^2/2)+O(eps^3)`.

Because `G` is linear, all first-order terms cancel. The first nonzero coefficient is order `eps^2`.

### Theorem 2.1 — centered tangent branch formulas

At order `eps^2`, the four centered embedded sectors become

- regular:

  `delta_reg F(X,Y)=F(XY)-F(X)Y-XF(Y)`;

- left:

  `delta_L F(X,Y)=F(XY)-X F(Y)`;

- right:

  `delta_R F(X,Y)=F(XY)-F(X)Y`;

- scalar:

  `delta_0 F(X,Y)=F(XY)`.

The paired inverse branch `(B_eps^(-1),A_eps^(-1))` has, at the same order, the reversed ordered pair `(Y,X)`.

Hence one genuine real square face has, after complexification and centered tangent degeneration, exactly the paired ordered probes

`(X,Y)` and `(Y,X)`.

If a tangent maximal minor is nonzero, the corresponding analytic finite-`eps` minor has a nonzero leading coefficient and is therefore nonzero for sufficiently small nonzero `eps` outside an isolated exceptional set.

No transport rescaling is used in this argument: `exp(eps X),exp(eps Y)` already lie in `SL_n(C)` because `X,Y` are traceless.

## 3. Explicit scalar/right tangent family

Let

`omega=exp(2 pi i/n)`

and

`H=diag(1,omega,...,omega^(n-1))`.

Since `n>1`, `tr H=0`, and `H^k` is traceless for `k=1,...,n-1`.

All `L` faces below use the first tangent `X=H`.

### 3.1 Special faces

For `k=1,...,n-1`, put

`Y_k=H^k+E_(0,k)`.

There are `n-1` such faces.

### 3.2 Same-row faces

For each row `p=1,...,n-1`, pair the `n-1` columns `q!=p` arbitrarily into `(n-1)/2` unordered pairs `{q,s}` and use

`Y=E_(p,q)+E_(p,s)`.

The number of these faces is `(n-1)^2/2`.

Thus the total number is

`(n-1)+(n-1)^2/2=(n^2-1)/2=L`.

## 4. Scalar sector is sharp

For a special face,

`H Y_k = H^(k+1)+E_(0,k)`,

`Y_k H = H^(k+1)+omega^k E_(0,k)`.

Since `omega^k!=1`, the two products isolate both

`E_(0,k)`

and

`H^(k+1)`.

As `k` runs from `1` to `n-1`, the diagonal products are

`H^2,...,H^n=I`,

which form `n-1` independent diagonal matrices. The special faces also give the `n-1` row-zero off-diagonal matrix units.

For a same-row face,

`H(E_(p,q)+E_(p,s))=omega^p(E_(p,q)+E_(p,s))`,

`(E_(p,q)+E_(p,s))H=omega^q E_(p,q)+omega^s E_(p,s)`.

Since `q!=s`, the two products isolate `E_(p,q)` and `E_(p,s)`.

Therefore the `2L=n^2-1` products span `n^2-1` independent input matrices, and

`rank_scalar=n^2-1`.

This is the exact odd-dimensional scalar row count.

## 5. Right sector is sharp

Let the right-module defect be

`R_F(X,Y)=F(XY)-F(X)Y`,

where the output is a row vector.

The universal kernel consists of the right module maps

`F(M)=v M`,

and has dimension `n`.

Assume all faces of Section 3 have zero right defect. Put

`v=F(H)H^(-1)`

and

`G(M)=F(M)-vM`.

Then `G(H)=0` and all right defects remain zero.

For the special faces write

`d_k=G(H^k)`, `a_k=G(E_(0,k))`,

with `d_1=0`.

The first orientation gives

`d_(k+1)+a_k=0`.

The reversed orientation gives

`d_(k+1)+omega^k a_k-(d_k+a_k)H=0`.

Hence

`a_k[(omega^k-1)I-H]=d_k H`.

For odd `n`, the diagonal matrix `((omega^k-1)I-H)` is invertible. Indeed, a zero diagonal entry would give

`omega^j=omega^k-1`.

Taking absolute values would force `|omega^k-1|=1`, hence an angle of `+/- pi/3`, which would require a sixth root of unity. This is impossible in odd order.

Starting from `d_1=0`, induction gives

`a_k=0`, `d_(k+1)=0`

for every `k`. In particular `G(I)=G(H^n)=0`. Thus `G` vanishes on the full diagonal basis and on all `E_(0,k)`.

For a same-row face set

`b=G(E_(p,q))`, `c=G(E_(p,s))`.

The first orientation gives

`b+c=0`,

and the reversed orientation gives

`omega^q b+omega^s c=0`.

Therefore

`(omega^q-omega^s)b=0`,

so `b=c=0`.

Hence `G=0`, and the right-sector kernel is exactly the `n`-dimensional module kernel. Therefore

`rank_right=n(n^2-1)=n^3-n`.

## 6. Left sector

Transpose converts the left defect into the right defect with the order reversed:

`[F(XY)-X F(Y)]^T`

is the right-module expression for the transposed map on the reversed transposed pair.

Because every face already contains both orientations, transposing the family of Section 3 gives a left-sector full-rank witness. Thus the left-full locus is nonempty and

`rank_left=n(n^2-1)`

is attainable.

The scalar-, left-, and right-full conditions are Zariski-open conditions on the irreducible tangent face-parameter space

`(sl_n(C) x sl_n(C))^L`.

Since each of the three open sets is nonempty, their finite intersection is nonempty. Therefore there are tangent face tuples which are simultaneously maximal in all three nonregular sectors.

## 7. Complete one-anchor regular kernel

Now consider

`delta_F(X,Y)=F(XY)-F(X)Y-XF(Y)`.

Fix the same simple-spectrum diagonal anchor `H` and impose

`delta_F(H,Y)=delta_F(Y,H)=0`

for every traceless `Y`.

### Theorem 7.1 — exact complete `H`-anchor kernel

The complete one-anchor kernel is

`F=ad_Koff + S_c`,

where

- `Koff` is an arbitrary off-diagonal matrix;
- `S_c` is an arbitrary off-diagonal Schur multiplier,

  `S_c(E_(p,q))=c_(p,q) E_(p,q)` for `p!=q`,

  and `S_c` vanishes on the diagonal algebra.

Hence

`dim ker_H = 2n(n-1)`

and

`rank_H = n^4-2n(n-1)=n^4-2n^2+2n`.

#### Proof

Take `Y=E_(p,q)`, `p!=q`. The `(p,q)` entry of the two anchor equations first forces the diagonal part of `F(H)` to vanish. Since `H` has simple spectrum, there is a unique off-diagonal `Koff` with

`[Koff,H]=F(H)`.

Subtract `ad_Koff`. We may therefore normalize to `F(H)=0`.

The two equations with `E_(p,q)` then force

`F(E_(p,q))=c_(p,q)E_(p,q)`.

For `Y=H^k`,

`F(H^(k+1))=H F(H^k)=F(H^k)H`.

Starting from `F(H)=0`, induction gives

`F(H^k)=0`

for `k=1,...,n`, including `F(I)=0`. Thus the normalized map vanishes on the entire diagonal algebra and is an arbitrary Schur multiplier on the off-diagonal matrix units. Restoring `ad_Koff` gives the claimed kernel. QED.

Modulo all inner derivations, the Schur coefficients are taken modulo gradient families

`c_(p,q)=k_p-k_q`.

The remaining quotient therefore has dimension

`n(n-1)-(n-1)=(n-1)^2`.

## 8. A complete-anchor second-face binder

Let `S` be the cyclic shift

`S=sum_i E_(i+1,i)`

with indices modulo `n`.

Choose a traceless matrix `Y_*` satisfying

- `(Y_*)_(i,i+1)=0` on every reverse-cycle position;
- every other off-diagonal entry is nonzero.

For a normalized Schur multiplier write

`a_i=c_(i+1,i)`.

### Theorem 8.1 — path-additivity binder

Imposing the two additional equations

`delta_(S_c)(S,Y_*)=0`,

`delta_(S_c)(Y_*,S)=0`

forces

`c_(r,s)=a_s+a_(s+1)+...+a_(r-1)`

along the positive cyclic path from `s` to `r`.

The solution family has dimension `n`.

#### Proof

At an off-diagonal position with `r!=s` and `r-1!=s`, the first branch gives

`c_(r,s)=a_(r-1)+c_(r-1,s)`.

At the base edge `r=s+1`, this is the definition `c_(s+1,s)=a_s`. The diagonal equation is multiplied by the deliberately vanishing entry `(Y_*)_(r-1,r)` and therefore imposes no cycle-sum constraint.

The reversed branch gives the equivalent column recurrence

`c_(r,s)=a_s+c_(r,s+1)`.

Iterating yields the path-sum formula. QED.

The `n` path parameters consist of

- the `(n-1)`-dimensional diagonal-inner-derivation subspace `sum_i a_i=0`;
- one extra cycle-holonomy direction.

Together with the arbitrary off-diagonal inner derivations, the complete `H` anchor plus this one binder has kernel dimension

`n(n-1)+n=n^2`.

Therefore its regular rowspace has the target dimension

`n^4-n^2=(n^2-1)n^2`.

This proves that there is no intrinsic regular/cohomological obstruction. The only issue is finite face compression.

## 9. Finite `H`-stage maximal compression

Put

`k=L-1=(n^2-3)/2`.

We now prove that `k` actual `H`-anchored faces can be chosen so that **all** their regular rows are independent.

Their total row count is

`2k n^2=(n^2-3)n^2`.

### Theorem 9.1 — maximal finite `H`-stage rank

There exist traceless matrices

`Y_1,...,Y_k`

such that the paired regular `H`-anchor matrix

`{delta(H,Y_i), delta(Y_i,H)}_(i=1)^k`

has rank

`(n^2-3)n^2`.

The same is true on a nonempty Zariski-open subset of `(sl_n(C))^k`.

#### Proof

Choose domain coordinates with the input value `F(H)` separated from all other input values. Delete the `F(H)` columns. In the remaining submatrix, different output entries `(a,b)` decouple.

For a fixed output entry, the two rows contributed by `Y` are represented, modulo the line `C H`, by

`T_a(Y)=[(H-h_a I)Y]`,

`R_b(Y)=[Y(H-h_b I)]`

in the `(n^2-1)`-dimensional space `M_n(C)/C H`.

It suffices to find, for each fixed `(a,b)`, a `k`-tuple for which the `2k=n^2-3` vectors

`T_a(Y_i),R_b(Y_i)`

are independent. Nonvanishing of one such minor is a Zariski-open condition. Once nonemptiness is proved separately for every one of the finitely many `(a,b)`, irreducibility of `(sl_n)^k` implies that all these open conditions hold simultaneously for some common tuple.

For an off-diagonal matrix unit `E_(p,q)`, put

`alpha_(p,q)=h_p-h_a`,

`beta_(p,q)=h_q-h_b`.

Then

`T_a(E_(p,q))=alpha_(p,q) E_(p,q)`,

`R_b(E_(p,q))=beta_(p,q) E_(p,q)`.

Thus a sum of two distinct off-diagonal units whose projective coefficient pairs

`[alpha:beta]`

are distinct contributes two independent off-diagonal directions.

We also need a controlled number of diagonal directions. Let `D_0` be the traceless diagonal subspace. The map

`D -> [D(H-h_b I)] in D/C H`

is an isomorphism. Its kernel is zero: if

`D(H-h_b I)=cH`,

the `b`-th diagonal coordinate forces `c=0`, then all other diagonal coordinates of `D` vanish, and tracelessness forces the last one to vanish as well.

**Case `a!=b`.** The unique off-diagonal direction `E_(a,b)` has coefficient pair `(0,0)` and is deliberately left unused. Choose exactly `n-2` distinct units

`E_(p,b)`, `p notin {a,b}`.

For these, `beta=0` and `alpha!=0`. Choose traceless diagonal matrices `D_p` so that the classes

`R_b(D_p)`

are `n-2` independent diagonal directions. The mixed samples

`Y_p=E_(p,b)+D_p`

then contribute one new off-diagonal direction and one new diagonal direction each.

After removing these `n-2` units and the invisible `E_(a,b)`, the remaining off-diagonal directions number

`(n-1)^2`.

Pair them so that the projective coefficient pairs differ inside every pair. Such a perfect pairing exists because every projective ratio class has size at most `n-1`, whereas half of the remaining set has size `(n-1)^2/2`; for `n=3` the bound is still exact enough. For each pair `{e,f}`, use `Y=e+f`. The two rows then span exactly the two directions `e,f`.

The resulting count is

`2(n-2)+(n-1)^2=n^2-3`.

**Case `a=b`.** There is no zero off-diagonal coefficient pair. Choose `n-3` distinct units `E_(p,b)`, `p!=b`, and mix them with diagonal matrices whose `R_b` images are independent. Pair all remaining

`n^2-2n+3`

off-diagonal directions by unequal projective ratios. Again the largest ratio class has size at most `n-1`, which is strictly below half of the remaining set for `n>=5` and is harmless at `n=3`.

The total number of independent vectors is again

`n^2-3`.

Thus the required minor is nonzero for each `(a,b)`. Finite intersection of the corresponding nonempty Zariski-open sets gives one common tuple with every output block full. The selected submatrix therefore has rank `(n^2-3)n^2`, proving the theorem. QED.

## 10. Exact remaining regular compression problem

Theorem 9.1 leaves an `H`-stage kernel of dimension

`n^4-(n^2-3)n^2=3n^2`.

One final paired face supplies exactly `2n^2` rows. Therefore the all-odd regular tangent theorem is now equivalent to the following sharp statement.

### Compression Lemma — remaining obligation

There exist

`Y_1,...,Y_k in sl_n(C)`

and one final pair `(S,Y_*)` such that

`rank [ H-stage ; delta(S,Y_*); delta(Y_*,S) ]`

`=(n^2-1)n^2`.

Equivalently, the final face has rank `2n^2` on the `3n^2`-dimensional kernel of the finite `H` stage and leaves exactly an `n^2`-dimensional kernel.

The complete-anchor Theorems 7.1-8.1 show that a suitable second anchor has exactly the correct cohomological action. Theorem 9.1 shows that the first `L-1` faces can already be compressed with no row loss. What remains is the transversality between these two facts.

A useful equivalent perturbative form is obtained by taking `L` `H`-anchored faces which span the complete `H`-anchor rowspace and perturbing one first anchor as

`H -> H+tS`.

The complete-anchor row deficiency is

`(n^2-1)n^2-(n^4-2n^2+2n)`

`=n(n-2)`.

The first-order Schur map of the perturbation is induced by the binder rows

`delta(S,Y_*), delta(Y_*,S)`

on this `n(n-2)`-dimensional defect. Proving that this Schur map has rank `n(n-2)` would close the finite regular compression lemma.

This is now the only tangent regular barrier.

## 11. Consequence if the Compression Lemma is closed

If the Compression Lemma holds, then the regular tangent sector has full row rank

`(n^2-1)n^2`.

Sections 3-6 already give nonempty maximal-rank loci for the scalar, left, and right sectors. All four maximal-rank conditions are Zariski open in the same irreducible tangent face space, so their intersection is nonempty.

The centered tangent lifting theorem then produces actual finite complex `SL_n(C)` faces attaining the odd structural embedded ceiling. Zariski density of `SU(n)` in `SL_n(C)` returns the witness to the unitary locus, and the engineered-square realization converts each transport pair into a genuine Coxeter square.

Thus closing the Compression Lemma would restore the all-odd extension-ready existence theorem on a centered, scalar-one-correct foundation.
