# CHECKPOINT-001 — centered tangent determinant factor reduction

Branch: `research/split-operator-order-article-II-v0.1`

Status: `PROVED_FACTOR_REDUCTION / SIMULTANEOUS_NONVANISHING_OPEN`

New result:

- The former opaque compressed determinant `det D_n` of size `n(n-2)` is reduced structurally.
- Off-diagonal block dependencies define a weighted directed-edge matrix `R` of rank `n`.
- If the positive-cycle submatrix `R_C` is invertible, global dependency coordinates can be chosen on non-cycle directed edges.
- In path-defect coordinates, the first-order binder derivative is triangular by cyclic distance.
- Its diagonal coefficients are

  `theta_e = lambda_(e,+) Y_*_(r-1,s) + lambda_(e,-) Y_*_(r,s+1)`.

Therefore, under the cycle-pivot hypothesis,

`det D_n != 0`

if and only if all `theta_e` are nonzero for non-cycle edges.

Detailed note:

`article-I/research/CENTERED-TANGENT-CYCLE-FACTOR-v0.1.md`

Next single obligation:

Prove that for every odd `n>=3` there exists a complete finite `H`-anchor compression satisfying both `det R_C != 0` and `theta_e != 0` for every non-cycle edge. After this, only the native tilt scalar remains in the odd extension-ready programme.
