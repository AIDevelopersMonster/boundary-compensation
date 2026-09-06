# Article III — Sharp Rank Slack and Near-Direct-Sum Geometry

**Author:** Malachevsky, A.A. / Малачевский А.А.  
**ORCID:** 0009-0008-6009-3196  
**Date:** 2026-09-06  
**Status:** `PROVED / SHARP-SUPPORT-RANK BUDGET / NEAR-DIRECT-SUM GEOMETRY`

## 0. Purpose

Article II proves the sharp face count

\[
L_d^{\mathrm{Cox}}=\left\lfloor\frac{d^2}{2}\right\rfloor,
\qquad d\ge3,
\]

for a quotient of real dimension

\[
N_d=(d^2-1)^2.
\]

A matrix-valued face takes values in \(M_d(\mathbb C)\), whose real dimension is \(2d^2\). Hence every real first-order face operator has support rank at most \(2d^2\).

This elementary count has a stronger geometric consequence than the usual information-theoretic lower bound: every sharp full-rank design is forced to be an almost direct sum of its face-support subspaces. The total exact overlap budget is only \(O(d^2)\), although the ambient quotient has dimension \(O(d^4)\).

---

## 1. Sequential support geometry

Let \(\mathcal H_d\) denote the real dissipative quotient, \(\dim\mathcal H_d=N_d\). Let a full-rank design contain support subspaces

\[
U_1,\dots,U_L\subset\mathcal H_d,
\qquad
r_j=\dim U_j\le2d^2.
\]

Fix any ordering and put

\[
V_0=\{0\},
\qquad
V_j=U_1+\cdots+U_j.
\]

Define the exact sequential overlap

\[
o_j=\dim(U_j\cap V_{j-1}).
\tag{1.1}
\]

Then

\[
\dim V_j-\dim V_{j-1}=r_j-o_j.
\tag{1.2}
\]

Because the final design is full rank,

\[
\dim V_L=N_d.
\]

Summing (1.2) gives the identity

\[
\boxed{
\sum_{j=1}^{L}o_j
=
\sum_{j=1}^{L}r_j-N_d.
}
\tag{1.3}
\]

The left side depends on the ordering term by term, but its total does not.

---

## 2. Sharp rank-slack theorem

### Theorem 2.1

Let \(\mathcal D\) be any full-rank Coxeter design with the sharp Article-II face count

\[
L=\left\lfloor\frac{d^2}{2}\right\rfloor.
\]

Then for every ordering of its faces,

\[
\boxed{
\sum_j o_j
\le
2d^2L-(d^2-1)^2.
}
\tag{2.1}
\]

Equivalently,

\[
\boxed{
\sum_j o_j
\le
\begin{cases}
2d^2-1, & d\ \text{even},\\[2mm]
d^2-1, & d\ \text{odd}.
\end{cases}
}
\tag{2.2}
\]

#### Proof

By (1.3),

\[
\sum_j o_j=\sum_j r_j-N_d.
\]

Every face rank satisfies \(r_j\le2d^2\), so

\[
\sum_j o_j\le2d^2L-N_d.
\]

If \(d\) is even, \(L=d^2/2\), giving

\[
2d^2L-N_d
=d^4-(d^2-1)^2
=2d^2-1.
\]

If \(d\) is odd, \(L=(d^2-1)/2\), giving

\[
2d^2L-N_d
=d^2(d^2-1)-(d^2-1)^2
=d^2-1.
\]

\(\square\)

### Corollary 2.2 — constant average exact overlap

For every sharp full-rank design,

\[
\boxed{
\frac1L\sum_j o_j
\le
\begin{cases}
4-\dfrac{2}{d^2}, & d\ \text{even},\\[3mm]
2, & d\ \text{odd}.
\end{cases}
}
\tag{2.3}
\]

Thus a sharp face of possible rank \(O(d^2)\) loses only \(O(1)\) dimensions to exact overlap with the previous span on average.

---

