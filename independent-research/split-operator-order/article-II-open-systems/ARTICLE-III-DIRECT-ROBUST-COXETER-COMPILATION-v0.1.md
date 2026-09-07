# Article III — Direct All-d Robust Coxeter Compilation with Explicit Fourier–Sidon Anchors

**Author:** Malachevsky, A.A. / Малачевский А.А.  
**ORCID:** 0009-0008-6009-3196  
**Date:** 2026-09-06  
**Status:** `PROVED / FRESH ALL-D ROBUST COXETER DESIGN / O(d^2) FACES / NO RECURSIVE ACCUMULATION`

## 0. Purpose

`ARTICLE-III-DIRECT-WEYL-COHOMOLOGICAL-GAP-v0.1.md` proves a fresh, nonrecursive, polynomially stable all-dimensional flat-loop design. The remaining compilation question is whether the same qualitative advantage survives inside the actual adjacent-transposition Coxeter geometry of Articles I–II.

`ALL-D-COXETER-OD2-v0.1.md` already gives a `3d^2-1` Coxeter-face identifiability theorem, but its proof uses two abstract dense anchors and therefore contains no quantitative spectral gap.

This note removes the dense-generation step completely. The two anchors are made explicit:

1. a polynomially separated diagonal Sidon phase anchor;
2. the discrete Fourier transform.

Their conjugation actions have a quantitatively controlled common commutant: on unital superoperators the only common fixed direction modulo Hamiltonian derivations is the depolarizing direction. Weyl backtracking then removes that direction.

The result is a fresh, all-`d`, genuine Coxeter design with `3d^2-1` faces and an inverse-polynomial lower singular-value bound. No parity recursion and no accumulation of stage losses occur.

---

## 1. Hilbert spaces and quotient gauge

Let

\[
\mathsf H_d=M_d(\mathbb C)
\]

with normalized Hilbert–Schmidt inner product

\[
\langle X,Y\rangle_{2,d}
=\frac1d\operatorname{Tr}(X^*Y).
\]

For a complex-linear map `D`, use the normalized superoperator Hilbert norm

\[
\boxed{
\|D\|_{\mathrm{sop}}^2
=\frac1{d^2}\sum_{a=1}^{d^2}\|D(E_a)\|_{2,d}^2,
}
\tag{1.1}
\]

where `{E_a}` is any orthonormal basis of `H_d`.

Let

\[
\mathcal G_d
=\{D:D(I)=0,\ D\text{ complex-linear and *-preserving}\}
\]

and let `D_d` be the Hamiltonian derivation subspace. Conjugation by a unitary preserves both `G_d` and `D_d` and is unitary for (1.1). Therefore

\[
\mathcal W_d:=\mathcal D_d^\perp\cap\mathcal G_d
\]

is an invariant orthogonal realization of the quotient

\[
\mathcal Q_d=\mathcal G_d/\mathcal D_d.
\]

All lower-gap estimates below are stated on `W_d`.

---

## 2. Explicit diagonal Sidon anchor

Put

\[
M=2d+1,
\qquad
 e_j=j+Mj^2,
\qquad j=0,\ldots,d-1,
\]

and

\[
\varepsilon_d=\frac1{48d^3}.
\]

Define

\[
Z_d=\operatorname{diag}
(e^{i\varepsilon_de_0},\ldots,e^{i\varepsilon_de_{d-1}}).
\tag{2.1}
\]

Multiply `Z_d` by one common phase so that its determinant is one. This does not change its conjugation action. Henceforth

\[
\boxed{Z_d\in SU(d).}
\]

The exponent set is Sidon: if

\[
e_i+e_j=e_k+e_\ell,
\]

then the unordered pairs coincide. Consequently, if `j!=k` and `r!=s`,

\[
e_k-e_j=e_s-e_r
\]

forces `(j,k)=(r,s)`.

Thus the conjugation operator

\[
V_Z(X)=Z_d^*XZ_d
\]

has eigenspace decomposition

- eigenvalue `1` on the diagonal algebra `D`;
- a distinct one-dimensional eigenspace `C E_jk` for every `j!=k`.

Since every nonzero difference of the relevant integer exponents has magnitude at least one and the total phase window is below `1/4`, there is an absolute `c_Z>0` such that distinct eigenvalues satisfy

