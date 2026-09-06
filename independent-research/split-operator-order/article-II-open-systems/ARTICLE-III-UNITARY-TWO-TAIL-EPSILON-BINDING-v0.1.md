# Article III — Unitary Two-Tail Epsilon Binding with an Inverse-Polynomial Gap

**Author:** Malachevsky, A.A. / Малачевский А.А.  
**ORCID:** 0009-0008-6009-3196  
**Date:** 2026-09-06  
**Status:** `PROVED / UNITARY TWO-TAIL LOCAL LAYER / FINITE-EPSILON GAP / NO ZARISKI RETURN`

## 0. Purpose

After the five-defect carrier has reduced the relative matrix variable to

\[
R=rE_{nN}+sE_{Nn},
\]

the repaired odd-to-even transfer uses `d` local faces to reduce

\[
P_j,Q_j
\]

to four tail slopes per old index and then a first perturbation scale to impose

\[
\beta_j=r,
\qquad
\delta_j=s.
\]

The old proof uses a determinant-one but nonunitary diagonal factor with `mu=1+epsilon`. This note replaces that factor by the unitary phase

\[
\boxed{\mu=e^{i\epsilon}}
\]

and proves a finite-`epsilon` inverse-polynomial singular gap.

---

## 1. A determinant-one unitary Sidon-tail anchor

Let `d>=3` and put `n=d+1`, `N=d+2`. Define

\[
M=2d+1,
\qquad
 e_j=j+Mj^2,
\qquad j=1,\dots,d.
\]

Let

\[
K=16d^3,
\qquad
 f_j=K+e_j,
\qquad
 S=\sum_{j=1}^d f_j,
\]

and

\[
\boxed{
\lambda_j=\exp\!\left(\frac{2\pi i f_j}{S}\right).
}
\tag{1.1}
\]

Then

\[
\prod_{j=1}^d\lambda_j=1,
\]

so

\[
\boxed{
\Lambda=\operatorname{diag}(\lambda_1,\ldots,\lambda_d,1)\in SU(n).
}
\tag{1.2}
\]

The shifted exponent set `{0,f_1,...,f_d}` is Sidon with respect to all pair comparisons needed by the two-tail local reduction: old-old pair equalities reduce to the Sidon property of the `e_j`, while an old-old pair cannot equal an old-plus-tail pair because the unmatched shift `K` dominates every unshifted exponent difference.

Moreover every nontrivial exponent difference relevant to

\[
\lambda_r\lambda_s-\lambda_j
\]

has absolute value at least `1` and at most a fixed fraction of `S`. Since `S=O(d^4)`, there is an absolute `c_S>0` such that

\[
\boxed{
|\lambda_j-1|\ge c_S d^{-4},
}
\tag{1.3}
\]

and, for every nonexceptional old/tail pair,

\[
\boxed{
|\lambda_r\lambda_s-\lambda_j|\ge c_S d^{-4}.
}
\tag{1.4}
\]

No modular wraparound occurs in these comparisons.

---

## 2. Explicit unitary two-tail local faces

For every `j<=d`, let `U_j` act as the identity outside `span{e_j,e_n}` and as

\[
\boxed{
\begin{pmatrix}
2^{-1/2}&2^{-1/2}\\
-2^{-1/2}&2^{-1/2}
\end{pmatrix}
}
\tag{2.1}
\]

on that plane. Then `U_j in SU(n)`.

Embed the pair `(U_j,Lambda)` by scalar one into `M_N`. After the carrier has left only

\[
R=rE_{nN}+sE_{Nn},
\]

the centered branch equations are the unitary-sign version of the repaired two-tail formulas. At every output entry the `2 x 2` determinant for the pair `(P_j,Q_j)` has modulus

\[
\boxed{
|\Delta_{j;r,s}|
=
\frac{|\lambda_j-1|\,|\lambda_j-\lambda_r\lambda_s|}
{|\lambda_j\lambda_r|}.
}
\tag{2.2}
\]

The only zero determinants occur at

\[
(j,n),(j,N),(n,j),(N,j).
\]

