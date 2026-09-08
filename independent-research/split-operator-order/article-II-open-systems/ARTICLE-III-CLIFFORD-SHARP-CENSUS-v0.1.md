# Article III — Clifford-Block Sharp Census and the Fresh Explicit Sharp-Design Conjecture

**Author:** Malachevsky, A.A. / Малачевский А.А.  
**ORCID:** 0009-0008-6009-3196  
**Date:** 2026-09-08  
**Status:** `NUMERICAL-CERTIFICATE-CENSUS / d=3,4,5 SHARP FULL RANK / ALL-d THEOREM OPEN`

## 0. Purpose

The block-compression programme asked for a block-compatible sharp core. The first Fourier block-lift theorem showed that non-Weyl mixing can compress an `O(d^2)` quotient sector into only a few whole Coxeter faces.

A direct numerical search over a much smaller structured pool now reveals a stronger pattern: the two-anchor family

\[
\boxed{\text{Fourier anchor }F_d\quad+\quad\text{quadratic phase anchor }P_d}
\]

already contains **sharp full-rank Coxeter designs** at the information-theoretic minimum in dimensions `d=3,4,5`.

This is not yet an all-dimensional proof. It is a reproducible numerical discovery that changes the next theorem target from abstract grouped restricted invertibility to an explicit finite Clifford-type construction.

The script is

`article-III-clifford-block-census.py`.

---

## 1. Structured face pool

Let

\[
W_{a,b}=X^aZ^b,
\qquad (a,b)\in\mathbb Z_d^2.
\]

Use two fixed first transports.

### Fourier anchor

\[
(F_d)_{jk}=d^{-1/2}\omega^{jk},
\qquad \omega=e^{2\pi i/d}.
\]

### Quadratic phase anchor

\[
\boxed{
P_d=\operatorname{diag}
\left(\omega^{j(j-1)/2}\right)_{j=0}^{d-1}.
}
\tag{1.1}
\]

For every nonzero `g=(a,b)`, form the engineered Coxeter square with first two contextual transports

\[
(F_d,W_g)
\qquad\text{or}\qquad
(P_d,W_g).
\]

Thus the candidate pool has only

\[
2(d^2-1)
\]

faces, all generated from two global anchors and the Weyl orbit.

---

## 2. Real measurement model used in the census

The domain is the real vector space of complex-linear normalized `*`-preserving maps

\[
D:M_d(\mathbb C)\to M_d(\mathbb C),
\qquad D(I)=0,
\]

represented in an orthonormal Hermitian basis.

Its real dimension before quotienting derivations is

\[
\boxed{d^2(d^2-1).}
\tag{2.1}
\]

For every engineered square the exact first-order coefficient is evaluated from

\[
K_D
=\sum_{k=1}^4
T_4\cdots T_{k+1}
D(T_k)
T_{k-1}\cdots T_1.
\tag{2.2}
\]

Real and imaginary matrix entries are stacked as scalar rows.

A universally identifying design must have rank

\[
\boxed{N_d=(d^2-1)^2,}
\tag{2.3}
\]

leaving exactly the `d^2-1` dimensional Hamiltonian kernel.

The sharp face count is

\[
\boxed{L_d^\sharp=\lfloor d^2/2\rfloor.}
\tag{2.4}
\]

---

## 3. Greedy block rule

The search is intentionally block-compatible.

At each step:

1. project every unused whole-face row block onto the orthogonal complement of the row span already selected;
2. maximize the exact numerical rank gain;
3. break rank-gain ties by the smallest positive singular value of the projected block;
4. select the entire face.

No scalar row is ever selected independently of its parent Coxeter face.

Thus the census directly attacks the grouped critical-selection problem isolated in `ARTICLE-III-CRITICAL-BLOCK-COMPRESSION-REDUCTION-v0.1.md`.

---

## 4. Dimension d=3

The sharp count is

\[
L_3^\sharp=4,
\qquad
N_3=64.
\]

The greedy `F/P` pool selects:

