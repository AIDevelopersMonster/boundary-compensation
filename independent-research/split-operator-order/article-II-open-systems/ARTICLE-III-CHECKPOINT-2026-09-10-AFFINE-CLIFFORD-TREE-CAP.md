# Article III checkpoint — affine Clifford spanning tree and one-cycle cap

**Date:** 2026-09-10  
**Branch:** `research/split-operator-order-article-II-v0.1`

## New theorem note

`ARTICLE-III-AFFINE-CLIFFORD-TREE-CAP-v0.1.md`

Commit:

`1c4e80c5bde7486adab92194d50e1c6ce2c8bfec`

## What is proved

For every odd prime `p`, define

- the affine quadratic chirp `P_tau`;
- its Fourier-conjugate chirp `Q_tau=F P_tau F^*`;
- the Weyl sign-class space `Omega_p=(F_p^2\{0})/{+-1}`.

The `P_tau` forest uses

`(p-1)^2/2`

faces and contracts `Omega_p` to `p-1` components.

The explicit `Q_tau` labels

`q_a=(-a,a)`, `a=1,...,(p-1)/2`,

and

`h_a=(a,1)`, `a=1,...,(p-3)/2`,

supply exactly `p-2` additional faces and connect those components into a spanning tree.

One final Fourier face with

`g_*=(-1,(p-1)/2)`

adds one cycle.

Total face count is exactly

`(p^2-1)/2`,

the information-theoretic sharp count.

The exact forest-elimination recurrence parametrizes the complete `P_tau`-forest kernel by only the horizontal/vertical axis Weyl values, giving a reduced completion matrix of size

`2p^2(p-1) x 2p^2(p-1)`.

Forest elimination has polynomial norm growth `O(p^2)`.

## Deterministic numerical evidence

For nonzero affine shift `tau`, the explicit sharp label pattern is full quotient rank in tested odd primes:

- `p=3`;
- `p=5`;
- `p=7`;
- `p=11`;
- `p=13`.

The `Q_tau` tree block is full row rank in the tested primes. After projecting the final Fourier face off the tree rowspace, its new rank is exactly `p^2+1`, leaving exactly `p^2-1` Hamiltonian gauge dimensions.

Observed reduced smallest positive singular values remain inverse-polynomial in the tested range.

The centered chirp `tau=0` has extra quotient nullity, while every tested nonzero affine shift gives full sharp rank. This isolates affine symmetry breaking as likely the missing one-cycle determinant factor.

## Strict next theorem target

Prove symbolically, for every odd prime `p` and every nonzero `tau`:

1. horizontal-tree gap

   `sigma_min^+(R^Q_{p,tau}) >= c p^-2`;

2. final Fourier cap on the `2p^2` residual kernel has rank exactly

   `p^2+1`

   and gap at least

   `c p^-1`;

3. the remaining kernel is exactly the Hamiltonian derivation space.

If these are proved, the branch obtains an explicit fresh sharp robust Coxeter theorem for every odd prime dimension.

## Claim firewall

Current status is not yet the all-prime sharp theorem. The spanning-tree combinatorics and forest elimination are proved; the all-prime `Q`-tree and final one-cycle spectral factors remain open. Numerical evidence is recorded separately from theorem claims.
