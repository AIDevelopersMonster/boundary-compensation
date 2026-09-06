# Article III — Explicit Unitary Five-Defect Carrier with an Inverse-Polynomial Gap

**Author:** Malachevsky, A.A. / Малачевский А.А.  
**ORCID:** 0009-0008-6009-3196  
**Date:** 2026-09-06  
**Status:** `PROVED / EXPLICIT UNITARY CARRIER / INVERSE-POLYNOMIAL LOCAL GAP / NO ZARISKI RETURN FOR CARRIER`

## 0. Purpose

The repaired odd-to-even transfer in

`article-I/research/ODD-TO-EVEN-TRANSFER-AUDIT-REPAIR-v0.1.md`

uses one carrier face to do two jobs simultaneously:

1. reduce the relative variable `R` to the two-dimensional tail gauge;
2. recover the five old restriction defects missed by the doubly embedded odd extension-ready design: one regular class and four copies of one scalar class.

The old proof constructs this carrier in `SL_n(C)` and returns to the unitary locus by Zariski density. That is sufficient for rank, but gives no quantitative lower bound.

This note replaces the carrier by a direct family in `SU(n)` and proves an inverse-polynomial singular gap in natural normalized Hilbert-Schmidt coordinates. Thus the **carrier itself is not a superpolynomial obstruction**.

The theorem is local to one odd-to-even transfer stage. It does not yet quantify the later two-tail `epsilon/t` binding family.

Throughout

\[
d\ge3\quad\text{is odd},\qquad n=d+1,\qquad N=d+2.
\]

---

## 1. Carrier domain and norms

The carrier acts on

\[
\mathcal E_5\oplus M_N(\mathbb C)_R,
\]

where `E_5` is the five-dimensional old-defect complement and `R` is the relative matrix variable from the repaired transfer.

Choose an orthonormal defect basis consisting of

- one regular class `[F]`, normalized in the quotient superoperator norm modulo inner derivations;
- four orthogonal output copies of one scalar functional `phi`, normalized in the dual normalized Hilbert-Schmidt norm.

The four scalar copies occupy the tail output matrix units

\[
E_{nn},\ E_{nN},\ E_{Nn},\ E_{NN}.
\]

For matrices use

\[
\|X\|_{2,m}^2=\frac1m\operatorname{Tr}(X^*X).
\]

All constants below are absolute and are not optimized.

---

## 2. A scalar-phase unitary anchor

Put

\[
w=e^{i\pi/4},
\qquad
c=c_d=e^{i\pi/[4(d+1)]}.
\tag{2.1}
\]

Then

\[
c^{d+1}=w.
\]

Define the tail phase

\[
s=c^{-d}=cw^{-1}.
\tag{2.2}
\]

For any `U,V in SU(d)` set

\[
C=cU,
\qquad
D=cV,
\tag{2.3}
\]

and

\[
A=\operatorname{diag}(C,s),
\qquad
B=\operatorname{diag}(D,s).
\tag{2.4}
\]

Because

\[
\det C=c^d,
\qquad
s=c^{-d},
\]

we have

\[
\boxed{A,B\in SU(n).}
\tag{2.5}
\]

Their scalar-one embeddings in `M_N` are

\[
\widetilde A=\operatorname{diag}(C,s,1),
\qquad
\widetilde B=\operatorname{diag}(D,s,1).
\]

The carrier uses the paired branches

\[
(A,B),
\qquad
(B^{-1},A^{-1}).
\]

---

## 3. The unperturbed `R` carrier already has a polynomial gap

First set

\[
U=V=I_d.
\]

Thus the old-block eigenvalue is `c`, the internal tail eigenvalue is `s`, and the external scalar-one eigenvalue is `1`.

For the forward branch the pure-`R` operator is

\[
T_+(R)
=(s^2-1)R-(s-1)R\widetilde B-(s-1)\widetilde A R.
\tag{3.1}
\]