\[
(P_3,W_{1,2}),
\quad
(P_3,W_{1,1}),
\quad
(F_3,W_{0,1}),
\quad
(F_3,W_{1,2}).
\tag{4.1}
\]

The cumulative numerical ranks are

\[
18,\ 36,\ 54,\ 64.
\]

Hence the four-face design reaches exactly the quotient target

\[
\boxed{\operatorname{rank}=64.}
\tag{4.2}
\]

This reproduces the sharp count using a highly structured two-anchor family rather than an unrestricted search.

---

## 5. Dimension d=4

The sharp count is

\[
L_4^\sharp=8,
\qquad
N_4=225.
\]

One greedy selection is

\[
\begin{aligned}
&(F_4,W_{0,1}),
(F_4,W_{1,2}),
(P_4,W_{2,3}),
(P_4,W_{3,1}),\\
&(P_4,W_{1,2}),
(F_4,W_{1,3}),
(P_4,W_{0,3}),
(F_4,W_{2,2}).
\end{aligned}
\tag{5.1}
\]

The cumulative numerical ranks are

\[
32,\ 64,\ 96,\ 128,\ 160,\ 192,\ 220,\ 225.
\tag{5.2}
\]

Therefore

\[
\boxed{\operatorname{rank}=225=N_4}
\tag{5.3}
\]

at the exact sharp count.

The first six blocks are completely transverse at full face rank `32`; only the final two faces encounter the information-theoretic slack.

---

## 6. Dimension d=5

The sharp count is

\[
L_5^\sharp=12,
\qquad
N_5=576.
\]

The greedy two-anchor design is

\[
\begin{aligned}
&(P_5,W_{1,0}),
(P_5,W_{1,3}),
(P_5,W_{3,0}),
(P_5,W_{2,1}),\\
&(P_5,W_{1,2}),
(P_5,W_{3,1}),
(P_5,W_{1,1}),
(P_5,W_{2,2}),\\
&(F_5,W_{1,3}),
(F_5,W_{4,0}),
(F_5,W_{0,2}),
(F_5,W_{4,1}).
\end{aligned}
\tag{6.1}
\]

The cumulative numerical ranks are

\[
50,100,150,200,250,300,350,400,450,500,550,576.
\tag{6.2}
\]

Thus

\[
\boxed{\operatorname{rank}=576=N_5.}
\tag{6.3}
\]

A striking feature is that the first eleven faces are mutually transverse at their full numerical face rank `50`; the twelfth contributes exactly the remaining `26` quotient directions.

This is the finite-dimensional geometry predicted by the sharp-rank-slack theorem in an especially clean form.

---

## 7. The near-direct-sum phenomenon is much stronger than expected

For a square face the real scalar output capacity is `2d^2`. In the observed structured sharp designs:

- `d=3`: first `3` faces contribute full rank `18` each;
- `d=4`: first `6` faces contribute full rank `32` each;
- `d=5`: first `11` faces contribute full rank `50` each.

For `d=5`, before the final face,

\[
\boxed{\operatorname{rank}=550}
\]

with **zero exact numerical overlap** among the first eleven face rowspaces.

The final quotient defect is

\[
576-550=26,
\]

while the last face has capacity `50`, so its overlap is `24`, exactly the odd sharp slack

\[
s_5=d^2-1=24.
\]

This is not merely compatible with the sharp-rank-slack theorem; it realizes the extremal architecture

\[
\boxed{
\text{all overlap postponed to the final face.}
}
\tag{7.1}
\]

That suggests a much sharper all-dimensional theorem target than generic block restricted invertibility.

---

## 8. Numerical conditioning snapshot

For the selected raw measurement matrices, the smallest singular value at the quotient target and the largest singular value are approximately:

### d=3

\[
\sigma_{64}\approx 6.37\times10^{-3},
\qquad
\sigma_{\max}\approx5.03.
\]

### d=4

\[
\sigma_{225}\approx2.84\times10^{-3},
\qquad
\sigma_{\max}\approx6.55.
\]

### d=5

