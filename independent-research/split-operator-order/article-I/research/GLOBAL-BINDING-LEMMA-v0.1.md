# Global binding lemma for sharp Coxeter block extension

**Article I post-publication research note — v0.1**  
**Author:** Malachevsky, A.A.  
**ORCID:** 0009-0008-6009-3196  
**Status:** `PROVED_GLOBAL_BINDING / EVEN_TO_ODD_SHARP_COMPLETION`

## 1. Purpose

The local-kernel reduction note proved that, after the old embedded design has resolved the whole block-diagonal restriction quotient

`B=M_d(C) direct-sum C subset M_(d+1)(C)`, 

the remaining complexified invisible space has coordinates

`P_j=D(E_(j,n))`, `Q_j=D(E_(n,j))`, `j=1,...,d`, `n=d+1`,

and that `d` canonical local square faces reduce this space to

`K_loc={P_j=alpha_j E_(j,n), Q_j=gamma_j E_(n,j)}`,

of complex dimension `2d`.

The unique derivation gauge line is

`G={alpha_1=...=alpha_d=lambda, gamma_1=...=gamma_d=-lambda}`.

Thus the sharp completion problem is to generate exactly `2d-1` independent scalar binding relations.

This note proves that this can be done explicitly by second-order cross-plane perturbations. The reduced binding operator is the incidence system of a connected non-bipartite graph.

## 2. Base local face and cokernel

Let

`Lambda=diag(lambda_1,...,lambda_n)`

with all `lambda_r` nonzero and pairwise distinct, and in addition satisfying the multiplicative-Sidon condition required by the local-kernel theorem.

For each `j<=d`, let `U_j` be the identity outside `span{e_j,e_n}` and have the `2 x 2` block

`[[1,1],[1,2]]`

on that plane.

At the unperturbed point, the two complex branches are

`Gamma_D(U_j,Lambda)`

and

`Gamma_D(Lambda^(-1),U_j^(-1))`.

For a fixed output entry `(r,s)`, the local equations on the scalar variables

`p=(P_j)_(r,s)`, `q=(Q_j)_(r,s)`

are

`(lambda_n-lambda_s)p+(lambda_j-lambda_s)q`,

`(lambda_r^(-1)-lambda_j^(-1))p+(lambda_r^(-1)-lambda_n^(-1))q`.

The determinant is

`-(lambda_j-lambda_n)(lambda_j lambda_n-lambda_r lambda_s)/(lambda_j lambda_n lambda_r)`.

By the multiplicative-Sidon condition it is nonzero except at `(j,n)` and `(n,j)`.

Hence each face has exactly two kernel directions and exactly two cokernel directions.

At `(j,n)` the two branch outputs are proportional to `Q_j(j,n)`. A left-cokernel functional may be chosen as

`ell_j^+ = (lambda_j^(-1)-lambda_n^(-1)) z_+ -(lambda_j-lambda_n) z_-`.

At `(n,j)` the two branch outputs are proportional to `P_j(n,j)`. A left-cokernel functional may be chosen as

`ell_j^- = (lambda_n^(-1)-lambda_j^(-1)) z_+ +(lambda_j-lambda_n) z_-`.

These `2d` functionals form a cokernel basis for the direct sum of the local faces.

## 3. One cross-plane perturbation

Fix distinct old indices `j,k<=d`.

Put

`x_k=E_(k,n)`, `y_k=E_(n,k)`

and perturb only the second transport of the `j`-th local face:

`B_(j,k)(t)=Lambda [ I+t(x_k+y_k) ]`.

For `t^2 != 1` this matrix is invertible. Scalar determinant normalization does not affect rank, because

`Gamma_D(aA,bB)=ab Gamma_D(A,B)`

and the inverse branch scales by `(ab)^(-1)`.

Use the two branches

`Gamma_D(U_j,B_(j,k)(t))`,

`Gamma_D(B_(j,k)(t)^(-1),U_j^(-1))`.

Let

`D_0 in K_loc`,

so

`P_r=alpha_r x_r`, `Q_r=gamma_r y_r`.

### Lemma 3.1 — first-order forcing

The coefficient of `t` in the first branch is supported only at the old-old entry `(j,k)` and equals

`-lambda_n (alpha_j+gamma_k) E_(j,k)`.

The coefficient of `t` in the inverse branch is supported only at `(k,j)` and equals

`-lambda_n^(-1) (alpha_k+gamma_j) E_(k,j)`.

In particular, the first-order projection to the local cokernel is zero.

#### Proof

