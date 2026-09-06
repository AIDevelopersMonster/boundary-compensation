# Article III checkpoint — 2026-09-06 — unitary two-tail epsilon binding

**Author:** Malachevsky, A.A. / Малачевский А.А.  
**ORCID:** 0009-0008-6009-3196  
**Status:** `CHECKPOINT / FIRST ODD-TO-EVEN BINDING SCALE CLOSED`

## Closed in this checkpoint

The first two-tail binding scale from the repaired odd-to-even extension is now direct unitary and inverse-polynomial.

The theorem note is:

`article-II-open-systems/ARTICLE-III-UNITARY-TWO-TAIL-EPSILON-BINDING-v0.1.md`.

Main ingredients:

1. determinant-one unitary Sidon-tail anchor `Lambda in SU(d+1)` with inverse-polynomial one- and two-product separation;
2. explicit Givens local faces `U_j in SU(d+1)`;
3. exact unitary diagonal first-scale perturbation
   `mu=exp(i epsilon)` with compensating `mu^(-1)` on an old coordinate;
4. exact residual equations
   `beta_j=r`, `delta_j=s`;
5. star-incidence first-scale singular gap independent of dimension before the common `|mu-1|` factor;
6. finite-epsilon remainder theorem and polynomial choice
   `epsilon_d=c_epsilon d^(-16)`;
7. local-plus-first-binding gap
   `sigma_min^+ >= c d^(-16)`.

No Zariski-density return is used in this layer.

## Current odd-to-even state

Already closed:

- five-defect carrier: direct unitary, inverse-polynomial;
- two-tail local reduction: direct unitary, inverse-polynomial;
- first epsilon binding: direct unitary, inverse-polynomial.

Remaining scalar kernel after the first scale:

`alpha_1,...,alpha_d, gamma_1,...,gamma_d, r,s`.

The second scale must bind the alpha/gamma variables by the connected non-bipartite graph while preserving the first-scale star gap.

## Next strict theorem target

Use

`B_(j,k)(epsilon,t)=Lambda D_j(epsilon) exp[t(E_(kn)-E_(nk))]`

with `ell_j notin {j,k}`.

At `epsilon=epsilon_d`, derive the exact/leading second-order graph coefficient, prove it remains inverse-polynomial, and prove a simultaneous two-scale finite-parameter theorem with

`epsilon=epsilon_d`, `t=t_d=d^(-O(1))`.

If successful, the entire **single odd-to-even extension-ready stage** becomes quantitatively polynomial and direct unitary.

## Claim firewall

Do not yet claim all-dimensional polynomial conditioning for recursively assembled sharp designs. The full odd-to-even two-scale theorem and inter-stage recursive accumulation remain open.