On a matrix unit whose row eigenvalue is `a` and column eigenvalue is `b`, its scalar coefficient is

\[
\eta_+(a,b)
=(s-1)(s+1-a-b).
\tag{3.2}
\]

There are three eigenvalue types: `c`, `s`, and `1`. Hence the coefficients are

\[
\begin{array}{c|ccc}
 & c&s&1\\ \hline
c&(s-1)(s+1-2c)&(s-1)(1-c)&(s-1)(s-c)\\
s&(s-1)(1-c)&-(s-1)^2&0\\
1&(s-1)(s-c)&0&(s-1)^2.
\end{array}
\tag{3.3}
\]

The two zeros are exactly

\[
E_{nN},\qquad E_{Nn},
\]

the desired relative Hamiltonian gauge directions.

### Lemma 3.1 — explicit forward `R` gap

There is an absolute `c_R>0` such that

\[
\boxed{
\sigma_{\min}^{+}(T_+|_R)
\ge
\frac{c_R}{d+1}.
}
\tag{3.4}
\]

#### Proof

Because `d>=3`,

\[
0<\arg c\le\frac\pi{16},
\]

while

\[
\arg s=\arg c-\frac\pi4.
\]

Therefore `|s-1|` is bounded below by an absolute constant. Also

\[
|1-c|
=2\sin\frac{\pi}{8(d+1)}
\ge\frac1{2(d+1)}.
\]

Further,

\[
|s-c|=|w^{-1}-1|
\]

is constant. Finally

\[
|s+1-2c|
=|1-c(2-w^{-1})|
\ge
\bigl||2-w^{-1}|-1\bigr|>0.
\]

Thus every nonzero entry of (3.3) is at least `c_R/(d+1)` in modulus. Since the operator is diagonal in the matrix-unit basis, (3.4) follows. `square`

---

## 4. Stability of the `R` gap under small unitary perturbations

Let

\[
U_\delta=e^{i\delta H},
\qquad
V_\delta=e^{i\delta K},
\tag{4.1}
\]

with traceless Hermitian `H,K` of uniformly bounded operator norm.

The tail phase `s` remains **exactly fixed** because `U_delta,V_delta in SU(d)`.

The forward `R` operator changes only through left multiplication by `C=cU_delta` and right multiplication by `D=cV_delta`. Hence

\[
\|T_+(\delta)-T_+(0)\|
\le C|\delta|.
\tag{4.2}
\]

Consequently, for

\[
|\delta|\le c_1d^{-1},
\]

one still has

\[
\boxed{
\sigma_{\min}^{+}(T_+(\delta)|_R)
\ge
\frac{c_R}{2(d+1)}.
}
\tag{4.3}
\]

The kernel remains exactly

\[
\operatorname{span}\{E_{nN},E_{Nn}\},
\]

because these two matrix units are annihilated identically for every old-block choice `U_delta,V_delta`.

---

## 5. The old-old mismatch phase

At the scalar anchor `U=V=I`, the forward old-old `R` coefficient is

\[
\eta_+
=(s-1)(s+1-2c),
\tag{5.1}
\]

and the inverse-branch coefficient is

\[
\eta_-
=(s^{-1}-1)(s^{-1}+1-2c^{-1}).
\tag{5.2}
\]

Set

\[
r=\eta_-/\eta_+,
\qquad
\rho=rc^4.
\tag{5.3}
\]

A direct simplification using `s=cw^{-1}` gives

\[
\boxed{
\rho
=c^2w^2\frac{c+w-2}{2cw-c-w}.
}
\tag{5.4}
\]

Since `w^2=i`,

\[
\boxed{
\frac\rho i-1
=
\frac{(c-1)^2(c+w)}{2cw-c-w}.
}
\tag{5.5}
\]

Moreover

\[
|2cw-c-w|
=|c(2w-1)-w|
\ge
\sqrt{5-2\sqrt2}-1.
\tag{5.6}
\]

