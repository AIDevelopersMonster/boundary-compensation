# BC-IDPR P5-UA01 WP0 — Chamber and Wall Registry

**Contract:** `BC-IDPR-P5-UA01-WP0`  
**Status:** `Q_WALL_AND_REAL_BRANCH_CHAMBER_CERTIFIED / FULL_WALL_REGISTRY_OPEN`  
**Upstream class:** finite algebraic two-channel carrier class `A6`  
**Frozen deformation coordinate:**

\[
\eta=\frac{12\theta}{\pi},\qquad \theta_0=\frac{\pi}{12},\qquad \eta_0=1.
\]

## 1. Purpose

WP0 fixes the target chamber before any frame optimization. It distinguishes:

1. the full frozen RC02 protocol interval;
2. an inherited outer q-wall-safe chamber;
3. an inherited local chamber on which carrier angular speed is already rigorously separated from zero.

No RC02 response value, selected mode, control pairing, or confirmatory advantage is used to choose these chambers.

## 2. Declared finite class

The upstream finite q-6j calculus supplies the exact class `A6`:

- 283 ordered two-channel carriers;
- 24 unordered external-label families;
- every q-index occurring in triangle factors, Racah numerators and denominators, and dimension amplitudes lies in
  \(\{1,\ldots,10\}\).

Hence the q-number wall set relevant to the whole class is

\[
\mathcal W_q
=
\left\{\eta=\frac{12\ell}{n}:n\in\{1,\ldots,10\},\ \ell\in\mathbb Z\right\}.
\]

## 3. Full frozen protocol chamber

The target interval inherited from RC02 is

\[
\Theta_{\mathrm{RC02}}
=
\left[\frac35,\frac{23}{20}\right]
=[0.60,1.15]
\]

in eta coordinates, equivalently

\[
\theta\in
\left[\frac{\pi}{20},\frac{23\pi}{240}\right].
\]

The nearest relevant q-number wall is

\[
\eta=\frac65=1.2,
\]

coming from \(n=10\), \(\ell=1\). Therefore the exact q-wall margin of the full protocol chamber is

\[
\boxed{
\mu_q^{\mathrm{RC02}}
=
\frac1{20}
}
\]

in eta coordinates, or

\[
\boxed{
\operatorname{dist}_\theta(\Theta_{\mathrm{RC02}},\mathcal W_q)
=
\frac{\pi}{240}
}.
\]

For every \(1\le n\le10\) and every \(\theta\in\Theta_{\mathrm{RC02}}\),

\[
0<n\theta
\le
10\frac{23\pi}{240}
=
\frac{23\pi}{24}
<\pi.
\]

Thus

\[
[n]_q=\frac{\sin(n\theta)}{\sin\theta}>0
\]

throughout the full real protocol chamber. Consequently every q-factorial used by `A6` remains positive, and the anchor-selected real square-root branches of all triangle and dimension radicands continue without a q-number or sign wall on this interval.

This closes the q-wall and real branch part of WP0. It does **not** certify all phase, rank, or measurement walls.

## 4. Nested chambers

### 4.1 Inherited local nonvanishing chamber

The rigorous Arb conditioning certificate gives

\[
\Theta_{\mathrm{loc}}
=[0.99,1.01],
\qquad
|\theta-\theta_0|\le\frac{\pi}{1200},
\]

and, uniformly over all 283 ordered carriers,

\[
\boxed{
|\omega_J(\theta)|
\ge
0.16025264148217666
}.
\]

This is the first admissible local chamber for the operator-adapted frame construction. It is inherited, not selected from RC02 outcomes.

### 4.2 Inherited outer q-safe chamber

The upstream outer analytic disk corresponds to

\[
\Theta_{\mathrm{out}}=[0.9,1.1],
\qquad
|\theta-\theta_0|\le\frac{\pi}{120}.
\]

It is q-wall and branch safe. Uniform nonvanishing of every carrier angular speed on the whole outer chamber is not inherited and remains an explicit P5 obligation.

### 4.3 Full target chamber

