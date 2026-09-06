# Article III — Projective Face Normalization and Polar Support Frames

**Author:** Malachevsky, A.A. / Малачевский А.А.  
**ORCID:** 0009-0008-6009-3196  
**Date:** 2026-09-06  
**Status:** `PROVED_NORMALIZATION_LAYER / FUSION-FRAME_REDUCTION / NUMERICAL_TESTS_SEPARATE`

## 0. Purpose

The exact quotient Gram theorem removes domain-coordinate ambiguity. The next ambiguity is face-side: different admissible Coxeter faces can have very different total response energy, and even after equal-energy normalization they can have different singular-value profiles inside their measured subspaces.

This note separates three layers:

\[
\boxed{
\text{face amplitude}
\longrightarrow
\text{within-face spectral shape}
\longrightarrow
\text{measured-subspace geometry}.
}
\]

The final layer is a normalized fusion-frame problem on the dissipative quotient.

---

## 1. Exactly whitened face operators

Let

\[
N=(d^2-1)^2
\]

and let \(\mathcal Q_d\) carry the exact quotient Hilbert metric from `ARTICLE-III-GRAM-SPECTRUM-THEOREM-v0.1.md`.

For a nonzero admissible face \(f\), let

\[
C_f:\mathcal Q_d\to\mathcal Y_f
\]

be its exactly whitened first-order measurement operator, with normalized Hilbert structure on the output.

Define its total face energy

\[
E_f=\|C_f\|_{HS}^2=\operatorname{Tr}(C_f^*C_f)>0.
\tag{1.1}
\]

---

## 2. Projective normalization: remove amplitude

Define

\[
\widehat C_f=E_f^{-1/2}C_f
\tag{2.1}
\]

and

\[
Q_f=\widehat C_f^*\widehat C_f.
\tag{2.2}
\]

Then

\[
Q_f\ge0,
\qquad
\operatorname{Tr}Q_f=1.
\tag{2.3}
\]

Thus \(Q_f\) is a positive trace-one operator on the real Hilbert space \(\mathcal Q_d\). It records the directional sensitivity profile of the face after all scalar amplitude information has been removed.

### Proposition 2.1 — invariance under face rescaling

For every nonzero scalar \(a_f\), replacing

\[
C_f\mapsto a_f C_f
\]

leaves \(Q_f\) unchanged.

#### Proof

Both \(C_f^*C_f\) and \(E_f\) are multiplied by \(|a_f|^2\), so the ratio is unchanged. \(\square\)

For a design \(\mathcal D\) of \(L\) nonzero faces define the projective frame operator

\[
\widehat S_{\mathcal D}
=
\frac1L\sum_{f\in\mathcal D}Q_f.
\tag{2.4}
\]

Since every \(Q_f\) has trace one,

\[
\boxed{
\operatorname{Tr}\widehat S_{\mathcal D}=1,
\qquad
\bar\lambda_{\mathcal D}=\frac1N.
}
\tag{2.5}
\]

Hence the projective lower-frame efficiency is simply

\[
\boxed{
\widehat\eta(\mathcal D)
=N\lambda_{\min}(\widehat S_{\mathcal D})
\in[0,1].
}
\tag{2.6}
\]

At this level any increase in \(\widehat\eta\) is impossible to attribute to larger total face amplitude.

---

## 3. Internal face shape

Projective normalization does not make individual faces spectrally identical. Let the nonzero singular values of \(\widehat C_f\) be

\[
s_{f,1},\dots,s_{f,r_f},
\qquad
r_f=\operatorname{rank}C_f.
\]

Then

\[
\sum_{j=1}^{r_f}s_{f,j}^2=1
\]

and the nonzero eigenvalues of \(Q_f\) are \(s_{f,j}^2\).

Define the face purity

\[
\pi_f=\operatorname{Tr}(Q_f^2)
=\sum_j s_{f,j}^4
\tag{3.1}
\]

and effective rank

\[
r_{\mathrm{eff}}(f)=\pi_f^{-1}.
\tag{3.2}
\]

Then

\[
1\le r_{\mathrm{eff}}(f)\le r_f,
\]

with equality \(r_{\mathrm{eff}}(f)=r_f\) exactly when the nonzero singular values are equal.

