# BC-IDPR P5-UA01 Analytical Contract

## 0. Contract identity

**Contract ID:** `BC-IDPR-P5-UA01`  
**Canonical title:** *A Priori Phase/Frame Lower Bounds from Geometry, Wall Margin, and Coherent-State Design*  
**State:** `OPEN_OBLIGATION_GRAPH`  
**Claim state:** `NO_UNIFORM_THEOREM_CLAIMED`  
**Upstream frozen object:** `BC-IDPR-P3-P1-RC02`  
**Downstream gate:** `P2_GLOBAL_GLUING_CLOSED`

## 1. Mission

The contract asks for a certified inequality chain of the form

\[
(\text{geometry margin},\ \text{wall margin},\ \text{coherent-state design})
\Longrightarrow
\underline c_{\mathrm{fr}}>0
\Longrightarrow
(\underline R_1,\underline R_2,\underline\Delta_E),
\]

where:

- \(\underline c_{\mathrm{fr}}\) is a lower frame bound for the declared residual channel;
- \(\underline R_1,\underline R_2\) are lower bounds for first- and second-harmonic directional concentration after the preregistered phase correction;
- \(\underline\Delta_E\) is a lower bound for predictor-versus-control energy advantage.

The bounds must be explicit functions of declared geometric, wall and design constants. A fitted positive value on the RC02 atlas is not an acceptable substitute.

## 2. Frozen upstream facts and non-import rule

RC02 established outcome `A_UNIVERSAL_PHASE_LOCK` on exactly eight sealed families and 106 ordered carriers with selected mode \(n_*=5\) and matched control \(m_{\mathrm{control}}=9.5\). That outcome is immutable and may be cited as finite-atlas motivation.

RC02 confirmatory observations must not be used to:

- choose a new coherent-state candidate pool;
- change the residual observable;
- change phase predictors, controls or thresholds;
- select a favorable geometric chamber after inspection;
- estimate a constant that is then presented as an a priori bound;
- authorize a second RC02 run.

Any conjecture first noticed in RC02 data remains post hoc until it is proved analytically or tested on a newly sealed external family set.

## 3. Typed mathematical objects

### 3.1 Admissible chamber

Let \(\Theta\) be the typed parameter space for the finite operator family. Define:

- a normalized geometry map \(g:\Theta\to\mathcal G\);
- a representation-scale map \(\rho:\Theta\to\mathcal R\);
- a wall set \(\mathcal W\subset\Theta\);
- a geometric degeneracy set \(\mathcal D_{\mathrm{geom}}\subset\Theta\).

For declared margins \(\mu,\nu>0\), the admissible chamber is

\[
\Theta_{\mu,\nu}
=
\left\{
\theta\in\Theta:
\operatorname{dist}(\theta,\mathcal W)\ge\mu,
\quad
\operatorname{marg}_{\mathrm{geom}}(g(\theta))\ge\nu
\right\}.
\]

The geometry-margin functional must be registered explicitly. It may include Gram-determinant, volume, angle, admissibility-slack or chart-conditioning components, but no component may be added after inspecting a failed bound without a versioned contract amendment.

### 3.2 Residual channel bundle

For each \(\theta\in\Theta_{\mu,\nu}\), let \(V_\theta\) be the declared finite-dimensional residual-channel space, with constant dimension \(d\) on the chamber. A local basis is

\[
\mathcal B(\theta)=\{B_1(\theta),\ldots,B_d(\theta)\}.
\]

Rank change, basis singularity or channel-dimension change is a wall event and invalidates continuation of the same certificate.

### 3.3 Coherent-state design and measurement matrix

Let

\[
\mathcal Z=\{(z_a,w_a)\}_{a=1}^M,
\qquad
w_a\ge0,
\qquad
\sum_{a=1}^M w_a=1,
\]

be a declared coherent-state design. Define measurement vectors

\[
(v_a(\theta))_\alpha
=
\langle z_a(\theta),B_\alpha(\theta)z_a(\theta)\rangle,
\]

and the weighted measurement matrix

\[
M_{a\alpha}(\theta)
=
\sqrt{w_a}\,(v_a(\theta))_\alpha.
\]

Complex lower symbols are permitted. All phase conventions, normalizations and active-support rules must be frozen in the contract registry.

### 3.4 Frame constant

