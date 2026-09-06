# Article III — Simultaneous Unitary Two-Scale Odd-to-Even Transfer

**Author:** Malachevsky, A.A. / Малачевский А.А.  
**ORCID:** 0009-0008-6009-3196  
**Date:** 2026-09-06  
**Status:** `PROVED / FINITE-EPSILON-AND-t UNITARY TRANSFER / SINGLE ODD-TO-EVEN RELATIVE STAGE POLYNOMIAL`

## 0. Purpose

`ARTICLE-III-UNITARY-TWO-TAIL-EPSILON-BINDING-v0.1.md` closes the first two-tail scale: after the carrier and local reduction, an explicit unitary phase perturbation with

\[
\epsilon_d=c_\epsilon d^{-16}
\]

imposes

\[
\beta_j=r,
\qquad
\delta_j=s
\]

with an inverse-polynomial gap.

The remaining odd-to-even wall is simultaneous insertion of the cross-plane graph perturbation while preserving that first-scale gap.

This note proves the required two-scale theorem. The final residual kernel is exactly the three-dimensional relative Hamiltonian gauge, and the whole **single odd-to-even relative extension stage** has an inverse-polynomial gap using genuine unitary Coxeter faces throughout.

The theorem is stage-local. It does not by itself imply a polynomial lower frame bound after recursively multiplying many stage losses across all dimensions.

---

## 1. Fixed first scale

Let `d>=3` be odd,

\[
n=d+1,
\qquad
N=d+2.
\]

Use the unitary five-defect carrier from

`ARTICLE-III-UNITARY-FIVE-DEFECT-CARRIER-v0.1.md`.

After the carrier, the relative matrix variable is

\[
R=rE_{nN}+sE_{Nn}.
\]

Use the unitary two-tail anchor and local Givens faces from

`ARTICLE-III-UNITARY-TWO-TAIL-EPSILON-BINDING-v0.1.md`.

Fix

\[
\boxed{
\epsilon=\epsilon_d=c_\epsilon d^{-16},
\qquad
\mu=e^{i\epsilon_d}.
}
\tag{1.1}
\]

At `t=0`, the local-plus-first-binding matrix has residual kernel

\[
\boxed{
K_\epsilon
=
\{\alpha_1,\ldots,\alpha_d,
\gamma_1,\ldots,\gamma_d,r,s\},
}
\tag{1.2}
\]

of complex dimension `2d+2`, and

\[
\boxed{
\sigma_{\min}^{+}(M(\epsilon_d,0))
\ge c_0d^{-16}.
}
\tag{1.3}
\]

---

## 2. Simultaneous unitary two-scale face family

Choose the same connected non-bipartite `d`-edge graph used in the global binding theorem:

- triangle `1-2-3-1`;
- edges `1-j` for `j>=4`.

For the directed edge attached to face `j`, denote its partner by `k_j`.

Choose the compensating old index `ell_j` so that

\[
\ell_j\notin\{j,k_j\}.
\]

This is possible because `d>=3`.

Let

\[
D_j(\epsilon)
\]

be the determinant-one diagonal phase used in the first binding scale: eigenvalue `mu` at coordinate `n`, `mu^{-1}` at `ell_j`, and `1` elsewhere.

Set

\[
K_{k_jn}=E_{k_jn}-E_{nk_j},
\]

and define

\[
\boxed{
B_j(\epsilon,t)
=
\Lambda D_j(\epsilon)
\exp(tK_{k_jn}).
}
\tag{2.1}
\]

Every factor is unitary with determinant one. Hence

\[
\boxed{
B_j(\epsilon,t)\in SU(n)
}
\tag{2.2}
\]

for every real `epsilon,t`.

Use the paired Coxeter branch

\[
(U_j,B_j(\epsilon,t)),
\qquad
(B_j(\epsilon,t)^{-1},U_j^{-1}),
\]

where `U_j` is the fixed `pi/4` Givens rotation on the `(j,n)` plane.

---

## 3. Exact three-coordinate second-order graph coefficient at nonzero epsilon

Fix one edge `{j,k}` and abbreviate

\[
a=\lambda_j,
\qquad
b=\lambda_k,
\qquad
c=\mu.
\]

Because the compensating coordinate `ell_j` is outside `{j,k}`, the restriction of the diagonal factor to

\[
\operatorname{span}\{e_j,e_k,e_n\}
\]

is exactly

