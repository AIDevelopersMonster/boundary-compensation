# Article III — Frame-Efficiency Benchmark for Robust Coxeter Designs

**Author:** Malachevsky, A.A. / Малачевский А.А.  
**ORCID:** 0009-0008-6009-3196  
**Date:** 2026-09-06  
**Status:** `PROVED / UNIVERSAL FRAME BENCHMARK`

## 0. Purpose

The exact Kossakowski Gram-spectrum theorem closes the domain-normalization problem. The remaining question is measurement-side: after exact whitening, how isotropically can a Coxeter design cover the dissipative quotient?

This note introduces a basis-independent efficiency functional and proves the universal tight-frame benchmark. It is deliberately weaker than a redundancy theorem: no Coxeter-specific lower bound on the condition number is claimed here.

---

## 1. Normalized design operator

Let

\[
N=(d^2-1)^2
\]

and let `Q_d` be the exactly whitened dissipative quotient. For a finite face multiset

\[
\mathcal D=\{f_1,\dots,f_L\}
\]

let

\[
\mathcal M_{\mathcal D}:\mathcal Q_d\to\bigoplus_{j=1}^L M_d
\]

be the normalized measurement map with averaged normalized Hilbert-Schmidt output metric. Its frame operator is

\[
S_{\mathcal D}
=
\mathcal M_{\mathcal D}^*\mathcal M_{\mathcal D}
=
\frac1L\sum_{j=1}^L C_{f_j}^*C_{f_j}.
\]

Write its eigenvalues as

\[
0\le\lambda_1\le\cdots\le\lambda_N.
\]

Then

\[
A_{\mathcal D}=\lambda_1,
\qquad
B_{\mathcal D}=\lambda_N,
\qquad
\kappa(\mathcal D)=\sqrt{B_{\mathcal D}/A_{\mathcal D}}
\]

when `A_D>0`.

---

## 2. Mean frame energy

Define

\[
\bar\lambda_{\mathcal D}
=
\frac1N\operatorname{Tr}S_{\mathcal D}.
\]

Equivalently,

\[
\boxed{
\bar\lambda_{\mathcal D}
=
\frac1{NL}\sum_{f\in\mathcal D}\|C_f\|_{HS}^2.
}
\tag{2.1}
\]

Here the Hilbert-Schmidt norm of `C_f` is computed between the exactly normalized domain and output Hilbert spaces.

This quantity is invariant under orthonormal coordinate changes and under simultaneous unitary conjugation of the physical face data.

---

## 3. Lower-frame efficiency

For an injective design define

\[
\boxed{
\eta(\mathcal D)
=
\frac{A_{\mathcal D}}{\bar\lambda_{\mathcal D}}
=
\frac{N A_{\mathcal D}}{\operatorname{Tr}S_{\mathcal D}}.
}
\tag{3.1}
\]

For a singular design set `eta(D)=0`.

### Theorem 3.1 — universal efficiency bound

For every finite design,

\[
\boxed{0\le\eta(\mathcal D)\le1.}
\tag{3.2}
\]

Moreover,

\[
\boxed{
\eta(\mathcal D)=1
\iff
S_{\mathcal D}=\bar\lambda_{\mathcal D}I
\iff
\mathcal M_{\mathcal D}\text{ is a tight frame on }\mathcal Q_d.
}
\tag{3.3}
\]

#### Proof

Since `A_D=lambda_min(S_D)`,

\[
A_{\mathcal D}=\lambda_1
\le
\frac1N\sum_{j=1}^N\lambda_j
=\bar\lambda_{\mathcal D}.
\]

Thus `eta<=1`, while positivity is immediate.

Equality between the minimum eigenvalue and the arithmetic mean is possible exactly when every eigenvalue equals that common value. Hence

\[
S_{\mathcal D}=\bar\lambda_{\mathcal D}I.
\]

This is precisely the tight-frame condition. `square`

---

## 4. Condition-number consequence

### Corollary 4.1

For every injective design,

\[
\boxed{
\kappa(\mathcal D)^2
=\frac{B_{\mathcal D}}{A_{\mathcal D}}
\ge
\frac{\bar\lambda_{\mathcal D}}{A_{\mathcal D}}
=\eta(\mathcal D)^{-1}.
}
\tag{4.1}
\]

Therefore

