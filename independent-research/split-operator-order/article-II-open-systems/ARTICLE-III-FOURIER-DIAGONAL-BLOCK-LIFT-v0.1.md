# Article III — Fourier Diagonal Block Lift at the Sharp Compression Frontier

**Author:** Malachevsky, A.A. / Малачевский А.А.  
**ORCID:** 0009-0008-6009-3196  
**Date:** 2026-09-08  
**Status:** `PROVED / WEYL-ONLY SHARP OBSTRUCTION / THREE-FACE FOURIER DIAGONAL RECOVERY / POLYNOMIAL BLOCK LIFT`

## 0. Purpose

The critical-block reduction shows that sharp robustness is not an ordinary scalar restricted-invertibility problem. The missing mechanism must exploit whole matrix-valued Coxeter faces.

This note isolates the first genuinely block-level phenomenon.

There are two complementary results.

1. If every transport in every selected square is a Weyl unitary, then the Weyl-diagonal dissipative sector can contribute at most **one real scalar constraint per face**. Hence a Weyl-only square design needs at least `d^2-1` faces and can never attain the sharp count `floor(d^2/2)`.

2. For every odd `d`, **three explicit Fourier--Weyl Coxeter squares** already determine that entire `d^2-1` dimensional Weyl-diagonal sector with an inverse-polynomial gap `Omega(d^-2)`.

Thus the sharp compression mechanism must use non-Weyl block mixing, and the discrete Fourier transform supplies exactly such a high-leverage block.

---

## 1. Weyl coordinates

Let

\[
G=\mathbb Z_d^2,
\qquad m=|G|=d^2.
\]

Choose a phase convention for the Weyl system `{W_x:x in G}` such that

\[
W_0=I,
\qquad
W_x^*=W_{-x},
\]

and

\[
W_xW_y=\sigma(x,y)W_{x+y}.
\]

The projective commutator is the alternating bicharacter

\[
\chi(x,y)
=\frac{\sigma(x,y)}{\sigma(y,x)},
\qquad
W_xW_y=\chi(x,y)W_yW_x.
\]

Conjugation is phase-free:

\[
\alpha_x(A)=W_x^*AW_x,
\qquad
\alpha_x(W_r)=\chi(x,r)W_r.
\tag{1.1}
\]

The Weyl operators are orthonormal for the normalized Hilbert--Schmidt product.

For a normalized map `D(I)=0`, put

\[
A_x=W_x^*D(W_x).
\tag{1.2}
\]

---

## 2. Weyl-diagonal dissipative sector

Define

\[
\mathcal V_d^{\mathrm{diag}}
=
\left\{
D:\ D(W_x)=\lambda_xW_x,
\ \lambda_0=0,
\ \lambda_{-x}=\overline{\lambda_x}
\right\}.
\tag{2.1}
\]

This is a real subspace of normalized complex-linear `*`-preserving maps of dimension

\[
\boxed{\dim_\mathbb R\mathcal V_d^{\mathrm{diag}}=d^2-1=m-1.}
\tag{2.2}
\]

It is the Weyl-diagonal Kossakowski sector. Hamiltonian derivations have no nonzero vector in this sector, so it embeds faithfully into the dissipative quotient.

In the normalized superoperator Hilbert norm,