\[
\operatorname{diag}(a,b,c).
\]

After the first scale has imposed

\[
\beta_j=r,
\qquad
\delta_j=s,
\]

the variables carrying an external `N` index do not contribute to the old-old output entries used by the graph reduction.

The exact unitary cross-plane calculation therefore applies with tail eigenvalue `c=mu`.

After eliminating the first-order bulk correction, the two unnormalized reduced rows are

\[
\ell_j^+
=
2^{-1/2}
\frac{\sin^2t}{\cos t}
\frac{b(a-c)}{a(b-c)}
(\alpha_j+\gamma_k),
\tag{3.1}
\]

and

\[
\ell_j^-
=
2^{-1/2}
\frac{\sin^2t}{\cos t}
\frac{a-c}{b-c}
(\alpha_k+\gamma_j).
\tag{3.2}
\]

The local cokernel vector has norm

\[
\sqrt2|a-c|.
\]

Hence in orthonormal cokernel coordinates the common edge-weight modulus is

\[
\boxed{
\widetilde w_{jk}(\epsilon)
=
\frac1{2|b-c|}
=
\frac1{2|\lambda_k-e^{i\epsilon}|}.
}
\tag{3.3}
\]

This identity is exact at the second-order coefficient.

---

## 4. Uniform polynomial weight window at epsilon_d

The unitary Sidon-tail anchor satisfies

\[
|\lambda_k-1|\ge c_Sd^{-4}.
\]

Also

\[
|e^{i\epsilon_d}-1|
\le|\epsilon_d|
=O(d^{-16}).
\]

After choosing `c_epsilon` sufficiently small,

\[
\boxed{
|\lambda_k-e^{i\epsilon_d}|
\ge\frac{c_S}{2}d^{-4}.
}
\tag{4.1}
\]

The trivial upper bound is `2`. Therefore

\[
\boxed{
\frac14
\le
\widetilde w_{jk}(\epsilon_d)
\le
C_1d^4.
}
\tag{4.2}
\]

Let `G_d(epsilon_d)` denote the resulting weighted graph operator on the `2d` variables `(alpha,gamma)`. From the graph spectral-gap theorem,

\[
\sigma_{\min}^{+}(B_d)>d^{-1/2}.
\]

Thus, on the orthogonal complement of the one-dimensional graph gauge,

\[
\boxed{
\sigma_{\min}^{+}(G_d(\epsilon_d))
\ge
\frac1{4\sqrt d}.
}
\tag{4.3}
\]

The two variables `r,s` are untouched by this graph block, so the second-order kernel is exactly three-dimensional:

\[
\boxed{
\alpha_1=\cdots=\alpha_d=q,
\qquad
\gamma_1=\cdots=\gamma_d=-q,
\qquad
r,s\ \text{free}.
}
\tag{4.4}
\]

This is precisely the relative Hamiltonian gauge.

---

## 5. Adapted Schur splitting at fixed epsilon_d

Fix `epsilon=epsilon_d` and write the complete `d`-face local measurement matrix as

\[
M_d(t)=M_d(\epsilon_d,t).
\]

Choose orthogonal domain and codomain decompositions associated with

\[
K_\epsilon=\ker M_d(0)
\]

and its cokernel. In adapted coordinates,

\[
M_d(t)
=
\begin{pmatrix}
A(t)&B(t)\\
C(t)&D(t)
\end{pmatrix},
\tag{5.1}
\]

where `A(0)` is invertible and

\[
B(0)=C(0)=D(0)=0.
\]

By (1.3),

\[
\boxed{
\|A(0)^{-1}\|\le C_2d^{16}.
}
\tag{5.2}
\]

The matrix dimension is `O(d^3)`. Every scalar coefficient is a bounded trigonometric polynomial in `t`, with `epsilon_d` fixed. Therefore for `r=0,1,2,3`,

\[
\boxed{
\|M_d^{(r)}(t)\|
\le C_3d^3,
\qquad |t|\le1/4.
}
\tag{5.3}
\]

---

## 6. Polynomial bulk-invertibility neighborhood

From (5.2)--(5.3), the Neumann criterion gives

\[
A(t)\text{ invertible}
\]

for

\[
\boxed{
|t|\le c_4d^{-19},
}
\tag{6.1}
\]

and there

\[
\boxed{
\|A(t)^{-1}\|\le C_4d^{16}.
}
\tag{6.2}
\]

Put

\[
H(t)=A(t)^{-1}.
\]

