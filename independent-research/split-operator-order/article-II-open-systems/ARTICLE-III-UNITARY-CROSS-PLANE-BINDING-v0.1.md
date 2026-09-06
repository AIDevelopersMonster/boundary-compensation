# Article III — Unitary Cross-Plane Binding and Direct Unitary Global Completion

**Author:** Malachevsky, A.A. / Малачевский А.А.  
**ORCID:** 0009-0008-6009-3196  
**Date:** 2026-09-06  
**Status:** `PROVED / UNITARY SECOND-ORDER BINDING / ZARISKI-FREE GLOBAL BINDING EXISTENCE`

## 0. Purpose

The remaining nonunitary ingredient in the Article-II global binding witness is the cross-plane perturbation

\[
\Lambda[I+t(E_{kn}+E_{nk})].
\]

The local two-level probe has already been replaced by an explicit Givens unitary in `ARTICLE-III-UNITARY-LOCAL-FACE-REPLACEMENT-v0.1.md`, and the diagonal Sidon anchor has already been placed on the unit circle with polynomial separation.

This note proves that the cross-plane perturbation can also be chosen unitary while retaining exactly the same reduced graph-binding relations, up to nonzero row weights. Consequently the even-to-odd global binding step admits a direct analytic family of genuine unitary Coxeter faces; the old qualitative Zariski-density return is not needed for existence at this stage.

The finite-\(t\) polynomial lower-frame problem remains separate and is stated explicitly at the end.

---

## 1. Unitary setup

Let \(n=d+1\), fix distinct old indices \(j,k\le d\), and let

\[
\Lambda=\operatorname{diag}(\lambda_1,\ldots,\lambda_n)\in SU(n)
\]

be a multiplicative-Sidon diagonal anchor with all \(|\lambda_r|=1\).

The determinant-one condition causes no loss of the quantitative Sidon construction: after choosing the unit-circle phases of `ARTICLE-III-POLYNOMIAL-SIDON-PHASES-v0.1.md`, multiply all phases by one common unit scalar whose \(n\)-th power corrects the determinant. All one-point and two-point separation moduli are unchanged.

Let

\[
U_j(\theta)
\]

be the explicit local Givens rotation from the unitary local-face theorem, with

\[
s_\theta=\sin\theta\ne0.
\]

On the \((k,n)\)-plane define

\[
K_{kn}=E_{kn}-E_{nk},
\qquad K_{kn}^*=-K_{kn},
\]

and

\[
R_{kn}(t)=e^{tK_{kn}}.
\]

Thus

\[
R_{kn}(t)|_{\operatorname{span}\{e_k,e_n\}}
=
\begin{pmatrix}
\cos t&\sin t\\
-\sin t&\cos t
\end{pmatrix}.
\]

Set

\[
\boxed{
B^u_{j,k}(t)=\Lambda R_{kn}(t)\in SU(n).
}
\tag{1.1}
\]

The paired branches are

\[
\Gamma_D(U_j(\theta),B^u_{j,k}(t)),
\]

and

\[
\Gamma_D((B^u_{j,k}(t))^{-1},U_j(\theta)^{-1}).
\]

---

## 2. Residual local kernel

At \(t=0\), the \(j\)-th local face is the unperturbed unitary face \((U_j(\theta),\Lambda)\). After the local bulk has been eliminated, the residual kernel has the usual form

\[
P_r=\alpha_rE_{rn},
\qquad
Q_r=\gamma_rE_{nr}.
\tag{2.1}
\]

Fix one residual vector and abbreviate

\[
a=\lambda_j,
\qquad
b=\lambda_k,
\qquad
c=\lambda_n.
\]

Only the three coordinate directions \(j,k,n\) enter the following calculation.

---

## 3. Exact finite-\(t\) single-edge elimination

Allow the \(j\)-th local variables to acquire the two bulk corrections

\[
P_j
=
\alpha_jE_{jn}+xE_{jk},
\]

\[
Q_j
=
\gamma_jE_{nj}+yE_{kj},
\tag{3.1}
\]

while keeping

\[
P_k=\alpha_kE_{kn},
\qquad
Q_k=\gamma_kE_{nk}
\]

for this single-edge reduction.

A direct substitution into the two Leibniz-defect branches gives only four potentially nonzero output entries. The two bulk equations are

\[
0
=
s_\theta
\left[
 c\sin t\,(\alpha_j+\gamma_k)
-(b-c)\cos t\,x
\right]
\tag{3.2}
\]

at \((j,k)\), and