\[
\boxed{
|\lambda-\mu|
\ge c_Zd^{-3}.
}
\tag{2.2}

---

## 3. Fourier anchor

Let `F_d` be the normalized discrete Fourier transform

\[
(F_d)_{ab}=d^{-1/2}\omega^{ab},
\qquad
\omega=e^{2\pi i/d}.
\]

Multiply by one common phase to obtain

\[
\boxed{F_d\in SU(d).}
\]

Again the conjugation action is unchanged.

For the normalized matrix-unit basis

\[
f_{jk}=\sqrt d\,E_{jk},
\]

one has

\[
\boxed{
F_df_{jk}F_d^*
=\frac1d\sum_{a,b=0}^{d-1}
\omega^{aj-bk}f_{ab}.
}
\tag{3.1}

Every coefficient has modulus `1/d`.

---

## 4. Exact common-commutant theorem

For a unitary `U`, write

\[
\mathscr U_U(T)
=\operatorname{Ad}_U\circ T\circ\operatorname{Ad}_{U^*}.
\]

### Theorem 4.1 — Fourier–Sidon common commutant

If a complex-linear superoperator `T:M_d->M_d` commutes with both conjugation actions `Ad_Z` and `Ad_F`, then there are scalars `a,b` such that

\[
\boxed{
T=aP_{\mathbf1}+bP_0,
}
\tag{4.1}

where

\[
P_{\mathbf1}(X)=\tau(X)I,
\qquad
P_0(X)=X-\tau(X)I.
\]

If moreover `T(I)=0`, then `a=0`, so the common fixed space is exactly

\[
\boxed{\mathbb C P_0.}
\tag{4.2}

#### Proof

Commutation with `Ad_Z` and the simple spectrum from Section 2 imply

\[
T(E_{jk})=c_{jk}E_{jk},
\qquad j\ne k,
\]

while `T` acts by an arbitrary linear map `A` on the diagonal algebra.

Now apply commutation with `Ad_F` to an off-diagonal unit `E_jk`. Formula (3.1) has a nonzero coefficient at every matrix unit. Comparing any off-diagonal coefficient gives

\[
c_{ab}=c_{jk}
\]

for all off-diagonal pairs. Hence all `c_jk` equal one scalar `b`.

The diagonal projection of (3.1) is the Fourier diagonal vector with frequency `j-k`. As `j-k` ranges over all nonzero residues, these vectors span the traceless diagonal algebra. Therefore `A=bI` on the traceless diagonal sector.

The identity direction is fixed separately, giving the scalar `a`. This proves (4.1). If `T(I)=0`, then `a=0`. `square`

This exact theorem replaces the dense-generation/Schur-lemma step of the earlier all-`d` Coxeter note.

---

## 5. Quantitative common-commutant gap

Let `P_Z` be the orthogonal projection of the superoperator Hilbert space onto the commutant of `Ad_Z`.

From the eigenspace separation (2.2), the matrix coefficients of a superoperator satisfy

\[
\boxed{
\|T-P_ZT\|_{\mathrm{sop}}
\le C_1d^3
\|\mathscr U_Z(T)-T\|_{\mathrm{sop}}.
}
\tag{5.1}

Now put

\[
T_0=P_ZT.
\]

It has the exact form used in Theorem 4.1: an arbitrary diagonal-sector block `A` and scalars `c_jk` on all off-diagonal matrix units.

Let

\[
\eta=\|\mathscr U_F(T_0)-T_0\|_{\mathrm{sop}}.
\]

Using (3.1), every off-diagonal coefficient of the commutator has the form

\[
\frac{c_{ab}-c_{jk}}d.
\]

Since the unnormalized superoperator Frobenius norm is `d eta`, every such coefficient gives the crude uniform estimate

\[
|c_{ab}-c_{jk}|\le d^2\eta.
\tag{5.2}
\]

Likewise the diagonal component of the same column is

\[
\frac1{\sqrt d}(Au_r-c_{jk}u_r),
\]

where `{u_r}` are the normalized Fourier vectors in the diagonal algebra. Thus for every `r!=0`,

\[
\|Au_r-c_{jk}u_r\|
\le d^{3/2}\eta.
\tag{5.3}
\]

Summing these coefficient bounds gives an absolute `C_2` such that

\[
\boxed{
\operatorname{dist}_{\mathrm{sop}}
(T_0,\operatorname{span}\{P_{\mathbf1},P_0\})
\le C_2d^2\eta.
}
\tag{5.4}

Since

\[
\|\mathscr U_F(T_0)-T_0\|
\le
\|\mathscr U_F(T)-T\|
+2\|T-T_0\|,
\]

(5.1) and (5.4) yield:

### Theorem 5.1 — explicit two-anchor spectral gap

For every unital superoperator `T`,

\[
\boxed{
\operatorname{dist}_{\mathrm{sop}}(T,\mathbb CP_0)
\le
C_3d^5
\left(
\|\mathscr U_Z(T)-T\|_{\mathrm{sop}}
+
\|\mathscr U_F(T)-T\|_{\mathrm{sop}}
\right).
}
\tag{5.5}

For *-preserving maps the scalar in front of `P_0` is real.

No exponent here is claimed optimal.

---

## 6. Coxeter face data

Let `{W_g:g in Z_d^2}` be a determinant-corrected Weyl unitary basis. Central determinant phases do not alter spanning or conjugation.

Use exactly the same face count as in `ALL-D-COXETER-OD2-v0.1.md`:

1. `d^2-1` degenerate braid faces realizing the Weyl backtracks `R_D(W_g)` for every nonidentity `g`;
2. two degenerate braid faces realizing `R_D(Z_d)` and `R_D(F_d)`;
3. `d^2-1` engineered square faces `(Z_d,W_g)`;
4. `d^2-1` engineered square faces `(F_d,W_g)`.

Total:

\[
\boxed{L_d=3d^2-1.}
\tag{6.1}

Every item is an actual adjacent-transposition Coxeter braid or square by the engineered realization theorems already proved in the Article-II research notes.

Define the equal-face measurement norm

\[
\boxed{
\|\mathcal C_dD\|_{\mathrm{face}}^2
=\frac1{L_d}\sum_f\|C_f(D)\|_{2,d}^2.
}
\tag{6.2}

---

## 7. Exact square-to-conjugation error identity

For arbitrary unitaries `U,V`, define

\[
R_D(U)=D(U^*)U+U^*D(U).
\]

Let

\[
J_D(U;X)
=D(U^*XU)-D(U^*)XU-U^*D(X)U-U^*XD(U).
\tag{7.1}

Let `K_D(U,V)` be the engineered-square coefficient and put

\[
C=U^*V^*U.
\]

A direct substitution gives the exact identity

\[
\boxed{
K_D(U,V)-J_D(U;V^*)C^*
=
C R_D(U)U^*VU
+R_D(U)
+U^*R_D(V)U.
}
\tag{7.2}

Therefore

\[
\boxed{
\|J_D(U;V^*)\|_2
\le
\|K_D(U,V)\|_2
+2\|R_D(U)\|_2
+\|R_D(V)\|_2.
}
\tag{7.3}

This is the quantitative replacement for the exact-backtrack hypothesis in the earlier square-to-conjugation lemma.

---

## 8. From square residuals to quotient conjugation residuals

Let

\[
H_U=D(U)U^*.
\]

Multiplying (7.1) by `U` and `U^*` gives

\[
\mathscr U_U(D)-D
=
U J_D(U;\cdot)U^*
-\operatorname{ad}_{H_U}
+L_{G_U},
\tag{8.1}

where

\[
G_U
=UD(U^*)+D(U)U^*
=UR_D(U)U^*.
\]

Because `D` is *-preserving,

\[
H_U+H_U^*=G_U.
\]

Thus the skew-adjoint part of `H_U` contributes a Hamiltonian derivation, while the non-Hamiltonian part is bounded by `R_D(U)`.

Projecting (8.1) to `W_d` therefore gives

\[
\boxed{
\|P_{\mathcal W_d}(\mathscr U_U(D)-D)\|_{\mathrm{sop}}
\le
\|J_D(U;\cdot)\|_{\mathrm{sop}}
+C_4\|R_D(U)\|_2.
}
\tag{8.2}

Using the Weyl basis in (7.3) and including the identity basis element, for which `J_D(U;I)=-R_D(U)`, gives

\[
\|J_D(U;\cdot)\|_{\mathrm{sop}}
\le
\left(\frac1{d^2}\sum_g\|K_D(U,W_g)\|_2^2\right)^{1/2}
+C_5\|R_D(U)\|_2
+C_5\left(\frac1{d^2}\sum_g\|R_D(W_g)\|_2^2\right)^{1/2}.
\tag{8.3}

For the equal-face norm (6.2), the group-averaged square and Weyl-backtrack terms are bounded by an absolute multiple of `||C_dD||_face`, whereas each single anchor backtrack obeys

\[
\|R_D(U)\|_2
\le\sqrt{L_d}\,\|\mathcal C_dD\|_{\mathrm{face}}
\le2d\,\|\mathcal C_dD\|_{\mathrm{face}}.
\]

Hence for `U=Z_d,F_d`,

\[
\boxed{
\|P_{\mathcal W_d}(\mathscr U_U(D)-D)\|_{\mathrm{sop}}
\le C_6d\,\|\mathcal C_dD\|_{\mathrm{face}}.
}
\tag{8.4}

---

## 9. Distance to the depolarizing line

Take `D in W_d`. Since `W_d` is invariant under unitary conjugation,

\[
P_{\mathcal W_d}(\mathscr U_U(D)-D)
=
\mathscr U_U(D)-D.
\]

Apply Theorem 5.1 and (8.4): there exists a real scalar `lambda` such that

\[
\boxed{
\|D-\lambda P_0\|_{\mathrm{sop}}
\le
C_7d^6\,\|\mathcal C_dD\|_{\mathrm{face}}.
}
\tag{9.1}

This is the quantitative version of the old qualitative statement that the only conjugation-invariant quotient direction is depolarizing.

---

## 10. Weyl backtracking removes the depolarizing line

Every nonidentity Weyl operator is traceless, so

\[
P_0(W_g)=W_g.
\]

Therefore

\[
\boxed{
R_{P_0}(W_g)=2I.
}
\tag{10.1}

Let

\[
r_W(D)^2
=\frac1{d^2}\sum_g\|R_D(W_g)\|_2^2.
\]

The identity term is zero. From the face count,

\[
r_W(D)\le\sqrt3\,\|\mathcal C_dD\|_{\mathrm{face}}.
\tag{10.2}
\]

Moreover for every superoperator `E`,

\[
\boxed{
r_W(E)\le2\|E\|_{\mathrm{sop}}.}
\tag{10.3}

Write

\[
D=\lambda P_0+E
\]

with `E` satisfying (9.1). Since the depolarizing backtrack RMS is bounded below by an absolute multiple of `|lambda|`, (10.2)--(10.3) give

\[
|\lambda|
\le C_8\left(
\|\mathcal C_dD\|_{\mathrm{face}}+
\|E\|_{\mathrm{sop}}
\right).
\]

Combining with (9.1):

\[
\boxed{
\|D\|_{\mathrm{sop}}
\le
C_9d^6\,\|\mathcal C_dD\|_{\mathrm{face}}
\qquad
(D\in\mathcal W_d).
}
\tag{10.4}

---

## 11. Direct robust Coxeter theorem

### Theorem 11.1 — fresh all-dimensional polynomially stable Coxeter tomography

For every `d>=2`, the explicit `3d^2-1` Coxeter-face design of Section 6 identifies every bounded unital *-preserving generator on `M_d(C)` modulo Hamiltonian derivations and satisfies

\[
\boxed{
\sigma_{\min}(\mathcal C_d|_{\mathcal Q_d})
\ge c\,d^{-6}
}
\tag{11.1}

for an absolute `c>0` in the equal-face normalized metric (6.2).

Consequently the lower frame bound obeys

\[
\boxed{
A_d^{\mathrm{Cox}}
\ge c^2d^{-12}.
}
\tag{11.2}

The construction is fresh in every dimension and has no recursively inherited conditioning factors.

---

## 12. Upper norm and condition number

A first-order coefficient of a Coxeter square contains four unitary left/right translates of values `D(U)`; a braid contains six. For a unitary input `U`,

\[
\|D(U)\|_{2,d}
\le d\|D\|_{\mathrm{sop}},
\]

because the operator norm of a `d^2 x d^2` superoperator is at most its unnormalized Frobenius norm.

Therefore every face coefficient obeys

\[
\|C_f(D)\|_{2,d}
\le6d\|D\|_{\mathrm{sop}},
\]

and

\[
\boxed{
\|\mathcal C_d\|
\le6d.
}
\tag{12.1}

Together with (11.1),

\[
\boxed{
\kappa(\mathcal C_d|_{\mathcal Q_d})
\le C_{10}d^7.
}
\tag{12.2}

The exponents `6,12,7` are deliberately crude proof-of-polynomiality exponents, not optimization claims.

---

## 13. Consequence for the Article-III programme

The global accumulation barrier is now bypassed **inside genuine Coxeter geometry**, not only for generalized Weyl triangles.

We have proved:

\[
\boxed{
\text{fresh all-}d\text{ robust Coxeter tomography exists with }O(d^2)\text{ faces},
}
\]

with an explicit inverse-polynomial lower frame bound.

Therefore the central unresolved problem is no longer whether robust Coxeter tomography exists asymptotically. It does.

The sharp frontier is now:

\[
\boxed{
L_d^{\mathrm{sharp}}=\lfloor d^2/2\rfloor
\quad\text{versus}\quad
L_d^{\mathrm{rob}}=O(d^2),
}
\]

and specifically whether the constant-factor compression from approximately `3d^2` faces down to the information-theoretic sharp count can retain an inverse-polynomial lower frame bound.

This is the natural central theorem problem for Article III.

---

## 14. Claim firewall

This note proves:

- an explicit Fourier–Sidon two-anchor common-commutant theorem;
- a quantitative polynomial two-anchor spectral gap;
- a quantitative square-to-conjugation error identity;
- a fresh all-dimensional `3d^2-1` genuine Coxeter design with inverse-polynomial stability;
- elimination of recursive parity accumulation as a necessary obstruction to robust Coxeter tomography.

It does **not** prove:

- polynomial stability at the sharp count `floor(d^2/2)`;
- optimal polynomial exponents;
- necessity of a constant-factor redundancy above the sharp count;
- statistical/sample-complexity optimality;
- process-tensor or non-Markovian results.
