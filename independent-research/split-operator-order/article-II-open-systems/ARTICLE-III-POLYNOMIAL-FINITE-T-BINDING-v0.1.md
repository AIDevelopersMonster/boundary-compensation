# Article III — Polynomial Finite-Parameter Gap for the Unitary Global-Binding Stage

**Author:** Malachevsky, A.A. / Малачевский А.А.  
**ORCID:** 0009-0008-6009-3196  
**Date:** 2026-09-06  
**Status:** `PROVED / POLYNOMIAL FINITE-t BINDING GAP / EVEN-TO-ODD STAGE QUANTITATIVELY UNITARY`

## 0. Purpose

`ARTICLE-III-UNITARY-CROSS-PLANE-BINDING-v0.1.md` proves that the second-order reduced Schur coefficient of the direct unitary binding family is a weighted connected non-bipartite graph operator with inverse-polynomial spectral gap. What remained open there was the finite-parameter passage

\[
S(t)=t^2S_2+O(t^3)
\]

when all \(d\) faces are perturbed simultaneously.

This note closes that local analytic wall. A deliberately crude but explicit polynomial derivative estimate gives a polynomial-size admissible choice of \(t\), an inverse-polynomial finite-\(t\) reduced gap, and consequently a polynomially conditioned **single even-to-odd invisible-completion stage**.

This is not yet a theorem that the full all-dimensional sharp design has one fixed polynomial condition-number exponent: repeated parity transfers and the odd-to-even two-tail carrier still require their own quantitative analysis.

---

## 1. Coordinate model and matrix size

Let

\[
n=d+1,
\qquad d\ge3.
\]

After the old block-diagonal restriction quotient has been resolved, the complexified invisible space is parametrized by

\[
P_j=D(E_{jn}),
\qquad
Q_j=D(E_{nj}),
\qquad j=1,\ldots,d,
\]

and has complex dimension

\[
m_d=2dn^2.
\tag{1.1}
\]

The \(d\) paired unitary square faces supply the same number of scalar output coordinates. Let

\[
M_d(t)
\]

be the resulting square complex measurement matrix for the simultaneous unitary perturbations

\[
B_j^u(t)
=
\Lambda\exp[t(E_{k_jn}-E_{nk_j})],
\]

where the \(k_j\) form the fixed connected non-bipartite star-triangle binding graph.

Use the explicit unitary local probes with

\[
\theta=\frac\pi4.
\]

All domain and output matrix-unit coordinates carry their standard Euclidean/Frobenius norms.

Since \(n\le2d\) for \(d\ge1\),

\[
\boxed{m_d\le8d^3.}
\tag{1.2}
\]

---

## 2. Polynomial lower bound for the unperturbed bulk block

At \(t=0\), the local unitary reduction is a direct sum of the nonexceptional \(2\times2\) systems from `ARTICLE-III-UNITARY-LOCAL-FACE-REPLACEMENT-v0.1.md`.

Let

\[
\delta_n=\frac1{6\pi n^3}
\]

be the phase-separation constant from `ARTICLE-III-POLYNOMIAL-SIDON-PHASES-v0.1.md`.

Each nonexceptional local determinant has modulus at least

\[
\delta_n^2,
\]

up to the fixed factor \(\sin^2(\pi/4)=1/2\). All entries of the corresponding \(2\times2\) block have absolute value bounded by an absolute constant.

Therefore there exists an absolute \(c_0>0\) such that the nonzero singular values of the full unperturbed local matrix obey

\[
\boxed{
\sigma_{\min}^{+}(M_d(0))
\ge
c_0 n^{-6}.
}
\tag{2.1}
\]

Choose orthogonal domain and codomain decompositions

\[
\mathbb C^{m_d}=X\oplus K,
\qquad
\mathbb C^{m_d}=Y\oplus C,
\]

where

\[
K=\ker M_d(0),
\qquad
C=\ker M_d(0)^*.
\]

In these decompositions write

\[
M_d(t)
=
\begin{pmatrix}
A(t)&B(t)\\
C(t)&D(t)
\end{pmatrix}.
\tag{2.2}
\]

Then \(A(0):X\to Y\) is invertible and

\[
\boxed{
\|A(0)^{-1}\|
\le C_0 d^6
}
\tag{2.3}
\]

for an absolute \(C_0\).

Also

\[
B(0)=C(0)=D(0)=0.
\tag{2.4}
\]

---

## 3. Uniform derivative bounds

Every entry of \(M_d(t)\) is a finite linear combination of products of:

- unit-modulus diagonal phases;
- fixed Givens coefficients \(2^{-1/2}\);
- \(\sin t\) and \(\cos t\).

The Leibniz-defect formulas contain only a bounded number of such terms per scalar coefficient. Therefore, for \(|t|\le1/4\), every scalar entry and each of its first three derivatives is bounded by one absolute constant.

The matrix has at most \(m_d^2\) scalar entries. Hence its Frobenius norm gives the crude but sufficient operator estimate