For `d>=3`, `|c-1|<=2 sin(pi/32)`, so (5.5) gives

\[
|\rho-i|<\frac16.
\tag{5.7}
\]

Because the carrier is unitary, `|rho|=1`. Therefore

\[
\boxed{
|1-\rho^2|>\frac53.
}
\tag{5.8}
\]

This fixed separation from `rho=+/-1` is the key regular-sector transversality constant.

---

## 6. Quantitative defect-detection lemma

For a regular cochain `F` define

\[
B_F(X,Y)
=F(XY)-F(X)Y-XF(Y).
\tag{6.1}
\]

Let `{W_a}_{a=1}^{d^2}` be a unitary error basis orthonormal for the normalized Hilbert-Schmidt product.

The separability idempotent identity

\[
\frac1{d^2}\sum_aW_a\otimes W_a^*
\]

gives the following contraction.

### Lemma 6.1 — defect controls distance from derivations

Define

\[
T_F=\frac1{d^2}\sum_aW_aF(W_a^*).
\]

Then for every `X`,

\[
\boxed{
F(X)-[X,T_F]
=-\frac1{d^2}\sum_aW_aB_F(W_a^*,X).
}
\tag{6.2}
\]

Consequently, if the quotient norm of `[F]` modulo inner derivations is one, then

\[
\boxed{
\frac1{d^4}\sum_{a,b}
\|B_F(W_a^*,W_b)\|_2^2
\ge1.
}
\tag{6.3}
\]

#### Proof

Let `e=sum x_a tensor y_a` denote the separability idempotent with

\[
\sum_ax_ay_a=I,
\qquad
Xe=eX.
\]

Then

\[
\sum_ax_aB_F(y_a,X)
=
XT_F-T_FX-F(X).
\]

This is (6.2). Taking the normalized superoperator norm and using Cauchy-Schwarz gives (6.3). `square`

Now define the paired mismatch bilinear form

\[
Q_{\rho,F}(X,Y)
=B_F(Y,X)-\rho B_F(X,Y).
\tag{6.4}
\]

The identity

\[
\boxed{
(1-\rho^2)B_F(X,Y)
=Q_{\rho,F}(Y,X)+\rho Q_{\rho,F}(X,Y)
}
\tag{6.5}
\]

and (5.8) imply that `Q_{rho,F}` quantitatively detects every non-derivation class.

If `F(I)` is smaller than a sufficiently small absolute constant, (6.3) allows the detecting Weyl pair to be chosen nonidentity; its Hermitian and anti-Hermitian parts are traceless. Splitting the pair into Hermitian parts therefore gives traceless Hermitian `H,K` with

\[
\|H\|_{op},\|K\|_{op}\le1
\]

and

\[
\boxed{
\|Q_{\rho,F}(H,K)\|_2\ge c_Q
}
\tag{6.6}
\]

for an absolute `c_Q>0`.

If `F(I)` is not small, the scalar anchor itself already detects the regular class; this is quantified next.

---

## 7. Regular old-defect survival on the unitary family

Let

\[
a=c-1.
\]

At `delta=0`,

\[
B_F(aI,aI)=-a^2F(I).
\]

After eliminating the old-old `R` image with the branch ratio `r`, the regular residual is

\[
\boxed{
G_F(0)
=a^2(r-c^{-2})F(I).
}
\tag{7.1}
\]

Since `r=rho c^{-4}`, (5.7) gives an absolute lower bound

\[
|r-c^{-2}|
=|c^{-4}(\rho-c^2)|
\ge c_2>0.
\tag{7.2}
\]

Hence

\[
\boxed{
\|G_F(0)\|_2
\ge
c_3d^{-2}\|F(I)\|_2.
}
\tag{7.3}
\]

When `F(I)` is small, choose the traceless Hermitian `H,K` from Lemma 6.1 and use

