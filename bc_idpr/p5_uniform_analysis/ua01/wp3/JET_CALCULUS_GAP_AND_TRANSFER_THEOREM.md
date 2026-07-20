# BC-IDPR P5-UA01 WP3 — Jet Calculus Gap, q-Factorial Curvature Closure, and Phase/Frame Nonimplication

**Contract:** `BC-IDPR-P5-UA01-WP3-JET-GAP`  
**Status:** `EXACT_NONIMPLICATIONS_CLOSED / Q_FACTORIAL_JET_CLOSURE_CLOSED / MODE5_UNIQUENESS_OPEN / PHYSICAL_JET_TRANSFER_OPEN`  
**Scope:** the declared finite q-Racah operator class, the frozen cubic residualization protocol, and the distinction between static frame observability and phase-resolved q-curvature response.

## 1. Three different mathematical objects

The following must not be conflated.

1. **Static residual frame**
   \[
   \alpha(\theta)=\sigma_{\min}(\widehat M(\theta))^2.
   \]
   It controls stable reconstruction of a residual coefficient vector from the lower-symbol measurements at fixed \(\theta\).

2. **Jet regularity**
   \[
   \|\partial_\theta^r\widehat M(\theta)\|,
   \qquad r=1,2,\ldots .
   \]
   It controls how the frame and residual coordinates vary under deformation.

3. **RC02 phase response**
   \[
   c_{J,m}=\frac{\langle r_J,\psi_m\rangle}{\|r_J\|},
   \qquad
   \psi_m=\frac{(I-P_3)\Phi_m}{\|(I-P_3)\Phi_m\|},
   \]
   where
   \[
   \Phi_m(\theta)=\partial_\theta^2\log[m]_q
   =-m^2\csc^2(m\theta)+\csc^2\theta.
   \]
   This is a global projection over the frozen deformation interval after cubic residualization.

A positive lower bound on the first object does not, by itself, bound the second or select a mode in the third.

## 2. Exact jet-gap counterexample

### Proposition 1 — Static frame positivity does not control derivatives

For any \(0<\alpha<1\), define
\[
D_\alpha=\operatorname{diag}(1,\sqrt\alpha),
\qquad
M_\omega(\theta)=R(\varepsilon\sin\omega\theta)D_\alpha,
\]
where \(R(\varphi)\) is a planar rotation.

Then for every \(\theta\) and every \(\omega\),
\[
\sigma_{\min}(M_\omega(\theta))^2=\alpha.
\]
Nevertheless, at \(\theta_\omega=\pi/(2\omega)\),
\[
\|M_\omega''(\theta_\omega)\|_{op}
\ge \varepsilon\omega^2\sqrt\alpha,
\]
and in the declared implementation the norm grows as \(\varepsilon\omega^2\).

Hence no inequality of the form
\[
\sup_\theta\|M''(\theta)\|
\le C(\inf_\theta\sigma_{\min}(M(\theta)))
\]
can hold without additional regularity hypotheses.

**Consequence.** The auxiliary q-Racah mixing floor near \(0.015\) is a denominator/noncollapse statement only. It cannot close `UA01-H5-JET-TO-LIPSCHITZ` and cannot by itself transfer RC02 curvature response.

## 3. Exact phase/frame nonimplication

### Proposition 2 — A frame constant does not determine phase concentration

Fix any \(\alpha>0\). The same static frame matrix can be assigned family phases
\[
\phi_f=0,
\]
which gives \(R_1=1\), or the uniformly spaced phases
\[
\phi_f=2\pi f/8,
\]
which give \(R_1=0\), or the bimodal set \(0,\pi,0,\pi,\ldots\), which also gives \(R_1=0\).

Therefore no positive function \(g\) can satisfy
\[
R_1\ge g(\alpha)
\]
from the frame constant alone.

**Consequence.** The value \(0.015\) is not a weak physical spring constant. It is an inverse-problem conditioning floor in a normalized auxiliary residual space. It neither predicts nor contradicts the frozen RC02 value \(R_1\approx0.9967285\).

## 4. Exact q-factorial jet closure

Define
\[
[n]_\theta=\frac{\sin(n\theta)}{\sin\theta},
\qquad
\Psi_n(\theta)=\partial_\theta\log[n]_\theta
=n\cot(n\theta)-\cot\theta,
\]
\[
\Phi_n(\theta)=\partial_\theta^2\log[n]_\theta
=-n^2\csc^2(n\theta)+\csc^2\theta.
\]

### Theorem 3 — Monomial closure

