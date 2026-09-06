# Article III — Polynomially Separated Multiplicative-Sidon Phases

**Author:** Malachevsky, A.A. / Малачевский А.А.  
**ORCID:** 0009-0008-6009-3196  
**Date:** 2026-09-06  
**Status:** `PROVED / POLYNOMIAL DIAGONAL-SEPARATION LAYER / UNITARY DIAGONAL WITNESS`

## 0. Purpose

`ARTICLE-III-BINDING-GRAPH-SPECTRAL-GAP-v0.1.md` proves that the bare graph-binding matrix in the sharp even-to-odd extension has condition number \(O(d)\). The next possible source of instability is the multiplicative-Sidon diagonal \(\Lambda\): the local inverse and the graph edge weights contain denominators such as

\[
\lambda_k-\lambda_n,
\qquad
\lambda_j\lambda_n-\lambda_r\lambda_s.
\]

The original Article-II proof requires these quantities only to be nonzero. This note strengthens that qualitative choice: the diagonal parameters can be chosen **on the unit circle** with inverse-polynomial separation.

This removes another potential superpolynomial source from the complex extension witness. It does not yet quantitatively replace the final Zariski-density return of the other transports by an explicit unitary construction.

---

## 1. An elementary polynomial Sidon set

Fix \(n\ge4\) and put

\[
M=2n+1.
\]

For

\[
j=0,1,\ldots,n-1
\]

define

\[
\boxed{
e_j=j+Mj^2.
}
\tag{1.1}
\]

### Lemma 1.1 — pair-sum uniqueness

If

\[
e_i+e_j=e_k+e_\ell,
\]

then

\[
\{i,j\}=\{k,\ell\}
\]

as unordered pairs.

#### Proof

The equality gives

\[
(i+j-k-\ell)
+M(i^2+j^2-k^2-\ell^2)=0.
\]

The first bracket has absolute value at most \(2n-2<M\). Hence the second integer bracket must vanish; otherwise its contribution has magnitude at least \(M\), too large to be cancelled by the first bracket. Therefore

\[
i^2+j^2=k^2+\ell^2.
\]

The first bracket then also vanishes, so

\[
i+j=k+\ell.
\]

The sum and sum of squares determine the unordered pair, because they determine the product via

\[
2ij=(i+j)^2-(i^2+j^2).
\]

Thus the pairs agree. \(\square\)

The largest exponent satisfies

\[
0\le e_j<3n^3.
\tag{1.2}
\]

---

## 2. Unit-circle multiplicative-Sidon parameters

Choose

\[
\boxed{
\varepsilon_n=\frac1{12n^3}
}
\tag{2.1}
\]

and define

\[
\boxed{
\lambda_j=\exp(i\varepsilon_n e_j),
\qquad j=0,\ldots,n-1.
}
\tag{2.2}
\]

Then every \(\lambda_j\) has unit modulus. By (1.2), all phases lie in an interval of length less than \(1/4\), so no modular wraparound is possible in any one- or two-exponent comparison used below.

### Theorem 2.1 — quantitative multiplicative Sidon property

The parameters \(\lambda_j\) are pairwise distinct and satisfy

\[
\lambda_i\lambda_j=\lambda_k\lambda_\ell
\iff
\{i,j\}=\{k,\ell\}.
\tag{2.3}
\]

Moreover, for unequal indices,

\[
\boxed{
|\lambda_i-\lambda_j|
\ge
\frac{1}{6\pi n^3}.
}
\tag{2.4}
\]

For unequal unordered pairs,

\[
\boxed{
|\lambda_i\lambda_j-\lambda_k\lambda_\ell|
\ge
\frac{1}{6\pi n^3}.
}
\tag{2.5}
\]

#### Proof

If two phases or two pair-products agree, their exponent difference is an integer multiple of \(2\pi/\varepsilon_n\). But every relevant exponent difference has absolute phase less than \(1/2\), so the only possible multiple is zero. Pair equality then follows from Lemma 1.1.

For a nonzero integer exponent difference \(m\), \(|m|\ge1\). Since the phase difference obeys \(|\varepsilon_n m|<1/2\),

\[
|e^{i\varepsilon_n m}-1|
=2|\sin(\varepsilon_n m/2)|
\ge\frac{2}{\pi}|\varepsilon_n m|
\ge\frac{1}{6\pi n^3}.
\]

The same argument applies to pair-sum differences. \(\square\)

---

## 3. Local-kernel determinants are inverse-polynomially separated

The local elimination in `GLOBAL-BINDING-LEMMA-v0.1.md` uses the determinant

\[
\Delta_{j;r,s}
=
-\frac{(\lambda_j-\lambda_n)
(\lambda_j\lambda_n-\lambda_r\lambda_s)}
{\lambda_j\lambda_n\lambda_r}.
\tag{3.1}
\]