\[
0
=
\frac{s_\theta}{bc}
\left[
 b\sin t\,(\alpha_k+\gamma_j)
+(b-c)\cos t\,y
\right]
\tag{3.3}
\]

at \((k,j)\).

Whenever \(\cos t\ne0\), these are solved exactly by

\[
\boxed{
 x
=
\frac{c\tan t}{b-c}(\alpha_j+\gamma_k),
}
\tag{3.4}
\]

and

\[
\boxed{
 y
=
-\frac{b\tan t}{b-c}(\alpha_k+\gamma_j).
}
\tag{3.5}
\]

After this exact elimination, the only remaining outputs are the exceptional local-cokernel positions:

\[
\Gamma_+|_{(j,n)}
=
-s_\theta
\frac{bc\sin^2t}{(b-c)\cos t}
(\alpha_j+\gamma_k),
\tag{3.6}
\]

and

\[
\Gamma_-|_{(n,j)}
=
 s_\theta
\frac{\sin^2t}{(b-c)\cos t}
(\alpha_k+\gamma_j).
\tag{3.7}
\]

No Taylor approximation is used in (3.2)--(3.7); these identities are exact for the isolated three-coordinate edge calculation.

---

## 4. Local cokernel projection

At the exceptional position \((j,n)\), the unperturbed unitary local branches are proportional on the surviving \(Q_j(j,n)\) coordinate. A left-cokernel functional is

\[
\ell_j^+
=
(a^{-1}-c^{-1})z_+
-(a-c)z_-.
\tag{4.1}
\]

At \((n,j)\), a left-cokernel functional is

\[
\ell_j^-
=
(c^{-1}-a^{-1})z_+
+(a-c)z_-.
\tag{4.2}
\]

Applying these functionals to (3.6)--(3.7) gives the exact single-edge reduced coefficients

\[
\boxed{
\ell_j^+
=
 s_\theta
\frac{\sin^2t}{\cos t}
\frac{b(a-c)}{a(b-c)}
(\alpha_j+\gamma_k),
}
\tag{4.3}
\]

and

\[
\boxed{
\ell_j^-
=
 s_\theta
\frac{\sin^2t}{\cos t}
\frac{a-c}{b-c}
(\alpha_k+\gamma_j).
}
\tag{4.4}
\]

Thus, whenever

\[
\sin\theta\ne0,
\qquad
\sin t\ne0,
\qquad
\cos t\ne0,
\]

and \(a,b,c\) are distinct, the reduced kernel relations are exactly

\[
\boxed{
\alpha_j+\gamma_k=0,
\qquad
\alpha_k+\gamma_j=0.
}
\tag{4.5}
\]

These are the same graph-binding relations as in `GLOBAL-BINDING-LEMMA-v0.1.md`.

---

## 5. Second-order coefficient and polynomial row weights

As \(t\to0\),

\[
\frac{\sin^2t}{\cos t}
=t^2+O(t^4).
\]

Hence the second-order reduced Schur coefficient for one edge is, up to the common factor \(s_\theta\), exactly the old graph weight:

\[
\boxed{
 w_{jk}^{(1)}
=
\frac{\lambda_k(\lambda_j-\lambda_n)}
{\lambda_j(\lambda_k-\lambda_n)},
\qquad
 w_{jk}^{(2)}
=
\frac{\lambda_j-\lambda_n}
{\lambda_k-\lambda_n}.
}
\tag{5.1}
\]

Because all phases have unit modulus,

\[
|w_{jk}^{(1)}|=|w_{jk}^{(2)}|
=
\frac{|\lambda_j-\lambda_n|}
{|\lambda_k-\lambda_n|}.
\tag{5.2}
\]

Using the polynomial Sidon separation

\[
|\lambda_r-\lambda_s|
\ge
\delta_n,
\qquad
\delta_n=\frac1{6\pi n^3},
\]

and the trivial upper bound \(|\lambda_r-\lambda_s|\le2\), one gets

\[
\boxed{
\frac{1}{12\pi n^3}
\le
|w_{jk}^{(a)}|
\le
12\pi n^3,
\qquad a=1,2.
}
\tag{5.3}
\]

The extra factor \(|s_\theta|\) is common to all second-order rows and therefore does not affect their condition number.

For the uniform choice

\[
\theta=\frac\pi4,
\]

one has \(|s_\theta|=2^{-1/2}\).

