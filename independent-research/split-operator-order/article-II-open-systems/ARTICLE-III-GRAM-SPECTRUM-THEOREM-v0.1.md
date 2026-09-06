# Article III — Exact Kossakowski Gram Spectrum and Closed-Form Whitening

**Author:** Malachevsky, A.A. / Малачевский А.А.  
**ORCID:** 0009-0008-6009-3196  
**Date:** 2026-09-06  
**Status:** `PROVED / THEOREM-LEVEL NORMALIZATION RESULT`

## 0. Result

The numerical pattern observed in `ARTICLE-III-FIRST-CONDITIONING-EXPERIMENT-v0.1.md` is exact.

For every `d>=2`, the canonical Hermitian Kossakowski coordinates for the dissipative quotient carry an induced Gram operator whose spectrum is

\[
\boxed{\operatorname{spec}(G_d)=\{1,d^2/2,d^2\}}
\]

with multiplicities

\[
\boxed{d^4-3d^2+1,\qquad d^2-1,\qquad 1.}
\]

Moreover the canonical Kossakowski section is exactly orthogonal to the Hamiltonian-derivation sector in the normalized superoperator Hilbert geometry, so the quotient metric requires no further numerical projection.

The proof yields explicit orthogonal projectors and the exact all-dimensional whitening operator.

---

## 1. Hilbert-space conventions

Let

\[
\tau(X)=\frac1d\operatorname{Tr}(X)
\]

and equip `M_d(C)` with

\[
\langle X,Y\rangle_{2,d}=\tau(X^*Y).
\]

Put

\[
q=d^2-1.
\]

Let

\[
\{F_a\}_{a=1}^{q}
\]

be any Hermitian traceless basis satisfying

\[
\tau(F_aF_b)=\delta_{ab}.
\]

On `Herm(q)` use the real Frobenius inner product

\[
\langle C,D\rangle_F=\operatorname{Tr}(CD).
\]

For complex-linear superoperators define the normalized Hilbert-Schmidt inner product by

\[
\langle \mathcal A,\mathcal B\rangle_{\mathrm{sop},d}
=
\frac1{d^2}
\sum_{\mu=1}^{d^2}
\langle \mathcal A(E_\mu),\mathcal B(E_\mu)\rangle_{2,d},
\]

where `E_mu` is any `tau`-orthonormal basis of `M_d(C)`.

---

## 2. Canonical Kossakowski section

For `C in Herm(q)` define

\[
\mathcal L_C(X)
=
\sum_{a,b=1}^{q}C_{ab}
\left(
F_aXF_b-\frac12\{F_aF_b,X\}
\right).
\]

Also define

\[
K_C=\sum_{a,b}C_{ab}F_aF_b,
\qquad
T(C)=K_C-\operatorname{Tr}(C)I.
\]

Because

\[
\tau(K_C)=\sum_{a,b}C_{ab}\tau(F_aF_b)=\operatorname{Tr}(C),
\]

we have

\[
T(C)\in \operatorname{Herm}_0(d).
\]

---

## 3. Completeness identities

The normalized traceless-Hermitian basis satisfies

\[
\boxed{
\sum_{a=1}^{q}F_aXF_a
=
d\operatorname{Tr}(X)I-X
=
d^2\tau(X)I-X.
}
\tag{3.1}
\]

Equivalently,

\[
\boxed{
\sum_a F_a^2=qI.
}
\tag{3.2}
\]

For every `X in M_d(C)`, complex-linearly,

\[
\boxed{
X=\tau(X)I+\sum_a\tau(F_aX)F_a.
}
\tag{3.3}
\]

These are the only basis identities needed below.

---

## 4. Exact Gram formula

### Proposition 4.1

For `C,D in Herm(q)`,

\[
\boxed{
\langle \mathcal L_C,\mathcal L_D\rangle_{\mathrm{sop},d}
=
\operatorname{Tr}(CD)
+\operatorname{Tr}(C)\operatorname{Tr}(D)
+\frac12\tau\!\left(T(C)T(D)\right).
}
\tag{4.1}
\]