\[
C=c e^{i\delta H},
\qquad
D=c e^{i\delta K}.
\tag{7.4}
\]

The mixed second-order coefficient of the regular branch mismatch is

\[
\boxed{
-\delta^2c^{-2}Q_{\rho,F}(H,K).
}
\tag{7.5}
\]

Terms coming from `F(I)` are uniformly small in the small-`F(I)` case. If needed, use the four sign choices

\[
(H,K),\ (H,-K),\ (-H,K),\ (-H,-K).
\]

Their alternating mixed difference cancels the constant and one-variable terms and isolates (7.5), up to higher order. Therefore one of the four sign choices satisfies

\[
\boxed{
\|G_F(\delta)\|_2
\ge c_4\delta^2
}
\tag{7.6}
\]

provided `delta` is sufficiently small by an inverse polynomial in `d`.

Thus the regular carrier column is quantitatively visible in both cases:

- large `F(I)`: already at order `d^{-2}`;
- small `F(I)`: at order `delta^2` through the paired bilinear mismatch.

---

## 8. Scalar detector direction

Let `phi` be the normalized scalar functional and put

\[
h=\phi(I).
\]

If `|h|` is bounded below by an absolute constant, the scalar anchor already separates all four scalar copies.

If `|h|` is small, the traceless component of `phi` has norm bounded below. By the Riesz representation theorem and the Hermitian/anti-Hermitian decomposition, there exists a traceless Hermitian `L` such that

\[
\|L\|_{op}\le1
\]

and

\[
\boxed{
|\phi(L)|\ge c_5d^{-1/2}.
}
\tag{8.1}
\]

Starting from the regular detector `H,K`, replace

\[
K\mapsto K+\eta_d tL,
\qquad |t|\le1,
\tag{8.2}
\]

where

\[
\boxed{
\eta_d=c_\eta d^{-2}
}
\tag{8.3}
\]

and `c_eta>0` is a sufficiently small absolute constant.

The perturbation of the regular mismatch (6.6) is at most `C d eta_d`, so the regular lower bound survives.

---

## 9. Exact scalar anchor and first-order slopes

The two gauge matrix units `E_(nN),E_(Nn)` remain outside the `R` image for every `U,V`.

For the two diagonal tail units, the `R` branch ratio is independent of `U,V` and equals

