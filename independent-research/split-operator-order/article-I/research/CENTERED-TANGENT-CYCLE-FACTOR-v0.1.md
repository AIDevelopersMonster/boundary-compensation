# Centered tangent cycle factorization

**Status:** `PROVED_FACTOR_REDUCTION / SIMULTANEOUS_NONVANISHING_OPEN`

For odd `n>=3`, the compressed dependency determinant from `CENTERED-TANGENT-COMPRESSION-AUDIT-v0.1.md` can be reduced from one opaque `n(n-2) x n(n-2)` determinant to a cycle pivot plus one scalar condition per non-cycle directed edge.

Let `H=diag(h_0,...,h_(n-1))`, `L=(n^2-1)/2`, and let `Y_1,...,Y_L` be a finite complete compression of the `H`-anchor regular equations. For each off-diagonal output block `(a,b)`, the restricted block has a one-dimensional left-nullspace. Write its aggregate coefficients as matrices `A_(a,b), B_(a,b)`. Restoring the diagonal part `Z=diag(z_0,...,z_(n-1))` of `F(H)` gives the edge row

`rho_(a,b)(z)=-(A_(a,b))_(a,b) z_a-(B_(a,b))_(a,b) z_b`.

The `n(n-1) x n` matrix `R` of these rows has rank `n`, because the full finite presentation has exactly `n(n-2)` row dependencies. Hence the global dependency space is `ker(R^T)`.

Choose the positive cycle edges `C={(s+1,s)}`. If the corresponding `n x n` submatrix `R_C` is invertible, then every global dependency is uniquely parametrized by its coefficients on the `n(n-2)` non-cycle edges. Writing the cycle-edge coefficients as `alpha_s z_(s+1)+beta_s z_s`, one has

`det R_C = prod_s beta_s + prod_s alpha_s`

because `n` is odd.

Now perturb the last face anchor by `H -> H+tS`, where `S` is the cyclic shift. On the complete `H`-anchor Schur kernel, define path-defect coordinates

`u_(r,s)=c_(r,s)-sum_{j=s}^{r-1} a_j`

for non-cycle directed edges. For edge `e=(r,s)` of cyclic distance at least two, the derivative of its local dependency has the triangular form

`g_e = theta_e u_(r,s) + lower-distance terms`,

with

`theta_e = lambda_(e,+) Y_*_(r-1,s) + lambda_(e,-) Y_*_(r,s+1)`.

Cycle-edge derivative terms vanish on the Schur kernel. Therefore after eliminating cycle dependencies through `R_C`, the compressed derivative operator `D_n` is triangular in increasing cyclic distance, with diagonal entries `theta_e` over all non-cycle edges.

Thus, under the cycle-pivot hypothesis,

`det D_n != 0`

iff

`theta_e != 0`

for every non-cycle directed edge.

This is the new reduced barrier. The remaining obligation is to prove simultaneous nonvanishing of `det R_C` and all `theta_e` for some complete finite `H`-anchor compression in every odd dimension. After that only the native tilt scalar remains.
