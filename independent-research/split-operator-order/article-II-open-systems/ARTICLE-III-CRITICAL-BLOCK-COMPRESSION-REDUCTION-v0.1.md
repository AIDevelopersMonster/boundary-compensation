# Article III — Critical Block Compression Reduction at the Sharp Coxeter Count

**Author:** Malachevsky, A.A. / Малачевский А.А.  
**ORCID:** 0009-0008-6009-3196  
**Date:** 2026-09-08  
**Status:** `PROVED_REDUCTION / UNRESTRICTED_CORE_POLYNOMIAL / BLOCK_COMPATIBILITY_OPEN`

## 1. Sharp slack

Let

\[
N_d=(d^2-1)^2,
\qquad r_d=2d^2,
\qquad L_d^\sharp=\lfloor d^2/2\rfloor.
\]

The total scalar-row capacity at the sharp face count is

\[
r_dL_d^\sharp=N_d+s_d,
\]

with

\[
\boxed{s_d=
\begin{cases}
2d^2-1,& d\text{ even},\\
d^2-1,& d\text{ odd}.
\end{cases}}
\]

Hence `s_d=O(d^2)` while `N_d=Theta(d^4)`.

## 2. Whitening a robust Coxeter pool

Take any robust `O(d^2)` Coxeter pool, in particular the explicit `3d^2-1` family from `ARTICLE-III-DIRECT-ROBUST-COXETER-COMPILATION-v0.1.md`. Whiten its frame operator and scalarize the matrix-valued faces into vectors `v_i` so that

\[
\sum_i v_iv_i^*=I_{N_d}.
\]

The number of scalar rows satisfies

\[
M_d<6d^4.
\]

## 3. Unrestricted near-full core

Apply sharp scalar restricted invertibility to choose

\[
k_d=N_d-s_d
\]

scalar rows. The standard estimate

\[
\lambda_{k_d}\left(\sum_{i\in I}v_iv_i^*\right)
\ge
\left(1-\sqrt{k_d/N_d}\right)^2\frac{N_d}{M_d}
\]

gives, since `s_d=Theta(d^2)`, `N_d=Theta(d^4)`, `M_d=O(d^4)`,

\[
\boxed{\lambda_{k_d}\ge c d^{-4}}
\]

and therefore

\[
\boxed{\sigma_{\min}^{+}\ge c d^{-2}}.
\]

Thus, if scalar rows may be selected independently of their parent Coxeter faces, a polynomially conditioned core of rank `N_d-s_d` always exists.

## 4. Exact sharp core-defect decomposition

Any sharp full-rank design has total row capacity `N_d+s_d`. After extracting `N_d-s_d` independent row directions, the remaining defect space has dimension

\[
\boxed{\dim K=s_d=O(d^2)}.
\]

The remaining row capacity is at most

\[
(N_d+s_d)-(N_d-s_d)=2s_d.
\]

Hence the sharp stability problem is exactly reducible to:

\[
\boxed{
\text{near-full polynomial core of codimension }s_d
+
\text{Schur completion on an }s_d\text{-dimensional defect space}.
}
\]

## 5. Quantitative Schur completion

Let `A` be the core Gram operator, `K=ker A`, and suppose

\[
A_+\succeq aI_{K^\perp}.
\]

Let `R` be the residual Gram contribution, with block decomposition relative to `K\oplus K^\perp`. Define

\[
\Sigma=R_{00}-R_{01}(A_++R_{11})^{-1}R_{10}.
\]

The already proved Schur-transversality theorem yields

\[
\lambda_{\min}(A+R)
\ge
\frac{\min\{a,\lambda_{\min}(\Sigma)\}}{\chi},
\]

where `chi` is the norm-square of the triangular Schur factor.

Therefore a sharp polynomial lower frame bound follows if one proves only

\[
\boxed{a\ge d^{-O(1)},\quad \lambda_{\min}(\Sigma)\ge d^{-O(1)},\quad \chi\le d^{O(1)}}
\]

on a defect space of dimension `s_d=O(d^2)`.

## 6. The exact missing theorem

The unrestricted core theorem is not yet a Coxeter-face theorem because scalar restricted invertibility may pick individual rows from different faces. In the actual problem one must select whole matrix-valued face blocks.

The missing statement is therefore a **block-compatible critical restricted-invertibility theorem**:

Find `L_d^sharp` genuine Coxeter faces whose combined row blocks contain a core of rank at least `N_d-s_d` and lower singular gap `d^{-O(1)}`.

Once such a block-compatible core exists, only an `O(d^2)` Schur closure remains.

## 7. Why generic small-leverage sparsification is not enough

For whitened face blocks `Y_f>=0`,

\[
\sum_fY_f=I,
\qquad \operatorname{rank}Y_f\le r_d.
\]

With `L_0=3d^2-1`,

\[
\frac1{L_0}\sum_f\|Y_f\|
\ge
\frac{N_d}{L_0r_d}
=\Theta(1),
\]

asymptotically about `1/6`.

So the robust decomposition is a constant-leverage block decomposition. Generic Chernoff/MSS arguments that need individually tiny block norms do not directly reach the critical sharp density.

This is not a no-go theorem; it identifies the method barrier.

## 8. Main reduction theorem

### Theorem 8.1

At the sharp Coxeter count, the `Theta(d^4)` robustness problem reduces to two tasks:

1. construct a block-compatible polynomial core of rank `N_d-s_d`;
2. close an `s_d=O(d^2)` residual kernel with polynomial Schur gap using at most `2s_d` residual row directions already present inside the same sharp face set.

Ignoring face grouping, Task 1 already has a polynomial solution with singular gap `Omega(d^-2)`.

Therefore the genuine unresolved obstruction is **critical block compatibility**, not ordinary restricted invertibility and not full-dimensional spectral sparsification.

## 9. Claim firewall

This note proves the reduction and the unrestricted scalar core theorem. It does not yet prove existence of a block-compatible sharp core or polynomial stability at the exact sharp count.
