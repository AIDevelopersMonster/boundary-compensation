# Article III — Explicit Unitary Replacement of the Local Two-Level Faces

**Author:** Malachevsky, A.A. / Малачевский А.А.  
**ORCID:** 0009-0008-6009-3196  
**Date:** 2026-09-06  
**Status:** `PROVED / EXPLICIT UNITARY LOCAL REDUCTION / NO ZARISKI RETURN NEEDED LOCALLY`

## 0. Purpose

`EVEN-STEP-LOCAL-KERNEL-REDUCTION-v0.1.md` uses the determinant-one but nonunitary block

\[
\begin{pmatrix}1&1\\1&2\end{pmatrix}
\]

for each local new-level plane. Rank is later returned to the unitary locus by a qualitative Zariski-density argument.

For Article III this is insufficient quantitatively. This note shows that the local reduction does not need that nonunitary block at all: any nontrivial determinant-one Givens rotation gives the same local kernel and the same multiplicative-Sidon determinant, up to harmless nonzero row scalings.

Thus the local two-level stage admits an explicit, uniformly conditioned unitary realization.

---

## 1. Setup

Let \(n=d+1\),

\[
B=M_d(\mathbb C)\oplus\mathbb C\subset M_n(\mathbb C),
\]

and let

\[
D:M_n(\mathbb C)\to M_n(\mathbb C)
\]

be complex-linear with \(D|_B=0\).

For \(j\le d\), put

\[
x_j=E_{j n},\qquad y_j=E_{n j},
\]

and

\[
P_j=D(x_j),\qquad Q_j=D(y_j).
\]

Let

\[
\Lambda=\operatorname{diag}(\lambda_1,\ldots,\lambda_n)
\]

be a multiplicative-Sidon diagonal anchor as in the local-kernel theorem.

---

## 2. Unitary local transport

Fix an angle \(\theta\) with

\[
s=\sin\theta\ne0,
\qquad c=\cos\theta.
\]

Let \(U_j(\theta)\in SU(n)\) be the identity outside \(\operatorname{span}\{e_j,e_n\}\) and on that plane equal to

\[
\boxed{
\begin{pmatrix}
c&s\\-s&c\end{pmatrix}.
}
\tag{2.1}
\]

Because the diagonal matrix units lie in \(B\),

\[
D(U_j)=sP_j-sQ_j.
\tag{2.2}
\]

Likewise

\[
U_j^{-1}=U_j^*,
\qquad
D(U_j^{-1})=-sP_j+sQ_j.
\tag{2.3}
\]

---

## 3. Forward branch

For the Leibniz-defect branch

\[
\Gamma_D(U_j,\Lambda)
=D(U_j\Lambda)-D(U_j)\Lambda-U_jD(\Lambda),
\]

we have \(D(\Lambda)=0\). The only off-block entries of \(U_j\Lambda\) are

\[
s\lambda_nE_{jn}-s\lambda_jE_{nj}.
\]

Therefore

\[
D(U_j\Lambda)=s\lambda_nP_j-s\lambda_jQ_j.
\]

Using (2.2),

\[
\Gamma_D(U_j,\Lambda)
=s\Bigl[
P_j(\lambda_nI-\Lambda)
-Q_j(\lambda_jI-\Lambda)
\Bigr].
\tag{3.1}
\]

Since \(s\ne0\), the scalar factor is irrelevant to kernel and condition number after row normalization.

---

## 4. Inverse branch

For the paired branch

\[
\Gamma_D(\Lambda^{-1},U_j^{-1}),
\]

again \(D(\Lambda^{-1})=0\). The off-block entries of \(\Lambda^{-1}U_j^{-1}\) are

\[
-s\lambda_j^{-1}E_{jn}
+s\lambda_n^{-1}E_{nj}.
\]

Hence

\[
D(\Lambda^{-1}U_j^{-1})
=-s\lambda_j^{-1}P_j+s\lambda_n^{-1}Q_j.
\]