Only the cross coefficients of `B_(j,k)(t)` vary. The top-left block of `U_j` is the identity, its top-right and bottom-left vectors are both `e_j`, and the perturbation contributes top-right and bottom-left vectors in the `k`-th direction. Direct substitution into the Leibniz defect gives the two displayed entries. Since `j!=k`, neither entry is one of the exceptional cokernel positions `(j,n)` or `(n,j)`. QED.

## 4. First-order correction inside the local bulk

Because the first-order forcing lies in the image of the unperturbed local operator, it can be cancelled uniquely after fixing the two local kernel coordinates.

At `(j,k)` the local `2 x 2` system gives

`P_j^(1)(j,k)=lambda_n/(lambda_n-lambda_k) (alpha_j+gamma_k)`,

`Q_j^(1)(j,k)=0`.

At `(k,j)` it gives

`P_j^(1)(k,j)=0`,

`Q_j^(1)(k,j)=lambda_k/(lambda_n-lambda_k) (alpha_k+gamma_j)`.

All other first-order correction entries may be taken zero.

## 5. Exact second-order Schur coefficient

Substitute

`D(t)=D_0+t D_1+O(t^2)`

with the correction from Section 4 into the two perturbed branch equations and project the coefficient of `t^2` to the two cokernel functionals of Section 2.

The calculation is confined to the three-dimensional coordinate subspace

`span{e_j,e_k,e_n}`

and is therefore independent of all other dimensions.

### Lemma 5.1 — edge-binding formula

For `j!=k`, the second-order reduced Schur map of the perturbation `B_(j,k)(t)` is

`ell_j^+ :`

`- lambda_k (lambda_j-lambda_n) / [lambda_j (lambda_k-lambda_n)]`

`  * (alpha_j+gamma_k)`,

and

`ell_j^- :`

`(lambda_j-lambda_n)/(lambda_k-lambda_n)`

`  * (alpha_k+gamma_j)`.

Both coefficients are nonzero because the diagonal entries are nonzero and pairwise distinct.

#### Proof

Relabel the three relevant indices as `(j,k,n)=(1,2,3)` and write

`a=lambda_j`, `b=lambda_k`, `c=lambda_n`.

On this three-dimensional subspace,

`B(t)=diag(a,b,c)[I+t(E_(2,3)+E_(3,2))]`.

The first-order forcing is

`-c(alpha_j+gamma_k) E_(j,k)`

and

`-c^(-1)(alpha_k+gamma_j) E_(k,j)`

in the two branches. Solving the unperturbed local equations yields

`P_j^(1)(j,k)=c/(c-b)(alpha_j+gamma_k)`,

`Q_j^(1)(k,j)=b/(c-b)(alpha_k+gamma_j)`.

Using

`[I+t(E_(k,n)+E_(n,k))]^(-1)`

`= I-t(E_(k,n)+E_(n,k))`

`  +t^2(E_(k,k)+E_(n,n))+O(t^3)`,

substitution into the two branch equations gives at the exceptional positions the reduced coefficients

`-b(a-c)/(a(b-c))(alpha_j+gamma_k)`

and

`(a-c)/(b-c)(alpha_k+gamma_j)`.

These are exactly the displayed formulas. QED.

Thus one perturbed face realizes, up to nonzero row scalings, the pair of scalar edge relations

`alpha_j+gamma_k=0`,

`alpha_k+gamma_j=0`.

## 6. Graph form of the binding operator

Let `H` be an undirected graph on the old labels `{1,...,d}`. For every directed choice `j -> k_j` use the perturbation of Section 3; only the underlying undirected edge `{j,k_j}` matters for the kernel.

Set

`a_j=alpha_j`, `b_j=-gamma_j`.

The two relations attached to an edge `{j,k}` become

`a_j=b_k`,

`a_k=b_j`.

### Lemma 6.1 — graph kernel

If `H` is connected and non-bipartite, then the common solution space of all edge relations is exactly

`a_1=...=a_d=b_1=...=b_d`.

Equivalently,

`alpha_1=...=alpha_d=lambda`,

`gamma_1=...=gamma_d=-lambda`.

#### Proof

Along one edge, passing from a vertex to its neighbour swaps the `a`- and `b`-value. Along an even path the type is preserved; along an odd path it is swapped. Connectivity propagates all values from one root. A non-bipartite connected graph contains an odd cycle, and going around that cycle identifies the root `a`-value with its root `b`-value. Hence there is a single common scalar. Conversely that scalar family satisfies every edge relation. QED.

