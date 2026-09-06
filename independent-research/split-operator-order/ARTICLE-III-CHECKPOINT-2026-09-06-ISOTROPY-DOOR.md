# Article III checkpoint — isotropy census and next door

**Date:** 2026-09-06  
**Branch:** `research/split-operator-order-article-II-v0.1`

## New commits

- `edffd8ee7da3ef8b2d05f75b33a49c76e3b3fa8b` — full-precision d=5 exact-whitening regression references.
- `4c5685e5dc31924aadcfec5fa5f6fa963dc9ec98` — `ARTICLE-III-ISOTROPY-CENSUS-v0.1.md`.

## Closed

The d=5 real/complex baseline has now been reproduced with theorem-level exact whitening:

`sigma_min=0.03978665131344871`

`sigma_max=4.843628225780513`

`kappa=121.74003254562082`

`A=0.00158297762273795`

`B=23.46073438957768`.

The exact theorem diagnostics are at machine precision.

## Main numerical finding

For d=3 and d=4, improved sharp and oversampled designs can raise the lower frame bound and the normalized efficiency `eta=A/bar_lambda` while the mean frame eigenvalue remains nearly fixed or even decreases. Hence the observed stability gain is not merely an average-energy effect.

For d=3, a condition-number-oriented sequence gives:

- L=4: `eta≈0.009985`, `delta_tight≈1.0540`, `kappa≈21.52`;
- L=5: `eta≈0.031361`, `delta_tight≈0.9647`, `kappa≈11.73`;
- L=6: `eta≈0.056536`, `delta_tight≈0.9061`, `kappa≈8.52`;
- L=7: `eta≈0.074191`, `delta_tight≈0.8552`, `kappa≈7.26`.

The mean frame energy decreases along this sequence.

For d=4, an efficiency-improved sharp design and greedy extensions give:

- L=8: `eta≈0.002744`, `kappa≈51.24`;
- L=9: `eta≈0.006519`, `kappa≈33.48`;
- L=10: `eta≈0.010291`, `kappa≈26.14`;
- L=11: `eta≈0.012481`, `kappa≈23.99`.

Mean frame energy stays within a few percent.

## New obstruction / next door

Single-face energy `E_f=||C_f||_HS^2` varies strongly across the present Coxeter pool. Therefore raw-response stability and pure directional frame geometry must now be separated.

Next strict experiment: projectivize each nonzero face,

`C_hat_f = C_f / ||C_f||_HS`,

and repeat the sharp/oversampled census. In this projective layer all single-face energies are equal, so any improvement in the lower frame bound is necessarily angular/isotropy gain.

Do not claim that per-face Hilbert-Schmidt normalization is physically canonical. It is currently a diagnostic direction-space normalization.