\[
\boxed{
s^{-2}=w^2c^{-2}=ic^{-2}.}
\tag{9.1}

### 9.1 Scalar anchor values

At `delta=0`, direct substitution gives

\[
S_{nN}^{(0)}=S_{Nn}^{(0)}
=(c-1)(c-s)h,
\tag{9.2}
\]

\[
S_{NN}^{(0)}
=(c-1)^2c^{-2}(1-w^2)h,
\tag{9.3}
\]

and, after eliminating the `R_(nn)` image,

\[
\boxed{
S_{nn}^{(0)}
=-(c-1)(c+1)(w-1)^2c^{-2}h.
}
\tag{9.4}
\]

Thus if `|h|` is bounded below, the smallest of the four scalar gaps is already

\[
\boxed{
\ge c_6d^{-2}|h|.
}
\tag{9.5}
\]

### 9.2 Slopes in the scalar detector

Now let

\[
C=c e^{i\delta H},
\qquad
D=c e^{i\delta K}.
\]

Write

\[
p=\phi(H),\qquad q=\phi(K).
\]

Differentiating at `delta=0`, the coefficient of `q` in the four scalar residuals is, respectively,

\[
\begin{array}{c|c}
\text{copy}&\partial_q\partial_\delta S|_{0}\\ \hline
nN&i c(c-s)\\[1mm]
Nn&i c(c-1)\\[1mm]
NN&(c-1)c^{-2}(i+c)\\[1mm]
nn&-i(w-1)(c^2w-1)c^{-2}.
\end{array}
\tag{9.6}
\]

Every entry in the right column is nonzero, and the smallest modulus is bounded below by

\[
\boxed{
\frac{c_7}{d+1}.
}
\tag{9.7}
\]

Therefore varying `t` in (8.2) changes every scalar residual with slope at least

\[
\boxed{
 c_8 d^{-7/2}
}
\tag{9.8}
\]

before multiplication by `delta`.

---

## 10. Simultaneous scalar avoidance

For fixed regular-sign choice, the leading scalar residuals are four affine functions of the real parameter `t`.

For one affine complex function `a+bt`, the subset of `[-1,1]` on which

\[
|a+bt|<\varepsilon
\]

has length at most `2 epsilon/|b|`.

Using four functions and the common slope lower bound (9.8), choose

\[
\varepsilon=\frac1{32}c_8d^{-7/2}.
\]

The four bad sets cannot cover `[-1,1]`. Hence there exists

\[
\boxed{t_*=t_*(F,\phi,d)\in[-1,1]}
\tag{10.1}
\]

such that all four leading scalar residuals have modulus at least

\[
 c_9d^{-7/2}.
\]

After restoring the perturbation parameter `delta`,

\[
\boxed{
\min_{\text{four scalar copies}}|S_{scalar}|
\ge
c_{10}|\delta|d^{-7/2}
}
\tag{10.2}
\]

up to the quadratic analytic remainder.

---

## 11. A polynomial finite parameter

Take

\[
\boxed{
\delta_d=c_\delta d^{-12}
}
\tag{11.1}
\]

with a sufficiently small absolute `c_delta>0`.

The carrier entries are analytic functions of `delta`. On the `R` complement, (4.3) gives

\[
\|T_+^{-1}\|=O(d).
\]

Differentiating the inverse and the Schur elimination shows, with deliberately crude estimates,

\[
\|\partial_\delta^r(T_+^{-1})\|=O(d^{r+1}),
\qquad r\le4.
\tag{11.2}
\]

A quotient-normalized regular representative has superoperator operator norm at most `O(d)`, while the scalar functional has norm one. Hence the third and fourth derivatives of the five-defect Schur columns are bounded by `O(d^6)`.

Therefore:

- the regular cubic remainder is `O(d^6 delta^3)`;
- the scalar quadratic remainder is `O(d^6 delta^2)`.

For `delta=delta_d`, these are smaller than the leading bounds (7.6) and (10.2). Consequently

\[
\boxed{
\|G_F(\delta_d)\|_2
\ge c_{11}d^{-24},
}
\tag{11.3}
\]

and

\[
\boxed{
\min_{\text{four scalar copies}}
|S_{scalar}(\delta_d)|
\ge c_{12}d^{-16}.
}
\tag{11.4}
\]

The exponent `16` is a convenient integer weakening of `12+7/2`.

Thus the regular column is the smaller five-defect scale.

---

## 12. Five-defect Schur gap

Compress the post-`R` output to:

- one normalized old-old functional detecting the regular residual;
- the four tail matrix units carrying the scalar copies.

These five output sectors are mutually orthogonal. Therefore the five-defect Schur block obeys

\[
\boxed{
\sigma_{\min}(S_{E_5})
\ge c_{13}d^{-24}.
}
\tag{12.1}

This is already the desired inverse-polynomial carrier transversality after the `R` bulk has been eliminated.

---

## 13. Full carrier gap

Write the carrier matrix, after splitting off the two exact gauge directions of `R`, in block form

\[
\mathcal C_d
=
\begin{pmatrix}
T_+&H_+\\
T_-&H_-
\end{pmatrix}.
\tag{13.1}
\]

The forward `R` block satisfies

\[
\sigma_{\min}(T_+)\ge c d^{-1},
\qquad
\|T_+^{-1}\|=O(d).
\]

The five-defect forward block has norm `O(d)` in normalized coordinates. Standard row and column Schur elimination therefore uses triangular factors of norms at most `O(d)` and `O(d^2)`.

Combining with (12.1) yields the deliberately weakened bound

\[
\boxed{
\sigma_{\min}^{+}(\mathcal C_d)
\ge c_{14}d^{-28}.
}
\tag{13.2}
\]

The only kernel is

\[
\boxed{
\operatorname{span}\{E_{nN},E_{Nn}\}.
}
\tag{13.3}
\]

Since `||C_d||=O(d)` in the same coordinates, one may record the crude condition estimate

\[
\boxed{
\kappa(\mathcal C_d|_{G^\perp})
=O(d^{30}).
}
\tag{13.4}
\]

No exponent in this note is claimed optimal.

---

## 14. Direct unitary five-defect carrier theorem

### Theorem 14.1

For every odd `d>=3`, let the doubly embedded old design leave the five-dimensional defect complement described in the repaired odd-to-even transfer. Normalize that complement as in Section 1.

Then there exist explicit carrier transports of the form

\[
\boxed{
A_d
=
\operatorname{diag}
\left(
 c_d e^{i\delta_d H_d},
 c_d^{-d}
\right),
}
\tag{14.1}
\]

\[
\boxed{
B_d
=
\operatorname{diag}
\left(
 c_d e^{i\delta_d(K_d+\eta_dt_dL_d)},
 c_d^{-d}
\right),
}
\tag{14.2}
\]

with

\[
c_d=e^{i\pi/[4(d+1)]},
\qquad
\delta_d=c_\delta d^{-12},
\qquad
\eta_d=c_\eta d^{-2},
\]

where `H_d,K_d,L_d` are traceless Hermitian, uniformly bounded in operator norm, and `t_d in [-1,1]`, such that

\[
A_d,B_d\in SU(d+1),
\]

and the paired carrier measurement has kernel exactly the two relative tail-gauge directions.

Moreover, in normalized Hilbert coordinates,

\[
\boxed{
\sigma_{\min}^{+}(\mathcal C_d)
\ge c d^{-28}.
}
\tag{14.3}

Hence the five-defect carrier admits an **inverse-polynomial direct unitary realization**. No Zariski-density return from `SL_n(C)` is needed for the carrier stage.

By the engineered-square realization theorem, the ordered unitary pair `(A_d,B_d)` is realized by a genuine unitary Coxeter square.

---

## 15. What this closes

The odd-to-even transfer no longer has a qualitative unitary gap at its carrier:

\[
\boxed{
\text{five-defect carrier}
:\quad
\text{SL/Zariski existence}
\longrightarrow
\text{direct unitary inverse-polynomial witness}.
}
\]

The following possible sources of a superpolynomial wall have now been excluded locally:

- carrier `R`-bulk removal;
- recovery of the one missing regular class;
- recovery of all four scalar copies;
- unitary realization of the carrier.

---

## 16. Remaining odd-to-even wall

The carrier is not the whole odd-to-even transfer. After it, the repaired proof still uses:

1. the two-tail local reduction;
2. the first diagonal binding scale `epsilon` imposing `beta_j=r`, `delta_j=s`;
3. the second cross-plane graph scale `t`;
4. simultaneous two-scale remainder control.

The next strict target is therefore

\[
\boxed{
\text{explicit unitary two-tail }\varepsilon\text{-binding with an inverse-polynomial gap.}
}
\]

If that layer and the subsequent unitary graph layer also admit polynomial finite-parameter control, the entire **single odd-to-even transfer stage** will become quantitatively polynomial.

---

## 17. Claim firewall

This note proves an inverse-polynomial gap for the isolated five-defect carrier stage under the natural normalized five-defect complement. It does not yet prove:

- a polynomial gap for the full odd-to-even transfer;
- an all-dimensional polynomial condition-number theorem for recursively assembled sharp designs;
- optimal exponents;
- necessity or non-necessity of oversampling;
- sample-complexity or experimental-noise bounds.