\[
\boxed{
\kappa(\mathcal D)\ge\eta(\mathcal D)^{-1/2}.
}
\tag{4.2}
\]

Equality in the strongest possible sense `kappa=1` occurs exactly for a tight design.

This inequality is not intended as a strong quantitative estimate by itself; its role is to distinguish two mechanisms for poor conditioning:

1. low total frame energy `Tr S_D`;
2. anisotropic allocation of that energy, measured by small `eta(D)`.

---

## 5. Replication invariance

If every face is repeated exactly `r` times, then by the averaged output convention

\[
S_{r\mathcal D}=S_{\mathcal D}.
\]

Hence

\[
\boxed{
\bar\lambda_{r\mathcal D}=\bar\lambda_{\mathcal D},
\qquad
\eta(r\mathcal D)=\eta(\mathcal D),
\qquad
\kappa(r\mathcal D)=\kappa(\mathcal D).
}
\tag{5.1}
\]

Thus any improvement in `eta` under oversampling must come from genuinely different face geometry, not measurement duplication.

---

## 6. Equal-energy face classes

Suppose an admissible normalized face class satisfies

\[
\|C_f\|_{HS}^2=E_d
\]

for every admissible face `f`. Then (2.1) becomes

\[
\boxed{
\bar\lambda_{\mathcal D}=\frac{E_d}{N},
}
\tag{6.1}
\]

independently of `L`.

Consequently

\[
\boxed{
A_{\mathcal D}\le\frac{E_d}{N},
}
\tag{6.2}
\]

and any benefit from adding genuinely new equal-energy faces is purely an **isotropy gain**: oversampling cannot raise the mean frame eigenvalue, but it can lift the weakest directions toward the mean.

This is the cleanest mathematical explanation of why averaged normalization removes the trivial advantage of taking more measurements while still allowing a real robustness benefit from diversified geometry.

---

## 7. Variable-energy faces

For the present Article-II/III pools not every loop type is guaranteed to have the same Hilbert-Schmidt face energy. Therefore comparisons among designs can separate

\[
\bar\lambda_{\mathcal D}
\quad\text{and}\quad
\eta(\mathcal D).
\]

A design may improve `A_D` because its average face energy increased, because its geometry became more isotropic, or both.

For every future search the required diagnostic tuple is therefore

\[
\boxed{
(L,\ A_D,\ B_D,\ \kappa_D,\ \operatorname{Tr}S_D,\ \bar\lambda_D,\ \eta_D).
}
\tag{7.1}
\]

Reporting only `kappa` or only `A_D` is no longer sufficient for interpreting oversampling gains.

---

## 8. Tightness defect

A complementary dimensionless anisotropy statistic is

\[
\delta_{\mathrm{tight}}(\mathcal D)
=
\frac{\|S_{\mathcal D}-\bar\lambda_{\mathcal D}I\|_F}
{\bar\lambda_{\mathcal D}\sqrt N}.
\tag{8.1}
\]

Then

\[
\delta_{\mathrm{tight}}=0
\iff
S_{\mathcal D}=\bar\lambda I.
\]

This statistic is again orthogonal-coordinate invariant and replication invariant. It should be recorded alongside `eta` in the next numerical census.

---

## 9. Next strict experiment

The next measurement-side experiment is now sharpened.

For every sharp and oversampled design, compute separately:

\[
\bar\lambda_D
\]

and

\[
\eta_D=\frac{A_D}{\bar\lambda_D}.
\]

If oversampling mainly raises `eta` while `bar lambda` remains approximately stable, that is direct evidence that redundancy is repairing angular coverage rather than merely injecting more operator energy.

The strongest next candidate statement is therefore not simply

`oversampling improves kappa`,

but rather:

> **genuine Coxeter redundancy can increase normalized frame isotropy.**

A theorem-level redundancy barrier would require a Coxeter-specific upper bound

\[
\eta(\mathcal D)\le\eta_d^{\mathrm{sharp}}<1
\]

for all sharp designs, together with an oversampled construction having larger efficiency. This remains open.

---

## 10. Claim firewall

This note proves only universal finite-dimensional frame inequalities. It does not prove:

- that all sharp Coxeter designs are badly conditioned;
- a nontrivial Coxeter-specific bound on `eta`;
- a redundancy threshold;
- statistical/sample-complexity optimality;
- a physically unique face-energy model;
- SPAM/noise robustness;
- non-Markovian/process-tensor results.