#### Proof

Write

\[
\mathcal L_C=\mathcal S_C-\frac12(L_{K_C}+R_{K_C}),
\]

where

\[
\mathcal S_C(X)=\sum_{a,b}C_{ab}F_aXF_b.
\]

For left/right multiplication, the superoperator Hilbert-Schmidt trace gives

\[
\langle L_A R_B,L_C R_D\rangle_{\mathrm{sop},d}
=
\frac1{d^2}\operatorname{Tr}(A^*C)\operatorname{Tr}(B^*D).
\]

Since every `F_a` is traceless, all cross terms between `S_C` and `L_{K_D}+R_{K_D}` vanish. The sandwich term gives

\[
\langle \mathcal S_C,\mathcal S_D\rangle_{\mathrm{sop},d}
=\operatorname{Tr}(CD).
\]

The anticommutator contribution is

\[
\frac12\tau(K_CK_D)
+\frac12\operatorname{Tr}(C)\operatorname{Tr}(D).
\]

Finally

\[
\tau(T(C)T(D))
=
\tau(K_CK_D)-\operatorname{Tr}(C)\operatorname{Tr}(D),
\]

which gives (4.1). `square`

---

## 5. Orthogonality to Hamiltonian derivations

Let

\[
\delta_H(X)=i[H,X],
\qquad H=H^*,\quad \operatorname{Tr}H=0.
\]

### Proposition 5.1

For every `C in Herm(q)` and every traceless Hermitian `H`,

\[
\boxed{
\langle \mathcal L_C,\delta_H\rangle_{\mathrm{sop},d}=0.
}
\tag{5.1}
\]

#### Proof

The sandwich part is orthogonal separately to `L_H` and `R_H` because each factor contains a traceless `F_a` on the opposite side.

For the anticommutator part, the only nonzero terms are

\[
\langle L_{K_C},iL_H\rangle_{\mathrm{sop},d}
\quad\text{and}\quad
\langle R_{K_C},-iR_H\rangle_{\mathrm{sop},d},
\]

and they have equal magnitude and opposite sign. The mixed left-right terms vanish because `Tr(H)=0`. Hence the total inner product is zero. `square`

### Corollary 5.2 — exact orthogonal quotient section

Let `G_d` be the real space of complex-linear, *-preserving maps `F:M_d->M_d` satisfying `F(I)=0`, and let `D_d` be the Hamiltonian derivation subspace. Then

\[
\boxed{
G_d=D_d\oplus^{\perp}\{\mathcal L_C:C\in\operatorname{Herm}(q)\}.
}
\tag{5.2}
\]

Indeed, Proposition 4.1 implies `||L_C||>0` for `C!=0`, so the Kossakowski section has real dimension `q^2`. Since

\[
\dim G_d=q(q+1),
\qquad
\dim D_d=q,
\]

its orthogonal complement has exactly dimension `q^2`.

Therefore the Kossakowski Gram form (4.1) is not merely a convenient coordinate metric: it is exactly the quotient metric on

\[
Q_d=G_d/D_d.
\]

---

## 6. The multiplication map `T`

Equip `Herm_0(d)` with the real Hilbert product `tau(AB)`.

### Proposition 6.1 — adjoint of `T`

For `A in Herm_0(d)`,

\[
\boxed{
(T^*A)_{ab}=\tau(F_aAF_b).
}
\tag{6.1}
\]

#### Proof

Because `tau(A)=0`,

\[
\tau(A T(C))=\tau(AK_C)
=\sum_{a,b}C_{ab}\tau(AF_aF_b).
\]

Using cyclicity,

\[
\tau(AF_aF_b)=\tau(F_bAF_a),
\]

which is exactly the Frobenius pairing with the Hermitian matrix whose `(a,b)` entry is `tau(F_aAF_b)`. `square`

### Proposition 6.2 — exact singular value of `T`

On `Herm_0(d)`,

\[
\boxed{
TT^*=(d^2-2)I.
}
\tag{6.2}
\]

#### Proof

Let `A` be traceless Hermitian. First,