\[
\boxed{
\|D\|_{\mathrm{sop}}^2
=\frac1m\sum_{x\ne0}|\lambda_x|^2.
}
\tag{2.3}

---

## 3. Exact square coefficient for Weyl first transports

For unitaries `U,V`, use the engineered square with contextual transports

\[
T_1=U,
\quad
T_2=V,
\quad
T_3=U^*,
\quad
T_4=U^*V^*U.
\]

Let

\[
P_k=T_k\cdots T_1,
\qquad P_0=I.
\]

For any normalized `D`, the first-order square coefficient is

\[
\boxed{
K_D(U,V)
=\sum_{k=1}^4P_{k-1}^{-1}A_{T_k}P_{k-1},
}
\tag{3.1}
\]

where

\[
A_T=T^*D(T).
\]

Indeed `D(T_k)=T_kA_{T_k}` and flatness gives

\[
T_4\cdots T_{k+1}T_k=P_{k-1}^{-1}.
\]

Now take

\[
U=W_h,
\qquad
V=W_g.
\]

For `D in V_diag`, every `A_{W_x}=lambda_x I`. Hence the complete square coefficient is scalar:

\[
\boxed{
K_D(W_h,W_g)
=
(\lambda_h+\lambda_g+\lambda_{-h}+\lambda_{-g})I.
}
\tag{3.2}

Because `lambda_-x=conj(lambda_x)`, its scalar coefficient is real:

\[
\lambda_h+\lambda_{-h}
+\lambda_g+\lambda_{-g}
=2\operatorname{Re}\lambda_h+2\operatorname{Re}\lambda_g.
\tag{3.3}
\]

Thus a Weyl--Weyl square supplies at most **one real scalar row** on `V_diag`.

The same statement holds for a Weyl backtracking braid: on `V_diag` its coefficient is

\[
R_D(W_h)
=(\lambda_h+\lambda_{-h})I,
\]
again one real row.

---

## 4. Weyl-only sharp obstruction

### Theorem 4.1 — Weyl-only faces cannot be sharp

Any Coxeter design built only from

- engineered squares whose first two contextual transports are Weyl unitaries, and/or
- degenerate Weyl backtracking braids,

requires at least

\[
\boxed{d^2-1}
\tag{4.1}
\]

faces to identify the quotient universally.

#### Proof

The restriction of the measurement map to the faithful quotient subspace `V_diag` has domain dimension `d^2-1`. By Section 3 each allowed face has real rank at most one on this subspace. Hence at least `d^2-1` faces are necessary. `square`

For every `d>=3`,

\[
d^2-1>\lfloor d^2/2\rfloor.
\]

Therefore a sharp design must contain genuinely non-Weyl mixing faces.

This is a block-compatibility obstruction, not merely a counting restatement: the Weyl faces have full matrix outputs, but all of that output collapses to one scalar on an explicit `d^2-1` dimensional quotient sector.

---

## 5. Flat Weyl spectrum of the Fourier transform

Assume now that `d` is odd. Let

\[
F_d=(d^{-1/2}\omega^{jk})_{j,k=0}^{d-1},
\qquad
\omega=e^{2\pi i/d}.
\]

Multiply by one scalar phase so that `F_d in SU(d)`; this does not affect any norm below.

Expand

\[
F_d=\sum_{x\in G}c_xW_x.
\tag{5.1}
\]

For `x=(a,b)`, direct trace evaluation gives a quadratic Gauss sum

\[
c_{a,b}
=\tau(W_{a,b}^*F_d)
=\frac1{d\sqrt d}\sum_{j=0}^{d-1}
\omega^{j^2+(a-b)j}
\]

up to a unit scalar depending only on the Weyl phase convention.

Since `d` is odd and the quadratic coefficient is a unit modulo `d`, the quadratic Gauss sum has modulus `sqrt(d)`. Therefore

\[
\boxed{|c_x|=\frac1d=\frac1{\sqrt m}}
\tag{5.2}
\]

for every `x in G`.

Hence the Fourier transform is a **flat Weyl vector**.

---

## 6. The Fourier evaluation map is an isometry on the diagonal sector

For `D in V_diag`,

\[
D(F_d)
=\sum_{x\ne0}c_x\lambda_xW_x.
\tag{6.1}
\]

Using (5.2),

\[
\|D(F_d)\|_{2,d}^2
=
\frac1m\sum_{x\ne0}|\lambda_x|^2
=
\|D\|_{\mathrm{sop}}^2.
\]

Thus with

\[
\boxed{A=F_d^*D(F_d)}
\tag{6.2}
\]

one has the exact norm identity

\[
\boxed{\|A\|_{2,d}=\|D\|_{\mathrm{sop}}.}
\tag{6.3}

This is the block-lift mechanism: one unitary input simultaneously carries all `d^2-1` Weyl-diagonal coordinates at equal amplitude.

---

## 7. Fourier--Weyl square formula

Let `V=W_g`. Since `F_d` normalizes the Weyl group, there is an invertible symplectic automorphism

\[
J:G\to G
\]

such that

\[
F_d^*W_gF_d
=\zeta_gW_{Jg}
\tag{7.1}
\]

for a unit scalar `zeta_g`.

For `D in V_diag`, use the square

\[
(U,V)=(F_d,W_g).
\]

The second and fourth logarithmic coefficients in (3.1) are scalar:

\[
A_{W_g}=\lambda_gI,
\qquad
A_{F_d^*W_g^*F_d}=\lambda_{-Jg}I.
\]

Because `D` is `*`-preserving,

\[
A_{F_d^*}
=F_dD(F_d^*)
=F_dA^*F_d^*.
\]

The third prefix is `W_gF_d`, so (3.1) gives the exact identity

\[
\boxed{
K_D(F_d,W_g)
=
A+\alpha_{Jg}(A^*)
+(\lambda_g+\lambda_{-Jg})I.
}
\tag{7.2}

Let

\[
P_0(X)=X-\tau(X)I.
\]

Writing

\[
B=P_0A,
\]

the traceless square data are therefore

\[
\boxed{
Q_g(D):=P_0K_D(F_d,W_g)
=B+\alpha_{Jg}(B^*).
}
\tag{7.3}

---

## 8. Three explicit faces force the traceless Fourier block to zero

Choose

\[
g_0=(1,0),
\qquad
g_1=(0,1),
\qquad
g_2=(1,1).
\tag{8.1}
\]

Put

\[
s_j=Jg_j.
\]

Then

\[
u_1=s_1-s_0,
\qquad
u_2=s_2-s_0
\]

form a basis of `G`, because `(g_1-g_0,g_2-g_0)` has determinant `-1` modulo `d`.

If

\[
Q_{g_0}(D)=Q_{g_1}(D)=Q_{g_2}(D)=0,
\]

then

\[
\alpha_{s_0}(B^*)
=\alpha_{s_1}(B^*)
=\alpha_{s_2}(B^*).
\]

Hence

\[
\alpha_{u_1}(C)=C,
\qquad
\alpha_{u_2}(C)=C,
\]

for

\[
C=\alpha_{s_0}(B^*).
\]

Since `u_1,u_2` generate `G`, the only matrix commuting with both corresponding Weyl generators is scalar. But `C` is traceless. Therefore

\[
B=0.
\tag{8.2}
\]

Thus `A` is scalar.

If `A=aI`, then

\[
D(F_d)=aF_d.
\]

The identity Weyl coefficient of the left side is zero because `lambda_0=0`; the identity Weyl coefficient of `aF_d` is `ac_0` and `c_0!=0`. Therefore `a=0`, hence `D=0` by the isometry (6.3).

So the three faces are exactly injective on `V_diag`.

---

## 9. Quantitative torus Poincare estimate

Let

\[
\varepsilon^2
=\frac13\sum_{j=0}^2\|Q_{g_j}(D)\|_{2,d}^2.
\tag{9.1}
\]

From (7.3),

\[
\alpha_{s_i}(B^*)-\alpha_{s_0}(B^*)
=Q_{g_i}(D)-Q_{g_0}(D).
\]

After conjugating by `alpha_-s0`, put

\[
C=\alpha_{s_0}(B^*).
\]

Then

\[
(\alpha_{u_i}-I)C
=\alpha_{-s_0}(Q_{g_i}-Q_{g_0}),
\qquad i=1,2.
\tag{9.2}
\]

Expand the traceless matrix

\[
C=\sum_{x\ne0}c_xW_x.
\]

Because `u_1,u_2` are a basis, for every `x!=0` at least one of the two phases

\[
\chi(u_1,x),\qquad\chi(u_2,x)
\]

is nontrivial. Hence

\[
|\chi(u_1,x)-1|^2+|\chi(u_2,x)-1|^2
\ge4\sin^2(\pi/d).
\]

For `d>=3`,

\[
\sin(\pi/d)\ge\frac2d.
\]

Therefore

\[
\boxed{
\|C\|_{2,d}
\le
\frac d4
\left(
\|(\alpha_{u_1}-I)C\|_2^2
+
\|(\alpha_{u_2}-I)C\|_2^2
\right)^{1/2}.
}
\tag{9.3}

Using

\[
\|Q_i-Q_0\|^2\le2\|Q_i\|^2+2\|Q_0\|^2
\]

and (9.1),

\[
\boxed{
\|B\|_{2,d}
\le
\frac{\sqrt{12}}4\,d\,\varepsilon.
}
\tag{9.4}

---

## 10. Recovering the scalar part of A

Write

\[
A=aI+B,
\qquad \tau(B)=0.
\]

Then

\[
D(F_d)=F_dA=aF_d+F_dB.
\]

The identity Weyl coefficient of `D(F_d)` is zero. Since

\[
|c_0|=1/d,
\]

we obtain

\[
\frac{|a|}{d}
=|\tau(F_dB)|
\le\|B\|_{2,d}.
\]

Thus

\[
|a|\le d\|B\|_{2,d}
\]

and therefore

\[
\|A\|_{2,d}
\le(d+1)\|B\|_{2,d}.
\]

Combining with (6.3) and (9.4) gives

\[
\boxed{
\|D\|_{\mathrm{sop}}
\le C d^2\varepsilon
}
\tag{10.1}
\]

for an absolute constant `C`.

---

## 11. Three-face Fourier diagonal theorem

### Theorem 11.1

For every odd `d>=3`, the three explicit genuine Coxeter squares

\[
(F_d,W_{(1,0)}),
\qquad
(F_d,W_{(0,1)}),
\qquad
(F_d,W_{(1,1)})
\]

identify the full Weyl-diagonal quotient sector `V_diag` of real dimension `d^2-1`.

In the equal-three-face norm of the traceless square outputs,

\[
\boxed{
\sigma_{\min}
\ge c d^{-2}
}
\tag{11.1}
\]

for an absolute `c>0`.

All three ordered pairs are realized by actual adjacent-transposition engineered Coxeter squares.

---

## 12. Consequence for block-compatible sharp compression

The Weyl-only obstruction and the Fourier block lift together show that the correct sharp architecture cannot be a homogeneous selection of weakly mixing Weyl faces.

Instead it must be hybrid:

\[
\boxed{
\text{a small number of dense non-Weyl mixing faces}
+
\text{many sparse/local faces}
+
\text{low-dimensional Schur closure}.
}
\]

One Fourier block uses only three whole faces yet controls an `O(d^2)` quotient sector with an inverse-polynomial gap. This is exactly the kind of block leverage absent from scalar restricted invertibility.

The next strict problem is to exploit the **remaining outputs of the same three Fourier faces** together with `L_d^sharp-3` additional local/sparse faces to build a core of codimension only `s_d=O(d^2)`.

---

## 13. Claim firewall

This note proves:

- a sharp-count obstruction for Weyl-only square/backtrack designs;
- flat Weyl expansion of the Fourier transform for odd `d`;
- exact three-face injectivity on the Weyl-diagonal sector;
- an inverse-polynomial `Omega(d^-2)` lower singular gap on that sector.

It does **not** yet prove:

- a block-compatible near-full core on the full quotient;
- sharp polynomial robustness;
- the analogous flat-Fourier statement for even `d` in the same phase convention;
- optimal constants or exponents.