\[
\boxed{
\|M_d^{(r)}(t)\|
\le C_1 d^3,
\qquad r=0,1,2,3,
\qquad |t|\le\frac14.
}
\tag{3.1}
\]

Orthogonal compression to the four blocks in (2.2) cannot increase operator norm, so the same estimate holds for \(A,B,C,D\) and their first three derivatives.

---

## 4. Polynomial neighborhood of bulk invertibility

Put

\[
H(t)=A(t)^{-1}.
\]

By (3.1),

\[
\|A(t)-A(0)\|
\le C_1d^3|t|.
\]

Together with (2.3), the Neumann criterion shows that there exists an absolute \(c_1>0\) such that

\[
\boxed{
|t|\le c_1d^{-9}
}
\tag{4.1}
\]

implies

\[
A(t)\text{ invertible},
\qquad
\boxed{
\|H(t)\|\le2C_0d^6.
}
\tag{4.2}
\]

Differentiate \(A(t)H(t)=I\). Using (3.1) and (4.2) gives the crude hierarchy

\[
\|H'(t)\|\le C_2d^{15},
\tag{4.3}
\]

\[
\|H''(t)\|\le C_3d^{24},
\tag{4.4}
\]

\[
\boxed{
\|H'''(t)\|\le C_4d^{33}.
}
\tag{4.5}
\]

No exponent here is claimed optimal.

---

## 5. Schur map and cubic remainder

Define the reduced Schur map on the local kernel by

\[
\boxed{
S_d(t)
=
D(t)-C(t)A(t)^{-1}B(t).
}
\tag{5.1}
\]

The unitary cross-plane calculation proves

\[
S_d(0)=0,
\qquad
S_d'(0)=0,
\tag{5.2}
\]

and

\[
\frac12S_d''(0)=S_{2,d},
\tag{5.3}
\]

where \(S_{2,d}\) is the weighted graph-binding coefficient.

Differentiate (5.1) three times. Every resulting term is a product of derivatives of \(B,C,D\) of order at most three and of \(H\) of order at most three. By (3.1) and (4.2)--(4.5), the worst crude monomial is bounded by

\[
(Cd^3)(Cd^{33})(Cd^3)=Cd^{39}.
\]

Thus there is an absolute \(C_5>0\) such that throughout the neighborhood (4.1),

\[
\boxed{
\|S_d'''(t)\|
\le C_5d^{39}.
}
\tag{5.4}
\]

Taylor's theorem with integral remainder yields

\[
\boxed{
\|S_d(t)-t^2S_{2,d}\|
\le
\frac{C_5}{6}d^{39}|t|^3.
}
\tag{5.5}
\]

This is the required polynomial finite-parameter remainder theorem.

---

## 6. Improved orthonormal second-order graph gap

The explicit cokernel functionals in the unitary cross-plane theorem were not normalized there. In orthonormal cokernel coordinates one gains a useful cancellation.

At \((j,n)\), the left-cokernel vector has two coefficients whose moduli are both

\[
|\lambda_j-\lambda_n|.
\]

Hence its norm is

\[
\sqrt2\,|\lambda_j-\lambda_n|.
\]

Dividing the edge formula by this norm cancels the potentially small numerator \(|\lambda_j-\lambda_n|\). With \(\theta=\pi/4\), the absolute value of every normalized second-order edge-row weight is therefore

\[
\boxed{
\widetilde w_{jk}
=
\frac{1}{2|\lambda_k-\lambda_n|}.
}
\tag{6.1}
\]

The same formula holds for the paired row. Since

\[
\delta_n\le|\lambda_k-\lambda_n|\le2,
\]

we obtain

\[
\boxed{
\frac14
\le
\widetilde w_{jk}
\le
3\pi n^3.
}
\tag{6.2}
\]

Let \(B_d\) denote the unweighted graph-binding incidence operator on the \(2d\) residual slope variables. From `ARTICLE-III-BINDING-GRAPH-SPECTRAL-GAP-v0.1.md`,

\[
\sigma_{\min}^{+}(B_d)>d^{-1/2}.
\]

Therefore on the gauge-orthogonal residual sector,

\[
\boxed{
\sigma_{\min}^{+}(S_{2,d})
\ge
\frac1{4\sqrt d}.
}
\tag{6.3}
\]

Also the graph degree bound and (6.2) give

\[
\|S_{2,d}\|
\le C_6d^{7/2}.
\tag{6.4}
\]

Consequently

\[
\boxed{
\kappa(S_{2,d}|_{G^\perp})
=O(d^4).
}
\tag{6.5}
\]

This improves the earlier crude \(O(d^7)\) row-coordinate estimate; the difference comes from using orthonormal cokernel coordinates rather than the raw algebraic functionals.

---

## 7. Polynomial finite-\(t\) gap

Choose

\[
\boxed{
t_d=c_*d^{-40},
}
\tag{7.1}
\]

where the absolute constant \(c_*>0\) is small enough that

\[
c_*\le c_1
\]

and

\[
\frac{C_5}{6}c_*\le\frac18.
\]

For every \(d\ge3\), (5.5) and (6.3) then give

