# Odd-dimensional centered-tangent transversality closure

**Article I post-publication research note — v0.1**  
**Author:** Malachevsky, A.A.  
**ORCID:** 0009-0008-6009-3196  
**Status:** `PROVED_DET_DN_NONZERO_FOR_ALL_ODD_N / NATIVE_TILT_REMAINS`

## 1. Purpose

The previous note `CENTERED-TANGENT-CYCLE-FACTOR-v0.1.md` reduced the compressed dependency determinant

`det D_n != 0`

for odd `n>=3` to two kinds of algebraic nonvanishing conditions on a finite complete `H`-anchor compression:

1. a cycle pivot `det R_C != 0`;
2. one scalar leading coefficient `theta_e != 0` for every non-cycle directed edge `e`.

This note proves that these conditions can be attained simultaneously for every odd `n>=3`. Therefore the first of the two final centered-tangent barriers is closed in all odd dimensions.

Only the native tilt scalar remains.

## 2. Parameter space

Fix odd `n>=3` and

`L=(n^2-1)/2`.

Let

`X=(sl_n(C))^L`

be the ordered sample space of tuples

`Y=(Y_1,...,Y_L)`.

Fix a diagonal anchor

`H=diag(h_0,...,h_(n-1))`

with pairwise distinct entries and `tr H=0`.

The finite complete-anchor compression theorem shows that there is a nonempty Zariski-open set

`U_comp subset X`

on which the sampled paired `H`-anchor equations have the complete-anchor rank

`r_H=n^4-2n^2+2n`.

For every off-diagonal output block `(a,b)`, the corresponding local presentation then has a one-dimensional dependency line after the `F(H)` residual is restored.

All conditions below are considered on this maximal-rank locus.

## 3. A canonical symmetric skeleton

For every unordered pair `{p,q}`, `p<q`, put

`U_pq=E_pq+E_qp`.

There are

`n(n-1)/2`

such matrices.

Add any `(n-1)/2` traceless diagonal matrices

`D_1,...,D_((n-1)/2)`.

The resulting ordered tuple has exactly

`n(n-1)/2+(n-1)/2=(n^2-1)/2=L`

samples.

Call such a tuple a **symmetric skeleton**.

The diagonal samples are irrelevant for the elementary off-diagonal calculation below; they merely complete the face count.

## 4. Exact local dependency on the symmetric skeleton

Fix an oriented edge `(a,b)`, `a!=b`, and use the symmetric sample

`U_ab=U_ba=E_ab+E_ba`.

For the restricted regular anchor maps

`T_a(Y)=(H-h_a I)Y`,

`R_b(Y)=Y(H-h_b I)`,

one has

`T_a(U_ab)=(h_b-h_a)E_ba`,

`R_b(U_ab)=(h_a-h_b)E_ba`.

Hence

`T_a(U_ab)+R_b(U_ab)=0`.

So the local block dependency contains the coefficient pair

`lambda_+=1`, `lambda_-=1`

on the sample `U_ab`, with zero `H` residual.

Whenever the local block is on its maximal one-dependency locus, this is its unique dependency line.

Restoring `Z=diag(z_0,...,z_(n-1))=diag F(H)` therefore gives the edge row

`rho_(a,b)(z)=-(z_a+z_b)`

up to nonzero normalization.

Thus on the maximal-rank part of the symmetric skeleton the edge matrix is the unsigned incidence matrix of the complete directed graph, with the two orientations of one geometric edge giving proportional rows.

## 5. Odd-cycle pivot is explicit

Choose the positive cycle

`C={(s+1,s): s in Z_n}`.

Its pivot matrix is, up to independent nonzero row scalings, the odd-cycle matrix

`z -> (z_(s+1)+z_s)_s`.

If

`z_(s+1)+z_s=0`

for all `s`, then iteration gives

`z_s=(-1)^s z_0`.

After one full cycle,

`z_0=(-1)^n z_0=-z_0`

because `n` is odd. Hence `z_0=0` and therefore every `z_s=0`.

So the cycle matrix is invertible.

In the normalization with all cycle rows exactly `z_(s+1)+z_s`, its determinant has absolute value `2`.

Therefore the cycle-pivot polynomial is not identically zero on `X`.

Since `U_comp` is Zariski dense, there exists a complete compression arbitrarily close to a symmetric skeleton for which

`det R_C != 0`.

Thus

`U_cycle={Y in U_comp : det R_C(Y)!=0}`

is a nonempty Zariski-open subset of `X`.

## 6. Each non-cycle leading coefficient is a genuine nonzero algebraic condition

Fix one non-cycle directed edge

`e=(r,s)`,

so `r!=s` and `r!=s+1 mod n`.

On the one-dimensional local-dependency locus, choose any algebraic normalization of the dependency vector. The leading binder coefficient from the cycle-factor theorem is

`theta_e=lambda_(e,+,L) (Y_L)_(r-1,s) + lambda_(e,-,L) (Y_L)_(r,s+1)`.