Thus \(Q_f\) still mixes two pieces of information:

1. the support subspace \((\ker C_f)^\perp\);
2. the nonuniform singular weighting inside that subspace.

---

## 4. Polar support normalization: remove within-face singular weighting

Let

\[
P_f=\operatorname{supp}(Q_f)
\]

be the orthogonal projector onto

\[
(\ker C_f)^\perp\subset\mathcal Q_d.
\]

Define

\[
R_f=\frac1{r_f}P_f.
\tag{4.1}
\]

Then

\[
R_f\ge0,
\qquad
\operatorname{Tr}R_f=1.
\tag{4.2}
\]

The operator \(R_f\) discards all singular-value information and retains only the measured subspace and its dimension.

### Proposition 4.1 — support invariance

The normalized support operator \(R_f\) depends only on \(\ker C_f\) and \(r_f\). In particular it is unchanged by:

- nonzero scalar rescaling of \(C_f\);
- replacing \(C_f\) by \(U_fC_f\) for any invertible output-space map \(U_f\).

#### Proof

An invertible postcomposition leaves \(\ker C_f\) unchanged, hence leaves \((\ker C_f)^\perp\), its orthogonal projector, and its rank unchanged. \(\square\)

For a design \(\mathcal D\), define the support-frame operator

\[
S^{\mathrm{supp}}_{\mathcal D}
=
\frac1L\sum_{f\in\mathcal D}\frac{P_f}{r_f}.
\tag{4.3}
\]

Again

\[
\boxed{
\operatorname{Tr}S^{\mathrm{supp}}_{\mathcal D}=1.
}
\tag{4.4}
\]

Define

\[
\boxed{
\eta_{\mathrm{supp}}(\mathcal D)
=N\lambda_{\min}(S^{\mathrm{supp}}_{\mathcal D})
\in[0,1].
}
\tag{4.5}
\]

and, when the support frame is injective,

\[
\kappa_{\mathrm{supp}}(\mathcal D)
=
\sqrt{
\frac{\lambda_{\max}(S^{\mathrm{supp}}_{\mathcal D})}
{\lambda_{\min}(S^{\mathrm{supp}}_{\mathcal D})}
}.
\tag{4.6}
\]

### Theorem 4.2 — tight support geometry

\[
\boxed{
\eta_{\mathrm{supp}}(\mathcal D)=1
\iff
S^{\mathrm{supp}}_{\mathcal D}=\frac1NI.
}
\tag{4.7}
\]

Thus the ideal polar-normalized design is exactly a tight normalized fusion frame of the measured subspaces.

If all face ranks are the same, \(r_f=r\), then (4.7) is equivalent to

\[
\boxed{
\sum_{f\in\mathcal D}P_f
=\frac{Lr}{N}I.
}
\tag{4.8}
\]

---

## 5. Projective frame-potential identity

Define the projective tightness defect

\[
\widehat\delta_{\mathcal D}^2
=N\operatorname{Tr}(\widehat S_{\mathcal D}^2)-1.
\tag{5.1}
\]

Then

\[
\boxed{
\operatorname{Tr}(\widehat S_{\mathcal D}^2)
=
\frac1{L^2}
\left[
\sum_f\operatorname{Tr}(Q_f^2)
+2\sum_{f<g}\operatorname{Tr}(Q_fQ_g)
\right].
}
\tag{5.2}
\]

This identity cleanly separates:

- self anisotropy, through \(\operatorname{Tr}(Q_f^2)\);
- pairwise directional overlap, through \(\operatorname{Tr}(Q_fQ_g)\).

#### Proof

Expand the square of \(L^{-1}\sum_fQ_f\) and use cyclicity of trace. \(\square\)

---

## 6. Support-frame potential and subspace overlap

Define

\[
\delta_{\mathrm{supp}}^2
=N\operatorname{Tr}[(S^{\mathrm{supp}}_{\mathcal D})^2]-1.
\tag{6.1}
\]

Then

\[
\boxed{
\operatorname{Tr}[(S^{\mathrm{supp}}_{\mathcal D})^2]
=
\frac1{L^2}
\left[
\sum_f\frac1{r_f}
+2\sum_{f<g}
\frac{\operatorname{Tr}(P_fP_g)}{r_fr_g}
\right].
}
\tag{6.2}
\]

