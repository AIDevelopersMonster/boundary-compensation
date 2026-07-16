# BC-IDPR P3→P1 Research Contract 01

## Phase-Resolved Residual Modulation on the Certified Finite Quantum-6j Atlas

**Contract ID:** `BC-IDPR-P3-P1-RC01`  
**Version:** `v0.1.0`  
**Date:** 2026-07-16  
**Status:** `PREREGISTRATION_FROZEN_AWAITING_PILOT`  

## 1. Research question

For the fixed 283-carrier finite quantum-6j universe, do deformation-dependent residuals contain a transferable phase component aligned with integer q-harmonic modes after removal of a frozen cubic smooth envelope, and does that alignment outperform matched half-integer control modes on previously unused external-label families?

The contract tests phase locking. It does not assume that a positive result is physical, geometric or asymptotic.

## 2. Upstream frozen universe

The carrier universe is exactly the one published with DOI `10.5281/zenodo.21401141`:

- 283 ordered carriers;
- 24 unordered family keys;
- family key equal to the sorted external-label quadruple;
- q-number indices no larger than ten;
- first positive q-number wall for the declared index range at `theta = pi/10`.

The carrier supplement is pinned by Git blob SHA `6485ceb3a4f34ee771d38ddf8f63a59d43b2608b` and SHA-256 `a8bcfb1038a288df29e4c76e4ef7ac8d711516df9d42c5da29e7f01a4fe79eb1`.

No carrier may be added, deleted or reclassified during RC01.

## 3. Deformation coordinate and frozen grids

Define

\[
\eta=\frac{12\theta}{\pi},\qquad
q(\eta)=\exp\!\left(\frac{i\pi\eta}{12}\right),\qquad
\eta_0=1.
\]

Two grids are frozen.

### 3.1 Broad phase grid

\[
\mathcal G_{\mathrm{phase}}
 = \{0.60+0.0005j: j=0,\ldots,1100\}.
\]

Thus `eta in [0.60,1.15]`, with 1101 points. The first declared q-number wall is at `eta = 1.20`, leaving a frozen upper wall margin of `0.05`.

The broad grid is used only for real-axis matrix, signed-speed and anchored complex-phase observables. The published Arb theorem does not certify zero-freeness of `omega` on the full broad interval.

### 3.2 Certified local grid

\[
\mathcal G_{\mathrm{cert}}
 = \{0.99+0.00005j: j=0,\ldots,400\}.
\]

Thus `eta in [0.99,1.01]`, with 401 points. This grid lies in the published common zero-free disk and is the only grid on which logarithmic-speed observables may contribute to a theorem-compatible local statement.

## 4. Frozen observables

For each ordered carrier `J`, let `F_J(eta)` be the two-channel recoupling matrix and

\[
K_J=\frac{\mathrm dF_J}{\mathrm d\theta}F_J^T,
\qquad
\omega_J=(K_J)_{21}.
\]

### 4.1 Primary complex observable

Let

\[
z_J(\eta)=F_{11,J}(\eta)+iF_{21,J}(\eta),
\qquad
Z_J(\eta)=\frac{z_J(\eta)}{z_J(1)}.
\]

Before forming the ratio, each column is normalized if its Euclidean norm differs from one by more than `1e-13`. If the deviation exceeds `1e-10`, the carrier fails the orthogonality gate.

The ratio removes an anchor-constant column sign and fixes `Z_J(1)=1`.

### 4.2 Signed-speed replication observable

Let

\[
s_J=\operatorname{sgn}\omega_J(1),
\qquad
Y_J^{\omega}(\eta)=s_J\omega_J(\eta).
\]

If `omega_J(1)=0` numerically or its sign is not reproducible at 192 and 256 bits, the carrier enters `ANCHOR_SPEED_SIGN_FAILURE`.

### 4.3 Certified-local secondary observables

On `G_cert` only:

\[
\partial_\theta\log|\omega_J|,
\qquad
\partial_\theta^2\log|\omega_J|.
\]

These are secondary consistency observables and cannot rescue a failed primary phase test.

## 5. Frozen smooth-envelope removal

On the broad phase grid, map `eta` affinely to `x in [-1,1]`. Let

\[
\mathcal B_3=\operatorname{span}\{1,x,x^2,x^3\}.
\]

For a scalar or complex curve `y`, define the residual

\[
r=(I-P_{\mathcal B_3})y,
\]

where `P_B3` is the unweighted discrete least-squares projector on all 1101 grid points. Complex curves are projected using the standard Hermitian inner product.

No polynomial degree, weighting rule or robust-loss replacement may be chosen after pilot freeze.

A carrier is marked `DEGENERATE_RESIDUAL` if

\[
\|r\|_2/\max(\|y\|_2,10^{-300})<10^{-12}.
\]

Degenerate carriers are reported and excluded from phase-angle aggregation. They are not silently assigned zero effect.

