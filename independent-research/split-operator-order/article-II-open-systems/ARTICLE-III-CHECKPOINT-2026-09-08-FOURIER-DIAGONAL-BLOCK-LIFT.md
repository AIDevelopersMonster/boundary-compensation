# Article III checkpoint — Fourier diagonal block lift

**Date:** 2026-09-08  
**Branch:** `research/split-operator-order-article-II-v0.1`

## New theorem

`ARTICLE-III-FOURIER-DIAGONAL-BLOCK-LIFT-v0.1.md`

Commit:

`cd675531ce9b895fdc451a5b2c64f55c80c95bfa`

## Closed

Two structural facts at the sharp compression frontier are now proved.

### 1. Weyl-only sharp obstruction

On the real Weyl-diagonal dissipative sector

\[
\mathcal V_d^{diag}
=\{D(W_x)=\lambda_xW_x,\ \lambda_{-x}=\bar\lambda_x,\ \lambda_0=0\},
\]

with

\[
\dim_\mathbb R\mathcal V_d^{diag}=d^2-1,
\]

every Weyl-Weyl engineered square and every Weyl backtracking braid has rank at most one.

Therefore every Coxeter design using only Weyl first transports needs at least

\[
d^2-1
\]

faces and cannot attain the sharp count

\[
\lfloor d^2/2\rfloor.
\]

Hence a sharp design must contain genuinely non-Weyl mixing faces.

### 2. Three-face Fourier block lift for odd d

For odd `d`, the discrete Fourier transform has a flat Weyl expansion:

\[
F_d=\sum_{x\in\mathbb Z_d^2}c_xW_x,
\qquad |c_x|=1/d.
\]

Therefore the evaluation map

\[
D\mapsto F_d^*D(F_d)
\]

is an isometry on the Weyl-diagonal sector.

For the three explicit square faces

\[
(F_d,W_{(1,0)}),
\quad
(F_d,W_{(0,1)}),
\quad
(F_d,W_{(1,1)}),
\]

the traceless square data are

\[
Q_g(D)=B+\alpha_{Jg}(B^*),
\qquad B=P_0(F_d^*D(F_d)).
\]

The differences of the three data vectors generate two independent torus translations. A discrete Poincare estimate then gives

\[
\|B\|_2\le Cd\,\|Q\|.
\]

The identity Weyl coefficient recovers the scalar part with one additional factor `d`, so

\[
\boxed{\sigma_{min}\ge c d^{-2}}
\]

on the whole `d^2-1` dimensional Weyl-diagonal sector.

Thus three whole Coxeter faces already control an `O(d^2)` quotient sector polynomially.

## Interpretation

Critical block compatibility is not hopeless: a dense non-Weyl face can carry `Theta(d^2)` useful coordinates at once. The correct sharp architecture should therefore be hybrid:

\[
\boxed{
\text{few dense Fourier-type faces}
+\text{many sparse/local faces}
+\text{O}(d^2)\text{ Schur closure}.
}
\]

## Active door

Use the **remaining outputs of the same three Fourier faces**, together with exactly

\[
L_d^\sharp-3
\]

additional explicit local/sparse Coxeter faces, to build a block-compatible core of rank at least

\[
N_d-s_d
\]

with lower singular gap `d^{-O(1)}`.

The strict next calculation should decompose the full quotient under Weyl characters and determine which non-diagonal superoperator sectors the three Fourier faces already couple. The goal is to show that their uncovered complement has a sparse block structure that can be filled at near-direct-sum cost.

## Claim firewall

Do not claim sharp polynomial robustness yet. The current theorem is exact only for the Weyl-diagonal sector and only the flat Fourier statement for odd `d` is proved in this note.