Let
\[
T(\theta)=C\prod_{n=1}^{N}[n]_\theta^{\gamma_n}
\]
be nonzero on a chamber. Then
\[
\partial_\theta\log T
=\sum_n\gamma_n\Psi_n,
\qquad
\partial_\theta^2\log T
=\sum_n\gamma_n\Phi_n.
\]

Thus every single q-factorial monomial has exact second logarithmic derivative in the finite integer dictionary \(\{\Phi_n\}_{n\le N}\).

### Theorem 4 — Signed finite-sum closure

Let
\[
F(\theta)=\sum_{z=1}^{Z}T_z(\theta),
\qquad F(\theta)\ne0,
\]
where each \(T_z\) is a signed q-factorial monomial. Put
\[
w_z=\frac{T_z}{F},
\quad
\lambda_z=\partial_\theta\log T_z,
\quad
\kappa_z=\partial_\theta^2\log T_z.
\]
Then \(\sum_z w_z=1\) and
\[
\boxed{
\partial_\theta^2\log F
=
\sum_z w_z\kappa_z
+
\sum_z w_z\lambda_z^2
-
\left(\sum_z w_z\lambda_z\right)^2.
}
\]

The first term is a signed, state-dependent mixture of integer q-curvature atoms. The second and third terms form a signed covariance correction. For q-Racah sums, this identity gives the exact algebraic source of the curvature dictionary but does not force one universal mode.

## 5. What this says about mode 5

The mode \(m=5\) does not appear in the static frame inequality because it belongs to a different layer of the problem.

- The static q-Racah frame asks whether two operator directions collapse.
- The RC02 mode comparison asks how the cubic-residualized response projects onto \(\psi_m\).
- The exact q-factorial identity shows why integer atoms are structurally natural.
- The effective weights \(w_z\), exponents \(\gamma_{zn}\), covariance terms, normalization derivatives, and cubic projection determine which mode dominates.

The calibration result that mode 5 exceeded mode 3 by approximately \(0.114124\) is an empirical finite-atlas selection result, not yet an analytic uniqueness theorem.

A valid mode-5 theorem must control, without using confirmatory data for tuning,
\[
\Delta_{5,m}
=
\operatorname{median}_J
\left(
|\langle \widehat r_J,\psi_5\rangle|^2
-
|\langle \widehat r_J,\psi_m\rangle|^2
\right)
\]
for all competing integer modes and the frozen half-integer control, or prove a stronger cone-separation statement for the residualized curvature coefficients.

## 6. Interpretation of the observed phase lock

For the frozen confirmatory value
\[
R_1=0.9967284980027259,
\]
the circular variance is
\[
1-R_1\approx0.003271502.
\]
The small-angle equivalent RMS spread is approximately
\[
\sqrt{2(1-R_1)}\approx0.08089\text{ rad}\approx4.63^\circ.
\]
A rigorous wrapped-RMS upper bound from
\[
\phi^2\le \frac{\pi^2}{2}(1-\cos\phi),
\qquad |\phi|\le\pi,
\]
is approximately
\[
0.12706\text{ rad}\approx7.28^\circ.
\]

This concentration is a property of the normalized complex coefficients across the eight frozen families. It is compatible with a small worst-case static frame constant because amplitude conditioning and cross-family phase alignment are logically independent quantities.

## 7. Correct next obligation

The next admissible analytical object is not another static mixing bound. It is the physical residual jet bundle
\[
\theta\longmapsto
\bigl(R_{\rm bulk}(\theta),W(\theta),\psi_a(\theta),w_a(\theta)\bigr)
\]
and its HS-whitened measurement matrix \(\widehat M_{\rm N15}(\theta)\).

Required outputs:

1. exact first- and second-derivative formulas for q-numbers, q-factorials, q-6j entries, normalization maps, projectors, residual generators, and coherent-state lower symbols;
2. wall-conditioned interval bounds for \(\widehat M'\) and \(\widehat M''\);
3. a perturbation bound for the whitening map \(G_{\rm HS}^{-1/2}\);
4. an explicit cubic-residualized curvature coefficient map into the RC02 atoms;
5. a mode-separation or obstruction certificate.

Until those outputs exist:

```text
STATIC AUXILIARY FRAME: CERTIFIED
PHYSICAL N15 FRAME: OPEN
JET-TO-LIPSCHITZ: OPEN
MODE-5 ANALYTIC UNIQUENESS: OPEN
PHASE/ENERGY TRANSFER: OPEN
P2 HANDOFF: BLOCKED
```

## 8. Claim firewall

This document proves exact nonimplication statements and exact q-factorial jet identities. It does not prove that mode 5 is universally unique, that the auxiliary frame constant causes the RC02 phase lock, that the deformation parameter is physical time, or that any dynamical spring or resonance has been identified.