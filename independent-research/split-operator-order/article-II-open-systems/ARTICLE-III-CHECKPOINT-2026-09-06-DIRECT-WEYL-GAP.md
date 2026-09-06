# Article III checkpoint — direct all-d Weyl cohomological gap

**Date:** 2026-09-06  
**Branch:** `research/split-operator-order-article-II-v0.1`  
**Status:** `NEW GLOBAL ROUTE / NONRECURSIVE POLYNOMIAL STABILITY PROVED`

## New theorem

File:

`ARTICLE-III-DIRECT-WEYL-COHOMOLOGICAL-GAP-v0.1.md`

Commit:

`a4a6d14e89c28c65cc641b53a1715b31c55139ee`

## Main result

For `G=Z_d x Z_d`, let `W_g` be the Weyl unitary basis and

`A_g=W_g^* D(W_g)`.

The two generator multiplication defects are

`E_j(g)=A_(e_j+g)-alpha_g(A_(e_j))-A_g`, `j=1,2`.

With normalized generator-defect norm,

`dist_sop(D,Der)<=4 sqrt(2) d^2 ||B_d D||_gen`.

Hence on the quotient by derivations,

`sigma_min(B_d)>=1/(4 sqrt(2) d^2)`.

For *-preserving maps the same bound holds modulo Hamiltonian derivations.

Using the exact loop extraction

`B_D(h,g)=R_D(W_hW_g)-K_D(h,g)`, 

a direct generalized flat-loop design with at most `3d^2-1` coefficients satisfies

`sigma_min(M_d|Q_d)>=1/(8 sqrt(3) d^2)`, 

and therefore

`A_d^Weyl>=1/(192 d^4)`.

A crude upper bound gives

`kappa_d^Weyl<=24 sqrt(3) d^3`.

## Strategic consequence

The recursive accumulation wall is not an intrinsic stability obstruction of contextual flat-loop tomography. A fresh dimension-d design rebuilt from the Weyl group is polynomially stable with no inherited stage loss.

The active problem therefore changes from

`control recursive parity accumulation`

to

`compile the quantitative Weyl cocycle gap into O(d^2) genuine adjacent-transposition Coxeter faces with only polynomial loss`.

If this robust Coxeter compilation succeeds, the remaining sharp problem becomes a constant-factor compression question from O(d^2) robust faces down to the exact sharp count `floor(d^2/2)`.

## Claim firewall

Not yet proved:

- polynomial stability for the `3d^2-1` Coxeter-only anchored construction;
- polynomial stability at sharp face count;
- optimal exponents;
- necessity of oversampling.