\[
\Theta_{\mathrm{loc}}
\subset
\Theta_{\mathrm{out}}
\subset
\Theta_{\mathrm{RC02}}.
\]

The programme route is therefore:

\[
\text{local exact frame theorem}
\longrightarrow
\text{certified enlargement}
\longrightarrow
\text{finite cover of }\Theta_{\mathrm{RC02}}.
\]

A dense grid alone is not accepted as the enlargement proof.

## 5. Wall taxonomy

| Wall family | Definition | Current status |
|---|---|---|
| q-number wall | some critical \([n]_q=0\), \(1\le n\le10\) | excluded on full RC02 chamber with margin \(1/20\) in eta |
| real branch wall | q-factorial or square-root radicand changes sign or vanishes | excluded on full RC02 chamber by strict q-number positivity |
| angular-speed wall | \(\omega_J(\theta)=0\) for some carrier | excluded only on \([0.99,1.01]\); open outside |
| residual-rank wall | declared residual channel changes dimension | open; must be tied to the operator-adapted basis map |
| measurement-frame wall | coherent-probe matrix loses column rank | reduced by WP1/WP2 to a basis-conditioning condition |
| phase-gauge wall | registered anchor component or aligned statistic vanishes | open for WP6; no continuation through the wall |
| chart/gauge wall | frozen signed gauge ceases to define the same analytic branch | excluded locally; extension requires an explicit reset certificate |

## 6. Registered geometry margin

For the real two-channel residual space, use the Hilbert--Schmidt orthonormal canonical basis

\[
E_1=\frac{\sigma_z}{\sqrt2},
\qquad
E_2=\frac{\sigma_x}{\sqrt2}
\]

of \(\operatorname{Sym}_0(2,\mathbb R)\). Let the operator-adapted residual basis for carrier \(J\) be

\[
B_{J,\alpha}(\eta)
=
\sum_{\beta=1}^2
E_\beta\,C_J(\eta)_{\beta\alpha}.
\]

The registered geometry/basis margin is

\[
\boxed{
\nu_J(\eta)=\sigma_{\min}(C_J(\eta))
}
\]

and for a declared finite carrier class

\[
\boxed{
\nu_{\mathfrak A_6}(\Theta)
=
\inf_{J\in\mathfrak A_6}
\inf_{\eta\in\Theta}
\sigma_{\min}(C_J(\eta)).
}
\]

This choice is invariant under orthogonal changes of the canonical residual coordinates and is directly connected to the exact frame lower bound proved in WP1/WP2. The rank wall is precisely \(\nu_J=0\).

No classical volume, spacetime metric, or physical geometric interpretation is imported.

## 7. Gate decision

Closed:

- target deformation coordinate and full protocol interval;
- exact critical q-index set;
- exact q-wall margin on the full protocol interval;
- positivity and real-branch continuation for every q-factorial and square-root radicand used by `A6`;
- inherited local angular-speed nonvanishing chamber;
- canonical basis-conditioning margin functional.

Open:

- construction of every operator-adapted map \(C_J(\eta)\);
- a positive lower bound for \(\nu_{\mathfrak A_6}\) on the local chamber;
- angular-speed and rank certification beyond the inherited local chamber;
- certified finite cover of the full RC02 interval.

```text
WP0_Q_WALL: CLOSED
WP0_REAL_BRANCH: CLOSED
WP0_LOCAL_OMEGA_WALL: CLOSED_ON_ETA_0.99_1.01
WP0_RESIDUAL_RANK: OPEN
WP0_FULL_CHAMBER: OPEN
P2_GLOBAL_GLUING: BLOCKED
```

## 8. Immediate handoff

The next calculation is not another predictor-mode comparison. It is the carrier-wise construction of \(C_J(\eta)\), followed by certification of

\[
\inf_{J\in\mathfrak A_6}
\inf_{\eta\in[0.99,1.01]}
\sigma_{\min}(C_J(\eta))>0.
\]

The exact two-channel coherent-probe theorem converts that single positive margin into a frame lower bound without fitting an empirical prefactor.
