# BC-IDPR P5-UA01 to P2 Global Gluing Handoff Contract

## 0. Gate state

**Gate ID:** `BC-IDPR-P5-UA01-G6-P2-HANDOFF`  
**Current state:** `CLOSED`  
**Reason:** no a priori local uniform bound and no certified compatibility-map lower singular value have yet been supplied.

P2 global gluing may begin only after this document is closed by explicit certificates. A strong RC02 phase result or a positive local frame constant alone is insufficient.

## 1. Declared finite gluing class

A P2 candidate must declare a finite combinatorial gluing object \(\mathcal K\), including:

- cells or local operator sites \(v\in V(\mathcal K)\);
- interfaces \(e\in E(\mathcal K)\);
- local residual spaces \(V_v\);
- interface/sector spaces \(W_e\);
- orientation and phase-gauge conventions;
- maximum size, degree or another explicit complexity parameter;
- the exact class over which a global lower bound is claimed.

No statement may silently pass from a fixed finite \(\mathcal K\) to arbitrary complexes or a continuum family.

## 2. Local analysis operators

For every site \(v\), P5 must provide an analysis operator

\[
A_v:V_v\to Y_v
\]

with certified lower frame bound

\[
\|A_vx_v\|^2\ge c_v\|x_v\|^2,
\qquad
c_v\ge\underline c_{\mathrm{loc}}>0.
\]

The certificate must carry:

- chamber and wall margins;
- level/label range;
- residual-basis convention;
- coherent-state design and weights;
- normalization;
- phase-gauge convention;
- evidence class and numerical precision if applicable.

Local constants from incompatible conventions may not be combined by taking their minimum.

## 3. Compatibility space and assembly map

Define the global compatible residual space

\[
V_{\mathrm{comp}}(\mathcal K)
\subseteq
\prod_{v\in V(\mathcal K)}V_v
\]

by explicit interface equations. Let

\[
J_{\mathcal K}:V_{\mathrm{comp}}(\mathcal K)
\longrightarrow
\bigoplus_{v\in V(\mathcal K)}V_v
\]

be the registered assembly/restriction map that sends a global compatible mode to its local components.

P2 eligibility requires a certified injectivity estimate

\[
\|J_{\mathcal K}x\|
\ge
\gamma_{\mathcal K}\|x\|,
\qquad
\gamma_{\mathcal K}>0.
\]

The constant \(\gamma_{\mathcal K}\) must be derived from interface maps, sector compatibility and the declared norm. It may depend on the finite size/shape parameters of \(\mathcal K\), but that dependence must be explicit.

A list of positive edge singular values is not automatically a proof that \(\gamma_{\mathcal K}>0\); cycle constraints, redundant equations and global gauge modes must be audited.

## 4. Basic global lower-bound skeleton

Let

\[
A_{\oplus}=\bigoplus_{v}A_v.
\]

On the exact compatible space, define

\[
A_{\mathrm{glob}}=A_{\oplus}J_{\mathcal K}.
\]

If the local and assembly estimates are certified, then the candidate global bound is

\[
\|A_{\mathrm{glob}}x\|^2
\ge
\underline c_{\mathrm{loc}}\,\gamma_{\mathcal K}^2\|x\|^2.
\]

Thus

\[
c_{\mathrm{glob}}(\mathcal K)
\ge
\underline c_{\mathrm{loc}}\,\gamma_{\mathcal K}^2>0.
\]

This inequality is the preferred handoff form because it isolates local observability from global compatibility. It does not assume a product of edge constants, and it exposes any size dependence through \(\gamma_{\mathcal K}\).

## 5. Sector and projector leakage

When compatibility is imposed through projectors or approximate sector maps, define:

- the ideal compatible projector \(Q_{\mathrm{comp}}\);
- the implemented projector or restriction \(\widetilde Q_{\mathrm{comp}}\);
- sector leakage \(\varepsilon_{\mathrm{sec}}=\|\widetilde Q_{\mathrm{comp}}-Q_{\mathrm{comp}}\|\);
- any commutator defects with local analysis operators or gluing maps.

If the implemented global analysis operator obeys

\[
\|\widetilde A_{\mathrm{glob}}-A_{\mathrm{glob}}\|
\le\varepsilon_{\mathrm{glob}},
\]

then a positive perturbed lower bound requires

\[
\sqrt{\underline c_{\mathrm{loc}}}\,\gamma_{\mathcal K}
-
\varepsilon_{\mathrm{glob}}
>0,
\]

and yields

