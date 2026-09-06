# Article III — Normalized Frame Formulation for Stable Coxeter Tomography

**Author:** Malachevsky, A.A. / Малачевский А.А.  
**ORCID:** 0009-0008-6009-3196  
**Date:** 2026-09-06  
**Status:** `PROVED_NORMALIZATION_LAYER / NUMERICS_PENDING`

## 0. Purpose and scope

Article II solved a binary first-order inverse problem in a declared finite-dimensional matrix-valued Coxeter-face model: which face families have full rank on the dissipative quotient, and what is the sharp minimum face count? The result was

\[
L_d^{\mathrm{Cox}}=\left\lfloor\frac{d^2}{2}\right\rfloor,
\qquad d\ge3.
\]

Article III asks the strictly stronger operational question: after fixing a canonical Hilbert geometry, how far from singular is an injective Coxeter measurement operator, and how much genuinely new face geometry is required to make the inverse problem stable?

This note fixes the **coordinate normalization layer** and proves its basic invariances. It does **not** yet fix a unique physical normalization of the admissible Coxeter faces themselves. No numerical conditioning claim is licensed until a deterministic real/complex measurement-matrix builder and a declared face-energy convention are available.

Finite-dimensional scope is mandatory throughout.

---

## 1. Generator tangent space and dissipative quotient

Let \(M_d=M_d(\mathbb C)\). Define the real vector space

\[
\mathcal G_d
=
\{F:M_d\to M_d:\ F\text{ complex-linear, *-preserving, and }F(I)=0\}.
\]

The Hamiltonian derivation subspace is

\[
\mathcal D_d
=
\{\delta_H:\delta_H(X)=i[H,X],\ H=H^*,\ \operatorname{Tr}H=0\}.
\]

The dissipative quotient is

\[
\mathcal Q_d=\mathcal G_d/\mathcal D_d.
\]

### Proposition 1.1 — quotient dimension

\[
\boxed{\dim_{\mathbb R}\mathcal Q_d=(d^2-1)^2.}
\]

#### Proof

A complex-linear *-preserving map is determined by its real-linear action on the real vector space of Hermitian matrices, of dimension \(d^2\). Hence the real dimension of the space of such maps is \(d^4\). The condition \(F(I)=0\) imposes \(d^2\) independent real constraints, so

\[
\dim_{\mathbb R}\mathcal G_d=d^4-d^2.
\]

The traceless Hermitian Hamiltonians have real dimension \(d^2-1\), and \(H\mapsto i[H,\cdot]\) is injective on that traceless subspace. Therefore

\[
\dim_{\mathbb R}\mathcal Q_d
=d^4-d^2-(d^2-1)
=(d^2-1)^2.
\]

\(\square\)

This is exactly the quotient dimension used in Article II.

---

## 2. Canonical normalized Hilbert geometry

On \(M_d\) use the normalized Hilbert–Schmidt inner product

\[
\langle X,Y\rangle_{2,d}
=\frac1d\operatorname{Tr}(X^*Y),
\qquad
\|X\|_{2,d}^2=\frac1d\operatorname{Tr}(X^*X).
\]

Thus

\[
\|I\|_{2,d}=1.
\]

Let \(\{E_a\}_{a=0}^{d^2-1}\) be any orthonormal basis of \(M_d\) for this inner product. For a complex-linear superoperator \(F\), define

\[
\|F\|_{\mathrm{sop},d}^2
=
\frac1{d^2}
\sum_{a=0}^{d^2-1}
\|F(E_a)\|_{2,d}^2.
\]

This is the normalized Hilbert–Schmidt norm of the superoperator. It is independent of the chosen orthonormal basis, and

\[
\|\operatorname{id}\|_{\mathrm{sop},d}=1.
\]

Equip \(\mathcal G_d\) with the corresponding real Hilbert inner product. Since \(\mathcal D_d\) is a finite-dimensional linear subspace, the quotient norm is

\[
\|[F]\|_{\mathcal Q_d}
=
\inf_{\delta\in\mathcal D_d}
\|F+\delta\|_{\mathrm{sop},d}.
\]

Equivalently,

\[
\mathcal Q_d\cong\mathcal D_d^\perp
\]

isometrically by taking the orthogonal representative of each coset.

