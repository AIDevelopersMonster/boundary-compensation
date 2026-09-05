# Exact local-kernel reduction for the sharp Coxeter extension step

**Article I post-publication research note — v0.1**  
**Author:** Malachevsky, A.A.  
**ORCID:** 0009-0008-6009-3196  
**Status:** `PROVED_LOCAL_KERNEL_REDUCTION / GLOBAL_BINDING_REMAINS`

## 1. Purpose

This note isolates the part of the sharp block-extension problem that can be proved uniformly in dimension without any genericity assumption.

Let `n=d+1` and

`B=M_d(C) direct-sum C subset M_n(C)`.

Suppose the old embedded design has already resolved the full restriction quotient on `B`. The remaining invisible directions are represented by complex-linear maps

`D:M_n(C)->M_n(C)`

with

`D|_B=0`.

The aim is to understand exactly what `d` local two-level square faces can and cannot do on this invisible kernel.

The result is sharp: a canonical local family reduces the invisible kernel to exactly `2d` scalar directions. The missing `2d-1` conditions are precisely the genuinely global cross-plane binding problem.

## 2. Coordinates on the invisible kernel

For `j=1,...,d`, put

`x_j=E_(j,n)`, `y_j=E_(n,j)`.

Since `D` vanishes on `B`, it is determined by

`P_j=D(x_j)`, `Q_j=D(y_j)`.

Thus the complexified invisible space has dimension

`2 d n^2`.

The one-dimensional complexified restricted-Hamiltonian gauge is

`P_j=lambda x_j`, `Q_j=-lambda y_j`

for all `j`.

Hence the quotient dimension is

`2 d n^2-1`,

in agreement with the restriction-quotient deficiency theorem.

## 3. Multiplicative-Sidon diagonal anchor

Choose nonzero complex numbers

`lambda_1,...,lambda_n`

with product `1` and such that

`lambda_r lambda_s=lambda_j lambda_n`

implies

`{r,s}={j,n}`

for every `j<=d`.

Such choices exist. For example, start from distinct powers

`mu_k=t^(2^k)`

with transcendental `t`, and rescale all `mu_k` by the same nonzero scalar so that the total product is `1`. The binary uniqueness of sums of two distinct powers gives the required product-Sidon property.

Put

`Lambda=diag(lambda_1,...,lambda_n) in SL_n(C)`.

## 4. Local face family

For each `j=1,...,d`, define `U_j in SL_n(C)` to be the identity outside the plane `span{e_j,e_n}` and, on that plane, to have the block

`[[1,1],[1,2]]`.

Its inverse has the block

`[[2,-1],[-1,1]]`.

Use the engineered square face whose two complexified ordered branches are

`(U_j,Lambda)`

and

`(Lambda^(-1),U_j^(-1))`.

Because arbitrary first-two transports can be realized by an actual adjacent-transposition Coxeter square, these are legitimate complexified Coxeter probes.

## 5. Exact branch equations

Since `D(Lambda)=D(Lambda^(-1))=0`, and

`D(U_j)=P_j+Q_j`, `D(U_j^(-1))=-P_j-Q_j`,

the first branch equation is

`P_j(lambda_n I-Lambda)+Q_j(lambda_j I-Lambda)=0`.        (5.1)

The paired branch equation is

`(Lambda^(-1)-lambda_j^(-1)I)P_j`

` +(Lambda^(-1)-lambda_n^(-1)I)Q_j=0`.                  (5.2)

These equations involve only `P_j,Q_j`; different planes are completely decoupled.

## 6. Entrywise determinant

Fix an output matrix entry `(r,s)`. Equations (5.1)-(5.2) give the `2 x 2` system

`(lambda_n-lambda_s) (P_j)_(rs)`

` +(lambda_j-lambda_s) (Q_j)_(rs)=0`,

`(lambda_r^(-1)-lambda_j^(-1)) (P_j)_(rs)`

` +(lambda_r^(-1)-lambda_n^(-1)) (Q_j)_(rs)=0`.

Its determinant is

`- (lambda_j-lambda_n)`

`  (lambda_j lambda_n-lambda_r lambda_s)`

`  /(lambda_j lambda_n lambda_r)`.

By the product-Sidon condition it is nonzero except when

`(r,s)=(j,n)` or `(r,s)=(n,j)`.

At `(j,n)`, both equations force `(Q_j)_(j,n)=0` and leave `(P_j)_(j,n)` free.

At `(n,j)`, both equations force `(P_j)_(n,j)=0` and leave `(Q_j)_(n,j)` free.

Therefore

`P_j=alpha_j E_(j,n)`,

`Q_j=gamma_j E_(n,j)`

for arbitrary scalars `alpha_j,gamma_j`.

## 7. Main theorem

### Theorem 7.1 — exact local-kernel reduction

For every `d>=2`, the `d` local square faces of Section 4 have joint kernel on the complexified invisible space exactly

`K_loc = { P_j=alpha_j x_j, Q_j=gamma_j y_j }_(j=1)^d`.

Hence

`dim_C K_loc=2d`

and the joint rank is

`2 d n^2-2d`.

Equivalently, each local face contributes exactly

`2n^2-2`

new independent scalar conditions when the faces are added plane by plane.

This proves the previously observed local-plane rank loss as an all-dimensional theorem.

## 8. Exact form of the remaining obstruction

The desired quotient kernel is only the one-dimensional gauge line

`G={alpha_1=...=alpha_d=lambda, gamma_1=...=gamma_d=-lambda}`.

Thus after the optimal local reduction the remaining task has dimension

`dim(K_loc/G)=2d-1`.

This gives a precise structural meaning to the failure of purely local sharp induction:

- local faces completely resolve all matrix-valued bulk freedom in every new-level plane;
- they do **not** compare the surviving scalar slopes between different planes;
- a sharp construction needs exactly `2d-1` independent cross-plane scalar relations.

## 9. Global perturbation target

Let the local faces be perturbed analytically by genuinely global top-right and bottom-left components. After eliminating the bulk directions of Sections 5-7, the perturbation induces a finite Schur map

`S:K_loc/G -> C^(2d-1)`

(up to the choice of a complementary cokernel basis).

If one can choose the global perturbations so that

`rank S=2d-1`,

then an analytic maximal minor has a nonzero leading coefficient and the perturbed `d`-face family has rank

`2dn^2-1`,

which is the exact invisible-quotient dimension.

Therefore the full even-step completion problem is now reduced to a `2d-1` dimensional scalar binding lemma rather than a `2dn^2-1` dimensional matrix-rank problem.

## 10. Computational audit of the binding target

Direct complex rank experiments were performed for `d=2,3,4,5` on perturbations of the local family by simultaneous dense top-right and bottom-left components. In every tested case the kernel dropped from dimension `2d` to dimension `1`, exactly the gauge line.

These calculations support the proposed global-binding lemma but are not used as a theorem premise.

The theorem-level status is therefore:

- exact local reduction to `2d` scalar slopes: **proved**;
- identification of the unique desired gauge line: **proved**;
- existence of a global perturbation with Schur rank `2d-1` for every `d`: **open**.

## 11. Relation to the sharp programme

This note explains the earlier finite-field observations that local `SU(2)`-plane faces were short of the generic global increment. The loss is not numerical bad luck: it is the exact `2`-scalar residual per plane proved above.

The next sharp theorem is now:

> **Global binding lemma.** There exist analytic global perturbations of the `d` local faces for which the induced Schur map on `K_loc/G` is invertible.

Proving that lemma would yield the exact `d`-face completion of a fully resolved restriction quotient in dimension `d+1`.
