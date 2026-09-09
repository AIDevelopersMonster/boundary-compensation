# Article III — Quadratic-Phase Forest Core at the Sharp Coxeter Frontier

**Author:** Malachevsky, A.A. / Малачевский А.А.  
**ORCID:** 0009-0008-6009-3196  
**Date:** 2026-09-09  
**Status:** `PROVED / ODD-PRIME BLOCK-COMPATIBLE CORE / EXACT RANK / POLYNOMIAL GAP / SHARP MINUS (p-1) FACES`

## 0. Purpose

The previous critical-block reduction isolated block compatibility as the real obstacle to sharp robustness. The Fourier/phase census then revealed a rigid pattern in `d=3,5`: a long run of quadratic-phase faces is exactly transverse, and only the last `d-1` faces need dense Fourier mixing.

This note proves that pattern for every odd prime dimension `p`.

Let

\[
m=p^2,
\qquad
N_p=(p^2-1)^2,
\qquad
L_p^\sharp=\frac{p^2-1}{2}.
\]

There is an explicit family of

\[
\boxed{K_p=\frac{(p-1)^2}{2}}
\]

genuine Coxeter square faces with one fixed quadratic-phase anchor such that:

1. every face contributes its full real rank `2p^2`;
2. the combined core rank is exactly
   \[
   \boxed{p^2(p-1)^2};
   \]
3. in the equal-face metric the smallest positive singular value is at least `1/p`;
4. only exactly `p-1` additional faces are needed to reach the sharp face count.

Thus the block-compatible core problem is solved on the odd-prime line. The remaining sharp-robustness problem is reduced to a structured `p-1`-face Fourier completion.

---

## 1. Weyl system and the quadratic phase

Work over

\[
G=\mathbb F_p^2.
\]

Choose a Weyl system `{W_(a,b)}` with

\[
W_{(a,b)}=X^aZ^b,
\]

up to the usual harmless projective phase convention.

Let

\[
\omega=e^{2\pi i/p}
\]

and define the quadratic phase gate

\[
\boxed{
P=\operatorname{diag}\bigl(\omega^{j(j-1)/2}\bigr)_{j=0}^{p-1}.
}
\tag{1.1}
\]

After multiplication by a common scalar phase we may take `P in SU(p)` without changing any conjugation action.

Its Weyl support lies entirely on the vertical line

\[
\boxed{
L_Z=\{(0,b):b\in\mathbb F_p\}.
}
\tag{1.2}
\]

Moreover

\[
P^*XP=XZ^{-1},
\qquad
P^*ZP=Z.
\]

Hence, modulo projective phases,