This quotient Hilbert structure removes arbitrary coordinate scaling from the inverse problem. Only orthonormal coordinate changes are admissible when singular values are compared.

---

## 3. First-order face coefficient as a quotient map

Let a flat face \(f\) be represented by transports

\[
T_{f,m_f}\cdots T_{f,1}=I,
\qquad
P_{f,k}=T_{f,k}\cdots T_{f,1}.
\]

For \(F\in\mathcal G_d\), define the Leibniz defect

\[
\Gamma_F(X,Y)
=F(XY)-F(X)Y-XF(Y).
\]

The first-order face coefficient is

\[
C_f(F)
=-\sum_{k=2}^{m_f}
T_{f,m_f}\cdots T_{f,k+1}
\Gamma_F(T_{f,k},P_{f,k-1}).
\]

If \(F=\delta_H\) is a derivation, then \(\Gamma_F=0\). Therefore \(C_f\) depends only on the quotient class \([F]\), and we obtain a well-defined real-linear map

\[
C_f:\mathcal Q_d\to M_d.
\]

This is the exact place where Article II's derivation quotient enters the stability problem.

---

## 4. Design output metric and normalized measurement operator

Let \(\mathcal D\) be a finite multiset of \(L\) admissible faces. Define

\[
\mathcal Y_{\mathcal D}
=\bigoplus_{f\in\mathcal D}M_d
\]

with averaged output norm

\[
\|(Y_f)_{f\in\mathcal D}\|_{\mathcal Y_{\mathcal D}}^2
=
\frac1L\sum_{f\in\mathcal D}\|Y_f\|_{2,d}^2.
\]

Define

\[
\mathcal M_{\mathcal D}:\mathcal Q_d\to\mathcal Y_{\mathcal D},
\qquad
\mathcal M_{\mathcal D}q=(C_fq)_{f\in\mathcal D}.
\]

The associated frame operator is

\[
S_{\mathcal D}
=\mathcal M_{\mathcal D}^*\mathcal M_{\mathcal D}
=\frac1L\sum_{f\in\mathcal D}C_f^*C_f.
\]

Define the lower and upper frame bounds

\[
A_{\mathcal D}
=
\inf_{\|q\|_{\mathcal Q_d}=1}
\frac1L\sum_{f\in\mathcal D}\|C_fq\|_{2,d}^2,
\]

\[
B_{\mathcal D}
=
\sup_{\|q\|_{\mathcal Q_d}=1}
\frac1L\sum_{f\in\mathcal D}\|C_fq\|_{2,d}^2.
\]

Equivalently,

\[
A_{\mathcal D}=\lambda_{\min}(S_{\mathcal D})
=\sigma_{\min}(\mathcal M_{\mathcal D})^2,
\]

\[
B_{\mathcal D}=\lambda_{\max}(S_{\mathcal D})
=\sigma_{\max}(\mathcal M_{\mathcal D})^2.
\]

For injective designs define

\[
\kappa(\mathcal D)
=
\frac{\sigma_{\max}(\mathcal M_{\mathcal D})}
{\sigma_{\min}(\mathcal M_{\mathcal D})}
=
\sqrt{\frac{B_{\mathcal D}}{A_{\mathcal D}}}.
\]

---

## 5. Four invariance propositions

### Proposition 5.1 — orthonormal coordinate invariance

The singular values of \(\mathcal M_{\mathcal D}\), and therefore \(A_{\mathcal D}\), \(B_{\mathcal D}\), and \(\kappa(\mathcal D)\), are independent of the orthonormal bases used to represent \(\mathcal Q_d\) and \(\mathcal Y_{\mathcal D}\).

#### Proof

Changing orthonormal coordinates in the domain and codomain replaces a matrix representative \(M\) by

\[
U M V,
\]

where \(U\) and \(V\) are real orthogonal transformations of the underlying real Hilbert spaces. Then

\[
(UMV)^*(UMV)=V^*M^*MV,
\]

which is orthogonally similar to \(M^*M\). Hence the eigenvalues of \(M^*M\), and therefore the singular values, are unchanged. \(\square\)

**Boundary.** Arbitrary nonorthogonal reparameterizations are not harmless coordinate changes for Article III: they alter the declared Hilbert geometry and may change the singular spectrum.

