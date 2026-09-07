# Article III checkpoint — direct robust Coxeter compilation

**Date:** 2026-09-07  
**Branch:** `research/split-operator-order-article-II-v0.1`

## New theorem

File:

`ARTICLE-III-DIRECT-ROBUST-COXETER-COMPILATION-v0.1.md`

Commit:

`cdfd4a0b793da73b5174366541f4e31bdb552d0e`

Status:

`PROVED / FRESH ALL-D ROBUST COXETER DESIGN / O(d^2) FACES / NO RECURSIVE ACCUMULATION`

## Main result

A fresh, nonrecursive, genuine adjacent-transposition Coxeter design exists in every dimension `d>=2` using exactly

`3d^2-1`

matrix-valued faces and has an inverse-polynomial lower singular-value bound in the equal-face normalized metric:

`σ_min >= c d^(-6)`.

Thus

`A_d^Cox >= c^2 d^(-12)`

and with the crude upper norm estimate

`||C_d|| <= 6d`,

one gets

`κ_d^Cox <= C d^7`.

The construction uses explicit anchors:

- polynomially separated diagonal Sidon phase anchor `Z_d`;
- determinant-corrected discrete Fourier anchor `F_d`.

No dense-generation argument remains in the stability proof.

## Key exact theorem

If a unital superoperator commutes with both `Ad_{Z_d}` and `Ad_{F_d}`, then it lies in

`span{P_1,P_0}`,

where `P_1(X)=τ(X)I` and `P_0(X)=X-τ(X)I`. Unital normalization leaves only the depolarizing line `C P_0`.

The quantitative version gives

`dist(T, C P_0) <= C d^5 (||U_Z(T)-T|| + ||U_F(T)-T||)`.

Square and backtracking residuals control these quotient conjugation residuals with an additional factor `O(d)`, hence

`dist(D, R P_0) <= C d^6 ||CoxeterData(D)||`.

Weyl backtracking removes the depolarizing line.

## Programme consequence

The recursive conditioning-accumulation wall is bypassed inside genuine Coxeter geometry itself.

Closed:

- robust generalized flat-loop tomography: all-d polynomial;
- robust Coxeter tomography: all-d polynomial with `O(d^2)` faces.

Open central Article-III problem:

`Can one compress the robust O(d^2) Coxeter design to the sharp count floor(d^2/2) while retaining an inverse-polynomial lower frame bound?`

This is now the strict active frontier.

Do not claim from the present theorem that sharp-count designs are polynomially stable, or that constant-factor redundancy is necessary.