\[
\operatorname{Tr}(T^*A)
=
\sum_a\tau(F_aAF_a)
=
\tau\left(\sum_aF_aAF_a\right)
=-\tau(A)=0
\]

by (3.1).

Next,

\[
K_{T^*A}
=
\sum_{a,b}\tau(F_aAF_b)F_aF_b.
\]

For fixed `a`, cyclicity and (3.3) give

\[
\sum_b\tau(F_aAF_b)F_b
=
\sum_b\tau(F_bF_aA)F_b
=
F_aA-\tau(F_aA)I.
\]

Hence

\[
K_{T^*A}
=
\sum_aF_a^2A-\sum_a\tau(F_aA)F_a.
\]

Using (3.2), and then (3.3) with `tau(A)=0`,

\[
K_{T^*A}
=qA-A=(q-1)A=(d^2-2)A.
\]

Since `Tr(T^*A)=0`, the subtraction in `T` contributes nothing. Therefore

\[
TT^*A=(d^2-2)A.
\]

`square`

### Corollary 6.3

`T` is surjective, has rank `q=d^2-1`, and all of its nonzero singular values are

\[
\sqrt{d^2-2}.
\]

---

## 7. Exact Gram-spectrum theorem

Define three mutually orthogonal subspaces of `Herm(q)`:

\[
\mathcal S_d=\mathbb RI_q,
\]

\[
\mathcal A_d=\operatorname{im}T^*,
\]

\[
\mathcal R_d=\ker T\cap\{C:\operatorname{Tr}C=0\}.
\]

Here `A_d` is the canonical copy of the adjoint sector selected by matrix multiplication; no claim is made that it is the only abstract adjoint copy in a full representation-theoretic decomposition.

Because `T(I_q)=0` and `Tr(T^*A)=0`,

\[
\operatorname{Herm}(q)
=
\mathcal R_d\oplus^{\perp}\mathcal A_d\oplus^{\perp}\mathcal S_d.
\tag{7.1}
\]

Their dimensions are

\[
\dim\mathcal S_d=1,
\]

\[
\dim\mathcal A_d=q=d^2-1,
\]

\[
\dim\mathcal R_d=q^2-q-1=d^4-3d^2+1.
\]

Let `bold G_d` denote the positive operator on `Herm(q)` representing the Gram form (4.1) relative to the Frobenius product. Then

\[
\boldsymbol G_d
=I+J+\frac12T^*T,
\qquad
J(C)=\operatorname{Tr}(C)I_q.
\tag{7.2}
\]

### Theorem 7.1 — exact spectrum

For every `d>=2`,

\[
\boxed{
\boldsymbol G_d|_{\mathcal R_d}=I,
}
\tag{7.3}
\]

\[
\boxed{
\boldsymbol G_d|_{\mathcal A_d}=\frac{d^2}{2}I,
}
\tag{7.4}
\]

\[
\boxed{
\boldsymbol G_d|_{\mathcal S_d}=d^2I.
}
\tag{7.5}
\]

Therefore

\[
\boxed{
\operatorname{spec}(G_d)
=
\left\{
1^{[d^4-3d^2+1]},
\left(\frac{d^2}{2}\right)^{[d^2-1]},
(d^2)^{[1]}
\right\}.
}
\tag{7.6}
\]

#### Proof

On `R_d`, both `J` and `T^*T` vanish, giving eigenvalue `1`.

On `A_d=im T^*`, Proposition 6.2 gives

\[
T^*T=(d^2-2)I,
\]

while `J=0`; hence

\[
1+\frac12(d^2-2)=\frac{d^2}{2}.
\]

On the scalar direction, `T=0` and

\[
J(I_q)=qI_q=(d^2-1)I_q,
\]

so the eigenvalue is

\[
1+q=d^2.
\]

The multiplicities are the dimensions above. `square`

---

## 8. Closed-form projectors and whitening

Define

\[
P_{\mathrm{s}}(C)=\frac{\operatorname{Tr}C}{q}I_q.
\tag{8.1}
\]

By Proposition 6.2,