### Proposition 5.2 — unitary conjugation invariance

Let \(U\in U(d)\). Simultaneously conjugate every face transport by

\[
T\mapsto U T U^*
\]

and every tangent map by

\[
F\mapsto F^{(U)},
\qquad
F^{(U)}(X)=U F(U^*XU)U^*.
\]

Then

\[
A_{U\mathcal D U^*}=A_{\mathcal D},
\qquad
B_{U\mathcal D U^*}=B_{\mathcal D},
\qquad
\kappa(U\mathcal D U^*)=\kappa(\mathcal D).
\]

#### Proof

Normalized Hilbert–Schmidt norm is invariant under unitary conjugation. The transformation \(F\mapsto F^{(U)}\) preserves \(\mathcal G_d\), carries Hamiltonian derivations to Hamiltonian derivations, and therefore induces an orthogonal map on \(\mathcal Q_d\). Direct substitution in the definition of \(\Gamma_F\) gives

\[
\Gamma_{F^{(U)}}(UXU^*,UYU^*)
=U\Gamma_F(X,Y)U^*.
\]

Consequently each transformed face coefficient satisfies the corresponding equivariance identity

\[
C_{UfU^*}(q^{(U)})=U C_f(q)U^*.
\]

Thus the transformed measurement operator differs from the original one only by orthogonal transformations of domain and output. Proposition 5.1 applies. \(\square\)

### Proposition 5.3 — replication invariance

Let \(r\mathcal D\) be obtained by repeating every face of \(\mathcal D\) exactly \(r\) times. Then

\[
\boxed{S_{r\mathcal D}=S_{\mathcal D}.}
\]

Hence

\[
A_{r\mathcal D}=A_{\mathcal D},
\quad
B_{r\mathcal D}=B_{\mathcal D},
\quad
\kappa(r\mathcal D)=\kappa(\mathcal D).
\]

#### Proof

The replicated design has \(rL\) outputs, so

\[
S_{r\mathcal D}
=
\frac1{rL}
\sum_{f\in\mathcal D}\sum_{j=1}^r C_f^*C_f
=
\frac1L\sum_{f\in\mathcal D}C_f^*C_f
=S_{\mathcal D}.
\]

\(\square\)

Therefore an apparent gain obtained merely by duplicating measurements is excluded by construction. Any improvement of \(A_{\mathcal D}\) must come from genuinely new face geometry or from a different experimental resource model.

### Proposition 5.4 — rank/stability equivalence

For every finite design \(\mathcal D\),

\[
\boxed{
A_{\mathcal D}>0
\iff
\mathcal M_{\mathcal D}\text{ is injective}
\iff
\operatorname{rank}\mathcal M_{\mathcal D}=(d^2-1)^2.
}
\]

#### Proof

Since \(\mathcal Q_d\) is finite-dimensional, \(A_{\mathcal D}\) is the smallest eigenvalue of the positive semidefinite operator \(S_{\mathcal D}=\mathcal M_{\mathcal D}^*\mathcal M_{\mathcal D}\). It is positive exactly when \(S_{\mathcal D}\) has trivial kernel. But

\[
\ker S_{\mathcal D}=\ker\mathcal M_{\mathcal D}.
\]

Thus \(A_{\mathcal D}>0\) is equivalent to injectivity, which is equivalent to full column rank \(\dim\mathcal Q_d=(d^2-1)^2\). \(\square\)

**Interpretation.** Article II solved the binary wall

\[
A_{\mathcal D}=0
\quad\text{versus}\quad
A_{\mathcal D}>0.
\]

Article III studies the magnitude and asymptotic scaling of \(A_{\mathcal D}\), \(B_{\mathcal D}\), and \(\kappa(\mathcal D)\).

---

## 6. Robust designs after normalization

Once an admissible normalized face class \(\mathfrak F_d^{\mathrm{norm}}\) is fixed, define a design to be \(\varepsilon\)-robust if

\[
\sigma_{\min}(\mathcal M_{\mathcal D})\ge\varepsilon,
\]

or equivalently

\[
A_{\mathcal D}\ge\varepsilon^2.
\]

Define