Therefore the reduced binding map has kernel exactly the gauge line and rank `2d-1`.

## 7. An explicit `d`-edge non-bipartite binding graph

For every `d>=3`, choose

`k_1=2`,

`k_2=3`,

`k_3=1`,

and for `j>=4`,

`k_j=1`.

The underlying graph consists of the triangle

`1-2-3-1`

with every remaining vertex attached to `1`.

It has exactly `d` edges, is connected, and contains an odd cycle.

Perturb the `j`-th local face by

`B_j(t)=Lambda[I+t(x_(k_j)+y_(k_j))]`.

By Lemmas 5.1 and 6.1, the second-order reduced Schur map on `K_loc` has rank

`2d-1`

and kernel exactly `G`.

## 8. Analytic rank lifting

Let `M(t)` be the square complex measurement matrix on the full invisible space supplied by the `d` perturbed faces. Its size is

`2d n^2 x 2d n^2`.

At `t=0`,

`rank M(0)=2d n^2-2d`,

with kernel and cokernel dimension `2d`.

Choose complements on which the unperturbed bulk block is invertible. In adapted row and column coordinates,

`M(t)` has a Schur complement on `K_loc` whose constant and first-order terms vanish, while its second-order term is precisely the graph-binding operator of Section 7.

A `(2d-1) x (2d-1)` minor of that second-order operator is nonzero. Hence a corresponding `(2d n^2-1) x (2d n^2-1)` minor of `M(t)` has leading term

`C t^(2(2d-1))`, `C!=0`.

Therefore for all sufficiently small nonzero `t`, outside a finite exceptional set,

`rank M(t)>=2d n^2-1`.

On the other hand every Hamiltonian derivation has zero Leibniz defect, so the gauge line `G` remains in the kernel for every `t`. Thus

`rank M(t)<=2d n^2-1`.

Consequently

`rank M(t)=2d n^2-1`.

### Theorem 8.1 — global binding lemma

For every `d>=3`, once the block-diagonal restriction quotient has been completely resolved, there exist exactly `d` additional Coxeter square faces whose joint measurement on the invisible quotient has full possible rank

`2d(d+1)^2-1`.

Equivalently, their only invisible kernel is the one-dimensional Hamiltonian gauge line.

## 9. Return to actual unitary Coxeter faces

The witness above is constructed in the complexified transport parameter space. Each `U_j` already has determinant `1`. `Lambda` may be chosen with determinant `1`, and each perturbed `B_j(t)` can be rescaled by a scalar to determinant `1`; scalar rescaling multiplies the two branch equations by nonzero reciprocal factors and does not change rank.

Thus the nonzero maximal minor is a nontrivial rational regular function on a product of `SL_n(C)` transport spaces.

`SU(n)` is Zariski dense in `SL_n(C)`. Therefore that maximal minor cannot vanish identically on the unitary locus. Hence actual unitary first-two transports exist with the same rank.

By the engineered-square realization theorem, each such ordered pair is realized by an actual adjacent-transposition Coxeter square.

Thus Theorem 8.1 holds for genuine unitary Coxeter faces, not merely for the complex witness.

## 10. Sharp even-to-odd completion

Suppose `d` is even and a minimal `d`-dimensional design is extension-ready. Then its block embedding into dimension `d+1` resolves the entire restriction quotient, because for even `d` the structural embedded ceiling equals the restriction-quotient dimension.

The global binding theorem adds exactly `d` new faces and resolves the remaining invisible quotient.

The total number of faces is

`d^2/2 + d`

`=((d+1)^2-1)/2`

`=floor((d+1)^2/2)`.

Therefore:

### Corollary 10.1 — sharp even-to-odd extension

For every even `d>=4`,

`extension-ready minimal design in dimension d`

implies

`minimal full-rank design in dimension d+1`

using exactly the information-theoretic lower-bound number of faces.

This implication is now theorem-level; the former `GLOBAL_BINDING_REMAINS` barrier is closed.

## 11. What remains

The all-dimensional sharp conjecture is not yet closed.

The remaining induction obstruction is now the opposite parity step:

> construct the even-dimensional stage from an odd-dimensional minimal stage in such a way that the new even design is itself extension-ready.

For odd `d`, the embedded old design is structurally two coordinates short of the full restriction quotient before the invisible kernel is considered. The odd-to-even step therefore requires a simultaneous repair of those two restriction coordinates and the invisible quotient, while also arranging extension-readiness of the resulting even design.

That is now the unique parity bottleneck of the block-extension programme.