Therefore the exact local kernel is

\[
\boxed{
P_j=\alpha_jE_{jn}+\beta_jE_{jN},
\qquad
Q_j=\gamma_jE_{nj}+\delta_jE_{Nj}.
}
\tag{2.3}
\]

By (1.3)--(1.4), every nonexceptional local block has determinant at least

\[
c_S^2d^{-8}.
\]

All local block entries are bounded by an absolute constant, so

\[
\boxed{
\sigma_{\min}^{+}(M_{loc}(0))\ge c_0d^{-8}.
}
\tag{2.4}
\]

Thus the two-tail local layer is explicitly unitary and polynomially invertible.

---

## 3. Unitary first binding scale

Fix, for every `j`, an old compensating index

\[
\ell_j\ne j.
\]

Put

\[
\mu=e^{i\epsilon}
\]

and define

\[
D_j(\epsilon)
=\operatorname{diag}(1,\ldots,\mu^{-1}\text{ at }\ell_j,\ldots,\mu\text{ at }n).
\tag{3.1}
\]

Then

\[
\boxed{D_j(\epsilon)\in SU(n)}
\]

and hence

\[
\boxed{B_j(\epsilon)=\Lambda D_j(\epsilon)\in SU(n).}
\tag{3.2}
\]

Use the paired unitary face

\[
(U_j,B_j(\epsilon)),
\qquad
(B_j(\epsilon)^{-1},U_j^{-1}).
\]

On the local residual kernel (2.3), direct substitution into the centered scalar-one master formula gives exactly

\[
\boxed{
K^+_{jN}
=
2^{-1/2}(\mu-1)(\beta_j-r),
}
\tag{3.3}
\]

and

\[
\boxed{
K^-_{Nj}
=
2^{-1/2}(1-\mu^{-1})(\delta_j-s).
}
\tag{3.4}
\]

The compensating coordinate `ell_j` does not enter these two output positions.

Thus for every nonzero `epsilon` with `mu!=1`, the exact first-scale kernel is

\[
\boxed{
\beta_j=r,
\qquad
\delta_j=s,
\qquad j=1,\ldots,d.
}
\tag{3.5}
\]

The remaining scalar variables are

\[
\alpha_1,\ldots,\alpha_d,
\gamma_1,\ldots,\gamma_d,
r,s.
\]

---

## 4. Exact star-incidence singular gap

The `beta/r` equations form the `d x (d+1)` star-incidence matrix

\[
T_d=[I_d\mid-\mathbf 1].
\]

Hence

\[
T_dT_d^*=I_d+\mathbf1\mathbf1^*,
\]

whose eigenvalues are

\[
1\quad(d-1\text{ times}),
\qquad d+1\quad(1\text{ time}).
\]

Therefore

\[
\boxed{\sigma_{\min}^{+}(T_d)=1.}
\tag{4.1}
\]

The `delta/s` block is identical. Consequently the leading first-scale Schur block has

\[
\boxed{
\sigma_{\min}^{+}(S_1(\epsilon))
=
2^{-1/2}|e^{i\epsilon}-1|
}
\tag{4.2}
\]

before higher-order bulk corrections.

For `|epsilon|<=1`,

\[
|e^{i\epsilon}-1|
=2|\sin(\epsilon/2)|
\ge\frac{2}{\pi}|\epsilon|.
\]

Thus the intrinsic first-scale gap is linear in `|epsilon|` with no dimension loss.

---

## 5. Finite-epsilon Schur remainder

Split the local measurement matrix at `epsilon=0` into its invertible bulk block `A_0` and the residual local kernel/cokernel blocks. By (2.4),

\[
\|A_0^{-1}\|\le C_0d^8.
\tag{5.1}
\]

The total local matrix size is `O(d^3)`. Every scalar entry is a bounded trigonometric polynomial in `epsilon`; therefore the first two derivative operator norms are bounded by

\[
\|M^{(r)}(\epsilon)\|\le C_1d^3,
\qquad r=0,1,2,
\tag{5.2}
\]

for `|epsilon|<=1/4`.