At every nonexceptional entry both numerator factors are nonzero by the Sidon property. Since all \(\lambda\)'s have unit modulus, Theorem 2.1 gives

\[
\boxed{
|\Delta_{j;r,s}|
\ge
\frac1{36\pi^2 n^6}.
}
\tag{3.2}
\]

All entries of the corresponding \(2\times2\) local systems are bounded by \(2\). Hence their inverses have operator norm bounded by a fixed polynomial in \(n\); for example, the adjugate formula gives the crude uniform estimate

\[
\boxed{
\|A_{j;r,s}^{-1}\|_2
\le C n^6
}
\tag{3.3}
\]

for an absolute constant \(C\).

Thus the local bulk inversion required to form the second-order Schur map need not be exponentially ill-conditioned because of the diagonal spectrum.

---

## 4. Polynomial window for the graph-binding weights

The second-order edge coefficients in the global binding lemma are, up to signs,

\[
w_{jk}^{(1)}
=
\frac{\lambda_k(\lambda_j-\lambda_n)}
{\lambda_j(\lambda_k-\lambda_n)},
\qquad
w_{jk}^{(2)}
=
\frac{\lambda_j-\lambda_n}
{\lambda_k-\lambda_n}.
\tag{4.1}
\]

Because \(|\lambda_j|=1\), the two weights have the same modulus. Every numerator difference is at most \(2\), while every denominator difference is at least \((6\pi n^3)^{-1}\). Interchanging \(j\) and \(k\) gives the reciprocal bound. Therefore

\[
\boxed{
\frac1{12\pi n^3}
\le
|w_{jk}^{(a)}|
\le
12\pi n^3,
\qquad a=1,2.
}
\tag{4.2}
\]

So the diagonal row-scaling matrix \(W\) that turns the unweighted binding incidence matrix \(B_d\) into the actual weighted graph layer obeys

\[
\kappa(W)\le(12\pi)^2n^6.
\tag{4.3}
\]

Combining with

\[
\kappa(B_d)<\sqrt2\,d
\]

from `ARTICLE-III-BINDING-GRAPH-SPECTRAL-GAP-v0.1.md` gives the crude polynomial estimate

\[
\boxed{
\kappa(WB_d)=O(d^7)
}
\tag{4.4}
\]

on the gauge-orthogonal binding sector, with \(n=d+1\).

The exponent \(7\) is not claimed optimal; the important point is polynomiality.

---

## 5. What is now ruled out

For the even-to-odd sharp extension witness, two previously qualitative layers can be made quantitatively polynomial:

1. the unweighted connected non-bipartite graph binding;
2. the multiplicative-Sidon diagonal separation, including the local \(2\times2\) bulk inverses and the edge-row weights.

Thus neither the graph topology nor the diagonal spectral separation forces superpolynomial loss.

---

## 6. The remaining quantitative wall: unitary realization of the non-diagonal transports

The diagonal \(\Lambda\) constructed here is already unitary. However, the Article-II global-binding witness also uses non-diagonal local transports such as the determinant-one \(2\times2\) block

\[
\begin{pmatrix}1&1\\1&2\end{pmatrix}
\]

and then returns to genuine unitary Coxeter faces through Zariski density of \(SU(n)\) in \(SL_n(\mathbb C)\).

Zariski density is sufficient for **nonvanishing of a maximal minor**, hence for rank. It gives no quantitative lower bound on that minor or on the smallest singular value of a nearby unitary witness.

Therefore:

\[
\boxed{
\text{qualitative unitary return}
\not\Rightarrow
\text{polynomially stable unitary return}.
}
\tag{6.1}
\]

This is now the main unresolved bridge for transferring the polynomial complex-witness estimates to actual unitary Coxeter designs.

---

## 7. Next theorem target

The sharp next target is an explicit unitary replacement for the local non-diagonal block, for example a determinant-one Givens rotation

\[
U(\theta)=
\begin{pmatrix}
\cos\theta&\sin\theta\\
-\sin\theta&\cos\theta
\end{pmatrix},
\]

with an angle chosen away from its algebraic exceptional set, followed by a re-derivation of the local determinant and second-order binding coefficients.

If those formulas retain inverse-polynomial lower bounds under the phases of Section 2, the Zariski-density step can be removed from the quantitative Article-III extension argument.

---

## 8. Claim firewall

This note does **not** yet prove polynomial conditioning of the full sharp unitary Coxeter design. It proves polynomial separation for the diagonal multiplicative-Sidon layer and the associated reduced graph weights.

The unresolved items are:

- explicit quantitatively controlled unitary local transports;
- perturbative remainder control at finite \(t\);
- accumulated Schur coupling across the full design;
- the determinant-one two-scale odd-to-even transfer.