Differentiating `AH=I` gives the crude hierarchy

\[
\|H'(t)\|\le C_5d^{35},
\tag{6.3}
\]

\[
\|H''(t)\|\le C_6d^{54},
\tag{6.4}
\]

\[
\boxed{
\|H'''(t)\|\le C_7d^{73}.
}
\tag{6.5}
\]

No exponent is optimized.

---

## 7. The reduced graph Schur map

Define

\[
\boxed{
S_d(t)=D(t)-C(t)A(t)^{-1}B(t).
}
\tag{7.1}
\]

By support of the first-order cross-plane forcing:

- it occurs only in nonexceptional old-old entries;
- those entries lie in the already invertible local bulk;
- the first-scale tail cokernel rows `(j,N)` and `(N,j)` are untouched to first order because the external coordinate `N` is fixed.

Hence

\[
\boxed{
S_d(0)=0,
\qquad
S_d'(0)=0.
}
\tag{7.2}
\]

Sections 3--4 give

\[
\boxed{
\frac12S_d''(0)
=G_d(\epsilon_d)\oplus0_{\operatorname{span}\{r,s\}}.
}
\tag{7.3}
\]

Thus the nonzero second-order singular gap is at least `1/(4 sqrt d)`.

---

## 8. Cubic simultaneous remainder

Differentiate (7.1) three times. Each term is a product of derivatives of `B,C,D` and of `H=A^{-1}`. Using (5.3) and (6.2)--(6.5), the worst crude monomial has size

\[
(Cd^3)(Cd^{73})(Cd^3)=Cd^{79}.
\]

Therefore

\[
\boxed{
\|S_d'''(t)\|
\le C_8d^{79}
}
\tag{8.1}
\]

throughout (6.1).

Taylor's theorem gives

\[
\boxed{
\|S_d(t)-t^2G_d(\epsilon_d)\|
\le C_9d^{79}|t|^3.
}
\tag{8.2}
\]

Here `G_d(epsilon_d)` is understood as zero on the `r,s` gauge coordinates.

---

## 9. Polynomial finite t

Choose

\[
\boxed{
t_d=c_td^{-81}}
\tag{9.1}
\]

with a sufficiently small absolute `c_t>0`.

Then `t_d` lies inside the bulk-invertibility region (6.1), and

\[
C_9d^{79}|t_d|^3
\le
\frac{t_d^2}{8\sqrt d}.
\]

Weyl's inequality and (4.3) yield, on the complement of the three-dimensional relative gauge,

\[
\boxed{
\sigma_{\min}^{+}(S_d(t_d))
\ge
\frac{t_d^2}{8\sqrt d}.
}
\tag{9.2}
\]

Hence, after weakening the half-integer exponent,

\[
\boxed{
\sigma_{\min}^{+}(S_d(t_d))
\ge c_{10}d^{-163}.
}
\tag{9.3}
\]

The graph condition number remains polynomial; the very small `t_d` changes the absolute signal scale but not the leading reduced angular geometry.

---

## 10. Full local two-scale stage

The standard Schur factorization is

\[
M_d(t)
=
\begin{pmatrix}
I&0\\
C(t)A(t)^{-1}&I
\end{pmatrix}
\begin{pmatrix}
A(t)&0\\
0&S_d(t)
\end{pmatrix}
\begin{pmatrix}
I&A(t)^{-1}B(t)\\
0&I
\end{pmatrix}.
\tag{10.1}
\]

Because `B(0)=C(0)=0`,

\[
\|A(t_d)^{-1}B(t_d)\|
+
\|C(t_d)A(t_d)^{-1}\|
\le
C d^{19}|t_d|
=O(d^{-62}).
\tag{10.2}
\]

Thus both triangular factors and their inverses are uniformly bounded.

The bulk gap is `Omega(d^-16)` while the graph Schur gap is `Omega(d^-163)`. Therefore

\[
\boxed{
\sigma_{\min}^{+}(M_d(\epsilon_d,t_d))
\ge c_{11}d^{-163}
}
\tag{10.3}
\]

on the complement of the three-dimensional relative Hamiltonian gauge.

Since `||M_d||=O(d^3)`, one may record

\[
\boxed{
\kappa(M_d|_{G_{rel}^\perp})
=O(d^{166}).
}
\tag{10.4}
\]

Again the exponent is deliberately nonoptimized.

---

## 11. Incorporating the unitary five-defect carrier