The cross term

\[
\frac{\operatorname{Tr}(P_fP_g)}{r_fr_g}
\tag{6.3}
\]

is a normalized aggregate principal-angle overlap of the two measured subspaces.

If all ranks equal \(r\), let

\[
\bar c
=
\frac{2}{L(L-1)}
\sum_{f<g}
\frac{\operatorname{Tr}(P_fP_g)}{r^2}.
\tag{6.4}
\]

Then

\[
\operatorname{Tr}[(S^{\mathrm{supp}})^2]
=
\frac1{Lr}+\frac{L-1}{L}\bar c.
\tag{6.5}
\]

Since every positive trace-one operator on an \(N\)-dimensional Hilbert space obeys

\[
\operatorname{Tr}S^2\ge\frac1N,
\]

we obtain the universal overlap bound

\[
\boxed{
\bar c
\ge
\frac{L/N-1/r}{L-1}.
}
\tag{6.6}
\]

Equality is attained exactly by a tight equal-rank support frame.

---

## 7. Nominal versus geometric redundancy

Define the nominal support redundancy ratio

\[
\boxed{
\rho_{\mathrm{supp}}(\mathcal D)
=
\frac1N\sum_{f\in\mathcal D}r_f.
}
\tag{7.1}
\]

For equal rank \(r\),

\[
\rho_{\mathrm{supp}}=\frac{Lr}{N}.
\]

A necessary condition for support injectivity is

\[
\rho_{\mathrm{supp}}\ge1,
\]

but this condition is far from sufficient for stability: it contains no information about mutual subspace orientation.

This distinction is essential for Article III:

\[
\boxed{
\text{nominal redundancy}
\neq
\text{geometric redundancy}.
}
\tag{7.2}
\]

The quantity \(\eta_{\mathrm{supp}}\) measures the worst-direction effectiveness of the actual subspace arrangement, not merely the sum of subspace dimensions.

---

## 8. A second-moment warning

The support tightness defect \(\delta_{\mathrm{supp}}\) and the lower-frame efficiency \(\eta_{\mathrm{supp}}\) are different spectral objectives.

The former depends only on

\[
\operatorname{Tr}S^2=\sum_j\lambda_j^2,
\]

whereas the latter depends only on

\[
\lambda_{\min}(S).
\]

Therefore a design can improve the weakest direction while its total second-moment defect remains unchanged or even worsens slightly. No implication in either direction is valid without additional spectral hypotheses.

This matters computationally: a search minimizing frame potential need not maximize the robust lower frame bound.

---

## 9. New robust target

The cleanest geometry-only extremal quantity is now

\[
\boxed{
\eta^{\mathrm{supp},*}_d(L)
=
\sup_{|\mathcal D|=L}
N\lambda_{\min}
\left(
\frac1L\sum_{f\in\mathcal D}\frac{P_f}{r_f}
\right).
}
\tag{9.1}
\]

At the Article-II sharp count

\[
L_d^{\mathrm{Cox}}=\left\lfloor\frac{d^2}{2}\right\rfloor,
\]

the asymptotic question becomes

\[
\boxed{
\eta^{\mathrm{supp},*}_d(L_d^{\mathrm{Cox}})
\stackrel{?}{\ge}d^{-O(1)}
}
\tag{9.2}
\]

versus a genuine geometric redundancy barrier.

A stronger negative result would be

\[
\eta^{\mathrm{supp},*}_d(L_d^{\mathrm{Cox}})\to0
\]

while some oversampled family with controlled \(L/L_d^{\mathrm{Cox}}\) retains a substantially larger support efficiency.

This remains open.

---

## 10. Claim firewall

This note proves normalization and frame identities only. It does not prove:

- asymptotic decay of sharp-design support efficiency;
- existence of a universal redundancy threshold;
- optimality of any finite pool or sampled design;
- a physical resource interpretation of polar support normalization;
- statistical/sample-complexity bounds;
- non-Markovian/process-tensor results.

The polar support frame is a diagnostic geometry designed to isolate the arrangement of measured quotient subspaces from face amplitude and from within-face singular weighting.