## 3. Nominal support redundancy is asymptotically critical

Define

\[
\rho_{\mathrm{supp}}
=
\frac{\sum_j r_j}{N_d}.
\tag{3.1}
\]

For a sharp full-rank design,

\[
1\le\rho_{\mathrm{supp}}
\le\rho_d^{\max},
\]

where

\[
\boxed{
\rho_d^{\max}
=
\begin{cases}
\dfrac{d^4}{(d^2-1)^2}, & d\ \text{even},\\[3mm]
\dfrac{d^2}{d^2-1}, & d\ \text{odd}.
\end{cases}
}
\tag{3.2}
\]

Hence

\[
\boxed{
\rho_d^{\max}=1+O(d^{-2}).
}
\tag{3.3}
\]

So sharp tomography operates in a near-critical rank regime: the total support dimension exceeds the ambient quotient dimension by only a relative \(O(d^{-2})\) margin.

---

## 4. Consequence: the instability problem is about near-overlap, not exact overlap

Theorem 2.1 rules out one possible explanation of poor sharp conditioning.

A sharp full-rank design cannot waste \(O(d^2)\) exact dimensions per face by repeatedly intersecting the previously measured span. Its average exact loss is bounded by a constant.

Therefore any severe conditioning degradation must be caused by quantitative phenomena invisible to rank:

- principal angles that are nonzero but very small;
- inherited weak directions in the previously measured complement;
- Schur coupling between the current blind sector and those weak directions;
- within-face singular weighting before polar normalization.

This gives the exact hierarchy

\[
\boxed{
\text{small exact-overlap budget}
\not\Rightarrow
\text{stable transversality}.
}
\tag{4.1}
\]

In particular, Article II's sharpness theorem places the problem precisely in the regime where **near intersections**, rather than large exact intersections, can dominate stability.

---

## 5. Principal-angle form of novelty

Let \(P_j\) be the support projector of \(U_j\), and let \(P_{V_{j-1}}\) project onto the previous span. The exact overlap \(o_j\) counts the principal angles equal to zero between \(U_j\) and \(V_{j-1}\).

The new support dimension is

\[
\nu_j=r_j-o_j.
\tag{5.1}
\]

For stability, however, the relevant quantity is not only \(\nu_j\), but the smallest positive sine of the remaining principal angles. Define

\[
s_j^2
=
\lambda_{\min}^{+}
\left(
P_{V_{j-1}^{\perp}}P_jP_{V_{j-1}^{\perp}}
\right).
\tag{5.2}
\]

Then \(s_j>0\) exactly on the newly added quotient directions, while small \(s_j\) records a near intersection that rank cannot see.

Theorem 2.1 says that only \(O(1)\) principal angles per face can be exactly zero on average in a sharp design. Article III must determine whether a much larger collection of principal angles is nevertheless forced to be very small.

---

## 6. New sharp-stability formulation

A sharp support design can be polynomially stable only if its near-direct-sum geometry is also quantitatively transverse.

The natural new target is therefore an ordering with

\[
\boxed{
s_j^2\ge d^{-O(1)}}
\tag{6.1}
\]

for every genuine rank-growth step, together with polynomial control of the accumulated positive spectral gap and Schur coupling from `ARTICLE-III-SCHUR-TRANSVERSALITY-THEOREM-v0.1.md`.

Conversely, an all-ordering theorem forcing some

\[
s_j^2\le d^{-\omega(1)}
\]

for every sharp Coxeter design would be a direct route to a stable-minimality obstruction.

---

## 7. Claim firewall

The theorem is an exact rank-budget statement. It does not prove:

- that sharp designs are ill-conditioned;
- that small principal angles are unavoidable;
- that a particular ordering is optimal;
- that oversampling is necessary;
- any asymptotic lower bound on the actual condition number.

It proves that sharp full-rank Coxeter tomography is necessarily a **near-direct-sum rank geometry**, so the unresolved robustness problem is genuinely quantitative rather than algebraic.
