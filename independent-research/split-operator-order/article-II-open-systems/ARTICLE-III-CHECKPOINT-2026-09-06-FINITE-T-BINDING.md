# Article III checkpoint — finite-t unitary binding closure

**Date:** 2026-09-06  
**Branch:** `research/split-operator-order-article-II-v0.1`  
**Status:** `EVEN-TO-ODD BINDING FINITE-t POLYNOMIAL GAP PROVED`

Read together with:

- `ARTICLE-III-UNITARY-CROSS-PLANE-BINDING-v0.1.md`;
- `ARTICLE-III-POLYNOMIAL-SIDON-PHASES-v0.1.md`;
- `ARTICLE-III-BINDING-GRAPH-SPECTRAL-GAP-v0.1.md`;
- `ARTICLE-III-POLYNOMIAL-FINITE-T-BINDING-v0.1.md`.

## New closure

The simultaneous direct-unitary global-binding family admits a polynomial finite-parameter Schur estimate.

With `n=d+1` and `m_d=2 d n^2 <= 8 d^3`, the unperturbed local bulk has

`||A(0)^(-1)|| <= C d^6`

from polynomial Sidon separation.

All first three derivatives of the full measurement matrix obey a crude bound

`||M_d^(r)(t)|| <= C d^3`, `r=0,1,2,3`, for `|t|<=1/4`.

Hence on `|t|<=c d^(-9)` the bulk inverse remains bounded by `O(d^6)`, with inverse derivatives through third order bounded by a crude hierarchy ending at `O(d^33)`.

For the reduced Schur map

`S_d(t)=D(t)-C(t)A(t)^(-1)B(t)`

one obtains

`S_d(0)=S_d'(0)=0`,

`(1/2)S_d''(0)=S_{2,d}`,

and

`||S_d(t)-t^2 S_{2,d}|| <= C d^39 |t|^3`.

In orthonormal cokernel coordinates the normalized second-order edge weights satisfy

`1/4 <= w_tilde_jk <= 3 pi n^3`,

so the star-triangle graph gap gives

`sigma_min^+(S_{2,d}) >= 1/(4 sqrt(d))`.

Choose

`t_d = c_* d^(-40)`

with a sufficiently small absolute constant. Then

`sigma_min^+(S_d(t_d)|G^perp) >= c d^(-81)`

and the reduced Schur block has polynomial condition number `O(d^4)`.

Using Schur block factorization and the polynomially stable bulk block,

`sigma_min^+(M_d(t_d)) >= c d^(-81)`

on the gauge complement, while `||M_d(t_d)|| <= C d^3`; hence the full single even-to-odd invisible-completion stage has a crude polynomial condition estimate

`kappa = O(d^84)`.

The exponent is intentionally nonoptimal. The theorem-level point is polynomiality.

## Important boundary

This does **not** yet prove an all-dimensional recursively sharp polynomial condition-number theorem.

The active barrier is now the repaired odd-to-even transfer (`article-I/research/ODD-TO-EVEN-TRANSFER-AUDIT-REPAIR-v0.1.md`), specifically:

- explicit unitary five-defect carrier;
- quantitative two-tail local reduction;
- two binding scales `epsilon` and `t` with polynomial finite-parameter gaps;
- removal of the remaining qualitative determinant-one/Zariski unitary return.

## Next hit

Attack the odd-to-even carrier first. Seek an explicit unitary block-Levi carrier family whose relative `R`-kernel is exactly the two-dimensional tail gauge and whose five old missing coordinates survive with inverse-polynomial margin. Only after that, quantize the two-scale local/binding mechanism.