\[
\boxed{
P_{\mathrm{a}}=\frac1{d^2-2}T^*T
}
\tag{8.2}
\]

is the orthogonal projector onto `A_d`. Explicitly,

\[
\boxed{
(P_{\mathrm{a}}C)_{ab}
=
\frac1{d^2-2}
\tau\left(F_aT(C)F_b\right).
}
\tag{8.3}
\]

Finally

\[
P_{\mathrm{r}}=I-P_{\mathrm{s}}-P_{\mathrm{a}}.
\tag{8.4}
\]

Hence

\[
\boxed{
\boldsymbol G_d
=
P_{\mathrm{r}}
+\frac{d^2}{2}P_{\mathrm{a}}
+d^2P_{\mathrm{s}}.
}
\tag{8.5}
\]

The exact inverse square root is

\[
\boxed{
\boldsymbol G_d^{-1/2}
=
P_{\mathrm{r}}
+\frac{\sqrt2}{d}P_{\mathrm{a}}
+\frac1dP_{\mathrm{s}}.
}
\tag{8.6}
\]

and

\[
\boxed{
\boldsymbol G_d^{-1}
=
P_{\mathrm{r}}
+\frac{2}{d^2}P_{\mathrm{a}}
+\frac1{d^2}P_{\mathrm{s}}.
}
\tag{8.7}
\]

Thus a raw real measurement matrix `M_raw` written in Frobenius-orthonormal Hermitian Kossakowski coordinates is canonically whitened by

\[
\boxed{
M_{\mathrm{norm}}=M_{\mathrm{raw}}\,\boldsymbol G_d^{-1/2}.
}
\tag{8.8}
\]

No numerical eigendecomposition of the domain Gram matrix is needed in any dimension.

---

## 9. Consequences for Article III

### Corollary 9.1 — domain-coordinate distortion is exactly controlled

The condition number of the Kossakowski Gram operator itself is

\[
\kappa(\boldsymbol G_d)=d^2,
\]

while the norm-distortion factor between raw Frobenius coordinates and canonical quotient coordinates is exactly

\[
\boxed{d.}
\]

Therefore any worse scaling observed after applying (8.6) belongs to the measurement design rather than to an unresolved domain-coordinate artifact.

### Corollary 9.2 — previous numerical spectrum promoted to theorem

The values observed for `d=2,3,4,5`,

- `d=2`: `1 x5`, `2 x3`, `4 x1`;
- `d=3`: `1 x55`, `4.5 x8`, `9 x1`;
- `d=4`: `1 x209`, `8 x15`, `16 x1`;
- `d=5`: `1 x551`, `12.5 x24`, `25 x1`,

are instances of Theorem 7.1 and no longer numerical evidence.

### Corollary 9.3 — quotient projection is closed

The earlier numerical observation that no additional Hamiltonian quotient correction was needed is now proved by Proposition 5.1 and Corollary 5.2.

---

## 10. What remains open

This theorem closes the **domain-normalization barrier**. It does not yet solve the independent **face-resource normalization problem** when designs with different loop lengths, control costs, or admissible transport classes are compared.

For the present finite unitary face pools, equal-face weighting is mathematically well-defined. A physical resource model may instead weight by edge count, control time, control energy, or experimental variance; those are distinct operational choices and must not be silently conflated.

The next strict Article-III problem is therefore measurement-side:

\[
\boxed{
\text{after exact whitening, what lower frame bounds are achievable by sharp and oversampled Coxeter designs?}
}
\]

The first numerical target is to re-run all small-dimensional searches using the closed-form projector formula (8.6), then build dimension-scalable unitary face pools and test whether the best sharp condition number is polynomially bounded or whether stable inversion requires genuine redundancy.

---

## 11. Claim firewall

The theorem proves an exact Hilbert-space normalization result for the finite-dimensional first-order Kossakowski quotient. It does not prove:

- asymptotic conditioning of Coxeter designs;
- a redundancy lower bound;
- statistical or sample-complexity optimality;
- robustness to SPAM or experimental noise;
- a process-tensor/non-Markovian extension;
- any physical spacetime or gauge curvature statement.
