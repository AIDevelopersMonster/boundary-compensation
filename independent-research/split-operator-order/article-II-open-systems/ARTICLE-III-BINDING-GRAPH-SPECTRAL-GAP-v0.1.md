# Article III — Spectral Gap of the Sharp Binding Graph

**Author:** Malachevsky, A.A. / Малачевский А.А.  
**ORCID:** 0009-0008-6009-3196  
**Date:** 2026-09-06  
**Status:** `PROVED / POLYNOMIAL COMBINATORIAL BINDING GAP`

## 0. Purpose

`GLOBAL-BINDING-LEMMA-v0.1.md` closes the even-to-odd sharp extension by reducing the residual scalar kernel to the edge relations

\[
a_j=b_k,\qquad a_k=b_j
\]

on the explicit connected non-bipartite graph

\[
H_d:\quad 1-2-3-1,\qquad 1-j\ (j=4,\ldots,d).
\]

The original proof used this graph only algebraically: connectedness plus an odd cycle forces the kernel to be the gauge line. For Article III we need the quantitative question: is this binding graph itself badly conditioned?

This note proves that it is not. The unweighted graph-binding operator has a smallest nonzero singular value of order \(d^{-1/2}\) and condition number \(O(d)\).

Therefore any superpolynomial instability in the full Coxeter extension must enter through the analytic weights, local elimination, perturbation scales, or their coupling — not through the bare graph combinatorics.

---

## 1. Binding matrix as an incidence matrix

Let the residual variables be

\[
x=(a_1,\ldots,a_d,b_1,\ldots,b_d)\in\mathbb R^{2d}.
\]

For every edge \(\{j,k\}\in E(H_d)\), introduce the two rows

\[
a_j-b_k,
\qquad
a_k-b_j.
\tag{1.1}
\]

Let \(B_d\) be the resulting \(2d\times 2d\) real matrix. Since \(H_d\) has exactly \(d\) edges, there are exactly \(2d\) scalar rows.

Define the bipartite double cover \(\widetilde H_d\) with vertices

\[
a_1,\ldots,a_d,b_1,\ldots,b_d
\]

and, for each \(\{j,k\}\in E(H_d)\), edges

\[
a_j-b_k,
\qquad a_k-b_j.
\]

Then \(B_d\) is an oriented incidence matrix of \(\widetilde H_d\), up to row signs. Hence

\[
\boxed{
B_d^*B_d=L(\widetilde H_d),
}
\tag{1.2}
\]

where \(L\) is the combinatorial graph Laplacian.

Because \(H_d\) is connected and non-bipartite, its bipartite double cover is connected. Therefore

\[
\ker B_d=\operatorname{span}\{(1,\ldots,1;1,\ldots,1)\},
\]

which is exactly the gauge line in the variables \(a_j=\alpha_j\), \(b_j=-\gamma_j\).

---

## 2. Double-cover spectral decomposition

Let \(A_H\) and \(D_H\) be the adjacency and degree matrices of \(H_d\). In the ordering \((a,b)\),

\[
L(\widetilde H_d)
=
\begin{pmatrix}
D_H & -A_H\\
-A_H & D_H
\end{pmatrix}.
\tag{2.1}
\]

The symmetric subspace \((x,x)\) is invariant and carries

\[
D_H-A_H=L(H_d),
\]

while the antisymmetric subspace \((x,-x)\) is invariant and carries the signless Laplacian

\[
Q(H_d)=D_H+A_H.
\]

Thus

\[
\boxed{
\operatorname{spec}L(\widetilde H_d)
=
\operatorname{spec}L(H_d)
\cup
\operatorname{spec}Q(H_d).
}
\tag{2.2}
\]

---

## 3. Spectrum of the base graph Laplacian

The graph \(H_d\) consists of a triangle on \(1,2,3\) and \(d-3\) leaves attached to vertex \(1\).

Differences of leaf coordinates give eigenvalue \(1\) with multiplicity \(d-4\) when \(d\ge4\). The vector supported on vertices \(2,3\) with values \((1,-1)\) gives eigenvalue \(3\).

On the remaining three-dimensional equitable subspace, with common values

- \(c\) at vertex \(1\),
- \(u\) at vertices \(2,3\),
- \(\ell\) at every leaf,

the Laplacian acts by

\[
\begin{pmatrix}
 d-1 & -2 & -(d-3)\\
 -1 & 1 & 0\\
 -1 & 0 & 1
\end{pmatrix},
\]

whose characteristic polynomial is

\[
\lambda(\lambda-1)(\lambda-d).
\]

Therefore, for \(d\ge4\),

\[
\boxed{
\operatorname{spec}L(H_d)
=
\{0,\ 1^{[d-3]},\ 3,\ d\}.
}
\tag{3.1}
\]

For \(d=3\), this reduces to the triangle spectrum \(\{0,3,3\}\).

---

## 4. The signless sector

For \(Q(H_d)\), leaf differences again have eigenvalue \(1\), and the antisymmetric vector on vertices \(2,3\) also has eigenvalue \(1\). Thus eigenvalue \(1\) has multiplicity \(d-3\) for \(d\ge4\).

On the same equitable three-dimensional subspace, the signless Laplacian has matrix

\[
M_d=
\begin{pmatrix}
 d-1 & 2 & d-3\\
 1 & 3 & 0\\
 1 & 0 & 1
\end{pmatrix}.
\tag{4.1}
\]

Its characteristic polynomial is