Its zero set is algebraic after clearing the chosen normalization minor. Therefore the condition

`theta_e != 0`

is Zariski open wherever the local dependency line is defined.

It remains to show that this open condition is nonempty.

### Lemma 6.1 — local activation of one edge

For every non-cycle edge `e`, there exists an ordered sample tuple on the maximal local-rank locus for which `theta_e != 0`.

#### Proof

Start from a symmetric skeleton and order the samples so that

`Y_L=U_rs`.

At the skeleton, the local dependency for `(r,s)` is supported on this sample with

`lambda_(e,+,L)=lambda_(e,-,L)=1`

up to common nonzero scale.

Perturb only the last sample by

`Y_L(epsilon)=U_rs+epsilon E_(r-1,s)`

and, if needed to preserve tracelessness, add a compensating diagonal traceless term. Because `e` is non-cycle, `r-1` is not equal to `s`, so the displayed off-diagonal perturbation is legitimate.

The local one-dimensional dependency line depends algebraically, hence continuously, on the sample tuple as long as the local rank does not drop. Therefore

`lambda_(e,+,L)(epsilon)=1+O(epsilon)`,

`lambda_(e,-,L)(epsilon)=1+O(epsilon)`

in a suitable normalization.

Moreover

`(Y_L(epsilon))_(r-1,s)=epsilon`,

while the second neighboring entry contributes only an analytic term. Hence

`theta_e(epsilon)=epsilon+O(epsilon^2)`

unless the alternative neighboring perturbation is required by an accidental first-order cancellation. In that exceptional chart, use instead

`Y_L(epsilon)=U_rs+epsilon E_(r,s+1)`.

The two perturbation directions enter `theta_e` through the two nonzero base dependency coefficients separately, so they cannot both have identically zero first-order derivative.

Therefore one of these two one-parameter perturbations gives `theta_e !=0` for all sufficiently small nonzero `epsilon` outside a finite algebraic exceptional set. QED.

Consequently, for every non-cycle edge `e`,

`U_e={Y in U_comp : theta_e(Y)!=0}`

is a nonempty Zariski-open subset of the irreducible parameter space `X`.

## 7. Simultaneous transversality

There are only finitely many non-cycle directed edges, namely

`n(n-2)`.

Consider

`U_good=U_comp intersect U_cycle intersect intersection_(e noncycle) U_e`.

Every factor is a nonempty Zariski-open subset of the irreducible affine space `X`.

A finite intersection of nonempty Zariski-open subsets of an irreducible variety is nonempty.

Therefore

`U_good != empty`.

Hence there exists a single ordered `L`-tuple which simultaneously:

1. is a complete finite `H`-anchor compression;
2. has invertible positive-cycle pivot `R_C`;
3. satisfies `theta_e!=0` for every non-cycle directed edge.

## 8. Main theorem

### Theorem 8.1 — all-odd nonvanishing of the compressed dependency determinant

For every odd `n>=3`, there exists a finite complete centered `H`-anchor compression with

`L=(n^2-1)/2`

paired faces such that the compressed first-order dependency operator satisfies

`det D_n != 0`.

#### Proof

By Section 7 choose a tuple in `U_good`. The cycle-factor theorem identifies `D_n`, after invertible row and column changes, with a triangular matrix indexed by the non-cycle directed edges. Its diagonal entries are exactly the `theta_e`. Since the cycle pivot is invertible and all `theta_e` are nonzero, the triangular matrix is invertible. Hence

`det D_n !=0`.

QED.

## 9. Consequence for the centered tangent programme

The first of the two final odd-dimensional barriers is now closed for every odd dimension:

`compressed dependency determinant: CLOSED`.

Thus the embedded regular sector can be lifted from the complete-anchor tangent base to full row rank

`(n^2-1)n^2`

using the centered finite perturbation.

The only remaining obstruction to an all-odd extension-ready theorem is the native one-dimensional non-derivation kernel line.

Its required condition is that, after the embedded regular rank has been lifted, the surviving line leave the native hyperplane

`N={F:F(I)=0}`.

Equivalently one must prove a nonzero native tilt coefficient

`tau_n !=0`

or, if the linear coefficient vanishes structurally, a nonzero first higher-order centered coefficient.

## 10. Numerical sanity check — not used in the proof

Independent random complex tuples were checked for `n=3,5,7`. In every tested sample:

- the edge matrix had rank `n`;
- the positive-cycle determinant was nonzero;
- all tested local `theta_e` magnitudes were nonzero.

These computations are only consistency checks. The theorem above is algebraic/transversality based and does not depend on the numerical tests.

## 11. Claim firewall

This note does **not** yet prove all-odd extension-ready existence, because native full rank has not yet been established.

It does prove that the entire embedded regular-rank determinant barrier `det D_n` is no longer open.

The next and only centered-tangent obligation is the native tilt.