\[
\|S_d(t_d)-t_d^2S_{2,d}\|
\le
\frac{t_d^2}{8\sqrt d}.
\tag{7.2}
\]

Weyl's singular-value inequality yields

\[
\boxed{
\sigma_{\min}^{+}(S_d(t_d)|_{G^\perp})
\ge
\frac{t_d^2}{8\sqrt d}.
}
\tag{7.3}
\]

Thus

\[
\boxed{
\sigma_{\min}^{+}(S_d(t_d)|_{G^\perp})
\ge
c_2d^{-81}
}
\tag{7.4}
\]

for an absolute \(c_2>0\); the integer exponent \(81\) is a convenient weakening of the direct exponent \(80+1/2\).

Similarly, using (6.4),

\[
\|S_d(t_d)\|
\le C_7 t_d^2d^{7/2},
\]

and hence

\[
\boxed{
\kappa(S_d(t_d)|_{G^\perp})
=O(d^4).
}
\tag{7.5}
\]

The tiny choice of \(t_d\) affects the absolute signal scale through \(t_d^2\), but not the reduced condition-number exponent once the leading graph block dominates the remainder.

---

## 8. Full invisible-stage singular gap

The full block matrix admits the standard Schur factorization

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
\tag{8.1}
\]

Because \(B(0)=C(0)=0\), (3.1), (4.2), and \(t_d=O(d^{-40})\) imply

\[
\|A(t_d)^{-1}B(t_d)\|+
\|C(t_d)A(t_d)^{-1}\|
=O(d^{-31}).
\tag{8.2}
\]

Thus both triangular factors and their inverses have uniformly bounded norm, say at most \(2\), for all \(d\ge3\) after reducing \(c_*\) if necessary.

The bulk block satisfies

\[
\sigma_{\min}(A(t_d))\ge c_3d^{-6},
\]

while the Schur block has the much smaller gap (7.4). Therefore on the complement of the one-dimensional Hamiltonian gauge,

\[
\boxed{
\sigma_{\min}^{+}(M_d(t_d))
\ge
c_4d^{-81}.
}
\tag{8.3}
\]

From (3.1),

\[
\|M_d(t_d)\|\le C_8d^3.
\]

Hence the complete invisible-completion stage obeys the crude polynomial condition estimate

\[
\boxed{
\kappa(M_d(t_d)|_{G^\perp})
=O(d^{84}).
}
\tag{8.4}
\]

The exponent \(84\) is intentionally nonoptimized. Its significance is qualitative but theorem-level: **the direct unitary even-to-odd binding stage has finite-parameter polynomial conditioning.**

---

## 9. Transfer to the normalized real quotient

The calculation above uses the complexified matrix-unit coordinate model in which the Article-II extension proof is simplest.

Returning to the real *-preserving dissipative quotient changes only polynomial coordinate factors:

1. realification of matrix-unit coordinates introduces only dimension-independent \(\sqrt2\)-type factors;
2. the exact Kossakowski quotient whitening has norm distortion exactly \(d\), by `ARTICLE-III-GRAM-SPECTRUM-THEOREM-v0.1.md`;
3. normalized Hilbert-Schmidt output scaling is common and polynomial in \(d\).

Therefore the conclusion "polynomially conditioned single binding stage" is unchanged under the canonical Article-III normalized metric, although the displayed exponent \(84\) is not asserted to remain literally optimal after every normalization convention.

---

## 10. What has now been closed

For the even-to-odd sharp invisible-completion mechanism, the following layers are all quantitatively polynomial:

- unit-circle multiplicative-Sidon separation;
- unperturbed local bulk inversion;
- explicit unitary local Givens faces;
- explicit unitary cross-plane rotations;
- graph-binding spectral gap;
- simultaneous finite-\(t\) Schur remainder;
- full single-stage invisible measurement gap.

Thus there is no superpolynomial obstruction inside the **one-step global binding mechanism itself**.

---

## 11. The next barrier

The unresolved parity bottleneck is now the quantitative version of the repaired odd-to-even extension-ready transfer in

`article-I/research/ODD-TO-EVEN-TRANSFER-AUDIT-REPAIR-v0.1.md`.

That construction contains additional ingredients absent from the even-to-odd binding stage:

- a five-defect carrier;
- a two-dimensional tail;
- two perturbation scales \(\varepsilon\) and \(t\);
- a final qualitative return from determinant-one complex witnesses to unitary witnesses.

The next strict problem is therefore:

\[
\boxed{
\text{replace the odd-to-even carrier and both binding scales by explicit unitary families with polynomial gaps.}
}
\tag{11.1}
\]

Until that is done, this note does not prove an all-dimensional polynomial conditioning theorem.

---

## 12. Claim firewall

This note proves a polynomial finite-parameter gap for one direct unitary even-to-odd invisible-completion stage. It does not prove:

- a uniform polynomial condition number for the complete recursively constructed sharp design in every dimension;
- a quantitative odd-to-even extension-ready transfer;
- a redundancy barrier;
- sample-complexity or experimental noise optimality;
- non-Markovian/process-tensor claims.