## 6. Frozen phase and control dictionaries

For `n=2,...,10`, define the integer q mode

\[
u_n(\eta)=\exp\!\left(i n\theta(\eta)\right),
\qquad \theta(\eta)=\pi\eta/12,
\]

and the matched half-integer control

\[
v_n(\eta)=\exp\!\left(i(n+1/2)\theta(\eta)\right).
\]

Each mode is orthogonalized against `B3` and normalized. For each nondegenerate carrier residual, compute normalized q-mode and control-mode correlations, their squared energies, and the energy advantage `Delta_J,n`.

Integer frequencies are the preregistered q-phase predictors. Half-integer frequencies are matched non-q controls. No additional frequency may enter the primary analysis.

## 7. Family aggregation and independence unit

Ordered carriers are not treated as independent observations. The independence unit is the unordered family.

For each family and mode, the energy statistic is the median of `Delta_J,n` over all nondegenerate ordered carriers in that family.

The family phase is the amplitude-weighted circular mean of q-mode correlation phases over its ordered carriers. The primary directional concentration is `R1 = |mean(exp(i phi_f))|`; the axial diagnostic is `R2 = |mean(exp(2 i phi_f))|`.

`R2` may support a phase-class result but cannot by itself establish universal directional phase locking.

## 8. Frozen family-disjoint stages

The 24 families are partitioned into:

- 4 pilot families;
- 12 calibration families;
- 8 confirmatory families.

The exact keys and deterministic SHA-256 derivation are recorded in `FROZEN_FAMILY_SPLIT.json`.

### Pilot

Pilot families may be used only to debug data layout, matrix orientation, precision, failure reporting and deterministic execution. Pilot results cannot select the primary frequency or alter thresholds.

### Calibration

After pilot freeze, calibration families select one integer mode `n_star` using the primary complex observable only:

1. compute the median family energy advantage for every `n=2,...,10`;
2. select the largest median;
3. ties within `1e-12` are resolved in favor of the smallest `n`;
4. write `CALIBRATION_FREEZE_CERTIFICATE.json` containing `n_star`, hashes, software versions and calibration summaries;
5. commit that certificate before any confirmatory observable is computed.

### Confirmatory

Only the frozen `n_star` is tested on the eight confirmatory families. No frequency reselection is permitted.

## 9. Primary confirmatory criterion

A universal phase-resolved modulation result requires all of the following on the primary complex observable:

1. at least seven of eight confirmatory families have positive family-level energy advantage;
2. the median confirmatory family advantage is at least `0.02`;
3. the exact one-sided family sign test is at most `9/256 = 0.03515625`;
4. directional phase concentration satisfies `R1 >= 0.60`;
5. no hard failure state is triggered.

The signed-speed observable is a preregistered replication endpoint. It is reported with the same frozen mode but is not required to pass for the primary complex-phase claim.

## 10. Outcome classes

- `A_UNIVERSAL_PHASE_LOCK`: all primary criteria pass.
- `B_PHASE_CLASSES`: energy criteria pass, `R1 < 0.60`, and `R2 >= 0.75`; only an axial or multi-class phase structure may be claimed.
- `C_PHASE_HYPOTHESIS_REJECTED`: the energy criteria fail without a hard integrity failure.
- `D_INCONCLUSIVE`: integrity, degeneracy, contamination or reproducibility gates prevent a valid decision.

The detailed logic is frozen in `OUTCOME_DECISION_TABLE.md`.

## 11. Failure states

Hard failure states are:

- `CARRIER_UNIVERSE_MISMATCH`;
- `FAMILY_SPLIT_MISMATCH`;
- `WALL_MARGIN_VIOLATION`;
- `ORTHOGONALITY_GATE_FAILURE` affecting more than 1% of ordered carriers;
- `ANCHOR_SPEED_SIGN_FAILURE` on any primary-scored carrier;
- `DEGENERATE_RESIDUAL_FAMILY_EXCESS` affecting more than two confirmatory families;
- `CONFIRMATORY_CONTAMINATION`;
- `PIPELINE_HASH_DRIFT`;
- `NUMERICAL_NONREPRODUCIBILITY`.

Hard failure produces outcome `D_INCONCLUSIVE`; it is not evidence against phase modulation.

## 12. Claim firewall

Even outcome A would establish only a finite-class, deformation-coordinate, model-comparison result. It would not establish physical oscillations, time dynamics, mass or matter, curvature or gravity, global gluing, a continuum exponent, or universality outside the declared carrier class and eta interval.

## 13. Change control

Any scientific change after this preregistration commit requires a new major preregistration version before calibration begins. After calibration freeze, changes to observables, grids, predictors, split, selection rule, primary thresholds or outcome logic invalidate RC01 and require a new contract identifier.

No statement from the Gemini advisory report is used as evidence.