Combining (5.3) with the graph spectral gap from `ARTICLE-III-BINDING-GRAPH-SPECTRAL-GAP-v0.1.md`, the second-order reduced binding operator on the gauge-orthogonal sector has inverse-polynomial smallest singular value and polynomial condition number. In particular, for the star-triangle binding graph used there,

\[
\sigma_{\min}^+(S_2)
\ge
\frac{1}{12\sqrt2\pi\,n^3\sqrt d},
\tag{5.4}
\]

and the crude condition estimate remains

\[
\boxed{
\kappa(S_2)=O(d^7).
}
\tag{5.5}
\]

The exponent is not asserted optimal.

---

## 6. Direct unitary global binding existence

Take the connected non-bipartite \(d\)-edge binding graph of `GLOBAL-BINDING-LEMMA-v0.1.md`. For the directed edge assigned to the \(j\)-th face, replace the old nonunitary perturbation by

\[
B_j^u(t)=\Lambda e^{t(E_{k_jn}-E_{nk_j})}.
\tag{6.1}
\]

Let \(M_u(t)\) be the full measurement matrix on the invisible quotient supplied by these \(d\) unitary faces.

At \(t=0\), the local bulk block has kernel \(K_{loc}\) of dimension \(2d\). After choosing row and column complements to this kernel and its cokernel, the reduced Schur map has vanishing constant and first-order terms. By Sections 4--5, its second-order coefficient is the same weighted connected non-bipartite graph-binding operator as before, with kernel exactly the Hamiltonian gauge line.

Therefore a maximal minor of \(M_u(t)\) has a nonzero leading coefficient. Hence for all sufficiently small nonzero real \(t\), outside a discrete exceptional set,

\[
\boxed{
\operatorname{rank}M_u(t)=2dn^2-1.
}
\tag{6.2}
\]

Every transport entering this construction is unitary:

- \(U_j(\theta)\in SU(n)\);
- \(\Lambda\in SU(n)\);
- \(B_j^u(t)\in SU(n)\).

The engineered-square realization then converts each ordered pair into a genuine unitary Coxeter square.

### Theorem 6.1 — Zariski-free unitary global binding

For every \(d\ge3\), once the block-diagonal restriction quotient has been resolved, there exist exactly \(d\) genuine unitary Coxeter square faces whose joint invisible kernel is precisely the one-dimensional Hamiltonian gauge line.

The existence proof is direct on an analytic unitary family and no longer requires Zariski density of \(SU(n)\) in \(SL_n(\mathbb C)\) for the global binding stage.

---

## 7. What this closes

The following potential sources of a qualitative-to-unitary gap are now removed for the even-to-odd global binding stage:

1. diagonal Sidon anchor: explicit unitary, polynomially separated;
2. local two-level probe: explicit unitary Givens rotation;
3. cross-plane binding perturbation: explicit unitary rotation;
4. reduced graph-binding coefficient: exactly the same edge relations as the complex witness;
5. unitary existence: obtained directly from an analytic unitary curve, not from Zariski return.

Thus the remaining difficulty is no longer **unitary realizability** of the binding mechanism.

---

## 8. Remaining quantitative wall

The theorem proves inverse-polynomial control of the **second-order coefficient** \(S_2\), but it does not yet give a dimension-uniform lower bound for the full finite-\(t\) Schur map

\[
S(t)=t^2S_2+O(t^3)
\]

when all \(d\) faces are perturbed simultaneously.

The isolated three-coordinate calculation is exact and has the common factor \(\sin^2t/\cos t\), but simultaneous faces share the global variables \(P_j,Q_j\). Higher-order cross-edge couplings can therefore enter the full reduced Schur map.

The next strict target is a polynomial remainder theorem of the form

\[
\boxed{
\|S(t)-t^2S_2\|
\le
C d^m |t|^3
}
\tag{8.1}
\]

on a polynomial-size neighborhood of \(t=0\), with absolute \(C,m\). Combined with (5.4), this would allow a choice

\[
|t|\ge d^{-O(1)}
\]

and yield an inverse-polynomial finite-\(t\) binding gap.

That finite-parameter estimate, together with accumulated Schur-coupling control across the extension hierarchy, is now the principal remaining robustness barrier.

---

## 9. Claim firewall

This note proves direct unitary global-binding existence and polynomial separation of the second-order reduced coefficient. It does not yet prove:

- a polynomial lower bound for the full finite-\(t\) global binding map;
- polynomial conditioning of the complete all-dimensional sharp design;
- a polynomially stable odd-to-even two-tail transfer;
- necessity of oversampling;
- statistical or experimental noise bounds.