\[
\sigma_{576}\approx5.62\times10^{-4},
\qquad
\sigma_{\max}\approx9.71.
\]

These are unwhitened raw-coordinate values and are **not** claimed to establish an asymptotic law. They only show that the sharp structured designs are numerically nondegenerate in all three tested dimensions.

---

## 9. A second anchor pair shows the phenomenon is structural

The `F/Z` family, where `Z` is the polynomial Sidon phase anchor of `ARTICLE-III-DIRECT-ROBUST-COXETER-COMPILATION-v0.1.md`, also gives sharp full rank in `d=3,4,5` under block-greedy selection.

For `d=4`, one `F/Z` selection reaches the cumulative ranks

\[
32,64,96,128,160,192,224,225.
\]

Thus the existence of a near-direct-sum sharp core is not an accident of one phase convention. What appears essential is the combination

\[
\boxed{
\text{dense Fourier-type mixing}
+\text{diagonal phase separation}.
}
\]

The quadratic phase anchor is nevertheless substantially better conditioned numerically than the tiny Sidon phase anchor in the tested dimensions.

---

## 10. New explicit conjecture

### Conjecture 10.1 — two-anchor Clifford sharp design

For every integer `d>=3`, the Coxeter pool

\[
\mathcal P_d
=
\{(F_d,W_g),(P_d,W_g):g\in\mathbb Z_d^2\setminus\{0\}\}
\tag{10.1}
\]

contains a subset of exactly

\[
L_d^\sharp=\lfloor d^2/2\rfloor
\]

faces whose first-order measurement map has quotient rank

\[
(d^2-1)^2.
\]

### Strong quantitative form

There exists such a subset with

\[
\boxed{
\sigma_{\min}^{+}\ge d^{-O(1)}.
}
\tag{10.2}
\]

The d=3,4,5 census supports both the exact-rank and polynomial-gap forms, but proves neither for arbitrary `d`.

---

## 11. New theorem target: character-block determinant factorization

The computational pattern suggests that the correct all-dimensional proof should not use generic sparsification.

Both anchors normalize or nearly diagonalize natural Weyl-character decompositions. Therefore the face matrix should admit a block Fourier transform in domain/output character coordinates.

The desired proof architecture is now:

1. derive the exact character-block matrix for `(P_d,W_g)`;
2. derive the exact character-block matrix for `(F_d,W_g)`;
3. identify a deterministic set of `floor(d^2/2)-1` labels for which the corresponding face blocks are pairwise transverse;
4. prove that the final face closes exactly the sharp slack `s_d`;
5. estimate the block determinants/singular gaps by roots-of-unity separation.

If successful, this would prove sharp robustness by a **fresh direct construction** rather than by recursive parity transfer or abstract block restricted invertibility.

---

## 12. Immediate algebraic observation from the census

The `d=5` selection already suggests a phase-dominant core plus Fourier closure:

\[
8\ P\text{-faces}
+3\ F\text{-faces}
\]

form a completely transverse rank-`550` core, and a fourth Fourier face closes the remaining `26` quotient directions.

Thus a plausible odd-dimensional template is

\[
\boxed{
\text{large direct-sum phase core}
+\text{small Fourier Schur closure}.
}
\tag{12.1}
\]

The exact number of Fourier closure faces is not yet stable enough across `d=3,4,5` to state a theorem.

---

## 13. Claim firewall

This note records reproducible numerical linear-algebra certificates only.

It proves computationally, to the stated numerical tolerance, that the explicit `F/P` face pool contains sharp full-rank selections in `d=3,4,5`.

It does **not** yet prove:

- exact symbolic rank of those selections over a number field;
- the all-dimensional two-anchor conjecture;
- an all-dimensional polynomial lower singular-value bound;
- that the greedy rule itself succeeds for every `d`;
- optimality of the particular selected labels.

The next mandatory step is an exact character-block derivation, followed by exact finite-field or algebraic certificates for the new structured `d=4,5` witnesses before any publication-level all-dimensional claim.
