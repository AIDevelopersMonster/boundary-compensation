# BC-IDPR P5-UA01 WP3 — Physical Measurement and Whitening Jet Calculus

**Contract:** `BC-IDPR-P5-UA01-WP3-H5A`  
**Status:** `EXACT_MEASUREMENT_AND_WHITENING_JET_CALCULUS_CLOSED / PRIMITIVE_N15_JET_BOUNDS_OPEN`  
**Upstream:** `BC-IDPR-P5-UA01-PHYSICAL-RESIDUAL-FRAME-MATRIX`  
**Scope:** a finite constant-rank physical residual bundle on one certified deformation chamber.

## 1. Purpose and novelty boundary

The static physical frame is described by

\[
M_{ai}(\theta)=\sqrt{w_a(\theta)}\,
\langle\psi_a(\theta),U_i(\theta)\psi_a(\theta)\rangle,
\qquad
G_{ij}(\theta)=\operatorname{Tr}(U_i(\theta)^*U_j(\theta)).
\]

Here the generators are the physical residual directions, eventually

\[
U_1=R_{\rm bulk},\qquad U_2=W,
\]

and the states are the registered projected-torus coherent states. The purpose of this work package is to derive the first two jets of the Hilbert--Schmidt-whitened matrix

\[
\widehat M(\theta)=M(\theta)G(\theta)^{-1/2}
\]

from supplied primitive jets of the generators, states and quadrature weights.

This closes the **calculus layer** only. It does not yet provide bounds for the actual N15 primitive jets, does not prove constant support rank on the whole deformation interval, and does not select RC02 mode 5.

## 2. Admissible chamber

Assume on an interval `I`:

1. `U_i(theta)` are twice differentiable Hermitian matrices on one fixed finite carrier;
2. `psi_a(theta)` are twice differentiable normalized states;
3. `w_a(theta)>0` are twice differentiable weights;
4. the Hilbert--Schmidt Gram matrix satisfies
   \[
   G(\theta)\succeq \gamma I_m
   \]
   for some declared `gamma>0`;
5. no support, chart, residual-rank or phase-gauge wall is crossed.

The normalized-state jets satisfy

\[
2\operatorname{Re}\langle\psi_a,\psi_a'\rangle=0,
\]

\[
2\operatorname{Re}
\left(
\langle\psi_a,\psi_a''\rangle+
\langle\psi_a',\psi_a'\rangle
\right)=0.
\]

A failure of any condition requires a certificate reset rather than silent continuation.

## 3. Lower-symbol jets

Set

\[
s_{ai}=\langle\psi_a,U_i\psi_a\rangle.
\]

### Theorem 1 — Exact lower-symbol jet formulas

For every state-generator pair,

\[
\boxed{
 s_{ai}'
 =
 \langle\psi_a',U_i\psi_a\rangle
 +\langle\psi_a,U_i'\psi_a\rangle
 +\langle\psi_a,U_i\psi_a'\rangle.
}
\]

The second derivative is

\[
\boxed{
\begin{aligned}
 s_{ai}''={}&
 \langle\psi_a'',U_i\psi_a\rangle
 +\langle\psi_a,U_i''\psi_a\rangle
 +\langle\psi_a,U_i\psi_a''\rangle\\
 &+2\langle\psi_a',U_i'\psi_a\rangle
 +2\langle\psi_a',U_i\psi_a'\rangle
 +2\langle\psi_a,U_i'\psi_a'\rangle.
\end{aligned}
}
\]

These formulas include the deformation of both the operator and the observation states. Omitting the state derivatives is legal only when the frozen physical protocol proves that the coherent-state vectors are independent of the deformation coordinate.

### Proof

Differentiate the sesquilinear expression `psi^* U psi` once and twice and apply the product rule to all three factors. Hermiticity makes the total derivative real but does not remove any of the terms. ∎

## 4. Weighted measurement jets

Let

\[
r_a=\sqrt{w_a}.
\]

Then