\[
\widetilde c_{\mathrm{glob}}
\ge
\left(
\sqrt{\underline c_{\mathrm{loc}}}\,\gamma_{\mathcal K}
-
\varepsilon_{\mathrm{glob}}
\right)^2.
\]

Every contribution to \(\varepsilon_{\mathrm{glob}}\) must be itemized. An unexplained compatibility prefactor is not admissible.

## 6. Phase-gauge compatibility

Local phase bounds can be transported to a global statement only after registering interface phase maps. For each oriented interface \(e:v\to w\), let

\[
U_e:\mathbb S^1_v\to\mathbb S^1_w
\]

be the phase-gauge transport. P2 must audit:

- reversal consistency \(U_{\bar e}=U_e^{-1}\);
- cycle discrepancy for every independent cycle;
- dependence on branch choices;
- stability under the declared wall margin.

For a cycle \(C\), define the phase cocycle defect

\[
\delta_C
=
 d_{\mathbb S^1}
\left(
\prod_{e\in C}U_e,
1
\right).
\]

The handoff requires either exact compatibility \(\delta_C=0\) or a certified bound whose accumulated contribution is included in the global phase-concentration estimate.

A local `R1` bound does not imply global phase coherence when cycle defects are uncontrolled.

## 7. Mandatory certificates

The gate may close only when all of the following are present.

### `P2-HO1 LOCAL-BOUND-REGISTRY`

A machine-readable list of all local \(c_v\), their domains and conventions, with

\[
\underline c_{\mathrm{loc}}=\min_v c_v>0.
\]

### `P2-HO2 COMPATIBILITY-EQUATIONS`

Exact equations defining \(V_{\mathrm{comp}}(\mathcal K)\), including gauge quotient or gauge fixing.

### `P2-HO3 ASSEMBLY-SINGULAR-VALUE`

A certified \(\gamma_{\mathcal K}>0\) for every object in the declared finite gluing class.

### `P2-HO4 SECTOR-LEAKAGE-LEDGER`

Explicit projector, commutator and implementation error bounds.

### `P2-HO5 GLOBAL-FRAME-BOUND`

A derived positive \(c_{\mathrm{glob}}\) or \(\widetilde c_{\mathrm{glob}}\), with size dependence shown.

### `P2-HO6 PHASE-COCYCLE-AUDIT`

Exact or certified cycle compatibility for the local phase gauges.

### `P2-HO7 NEGATIVE-CONTROLS`

At least one incompatible-sector, rank-deficient or gauge-unfixed model in which the proposed global bound correctly collapses or the gate rejects the model.

### `P2-HO8 INDEPENDENT-VALIDATOR`

A second implementation must verify dimensions, ranks, singular values, compatibility residuals and bound arithmetic.

## 8. Gate outcomes

### `P2_HANDOFF_ACCEPTED_FINITE_CLASS`

All mandatory certificates close and a positive global lower bound is proved for the declared finite gluing class. P2 may open only for that class.

### `P2_HANDOFF_ACCEPTED_SIZE_DEPENDENT`

The bound is positive for each declared finite size but decays explicitly with size. P2 may study that finite-size law, but no uniform manifold-level claim is allowed.

### `P2_HANDOFF_LOCAL_ONLY`

Local P5 bounds hold, but \(\gamma_{\mathcal K}\), sector compatibility or phase cocycles remain unresolved. P2 remains blocked.

### `P2_HANDOFF_OBSTRUCTED`

A global gauge mode, compatibility kernel, zero singular value or uncontrolled cycle defect forces the proposed bound to vanish. The obstruction must be retained and may motivate a revised P2 object, not an empirical correction factor.

## 9. Prohibited shortcuts

- multiplying local frame constants without defining the global norm and assembly map;
- inferring global injectivity from edgewise injectivity alone;
- deleting global gauge modes after seeing a singular value without registering the quotient;
- absorbing sector leakage into a fitted prefactor;
- treating a fixed-complex computation as a manifold theorem;
- using phase agreement on a spanning tree while ignoring independent cycles;
- invoking pentagon, braiding or modular coherence without separate proofs.

## 10. Current decision

```text
P5 local uniform-analysis contract: ACTIVE
P2 handoff gate:                    CLOSED
P2 global gluing calculations:      NOT AUTHORIZED AS A CLAIM-BEARING STAGE
```

Exploratory algebra for possible compatibility maps is allowed, but it must be labeled `P2_PRE-GATE_EXPLORATORY` and may not be used as evidence of global gluing.

No statement from the Gemini advisory report is used as evidence.
