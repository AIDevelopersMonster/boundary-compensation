# Article III checkpoint — critical block compression

**Date:** 2026-09-08  
**Branch:** `research/split-operator-order-article-II-v0.1`

## New result

The sharp robustness problem has been reduced from an ambient `Theta(d^4)` frame-selection problem to a grouped core-plus-defect problem of residual dimension only `O(d^2)`.

For

`N_d=(d^2-1)^2`, `r_d=2d^2`, `L_sharp=floor(d^2/2)`,

the exact scalar rank slack is

`s_d=2d^2-1` for even `d`, and `s_d=d^2-1` for odd `d`.

Ignoring face grouping, whitening the explicit robust `3d^2-1` Coxeter pool and applying sharp scalar restricted invertibility yields a core of rank

`N_d-s_d`

with

`sigma_min^+ >= c d^-2`.

Thus ordinary restricted invertibility is not the real obstruction.

## New active barrier

The unresolved theorem is block-compatible critical restricted invertibility:

select exactly `floor(d^2/2)` genuine Coxeter faces whose combined matrix-valued row blocks contain a polynomially conditioned core of rank at least `N_d-s_d`.

Once such a core exists, only an `s_d=O(d^2)` Schur-completion problem remains, with at most `2s_d` residual scalar-row capacity available.

Generic small-leverage sparsification is not directly adapted to this critical regime because whitened face blocks have `Theta(1)` average leverage when there are only `O(d^2)` high-rank blocks.

## Next strict attack

Exploit the algebraic structure of Coxeter face blocks rather than generic PSD sparsification. The best target is a block-compatible selection theorem tailored to the explicit Fourier-Sidon robust family, ideally producing a near-direct-sum core and reducing the final closure to the already isolated `O(d^2)` defect space.

Main theorem file commit:

`24a141494d848f89d7189b944b6abdc817ea4041`