\[
r_a'=\frac{w_a'}{2\sqrt{w_a}},
\qquad
r_a''=\frac{w_a''}{2\sqrt{w_a}}
-\frac{(w_a')^2}{4w_a^{3/2}}.
\]

Because `M_ai=r_a s_ai`,

\[
\boxed{M'=r's+rs'},
\]

\[
\boxed{M''=r''s+2r's'+rs''}.
\]

For the frozen N15 quadrature convention, once the geometry-to-chart map is proved fixed under the independent deformation,

\[
w_a'=w_a''=0,
\]

and these reduce to `M'=sqrt(w) s'` and `M''=sqrt(w) s''`.

## 5. Hilbert--Schmidt Gram jets

### Theorem 2 — Exact Gram jet formulas

For

\[
G_{ij}=\operatorname{Tr}(U_i^*U_j),
\]

one has

\[
\boxed{
G_{ij}'=
\operatorname{Tr}(U_i'^*U_j+U_i^*U_j')
}
\]

and

\[
\boxed{
G_{ij}''=
\operatorname{Tr}(U_i''^*U_j+2U_i'^*U_j'+U_i^*U_j'').
}
\]

These identities are exact and require no choice of generator coordinates beyond the declared differentiable basis.

## 6. Whitening without eigenvector derivatives

Direct differentiation of eigenvectors of `G(theta)` is gauge-unstable near clustered eigenvalues. Instead define

\[
H=G^{1/2},\qquad W=H^{-1}=G^{-1/2}.
\]

### Theorem 3 — Sylvester whitening jets

The unique Hermitian derivatives `H'` and `H''` are determined by

\[
\boxed{HH'+H'H=G'},
\]

\[
\boxed{HH''+H''H=G''-2(H')^2}.
\]

The whitening derivatives are

\[
\boxed{W'=-WH'W},
\]

\[
\boxed{W''=2WH'WH'W-WH''W}.
\]

### Proof

Differentiate `H^2=G` once and twice. Since `H` is positive definite, the Sylvester map

\[
\mathcal L_H(X)=HX+XH
\]

is invertible. Differentiate `WH=I` to obtain the inverse derivatives. ∎

This construction never differentiates a chosen eigenvector frame and is therefore suitable for clustered but positive Hilbert--Schmidt spectra.

## 7. Explicit wall-conditioned whitening bounds

Let

\[
\gamma=\lambda_{\min}(G)>0,
\qquad
A_1=\|G'\|_{op},
\qquad
A_2=\|G''\|_{op}.
\]

The integral representation of the Sylvester inverse gives

\[
\|\mathcal L_H^{-1}\|\le\frac{1}{2\sqrt\gamma}.
\]

Consequently,

\[
\boxed{\|W\|\le\gamma^{-1/2}},
\]

\[
\boxed{\|H'\|\le\frac{A_1}{2\sqrt\gamma}},
\]

\[
\boxed{\|W'\|\le\frac{A_1}{2\gamma^{3/2}}},
\]

and

\[
\boxed{
\|W''\|
\le
\frac{A_2}{2\gamma^{3/2}}
+
\frac{3A_1^2}{4\gamma^{5/2}}.
}
\]

Thus the exact obstruction is visible: whitening jets diverge as the residual Hilbert--Schmidt Gram margin approaches zero. This is a residual-rank wall, not a numerical nuisance.

## 8. Whitened physical measurement jets

### Theorem 4 — Exact physical frame jets

For

\[
\widehat M=MW,
\]

one has

\[
\boxed{
\widehat M'=M'W+MW'
}
\]

and

\[
\boxed{
\widehat M''=M''W+2M'W'+MW''.
}
\]

Therefore primitive interval bounds for

\[
U_i,U_i',U_i'',\qquad
\psi_a,\psi_a',\psi_a'',\qquad
w_a,w_a',w_a''
\]

produce explicit interval bounds for the physical matrix jets. No auxiliary channel-space frame is needed for this step.

## 9. Local frame propagation

Let `theta0` be a certified anchor and put

\[
\sigma_0=\sigma_{\min}(\widehat M(\theta_0))>0.
\]

If

\[
\sup_{|t-\theta_0|\le r}\|\widehat M'(t)\|_{op}\le L_1,
\]

then Weyl's singular-value perturbation inequality gives

\[
\sigma_{\min}(\widehat M(\theta))
\ge
\sigma_0-L_1|\theta-\theta_0|.
\]

Hence every

\[
0<r<\frac{\sigma_0}{L_1}
\]

is a positive local-frame radius and

\[
\boxed{
\alpha_{\mathcal U}(\theta)
\ge
(\sigma_0-L_1r)^2.
}
\]

If a second-jet bound

\[
\sup_{|t-\theta_0|\le r}\|\widehat M''(t)\|_{op}\le L_2
\]

is also available, Taylor's theorem gives

\[
\sigma_{\min}(\widehat M(\theta))
\ge
\sigma_0-L_1|h|-\frac12L_2h^2.
\]

A sufficient positive radius is therefore any `r` satisfying

\[
L_1r+\frac12L_2r^2<\sigma_0.
\]

The maximal threshold predicted by these constants is

\[
\boxed{
r_*=
\frac{-L_1+\sqrt{L_1^2+2L_2\sigma_0}}{L_2}
}
\]

when `L2>0`.

## 10. Basis invariance

Under an invertible differentiable generator change `U -> U A`, both matrix pencils transform by congruence:

\[
M^*M\mapsto A^*M^*MA,
\qquad
G\mapsto A^*GA.
\]

The generalized singular values, and therefore

\[
\alpha_{\mathcal U}=\sigma_{\min}(MG^{-1/2})^2,
\]

are unchanged. The symmetric whitening matrices themselves depend on the chosen generator coordinates, but the frame spectrum and the local positivity statement do not.

## 11. Executable verification

The accompanying script implements all formulas and validates them on a synthetic path with:

- nontrivial unitary rotation of operators and states;
- nonorthogonal, parameter-dependent mixing of residual generators;
- nonconstant positive quadrature weights;
- nonconstant Hilbert--Schmidt whitening.

A five-point finite-difference audit at step `2e-4` produced:

```text
first-jet relative operator error   8.42e-12
second-jet relative operator error  6.44e-7
```

The synthetic anchor had

```text
sigma_min(Mhat)  0.3059778934
alpha            0.09362247125
||Mhat'||        0.05339659477
||Mhat''||       0.02086601817
```

These values verify the implementation only; they are not N15 physical constants.

## 12. Gate consequence

```text
UA01-H5A MEASUREMENT_JET_CALCULUS:       PASS
UA01-H5B PRIMITIVE_N15_JET_BOUNDS:       OPEN
UA01-G1A PHYSICAL_MATRIX_REPRODUCTION:   OPEN
UA01-G2 LOCAL_FRAME:                     BLOCKED
UA01-G3 UNIFORM_FRAME:                   BLOCKED
MODE-5 ANALYTIC UNIQUENESS:              OPEN
P2 HANDOFF:                              BLOCKED
```

The next admissible object is the primitive N15/P3 deformation jet registry. It must derive or certify, on a fixed-support chamber:

1. q-number, q-factorial and q-6j jets;
2. target-component and registered-XY operator jets;
3. support Gram, spectral projector and inverse-square-root jets;
4. `R_bulk` and `W` jets after every normalization;
5. projected-torus coherent-state jets;
6. a positive lower bound for `lambda_min(G_HS)`.

Only those inputs can turn the present calculus into a physical local-frame theorem.

## 13. Claim firewall

This work proves an exact finite-dimensional calculus from supplied primitive jets to the first two jets of the physical whitened measurement matrix. It does not prove that the N15 primitive jets are uniformly bounded, that the N15 support projector is constant over the full deformation interval, that mode 5 is analytically unique, that the RC02 phase lock follows from a frame inequality, or that the deformation parameter is physical time.
