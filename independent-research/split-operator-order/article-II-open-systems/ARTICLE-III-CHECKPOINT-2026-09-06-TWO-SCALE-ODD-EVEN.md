# Article III checkpoint — 2026-09-06 — two-scale odd-to-even transfer

**Branch:** `research/split-operator-order-article-II-v0.1`  
**Status:** `SINGLE-STAGE ODD-TO-EVEN QUANTITATIVE UNITARY TRANSFER CLOSED`

## New theorem

See:

`ARTICLE-III-UNITARY-TWO-SCALE-ODD-EVEN-TRANSFER-v0.1.md`

The full **new relative odd-to-even stage** is now direct-unitary and inverse-polynomially conditioned.

### Fixed first scale

Use

`epsilon_d = c_epsilon d^(-16)`

from the unitary two-tail epsilon theorem. At `t=0`:

`beta_j=r`, `delta_j=s`,

and the remaining kernel is

`alpha_1,...,alpha_d, gamma_1,...,gamma_d, r,s`.

The local-plus-first-binding gap is

`sigma_min^+ >= c d^(-16)`.

### Second unitary scale

For edge partner `k_j`, use

`B_j(epsilon,t) = Lambda D_j(epsilon) exp[t(E_(k_j,n)-E_(n,k_j))] in SU(n)`.

Choose `ell_j notin {j,k_j}` so the determinant compensation does not touch the three-coordinate cross-plane calculation.

At fixed nonzero `epsilon`, the second-order graph coefficient is exactly the unitary cross-plane coefficient with tail eigenvalue `mu=e^(i epsilon)`.

After orthonormal cokernel normalization, the edge-weight modulus is

`w_tilde_jk(epsilon)=1/(2 |lambda_k-e^(i epsilon)|)`.

At `epsilon=epsilon_d`, Sidon-tail separation gives

`1/4 <= w_tilde_jk <= C d^4`.

The weighted graph gap satisfies

`sigma_min^+ >= 1/(4 sqrt(d))`.

### Finite-t remainder

Using the `d^(-16)` bulk gap at fixed epsilon, adapted Schur inversion gives the crude derivative hierarchy culminating in

`||S'''(t)|| <= C d^79`.

Hence

`||S(t)-t^2 G_d(epsilon_d)|| <= C d^79 |t|^3`.

Choose

`t_d = c_t d^(-81)`.

Then

`sigma_min^+(S(t_d)) >= c d^(-163)`

on the complement of the graph gauge.

The residual kernel is exactly the 3-dimensional relative Hamiltonian gauge:

`alpha_1=...=alpha_d=q`,

`gamma_1=...=gamma_d=-q`,

with `r,s` free.

### Carrier plus local stage

The unitary five-defect carrier has

`sigma_min^+ >= c d^(-28)`.

Because the carrier has no columns in the `P_j,Q_j` variables, the combined new-stage matrix is block lower triangular. Conservative Schur elimination gives

`sigma_min^+(T_d) >= c d^(-194)`

for the complete `d+1`-face new relative odd-to-even stage.

No Zariski-density return is used in any layer of this stage.

## Major conclusion

Both parity mechanisms are now polynomially conditioned **stage by stage**. There is no remaining local superpolynomial obstruction inside either a single even-to-odd or a single odd-to-even extension step.

## New active barrier

Do NOT infer an all-dimensional polynomial lower frame bound by naive recursion.

A recurrence such as

`g_(d+1) >= d^(-C) g_d`

would give

`g_d >= (d!)^(-C)=exp[-Theta(d log d)]`,

which is superpolynomially small.

The active problem is now global accumulation:

1. prove a near-isometric transfer whose cumulative log-loss is only `O(log d)`, or
2. construct a fresh dimension-`d` sharp unitary design with a direct global lower-frame theorem rather than recursively inheriting old conditioning.

This is now the strict Article-III front.