The local frame operator and frame constant are

\[
F(\theta)=M(\theta)^*M(\theta),
\qquad
c_{\mathrm{fr}}(\theta)=\lambda_{\min}(F(\theta))=\sigma_{\min}(M(\theta))^2.
\]

The uniform target is

\[
\underline c_{\mathrm{fr}}(\mu,\nu,\mathcal Z)
=
\inf_{\theta\in\Theta_{\mu,\nu}}c_{\mathrm{fr}}(\theta)>0.
\]

### 3.5 Phase statistics

For each registered family \(F\), let \(S_F(\theta)\in\mathbb C\) be the complex phase statistic produced by the frozen residual protocol, and let \(P_F(\theta)\in\mathbb S^1\) be the preregistered predictor phase. Define the aligned statistic

\[
Z_F(\theta)=\overline{P_F(\theta)}S_F(\theta).
\]

On a declared family class \(\mathfrak F\) with nonnegative normalized weights \(\omega_F\), define

\[
R_1(\theta)
=
\left|\sum_{F\in\mathfrak F}\omega_F
\frac{Z_F(\theta)}{|Z_F(\theta)|}\right|,
\]

\[
R_2(\theta)
=
\left|\sum_{F\in\mathfrak F}\omega_F
\left(\frac{Z_F(\theta)}{|Z_F(\theta)|}\right)^2\right|.
\]

These quantities are undefined when an included \(Z_F\) vanishes. Therefore a positive amplitude floor is a mandatory theorem obligation, not a numerical convenience.

### 3.6 Energy advantage

Let \(\Pi_q\) and \(\Pi_c\) be the frozen predictor and matched-control analysis operators. For residual data \(r_F(\theta)\), define

\[
\Delta_E(F,\theta)
=
\|\Pi_q r_F(\theta)\|^2
-
\|\Pi_c r_F(\theta)\|^2.
\]

The family aggregate and its lower bound must use a preregistered aggregation rule. The RC02 benchmark \(0.02\) may be retained as a fixed external comparison threshold, but it may not be lowered after analysis.

## 4. Deterministic transfer skeleton

The following elementary transfer mechanism is admissible and must be instantiated with certified constants.

### 4.1 Anchor-to-neighborhood frame transfer

At an anchor \(\theta_j\), let

\[
\sigma_j=\sigma_{\min}(M(\theta_j))>0.
\]

If a certified estimate gives

\[
\|M(\theta)-M(\theta_j)\|_2\le\varepsilon_j(\theta)<\sigma_j,
\]

then

\[
c_{\mathrm{fr}}(\theta)
\ge
\bigl(\sigma_j-\varepsilon_j(\theta)\bigr)^2.
\]

A local Lipschitz form

\[
\varepsilon_j(\theta)
\le
L_j(\mu,\nu,\mathcal Z)\,d(\theta,\theta_j)
\]

produces a positive certified radius only when

\[
r_j<\sigma_j/L_j.
\]

### 4.2 Finite-cover uniformization

For a certified cover

\[
\Theta_{\mu,\nu}\subseteq\bigcup_{j=1}^J B(\theta_j,r_j),
\]

one obtains the target bound

\[
\underline c_{\mathrm{fr}}
\ge
\min_{1\le j\le J}
\bigl(\sigma_j-L_jr_j\bigr)^2,
\]

provided every term is strictly positive and every ball remains inside the same typed chamber.

A dense grid without a certified covering radius is not a proof of this statement.

### 4.3 Phase-error transfer

For each family, suppose a reference aligned statistic has the form

\[
Z_F^{(0)}=a_F e^{i\phi_*},
\qquad
a_F\ge a_0>0,
\]

and a certified perturbation estimate gives

\[
|Z_F-Z_F^{(0)}|\le\varepsilon<a_0.
\]

Then the target angular bound is

\[
d_{\mathbb S^1}(\arg Z_F,\phi_*)
\le
\delta
:=
\arcsin(\varepsilon/a_0).
\]

Consequently,

\[
R_1\ge\cos\delta,
\]

and, when \(2\delta\le\pi/2\),

\[
R_2\ge\cos(2\delta).
\]

P5 must supply \(a_0\) and \(\varepsilon\) from operator, geometry, wall and design bounds. Reading them from RC02 confirmatory outputs is forbidden.