\[
L_{d,\mathfrak F}^{\mathrm{rob}}(\varepsilon)
=
\min\left\{
|\mathcal D|:
\mathcal D\subset\mathfrak F_d^{\mathrm{norm}},
\ A_{\mathcal D}\ge\varepsilon^2
\right\}.
\]

For fixed face count \(L\), a useful extremal quantity is

\[
A_d^*(L)
=
\sup_{\substack{\mathcal D\subset\mathfrak F_d^{\mathrm{norm}}\\|\mathcal D|=L}}
A_{\mathcal D},
\]

with the analogous best condition number

\[
\kappa_d^*(L)
=
\inf_{\substack{\mathcal D\subset\mathfrak F_d^{\mathrm{norm}}\\|\mathcal D|=L\\A_{\mathcal D}>0}}
\kappa(\mathcal D).
\]

The sharp-face question becomes

\[
\boxed{
\kappa_d^{\mathrm{sharp}}
=
\kappa_d^*\!\left(\left\lfloor\frac{d^2}{2}\right\rfloor\right)
\stackrel{?}{\le}\operatorname{poly}(d).
}
\]

A negative answer would motivate a quantitative redundancy barrier.

---

## 7. The normalization wall that must not be crossed silently

The Hilbert geometry above removes **coordinate** ambiguity. It does not by itself remove **physical face-amplitude** ambiguity.

If the Article-II rank construction allows arbitrary rescaling of tangent generators, edge parameters, or nonunitary/integer/SL representatives, then a face coefficient can be enlarged or suppressed without changing rank. Singular values computed before fixing this freedom would therefore have no invariant operational meaning.

A valid numerical Article-III experiment must first declare an admissible face class such as, for example,

\[
\|X_f\|_{2,d}=\|Y_f\|_{2,d}=1
\]

for tangent-generated faces, or must divide the bilinear face coefficient by a fixed bilinear face-energy scale. Which convention is physically correct is **not decided in this note**.

Accordingly:

> **NO NUMERICAL CONDITIONING CLAIM may be made from modular rank certificates, arbitrary integer witnesses, or unnormalized symbolic face matrices.**

In particular, the Article-II finite-field certificate

`prime=1000033, shape=600x576, rank=576`

certifies exact rational full column rank for its stated purpose. It does not determine any real singular value, frame bound, or condition number.

---

## 8. Numerical experiment gate

A numerical conditioning experiment is licensed only after all of the following are available:

1. a deterministic real or complex builder for the Article-II first-order measurement operator;
2. an explicit map from each generated row/block to its Coxeter face data;
3. a declared normalized Hilbert basis of \(\mathcal Q_d\);
4. a declared face-energy normalization or a proof that the admissible builder already fixes it canonically;
5. real/complex floating-point or high-precision SVD performed on the normalized matrix, not on a modular certificate;
6. reproducible recording of \(d\), design, normalization, \(A_{\mathcal D}\), \(B_{\mathcal D}\), \(\kappa\), numerical precision, and residual rank diagnostics.

Until this gate is passed the Article-III status remains `NUMERICS_PENDING`.

---

## 9. First theorem fork for Article III

The first real theorem should aim at one of two mutually exclusive regimes.

### Branch A — robust sharp frames

There exist constants \(C,p>0\) and a physically justified normalized face class such that for every sufficiently large \(d\) there is a sharp design

\[
|\mathcal D|=\left\lfloor\frac{d^2}{2}\right\rfloor
\]

with

\[
\kappa(\mathcal D)\le C d^p.
\]

### Branch B — redundancy barrier

For every sharp normalized design, \(A_{\mathcal D}\) decays too rapidly, or \(\kappa(\mathcal D)\) grows too rapidly, while a strictly larger face family attains a substantially better frame bound.

A theorem of Branch B type would show that algebraic minimality and operational minimality are genuinely different notions.

---

## 10. Handoff

The normalization layer is now mathematically fixed up to the unresolved **face-energy convention**. The next action is not another abstract conjecture. It is to locate or reconstruct the exact Article-II real measurement-matrix builder and determine whether its face data admit a canonical physical normalization.

If such a builder exists, the next artifact should be a reproducible small-\(d\) singular-spectrum experiment. If only modular/rank-certificate machinery exists, the next artifact must instead be a deterministic reconstruction protocol, with numerical claims explicitly blocked until the real normalized builder is implemented.
