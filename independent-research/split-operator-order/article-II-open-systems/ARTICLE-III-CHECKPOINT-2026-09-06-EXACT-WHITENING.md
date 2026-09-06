# Article III checkpoint — exact whitening implementation

**Date:** 2026-09-06  
**Status:** `IMPLEMENTED / D3-D4 REGRESSION VERIFIED / D5 REGRESSION WIRED`

## New implementation

`examples/article_iii_conditioning_common_v010.py`

Commit: `c43b289b3fc5b87d4c9e6d85b2c9f8b3ea843e65`.

Implements the theorem-level domain whitener

`G_d^(-1/2)=P_r+(sqrt(2)/d)P_a+(1/d)P_s`

without numerical diagonalization, together with real/complex Coxeter-loop builders, normalized Kossakowski coordinates, frame diagnostics, and the d=3/d=4 72-face pool.

## Independent local regression

The exact projector implementation was independently executed for d=3 and d=4.

For d=3:

`sigma_min=0.12173880409571293`

`sigma_max=4.59941043232095`

`kappa=37.780972685626374`

`A=0.014820336422654371`

For d=4:

`sigma_min=0.0535512399868459`

`sigma_max=4.3512436874946685`

`kappa=81.25383629890717`

`A=0.002867735304128763`

The theorem identity residuals and whitening residuals were approximately `1e-14`.

Thus the old numerical Gram eigendecomposition and the new closed-form theorem whitener agree to machine precision for d=3,4.

## Repository regression entrypoint

`examples/article_iii_exact_whitening_regression_v010.py`

Commit: `a9a3b11fabd1b7f95a46095a139dd84ec3b05502`.

The script is wired for d=3,4,5. The d=5 path reconstructs the archived twelve engineered squares from `exact_face_rank_certificate_d5_v010.py` in real/complex arithmetic. The d=5 regression is not yet claimed as executed successfully; that remains the next reproducibility gate.

## New frame benchmark

`ARTICLE-III-FRAME-EFFICIENCY-BOUND-v0.1.md`

Commit: `d39d53ad6f26d5e86aa054968a7b418722d536a9`.

For `N=(d^2-1)^2`, define

`bar_lambda=Tr(S_D)/N`

and

`eta(D)=A_D/bar_lambda=N A_D/Tr(S_D)`.

Proved:

`0 <= eta(D) <= 1`,

with equality `eta=1` exactly for tight designs `S_D=bar_lambda I`.

Also

`kappa(D) >= eta(D)^(-1/2)`.

Replication leaves `bar_lambda`, `eta`, and `kappa` unchanged.

For equal-energy face classes, `bar_lambda=E_d/N` is independent of face count, so any oversampling benefit must be an isotropy gain rather than a trivial gain from duplicating measurement energy.

## Next action

1. execute and certify the d=5 exact-whitening regression;
2. rerun d=3/d=4 sharp and oversampling searches with closed-form whitening;
3. report `(L,A,B,kappa,Tr S,bar_lambda,eta,delta_tight)`;
4. determine whether oversampling primarily improves isotropy;
5. seek a Coxeter-specific upper bound on sharp-design `eta` as a route to a theorem-level redundancy barrier.

No asymptotic conditioning or redundancy theorem is claimed yet.
