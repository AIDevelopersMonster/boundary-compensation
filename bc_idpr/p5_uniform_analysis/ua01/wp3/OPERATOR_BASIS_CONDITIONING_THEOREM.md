# BC-IDPR P5-UA01 WP3 — Two-Channel Operator-Basis Conditioning

**Contract:** `BC-IDPR-P5-UA01-WP3`  
**Status:** `EXACT_REDUCTION_THEOREM_CLOSED / NUMERICAL_INTERVAL_DIAGNOSTIC_PASS / RELEASE_CERTIFICATE_OPEN`  
**Upstream:** `WP1/WP2 EXACT_TWO_CHANNEL_E_OPTIMAL_FRAME_CERTIFIED`  
**Scope:** real traceless symmetric residual operators on the declared two-channel carrier class.

## 1. Canonical adapted pair

For a two-channel carrier \(J\), let \(F_J(\theta)\in O(2)\) be the frozen real recoupling matrix. After trace removal and Hilbert--Schmidt normalization, any diagonal channel observable with distinct eigenvalues becomes a signed copy of

\[
E_z=\frac1{\sqrt2}\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]

With the increasing channel order fixing the sign, define

\[
B_{E,J}=E_z,
\qquad
B_{G,J}(\theta)=F_J(\theta)E_zF_J(\theta)^T,
\]

and the channel correlation

\[
c_J(\theta)=\langle B_{E,J},B_{G,J}(\theta)\rangle_{HS}.
\]

Let \(C_J(\theta)\) be the coordinate matrix whose columns are \(B_{E,J}\) and \(B_{G,J}(\theta)\) in the canonical orthonormal basis of \(\operatorname{Sym}_0(2,\mathbb R)\).

## 2. Exact conditioning theorem

### Theorem 2

For every regular two-channel carrier,

\[
C_J(\theta)^TC_J(\theta)
=
\begin{pmatrix}
1&c_J(\theta)\\
c_J(\theta)&1
\end{pmatrix}.
\]

Therefore

\[
\boxed{\sigma_{\min}(C_J(\theta))^2=1-|c_J(\theta)|}
\]

and, for the exact E-optimal four-state design from WP1/WP2,

\[
\boxed{
c_{\mathrm{frame},J}(\theta)
=\frac14\bigl(1-|c_J(\theta)|\bigr).
}
\]

Moreover,

\[
\boxed{
\|[B_{E,J},B_{G,J}(\theta)]\|_{HS}^2
=2\bigl(1-c_J(\theta)^2\bigr).
}
\]

Hence

\[
c_{\mathrm{frame},J}(\theta)
=
\frac{\|[B_{E,J},B_{G,J}(\theta)]\|_{HS}^2}
{8(1+|c_J(\theta)|)}
\ge
\frac1{16}\|[B_{E,J},B_{G,J}(\theta)]\|_{HS}^2.
\]

### Proof

The two normalized adapted operators are unit vectors in the two-dimensional Hilbert space \(\operatorname{Sym}_0(2,\mathbb R)\), so their coordinate Gram matrix has diagonal entries one and off-diagonal entry \(c_J\). Its eigenvalues are \(1\pm|c_J|\), proving the singular-value identity. Substitution into the WP1/WP2 identity \(F_B=\tfrac14C^TC\) gives the frame formula.

Writing \(B_{G,J}=c_JE_z+s_JE_x\), with \(c_J^2+s_J^2=1\), and using \(\|[E_z,E_x]\|_{HS}^2=2\), gives the commutator identity. ∎

## 3. Exact frame-wall classification

The following conditions are equivalent:

\[
\sigma_{\min}(C_J(\theta))=0,
\]

\[
|c_J(\theta)|=1,
\]

\[
[B_{E,J},B_{G,J}(\theta)]=0,
\]

\[
F_J(\theta)\text{ is a signed permutation matrix in the ordered channel bases.}
\]

Thus the two-channel P5 frame wall is exactly the projective coincidence of the two normalized channel-observable directions. It is not an unspecified numerical rank loss.

For

\[
F_J(\theta)=\begin{pmatrix}a&b\\c&d\end{pmatrix},
\]

orthogonality gives the scalar reduction

\[
\boxed{c_J(\theta)=2a(\theta)^2-1.}
\]

The complete WP3 conditioning problem is therefore reduced to enclosing one q-Racah matrix entry.

## 4. Finite-class diagnostic

A reproducible adaptive interval diagnostic was run on the exact ordered `A6` enumeration:

- 283 ordered carriers;
- doubled external labels \(1,\ldots,6\);
- exactly two channels in both pairings;
- all q-indices at most ten;
- frozen deformation interval \(\eta\in[0.60,1.15]\), \(\theta=\pi\eta/12\);
- initial cell width \(0.005\);
- adaptive subdivision to depth at most 12.

The run resolved every cell and verified the conservative test

\[
1-|c_J(\eta)|>0.06
\]

through the interval backend used for the diagnostic. The smallest proved cell margin reported by that run was approximately

\[
0.0600046138.
\]

The corresponding provisional frame floor is

\[
c_{\mathrm{frame}}>0.015.
\]

This numerical interval result is **not yet promoted to a release theorem** because the current diagnostic backend must be independently replicated with the programme's established outward-rounded Arb pipeline. The exact reduction theorem above does not depend on this numerical diagnostic.

## 5. Programme consequence

WP3 has converted the open basis-conditioning quantity into the explicit scalar margin

\[
\inf_{J,\eta}\bigl(1-|c_J(\eta)|\bigr).
\]

The next admissible step is a release-grade Arb certificate for a rational positive margin, followed by WP4 insertion into

\[
c_{\mathrm{frame},J}(\eta)
=\frac14\bigl(1-|c_J(\eta)|\bigr).
\]

No RC02 predictor, control, pairing, threshold, or confirmatory result is reopened.

## 6. Claim firewall

This theorem is finite-dimensional and two-channel. The numerical diagnostic is restricted to the declared finite `A6` class and frozen chamber. Neither establishes an arbitrary-label theorem, full categorical coherence, global gluing, a continuum limit, or physical dynamics.