### 4.4 Energy-margin transfer

P5 must derive an explicit perturbation inequality

\[
|\Delta_E(F,\theta)-\Delta_E(F,\theta_j)|
\le
C_{\Delta,j}\,d(\theta,\theta_j)
+
C_{\mathrm{protocol},j}\,\varepsilon_{\mathrm{protocol}},
\]

with \(\varepsilon_{\mathrm{protocol}}=0\) for an exactly frozen protocol. A positive uniform result requires

\[
\inf_{F,j}\Delta_E(F,\theta_j)
-
\sup_j C_{\Delta,j}r_j
>0.
\]

The stronger RC02 comparison target requires the left-hand side to be at least \(0.02\).

## 5. Coherent-state design as an extremal problem

For a fixed candidate pool \(z_1,\ldots,z_M\) at an anchor, define

\[
G(w)=\sum_{a=1}^M w_a v_av_a^*.
\]

The primary design problem is the E-optimal semidefinite program

\[
\begin{aligned}
\text{maximize}\quad & t\\
\text{subject to}\quad
& G(w)\succeq tI_d,\\
& w_a\ge0,\\
& \sum_a w_a=1.
\end{aligned}
\]

Its value is the best lower frame constant available from the frozen candidate pool. The corresponding minimax dual form is

\[
\min_{Y\succeq0,\ \operatorname{tr}Y=1}
\max_a v_a^*Yv_a.
\]

A valid design certificate must include:

- primal weights \(w_*\);
- the achieved \(t_*\);
- a dual witness \(Y_*\);
- primal and dual residuals;
- the support/contact set where \(v_a^*Y_*v_a=t_*\) within certified tolerance;
- a KKT or equivalent optimality certificate;
- a rank and conditioning audit.

This stage explicitly tests whether the frame strength is governed by an extremal Gram/KKT structure rather than by accidental sampling.

Choosing the candidate coherent states themselves is a separate, potentially nonconvex problem. Any adaptive candidate-pool search must be isolated from confirmatory evidence and followed by an independent sealed validation or an exact proof.

## 6. Geometry and wall obligations

P5 must produce explicit constants controlling all sources of variation in \(M(\theta)\):

1. variation of the residual basis \(B_\alpha(\theta)\);
2. variation of coherent states \(z_a(\theta)\);
3. variation of normalization factors;
4. spectral-projector or branch selection;
5. phase-statistic extraction;
6. representation and label dependence within the declared class.

The wall registry must include at least:

- spectral degeneracy or gap closure;
- rank change of \(V_\theta\);
- admissibility-boundary contact;
- singular basis or chart transition;
- vanishing phase statistic;
- branch-cut ambiguity not removed by a registered gauge;
- coherent-state design rank loss.

Existing recursive jet calculus may be used to bound derivatives, but P5 must expose the dependence of every bound on \(\mu\), \(\nu\), level, labels and design conditioning. An unspecified constant \(C\) is not sufficient for the P2 handoff.

## 7. Typed holes

| Hole ID | Required output | Acceptable witness | Primary falsifier |
|---|---|---|---|
| `UA01-H0-GEOMETRY-MARGIN` | Registered \(\operatorname{marg}_{\mathrm{geom}}\) and nonempty \(\Theta_{\mu,\nu}\) | exact inequalities or interval certificate | admissible chamber empty |
| `UA01-H1-WALL-REGISTRY` | Complete wall set and computable distance lower bound | symbolic discriminants, gap estimates, interval exclusion | unregistered rank/branch event |
| `UA01-H2-RESIDUAL-BUNDLE` | Constant-rank bundle and conditioned basis | exact rank proof or certified singular values | rank change or basis blow-up |
| `UA01-H3-MEASUREMENT-MATRIX` | Reproducible \(M(\theta)\) with phase conventions | exact formula plus independent evaluator | evaluator disagreement |
| `UA01-H4-E-OPTIMAL-DESIGN` | Positive \(t_*\) and primal-dual certificate | SDP/KKT certificate with residual bounds | \(t_*=0\) or dual gap unresolved |
| `UA01-H5-JET-TO-LIPSCHITZ` | Explicit \(L_j(\mu,\nu,\mathcal Z)\) | analytic derivative bound or interval enclosure | constant diverges in chamber |
| `UA01-H6-UNIFORM-COVER` | Certified finite cover and positive frame bound | interval subdivision with covering proof | uncovered region or zero radius |
| `UA01-H7-PHASE-AMPLITUDE` | Uniform \(a_0>0\) | analytic lower bound or certified interval minimum | statistic crosses zero |
| `UA01-H8-PHASE-TRANSFER` | Explicit \(\underline R_1,\underline R_2\) | angular perturbation proof | phase branch nonunique |
| `UA01-H9-ENERGY-TRANSFER` | Explicit \(\underline\Delta_E\) | quadratic-form perturbation bound | lower margin nonpositive |
| `UA01-H10-EXTERNAL-CHECK` | Independent non-tuning validation | newly sealed families or exact exhaustive finite class | only RC02 reuse available |
| `UA01-H11-P2-HANDOFF` | Positive gluing-ready local constants with compatibility metadata | completed handoff contract | global bound still size- or sector-undefined |