\[
\boxed{
P^*W_{(a,b)}P
\sim W_{S(a,b)},
\qquad
S(a,b)=(a,b-a).
}
\tag{1.3}

---

## 2. Sign classes

For odd `p`, every nonzero Weyl label has a distinct negative. Let

\[
\Omega_p=(G\setminus\{0\})/\{\pm1\}.
\tag{2.1}
\]

Then

\[
\boxed{|\Omega_p|=\frac{p^2-1}{2}=L_p^\sharp.}
\tag{2.2}
\]

A normalized `*`-preserving map is determined, on every sign class `[g]`, by the arbitrary complex matrix

\[
X_{[g]}:=D(W_g),
\]

because `D(W_{-g})` is its adjoint up to the fixed Weyl phase.

Thus every sign class carries a real fiber of dimension

\[
\boxed{2p^2.}
\tag{2.3}
\]

In the normalized superoperator Hilbert norm,

\[
\boxed{
\|D\|_{\mathrm{sop}}^2
=\frac{2}{p^2}\sum_{[g]\in\Omega_p}\|X_{[g]}\|_{2,p}^2.
}
\tag{2.4}
\]

---

## 3. The quadratic-phase orbit cycles

Fix a nonzero first coordinate `a`. Since `p` is prime, multiplication by `a` permutes `F_p`. Therefore

\[
(a,0),
(a,a),
(a,2a),
\ldots,
(a,(p-1)a)
\]

is the complete `S^{-1}`-orbit at first coordinate `a`.

Modulo the sign relation, choose representatives

\[
\boxed{
A_p=\{1,2,\ldots,(p-1)/2\}\subset\mathbb F_p^*.
}
\tag{3.1}
\]

For every `a in A_p`, the `p` sign classes

\[
[(a,ka)],
\qquad k=0,1,\ldots,p-1,
\]

form one `p`-cycle under the quadratic shear.

These cycles are pairwise disjoint and exhaust every sign class with first coordinate nonzero.

The remaining

\[
\frac{p-1}{2}
\]

sign classes are exactly the vertical-axis classes `[(0,b)]`.

---

## 4. Forest face family

For every

\[
a\in A_p,
\qquad
k=1,\ldots,p-1,
\]

put

\[
\boxed{
g_{a,k}=(a,ka).}
\tag{4.1}
\]

Use the engineered Coxeter square whose first two contextual transports are

\[
\boxed{(P,W_{g_{a,k}}).}
\tag{4.2}
\]

The fourth contextual transport is, up to a scalar phase,

\[
P^*W_{g_{a,k}}^*P
\sim W_{-Sg_{a,k}}
=W_{(-a,-(k-1)a)}.
\]

Thus, at sign-class level, this face joins

\[
[(a,ka)]
\quad\text{to}\quad
[(a,(k-1)a)].
\tag{4.3}
\]

For fixed `a`, the selected `p-1` faces therefore form a path through all `p` vertices of the shear cycle, with root `[(a,0)]`.

Across all `a in A_p`, we obtain a forest of

\[
\frac{p-1}{2}
\]

disjoint paths.

The number of faces is

\[
\boxed{
K_p
=\frac{p-1}{2}(p-1)
=\frac{(p-1)^2}{2}.
}
\tag{4.4}

---

## 5. Exact two-endpoint submatrix

Let `K_D(P,W_g)` be the first-order coefficient of one engineered square.

With contextual transports

\[
T_1=P,
\quad
T_2=W_g,
\quad
T_3=P^*,
\quad
T_4=P^*W_g^*P,
\]

the square coefficient contains four terms. If we restrict the domain to the two Weyl evaluation fibers at the endpoint sign classes `[g]` and `[Sg]`, then

\[
D(P)=D(P^*)=0
\]

because the Weyl support of `P` and `P^*` is contained in the vertical line `L_Z`, while every selected endpoint has first coordinate `a!=0`.

Hence the restricted face map is exactly

\[
\boxed{
K_D(P,W_g)
=
P^*W_g^*D(W_g)P
+
D(P^*W_g^*P)\,PW_gP^*.
}
\tag{5.1}
\]

Each summand is obtained from the corresponding endpoint matrix by left/right multiplication by unitaries, together, on the second endpoint if necessary, with the real orthogonal adjoint operation coming from the sign-class convention.

Therefore the two endpoint coefficient maps are real isometries of the `2p^2`-dimensional fiber.

---

## 6. Private-child block triangularity

Order the faces for each fixed `a` by increasing `k=1,...,p-1`.

Select from the domain only the child fibers

\[
[(a,a)],
[(a,2a)],
\ldots,
[(a,(p-1)a)],
\]

and omit the root fiber `[(a,0)]`.

Because all selected child labels have first coordinate nonzero, no quadratic-anchor term `D(P)` or `D(P^*)` uses any of these selected columns.

Relative to these selected child columns, the path block is lower bidiagonal:

\[
\mathcal L_a
=\begin{pmatrix}
U_1&0&0&\cdots&0\\
V_2&U_2&0&\cdots&0\\
0&V_3&U_3&\ddots&\vdots\\
\vdots&\ddots&\ddots&\ddots&0\\
0&\cdots&0&V_{p-1}&U_{p-1}
\end{pmatrix},
\tag{6.1}
\]

where every `U_k,V_k` is an orthogonal transformation of the real fiber.

By orthogonal row and column gauges along the path, `L_a` is unitarily equivalent to

\[
\boxed{
L_{p-1}\otimes I_{2p^2},
}
\tag{6.2}
\]

where

\[
L_n=
\begin{pmatrix}
1&0&\cdots&0\\
-1&1&\ddots&\vdots\\
0&-1&\ddots&0\\
\vdots&\ddots&\ddots&1
\end{pmatrix}.
\]

In particular every face contributes its full real rank `2p^2`.

---

## 7. Polynomial singular gap

The inverse of `L_n` is the cumulative-sum matrix. Hence

\[
\|L_n^{-1}\|\le n,
\]

so

\[
\boxed{
\sigma_{\min}(L_{p-1})\ge\frac1{p-1}.
}
\tag{7.1}
\]

The selected sign-class fiber coordinates have the normalization (2.4). Passing from the raw endpoint matrix variable to an orthonormal superoperator coordinate multiplies the face coefficient by

\[
\sqrt{\frac{p^2}{2}}=\frac p{\sqrt2}.
\]

Therefore the stacked, unaveraged forest analysis operator has

\[
\sigma_{\min}^{+}
\ge
\frac{p}{\sqrt2(p-1)}.
\tag{7.2}
\]

The full forest matrix contains additional columns, so its row Gram matrix dominates that of the selected child-column submatrix. Thus the same lower bound applies to its smallest positive singular value.

Normalize now by equal-face averaging:

\[
\|\mathcal M_{\mathrm{forest}}D\|^2
=\frac1{K_p}\sum_f\|K_f(D)\|_{2,p}^2.
\]

Since

\[
\sqrt{K_p}=\frac{p-1}{\sqrt2},
\]

we obtain

\[
\boxed{
\sigma_{\min}^{+}
\ge
\frac{p}{(p-1)^2}
\ge
\frac1p.
}
\tag{7.3}
\]

Consequently the forest lower frame bound obeys

\[
\boxed{
A_p^{\mathrm{forest}}\ge p^{-2}.
}
\tag{7.4}

No exponent optimization is needed here; the bound is already sharp enough for the Article-III programme.

---

## 8. Exact core rank

Every one of the `K_p` faces contributes full real rank `2p^2`. Therefore

\[
\boxed{
R_p^{\mathrm{forest}}
=2p^2K_p
=p^2(p-1)^2.
}
\tag{8.1}

Hamiltonian derivations lie in the kernel of every Coxeter-loop first-order measurement, so passing to the quotient does not change this nonzero rank.

The dissipative quotient dimension is

\[
N_p=(p^2-1)^2.
\]

Thus the residual quotient dimension is exactly

\[
\boxed{
N_p-R_p^{\mathrm{forest}}
=(p-1)^2(2p+1)
=2p^3-3p^2+1.
}
\tag{8.2}

---

## 9. Exact remaining face count and slack

The sharp face count is

\[
L_p^\sharp=\frac{p^2-1}{2}.
\]

Subtracting the forest count gives

\[
\boxed{
L_p^\sharp-K_p=p-1.
}
\tag{9.1}

Those `p-1` remaining matrix-valued faces have total real scalar capacity

\[
2p^2(p-1).
\]

Against the residual quotient dimension (8.2), their exact slack is

\[
\boxed{
2p^2(p-1)-(2p^3-3p^2+1)
=p^2-1.
}
\tag{9.2}

That is precisely the odd sharp rank slack.

So the full sharp problem has been reduced to the exact finite-dimensional statement:

\[
\boxed{
\text{close a residual space of dimension }2p^3-3p^2+1
\text{ with }p-1\text{ faces and only }p^2-1\text{ total overlap}.
}
\]

---

## 10. Agreement with the finite census

The deterministic count agrees exactly with the previously observed Fourier/quadratic-phase sharp census:

- `p=3`: `K_p=2` phase faces, followed by `p-1=2` dense faces;
- `p=5`: `K_p=8` phase faces, followed by `p-1=4` dense faces.

For `p=5`, the first eight phase faces indeed account for rank

\[
8\times50=400,
\]

which is exactly (8.1).

The numerical census is evidence only for the completion step; the forest theorem itself is proved above and does not depend on numerics.

---

## 11. New active problem: the Fourier completion theorem

The block-compatible core obstruction is now closed for odd primes.

The strict next target is no longer a generic grouped restricted-invertibility statement. It is the much more structured theorem:

### Fourier completion target

Find explicit labels

\[
h_1,\ldots,h_{p-1}\in\mathbb F_p^2\setminus\{0\}
\]

such that the `p-1` engineered squares

\[
(F_p,W_{h_j})
\]

complete the quadratic-phase forest to full quotient rank, with a polynomial Schur gap on the residual space (8.2).

The finite `p=3,5` census shows this target is plausible and already sharp in count.

A particularly strong form would prove that the first `p-2` Fourier faces add their full `2p^2` rank and the last Fourier face contributes exactly

\[
\boxed{p^2+1}
\]

new directions, because

\[
(2p^3-3p^2+1)-2p^2(p-2)=p^2+1.
\]

Then the entire odd-prime sharp design would have the extremal overlap pattern

\[
\boxed{
\text{all faces transverse except the last, whose overlap is exactly }p^2-1.
}
\]

This is exactly what occurs in the `p=3,5` census.

---

## 12. Claim firewall

This note proves:

- an explicit block-compatible quadratic-phase forest for every odd prime dimension;
- exact full `2p^2` rank contribution from every forest face;
- exact core rank `p^2(p-1)^2`;
- an equal-face lower singular gap at least `1/p`;
- reduction of the remaining sharp problem to exactly `p-1` dense faces.

It does **not** yet prove:

- the all-prime Fourier completion theorem;
- sharp polynomial robustness for the completed design;
- the same forest count for arbitrary odd composite dimensions;
- the even-dimensional analogue;
- optimality of the particular quadratic-phase forest among all sharp cores.
