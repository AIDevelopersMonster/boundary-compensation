# Audit note: order-three Clifford anchor in arbitrary finite dimension

**Article II — infrastructure audit v0.1**  
**Author:** Malachevsky, A.A.  
**Status:** `INFRASTRUCTURE_VERIFIED_WITH_EVEN-DIMENSION_CAVEAT`

## Purpose

The improved all-d Coxeter upper bound `L_d^Cox <= 2 d^2` uses a unitary anchor whose conjugation action implements the order-three phase-space map

`F_Z = [[0,-1],[1,-1]]`.

The mathematical argument needs only the existence, for every finite `d>=2`, of a unitary `S` such that

`S^* W_g S = phase(g) W_(F_Z g)`

and `S^3` is scalar.

## What is verified

This is standard finite Weyl-Heisenberg / Clifford infrastructure. Order-three Clifford unitaries associated with the Zauner matrix are treated in the extended-Clifford literature in arbitrary finite dimension. The arbitrary-dimension Clifford representation has well-known even-dimensional bookkeeping subtleties: one should not state naively that every relevant operation is represented by the same `SL(2,Z_d)` formula used in odd dimension. In even dimension, standard formulations use the appropriate doubled-modulus / central-extension convention.

Accordingly, Article II should state only the implementation property actually needed above, not an over-broad symplectic-surjectivity claim.

## Self-contained group-level formulation

Let `X,Z` be the standard Weyl pair with

`ZX = omega XZ`, `omega=exp(2 pi i/d)`.

Define an automorphism of the finite Heisenberg group by

`X -> Z`,

`Z -> nu X^(-1) Z^(-1)`,

where the phase `nu` is chosen so that

`nu^d = (-1)^(d-1)`.

Indeed,

`(X^(-1) Z^(-1))^d = (-1)^(d-1) I`,

so the declared image of `Z` again has order `d`, and the commutation relation is preserved. Modulo the center, the induced map on `Z_d^2` is exactly `F_Z`, which satisfies `F_Z^3=I` over the integers and therefore modulo every `d`.

By finite Stone-von Neumann uniqueness, any automorphism of the finite Heisenberg group fixing the center is unitarily implemented in its irreducible `d`-dimensional representation, uniquely up to phase. Therefore an implementing unitary `S` exists for every finite `d`; because the induced automorphism has projective order three, `S^3` is scalar by Schur's lemma.

This is sufficient for the sign-flip iteration used in `COXETER-CONSTANT-2-v0.1.md`.

## Publication wording

Safe wording:

> Choose an order-three Clifford (Zauner-type) unitary `S` implementing the phase-space automorphism `F_Z`. Such an implementer exists in every finite dimension; in even dimensions we use the standard finite-Heisenberg central-extension convention rather than the simplified odd-dimensional `SL(2,Z_d)` parametrization.

Avoid wording such as:

> Every element of `SL(2,Z_d)` has the same direct Clifford implementation in all dimensions.

That stronger statement is unnecessary and obscures the even-dimensional convention.

## Literature infrastructure

- D. M. Appleby, *SIC-POVMs and the Extended Clifford Group*, arXiv:quant-ph/0412001; J. Math. Phys. 46 (2005) 052107.
- D. M. Appleby et al., *Systems of Imprimitivity for the Clifford Group*, arXiv:1210.1055.

No novelty is claimed for the Clifford/Heisenberg implementation itself.