Now include the carrier from `ARTICLE-III-UNITARY-FIVE-DEFECT-CARRIER-v0.1.md`.

The carrier has no columns in the `P_j,Q_j` variables because its transport pair is block-Levi: all centered carrier inputs are block diagonal. Therefore, after splitting carrier-observed coordinates from the residual variables, the combined new-face measurement has block form

\[
\mathcal T_d
=
\begin{pmatrix}
\mathcal C_d&0\\
L_d&M_d
\end{pmatrix}.
\tag{11.1}
\]

The carrier gap obeys

\[
\sigma_{\min}^{+}(\mathcal C_d)
\ge c d^{-28}.
\tag{11.2}
\]

The lower-left coupling has norm at most `O(d^3)` in the same normalized coordinate scale. Hence

\[
\|L_d\mathcal C_d^{-1}\|
=O(d^{31}).
\tag{11.3}
\]

Left block elimination gives

\[
\begin{pmatrix}
I&0\\
-L_d\mathcal C_d^{-1}&I
\end{pmatrix}
\mathcal T_d
=
\operatorname{diag}(\mathcal C_d,M_d).
\]

Therefore, after a conservative polynomial weakening,

\[
\boxed{
\sigma_{\min}^{+}(\mathcal T_d)
\ge c_{12}d^{-194}.
}
\tag{11.4}
\]

The only kernel is the three-dimensional relative Hamiltonian gauge.

This proves that the complete **new relative odd-to-even stage** — carrier plus two-tail local reduction plus epsilon binding plus graph t binding — is polynomially conditioned and explicitly unitary.

---

## 12. Main theorem

### Theorem 12.1 — single-stage quantitative odd-to-even transfer

For every odd `d>=3`, there exists a fully explicit family of `d+1` new genuine unitary Coxeter square faces realizing the odd-to-even extension-ready transfer in dimension `n=d+1` such that, on the relative quotient added at this extension step,

\[
\boxed{
\ker\mathcal T_d
=\mathcal D_{rel},
\qquad
\dim\mathcal D_{rel}=3,
}
\]

and

\[
\boxed{
\sigma_{\min}^{+}(\mathcal T_d)
\ge c d^{-194}.
}
\tag{12.1}
\]

Every transport is in `SU(n)` before the rank or spectral calculation. No Zariski-density return is used in any layer of this odd-to-even relative stage.

The exponent `194` is a proof-of-polynomiality exponent, not an optimization claim.

---

## 13. What is now closed

The single odd-to-even relative extension stage is quantitatively controlled at all of its formerly qualitative layers:

1. five-defect carrier — direct unitary, inverse-polynomial;
2. two-tail local reduction — direct unitary, inverse-polynomial;
3. first `epsilon` star binding — direct unitary, finite-parameter inverse-polynomial;
4. second cross-plane graph binding — direct unitary;
5. simultaneous `epsilon/t` remainder — inverse-polynomial;
6. combined carrier-plus-local stage — inverse-polynomial.

Thus neither parity step contains an intrinsic superpolynomial obstruction at the level of a **single extension stage**.

---

## 14. The new global barrier: accumulation across dimensions

Stage-wise polynomiality does not automatically imply an all-dimensional polynomial sharp condition number.

If a recursive construction only gives a transfer inequality of the schematic form

\[
g_{d+1}\ge d^{-C}g_d,
\]

then iterating from a fixed base dimension yields

\[
g_d
\ge
\prod_{k\le d}k^{-C}
=
(d!)^{-C}
=
\exp[-\Theta(d\log d)],
\]

which is superpolynomially small.

Therefore the next Article-III problem is no longer to repair a local parity block. It is to prevent **multiplicative accumulation of polynomial stage losses**.

Two routes are now structurally distinct:

- prove a near-isometric transfer law whose accumulated logarithmic loss is only `O(log d)`;
- abandon recursive inheritance and construct a fresh dimension-`d` sharp unitary design with a direct global lower-frame bound.

This is the new active barrier.

---

## 15. Claim firewall

This note proves polynomial conditioning of one complete relative odd-to-even extension stage. It does not prove:

- a polynomial lower frame bound for the recursively inherited full sharp design in dimension `d`;
- that the current large exponents are optimal or close to optimal;
- that oversampling is unnecessary for robust tomography;
- sample-complexity or experimental-noise bounds;
- a non-Markovian/process-tensor extension.