Hence the bulk remains invertible whenever

\[
|\epsilon|\le c_1d^{-11}.
\]

For the Schur complement `S_tail(epsilon)`, the standard differentiation formula

\[
S=D-CA^{-1}B
\]

gives the deliberately crude bound

\[
\boxed{
\|S_{tail}(\epsilon)-\epsilon T_1\|
\le C_2d^{14}\epsilon^2,
}
\tag{5.3}
\]

where `T_1` is the orthonormalized star-incidence first derivative and

\[
\sigma_{\min}^{+}(T_1)\ge c_2>0.
\]

---

## 6. Polynomial finite parameter

Choose

\[
\boxed{
\epsilon_d=c_\epsilon d^{-16}
}
\tag{6.1}
\]

with a sufficiently small absolute `c_epsilon>0`.

Then the quadratic remainder in (5.3) is smaller than one half of the leading singular gap. Therefore

\[
\boxed{
\sigma_{\min}^{+}(S_{tail}(\epsilon_d))
\ge c_3d^{-16}.
}
\tag{6.2}
\]

The full local-plus-first-binding block has bulk gap `Omega(d^-8)` and tail gap `Omega(d^-16)`. Its Schur triangular factors remain uniformly polynomial because

\[
\|A^{-1}B\|+\|CA^{-1}\|=O(d^{11}\epsilon_d)=O(d^{-5}).
\]

Hence, on the complement of the residual `2d+2` dimensional scalar kernel,

\[
\boxed{
\sigma_{\min}^{+}(M_{loc+tail}(\epsilon_d))
\ge c_4d^{-16}.
}
\tag{6.3}
\]

Since the total operator norm is `O(d^3)`, one may record the crude condition estimate

\[
\boxed{
\kappa(M_{loc+tail})=O(d^{19}).
}
\tag{6.4}
\]

No exponent is claimed optimal.

---

## 7. Main theorem

### Theorem 7.1 — direct unitary two-tail epsilon binding

For every odd `d>=3`, after the five-defect carrier has reduced `R` to the two relative tail-gauge directions, there exist `d` explicit genuine unitary Coxeter square faces with first transports `U_j` from (2.1) and second transports `B_j(epsilon_d)` from (3.2), where

\[
\epsilon_d=c_\epsilon d^{-16},
\]

such that:

1. the local bulk is reduced to the four tail slopes (2.3);
2. the first binding scale imposes exactly
   \[
   \beta_j=r,
   \qquad
   \delta_j=s;
   \]
3. the remaining scalar kernel has dimension `2d+2`;
4. the local-plus-first-binding block has inverse-polynomial singular gap
   \[
   \boxed{\sigma_{\min}^{+}\ge c d^{-16}}.
   \]

No Zariski-density return is used anywhere in this layer.

---

## 8. Next strict problem

The remaining odd-to-even scalar kernel is

\[
\alpha_1,\ldots,\alpha_d,
\gamma_1,\ldots,\gamma_d,
r,s.
\]

The second scale must impose the graph relations

\[
\alpha_j+\gamma_k=0,
\qquad
\alpha_k+\gamma_j=0
\]

while preserving the first-scale star gap.

The natural direct unitary family is

\[
\boxed{
B_{j,k}(\epsilon,t)
=
\Lambda D_j(\epsilon)
\exp[t(E_{kn}-E_{nk})],
}
\tag{8.1}
\]

with `ell_j notin {j,k}`.

At fixed `epsilon`, its three-coordinate second-order coefficient is the unitary cross-plane coefficient with tail eigenvalue `mu=e^{i epsilon}`. The next theorem should quantify this coefficient uniformly at `epsilon=epsilon_d` and control the simultaneous finite-`t` remainder.

---

## 9. Claim firewall

This note proves the unitary two-tail local layer and the finite-`epsilon` first binding gap. It does not yet prove:

- the full two-scale odd-to-even transfer gap;
- a finite-`t` graph gap at nonzero `epsilon`;
- all-dimensional polynomial conditioning of the recursively assembled sharp design;
- optimal exponents or necessity of oversampling.
