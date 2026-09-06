# Article III checkpoint — unitary cross-plane binding

**Date:** 2026-09-06  
**Branch:** `research/split-operator-order-article-II-v0.1`  
**Status:** `UNITARY_GLOBAL_BINDING_PROVED / FINITE-t_REMAINDER_OPEN`

## New theorem

`ARTICLE-III-UNITARY-CROSS-PLANE-BINDING-v0.1.md`

proves that the old nonunitary cross-plane perturbation can be replaced by the explicit unitary family

\[
B^u_{j,k}(t)=\Lambda\exp(t(E_{kn}-E_{nk})).
\]

For the explicit local Givens probe \(U_j(\theta)\), exact finite-\(t\) elimination in the isolated three-coordinate edge calculation gives the reduced residual relations

\[
\alpha_j+\gamma_k=0,
\qquad
\alpha_k+\gamma_j=0,
\]

with coefficients proportional to

\[
\frac{\sin^2t}{\cos t}
\frac{\lambda_k(\lambda_j-\lambda_n)}
{\lambda_j(\lambda_k-\lambda_n)}
\]

and

\[
\frac{\sin^2t}{\cos t}
\frac{\lambda_j-\lambda_n}{\lambda_k-\lambda_n}.
\]

Hence the second-order Schur coefficient is exactly the same weighted graph-binding operator used in the Article-II global-binding proof.

With polynomially separated unit-circle Sidon phases, all row weights are inverse-polynomially bounded. Combining with the graph spectral gap gives a crude polynomial condition estimate for the second-order reduced binding layer.

## Structural consequence

The even-to-odd global binding existence can now be proved directly on a real analytic unitary family. The Zariski-density return from `SL_n(C)` to `SU(n)` is no longer needed for the local or cross-plane binding mechanism.

## Remaining wall

What is not yet proved is a dimension-uniform finite-parameter estimate for the simultaneously perturbed full Schur map:

\[
S(t)=t^2S_2+O(t^3).
\]

The next theorem target is an explicit polynomial remainder bound

\[
\|S(t)-t^2S_2\|\le C d^m |t|^3
\]

on a polynomial-size neighborhood of zero. Together with the inverse-polynomial lower bound on \(S_2\), this would permit a polynomially small but finite choice of \(t\) and yield a quantitative unitary binding gap.

After that, the remaining higher-level issue is accumulated Schur coupling across the recursive extension hierarchy, especially the odd-to-even two-tail transfer.