Subtracting \(\Lambda^{-1}D(U_j^{-1})\) yields

\[
\Gamma_D(\Lambda^{-1},U_j^{-1})
=s\Bigl[
(\Lambda^{-1}-\lambda_j^{-1}I)P_j
-(\Lambda^{-1}-\lambda_n^{-1}I)Q_j
\Bigr].
\tag{4.1}
\]

---

## 5. Entrywise determinant

Fix an output entry \((r,s)\), and write

\[
p=(P_j)_{rs},\qquad q=(Q_j)_{rs}.
\]

After dividing both branch equations by the common nonzero scalar \(\sin\theta\), the system is

\[
(\lambda_n-\lambda_s)p
-(\lambda_j-\lambda_s)q=0,
\tag{5.1}
\]

\[
(\lambda_r^{-1}-\lambda_j^{-1})p
-(\lambda_r^{-1}-\lambda_n^{-1})q=0.
\tag{5.2}
\]

Its determinant differs only by an overall sign from the determinant in `EVEN-STEP-LOCAL-KERNEL-REDUCTION-v0.1.md`:

\[
\boxed{
\Delta_{j;r,s}
=
\frac{(\lambda_j-\lambda_n)
(\lambda_j\lambda_n-\lambda_r\lambda_s)}
{\lambda_j\lambda_n\lambda_r}.
}
\tag{5.3}
\]

Therefore the multiplicative-Sidon condition makes the system invertible at every entry except

\[
(r,s)=(j,n),\qquad(n,j).
\]

At \((j,n)\), \(Q_j(j,n)=0\) and \(P_j(j,n)\) is free. At \((n,j)\), \(P_j(n,j)=0\) and \(Q_j(n,j)\) is free.

Hence:

### Theorem 5.1 — unitary local-kernel reduction

For every \(d\ge2\) and every angle \(\theta\) with \(\sin\theta\ne0\), the \(d\) explicit unitary local faces built from \(U_j(\theta)\) and \(\Lambda\) have joint kernel

\[
\boxed{
P_j=\alpha_jE_{jn},
\qquad
Q_j=\gamma_jE_{nj},
\qquad j=1,\ldots,d.
}
\tag{5.4}
\]

Thus the local kernel has complex dimension \(2d\), exactly as in the original nonunitary local construction.

---

## 6. Uniform choice of angle

Take, for example,

\[
\boxed{
\theta=\frac\pi4.
}
\tag{6.1}
\]

Then

\[
|\sin\theta|=|\cos\theta|=2^{-1/2}.
\]

No small angular parameter appears in the local branch equations. Together with the polynomially separated unitary Sidon phases of `ARTICLE-III-POLYNOMIAL-SIDON-PHASES-v0.1.md`, the nonexceptional local \(2\times2\) systems therefore have inverse-polynomial determinant bounds with no qualitative Zariski step.

In particular the **entire unperturbed local reduction layer** can be realized explicitly on the unitary locus.

---

## 7. Updated location of the quantitative unitary wall

The remaining nonunitary object in the global binding construction is not the local two-level probe. It is the cross-plane perturbation used to bind the residual slopes, schematically

\[
B_{j,k}(t)=\Lambda[I+t(E_{kn}+E_{nk})].
\]

The next task is to replace this by an explicit unitary one-parameter perturbation, naturally

\[
\boxed{
B^{\mathrm{u}}_{j,k}(t)
=
\Lambda\exp\bigl(t(E_{kn}-E_{nk})\bigr),
}
\tag{7.1}
\]

and rederive the reduced second-order binding coefficient.

If the resulting edge relations remain the same up to inverse-polynomial nonzero weights, then the even-to-odd quantitative witness can be made unitary without invoking Zariski density at the local/binding stages.

---

## 8. Claim firewall

This theorem replaces only the **local** non-diagonal transports by explicit unitaries. It does not yet prove that the cross-plane perturbation can be made unitary with the required second-order graph binding, nor does it prove a full polynomial condition-number bound for the sharp Coxeter design.