\[
\boxed{
p_d(\lambda)
=
\lambda^3-(d+3)\lambda^2+3d\lambda-4.
}
\tag{4.2}
\]

Hence

\[
\boxed{
\operatorname{spec}Q(H_d)
=
\{1^{[d-3]},\ \lambda_{d,1},\lambda_{d,2},\lambda_{d,3}\},
}
\tag{4.3}
\]

where the three remaining eigenvalues are the roots of \(p_d\).

For \(d=3\),

\[
p_3(\lambda)=(\lambda-1)^2(\lambda-4).
\]

---

## 5. Polynomial lower bound for the binding gap

Let \(\lambda_d\) denote the smallest root of \(p_d\). For \(d\ge4\),

\[
p_d(0)=-4.
\]

At \(\lambda=1/d\),

\[
p_d(1/d)
=-1-\frac1d-\frac3{d^2}+\frac1{d^3}<0.
\tag{5.1}
\]

At \(\lambda=2/d\),

\[
p_d(2/d)
=2-\frac4d-\frac{12}{d^2}+\frac8{d^3}>0
\qquad(d\ge4).
\tag{5.2}
\]

Moreover, on \([0,2/d]\),

\[
p_d'(\lambda)
=3\lambda^2-2(d+3)\lambda+3d
\]

obeys

\[
p_d'(\lambda)
\ge
3d-\frac{4(d+3)}d
>0
\qquad(d\ge4).
\tag{5.3}
\]

Thus \(p_d\) is strictly increasing on this interval and has exactly one root there. Consequently

\[
\boxed{
\frac1d<\lambda_d<\frac2d,
\qquad d\ge4.
}
\tag{5.4}
\]

Together with Sections 2–4, this root is the smallest nonzero eigenvalue of the double-cover Laplacian. Hence:

### Theorem 5.1 — binding spectral gap

For the explicit sharp binding graph of `GLOBAL-BINDING-LEMMA-v0.1.md`,

\[
\boxed{
\lambda_2(L(\widetilde H_3))=1,
}
\tag{5.5}
\]

and for every \(d\ge4\),

\[
\boxed{
\frac1d
<
\lambda_2(L(\widetilde H_d))
<
\frac2d.
}
\tag{5.6}
\]

Since the nonzero singular values of \(B_d\) are the square roots of the nonzero Laplacian eigenvalues,

\[
\boxed{
\sigma_{\min}^{+}(B_d)
>
\frac1{\sqrt d}.
}
\tag{5.7}
\]

---

## 6. Condition number of the unweighted binding operator

The maximum degree of \(\widetilde H_d\) is \(d-1\), so the standard Laplacian estimate gives

\[
\lambda_{\max}(L(\widetilde H_d))\le2(d-1).
\]

Therefore on the gauge-orthogonal subspace,

\[
\kappa(B_d)
=
\frac{\sigma_{\max}(B_d)}{\sigma_{\min}^{+}(B_d)}
<
\sqrt{2(d-1)d}.
\]

Thus

\[
\boxed{
\kappa(B_d)<\sqrt2\,d.
}
\tag{6.1}
\]

The bare graph-binding layer is polynomially conditioned.

---

## 7. What this removes from the Article-III suspect list

The global binding proof contains several layers:

\[
\boxed{
\text{local elimination}
\to
\text{second-order edge coefficients}
\to
\text{graph binding}
\to
\text{analytic rank lift}.
}
\]

Theorem 5.1 shows that the **unweighted graph-binding factor** itself has only polynomial spectral loss. In particular, the connected non-bipartite graph used for sharp completion does not create a hidden exponentially small algebraic connectivity.

Therefore a superpolynomial conditioning obstruction, if present, must come from one or more of:

1. nonuniform edge weights

\[
\frac{\lambda_k(\lambda_j-\lambda_n)}{\lambda_j(\lambda_k-\lambda_n)}
\quad\text{and}\quad
\frac{\lambda_j-\lambda_n}{\lambda_k-\lambda_n};
\]

2. conditioning of the local bulk inverse used to form the Schur complement;
3. the small perturbation scale \(t^2\);
4. coupling distortion between the residual kernel and the already resolved block;
5. the analogous two-scale \((\epsilon,t)\) structure in the odd-to-even transfer repair.

This is a genuine narrowing of the Article-III problem.

---

## 8. Weighted binding target

Let \(W_d\) denote the actual reduced binding matrix after the nonzero scalar edge coefficients from the Coxeter construction are included.

If one can choose the multiplicative-Sidon diagonal parameters so that every nonzero edge coefficient lies in a polynomial window

\[
d^{-C}\le |w_e|\le d^C,
\tag{8.1}
\]

then the graph estimate immediately converts to a polynomial bound for the weighted combinatorial layer.

The next constructive target is therefore:

\[
\boxed{
\text{polynomially separated multiplicative-Sidon transport parameters}
}
\tag{8.2}
\]

compatible with the exact local-kernel and determinant-one constraints of the Article-II extension proof.

That is a much sharper problem than asking abstractly whether the full sharp construction is stable.

---

## 9. Claim firewall

This note proves a polynomial spectral gap only for the **unweighted graph-binding matrix**. It does not yet prove polynomial conditioning of the full Coxeter measurement design.

In particular it does not control:

- multiplicative-Sidon edge weights;
- local block inverses;
- perturbation scales;
- the full Schur coupling constant;
- the odd-to-even two-scale transfer;
- the final Article-III condition number.
