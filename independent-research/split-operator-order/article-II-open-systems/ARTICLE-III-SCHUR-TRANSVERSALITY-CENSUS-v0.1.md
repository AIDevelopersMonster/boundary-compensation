# Article III — Schur Transversality Census at Sharp Completion

**Author:** Malachevsky, A.A. / Малачевский А.А.  
**ORCID:** 0009-0008-6009-3196  
**Date:** 2026-09-06  
**Status:** `NUMERICAL_EVIDENCE / SHARP-COMPLETION BOTTLENECK RESOLVED LOCALLY`

## 0. Purpose

This note applies the exact Schur-complement criterion from
`ARTICLE-III-SCHUR-TRANSVERSALITY-THEOREM-v0.1.md`
to the polar support-frame sequences used in the projective/polar census.

The aim is to identify where rank completion becomes poorly conditioned.

---

## 1. d=3 kernel profile

For the four-face projective/polar sharp seed, each face has support rank `18` in a quotient of dimension

\[
N=64.
\]

The stacked support ranks evolve as

\[
18,\ 36,\ 54,\ 64,
\]

so the blind dimensions are

\[
\boxed{46,\ 28,\ 10,\ 0.}
\]

Thus the first three faces are in algebraically maximal transverse position inside this small pool: each removes all 18 dimensions it can remove. The fourth face kills the remaining 10-dimensional blind subspace.

Immediately before the fourth face, the smallest positive eigenvalue of the unaveraged accumulated support frame is approximately

\[
\gamma_3\approx5.93744\times10^{-4}.
\]

For the fourth face, the raw kernel block has

\[
\lambda_{\min}(R_{00})\approx6.38839\times10^{-3}.
\]

Equivalently, because `r=18`, the raw projector coverage of the current blind sector has minimum

\[
\lambda_{\min}(P_KPP_K|_K)
\approx0.114991.
\]

However the exact Schur transversality coefficient is only

\[
\boxed{
\theta_3
\approx2.06230\times10^{-3}.
}
\]

The actual smallest eigenvalue after adding the fourth face, before averaging by four, is

\[
\lambda_{\min}(A_4)
\approx1.64260\times10^{-3}.
\]

After averaging,

\[
\lambda_{\min}(S_4)
\approx4.10649\times10^{-4},
\]

which matches the polar sharp census.

Thus in `d=3`, sharp completion is already not controlled by raw kernel coverage alone; Schur leakage reduces the effective transversal strength by a factor of roughly three.

---

## 2. d=4 kernel profile

For the eight-face sharp seed used in the polar census, all selected faces have support rank `32` and

\[
N=225.
\]

The stacked support ranks evolve as

\[
32,\ 64,\ 96,\ 128,\ 160,\ 192,\ 224,\ 225.
\]

Hence the blind dimensions are

\[
\boxed{
193,\ 161,\ 129,\ 97,\ 65,\ 33,\ 1,\ 0.
}
\]

This is a striking structure: the first seven faces remove exactly 32 new dimensions at every step until only **one** blind direction remains. Algebraically the design is almost perfectly extension-efficient.

But immediately before the final face, the smallest positive eigenvalue of the unaveraged accumulated support frame has collapsed to

\[
\boxed{
\gamma_7
\approx4.28926\times10^{-7}.
}
\]

The last face does have substantial raw overlap with the final blind direction. Since that blind space is one-dimensional,

\[
\|Pv\|^2
\approx0.0954958.
\]

With `r=32`, this corresponds to

\[
R_{00}
\approx2.98424\times10^{-3}.
\]

So the last face is not nearly tangent to the final blind direction in the naive principal-angle sense.

Nevertheless the exact Schur transversality coefficient is only

\[
\boxed{
\theta_7
\approx3.31747\times10^{-4}.
}
\]

The actual smallest eigenvalue after adding the eighth face, before averaging, is

\[
\lambda_{\min}(A_8)
\approx9.56869\times10^{-5}.
\]

After averaging by eight,

\[
\boxed{
\lambda_{\min}(S_8)
\approx1.19609\times10^{-5},
}
\]

which yields the observed

\[
\eta_{\mathrm{supp}}
\approx0.002691.
\]

---

## 3. Main diagnostic conclusion

The `d=4` sharp design is algebraically excellent but spectrally fragile.

Its first seven faces almost saturate dimension removal:

\[
32\times7=224
\]

independent measured directions are accumulated in a 225-dimensional quotient.

Yet the smallest positive frame eigenvalue by that point is already of order

\[
10^{-7}.
\]

This produces the separation

\[
\boxed{
\text{maximal rank growth}
\not\Rightarrow
\text{stable transversality}.
}
\]

More sharply, the final face has respectable direct overlap with the last blind vector, but the effective Schur coefficient is much smaller because that direction is coupled to an already observed sector containing extremely weak directions.

Therefore the dominant obstruction is not the final missing dimension itself. It is the **conditioning history of the complement before the final rank-completion step**.

This is the key new door.

---

## 4. Refined Article-III target

The previous candidate invariant

\[
K_j=\dim\bigcap_{k\le j}\ker C_{f_k}
\]

is necessary but insufficient.

The next sufficient state descriptor along an ordered design should include

\[
\boxed{
(K_j,\ \gamma_j,\ \theta_j,\ \chi_j),
}
\]

where

\[
\gamma_j
=
\lambda_{\min}^+(A_j)
\]

is the smallest positive accumulated support eigenvalue,

\[
\theta_j
=
\lambda_{\min}(\Sigma_{A_j}(R_{j+1}))
\]

is the Schur transversality of the next face, and `chi_j` is the triangular coupling distortion from the theorem note.

A robust extension-ready design must preserve not only rapid kernel decay but a controlled positive spectral floor throughout the extension.

This suggests replacing the old slogan

`extension-ready minimal design`

by the stronger quantitative notion

\[
\boxed{
\text{spectrally extension-ready design}.
}
\]

A candidate definition is an ordered design for which every nonzero positive spectral floor and every kernel-killing Schur coefficient is bounded below by a declared dimension-dependent function.

---

## 5. Research consequence

The next proof attempt should not begin with more random search.

The strongest route is now structural:

1. derive exact support/kernel descriptions for the all-dimensional Coxeter construction used in Article II;
2. track `K_j` and the smallest positive support-frame eigenvalue under the extension induction;
3. identify whether the odd-to-even and block-extension mechanisms preserve polynomial Schur transversality;
4. if they do, obtain a polynomial conditioning theorem;
5. if they do not, isolate the first forced small-Schur step and convert it into a redundancy lower bound.

This directly connects Article III to the existing Article-II extension-ready proof architecture rather than treating conditioning as an unrelated numerical optimization problem.

---

## 6. Claim firewall

The `d=3,4` census does not establish an asymptotic law. In particular it does not prove that the Article-II all-dimensional construction has superpolynomially small Schur transversality, nor that every sharp design does.

It does establish a concrete finite-dimensional mechanism that rank-only proofs cannot detect:

\[
\boxed{
\text{the complement can become spectrally weak long before the final kernel disappears.}
}