## 8. Evidence classes

Evidence must be labeled as one of:

- `EXACT_SYMBOLIC`;
- `EXACT_FINITE_ENUMERATION`;
- `CERTIFIED_INTERVAL`;
- `CERTIFIED_FLOATING_POINT`;
- `SEALED_EXTERNAL_VALIDATION`;
- `POST_HOC_DIAGNOSTIC`;
- `HEURISTIC_ONLY`.

Only the first five classes may close a P5 gate. Certified floating-point evidence must include precision, residuals, condition estimates and an independent evaluator where feasible.

## 9. Outcome map

### `P5_A_UNIFORM_PHASE_FRAME_BOUND`

All mandatory holes close; \(\underline c_{\mathrm{fr}}>0\), the phase statistic has a positive amplitude floor, and explicit positive phase and energy margins hold on the declared chamber or family class.

### `P5_B_LOCAL_BOUND_ONLY`

Positive bounds are proved only on certified neighborhoods or a finite subcover that does not cover the full target class. P2 remains closed outside those neighborhoods.

### `P5_C_NUMERICAL_CERTIFICATE_ONLY`

Finite anchor certificates are strong, but jet, covering or amplitude-floor obligations remain open. No uniform theorem and no P2 promotion.

### `P5_D_ANALYTICAL_OBSTRUCTION`

A required constant vanishes, a wall cannot be excluded, the design is rank deficient, or uniformity fails. The negative result must be retained as a programme theorem/obstruction rather than bypassed by retuning.

## 10. Gate criteria

`UA01-G1 DESIGN` passes only if `H2`--`H4` close with \(t_*>0\).

`UA01-G2 LOCAL FRAME` passes only if `H5` produces a positive certified radius around at least one anchor.

`UA01-G3 UNIFORM FRAME` passes only if `H6` covers the declared target domain and yields \(\underline c_{\mathrm{fr}}>0\).

`UA01-G4 PHASE` passes only if `H7`--`H9` produce explicit positive lower bounds. For direct comparison with RC02, the stronger benchmark is \(\underline R_1\ge0.60\) and \(\underline\Delta_E\ge0.02\).

`UA01-G5 EXTERNAL` passes only if `H10` uses evidence independent of RC02 confirmatory tuning.

`UA01-G6 P2 HANDOFF` passes only if `H11` and `P2_HANDOFF_CONTRACT.md` close. Passing `G3` alone does not open P2.

## 11. Claim firewall

Even outcome `P5_A_UNIFORM_PHASE_FRAME_BOUND` is restricted to the declared finite operator class, chamber, residual bundle, predictor/control pair and coherent-state design.

The contract does not establish:

- arbitrary \(k\) or arbitrary labels;
- a full `SU(2)_k` category theorem;
- pentagon, braiding or modular coherence;
- manifold-level gluing;
- continuum or large-label asymptotics;
- physical time, oscillation, dynamics, mass, matter or gravity.

No statement from the Gemini advisory report is used as evidence.

## 12. Immediate execution order

1. Freeze the geometry-margin and wall registries.
2. Build \(M(\theta)\) at one exact reference family with independent evaluation.
3. Solve the fixed-pool E-optimal design SDP and extract the primal-dual/KKT certificate.
4. Derive first derivative and basis-conditioning bounds from the existing jet apparatus.
5. Compute the first certified positive neighborhood radius.
6. Only then decide whether finite-cover uniformization is feasible.
