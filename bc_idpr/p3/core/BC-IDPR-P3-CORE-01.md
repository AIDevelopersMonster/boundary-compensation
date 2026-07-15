# BC-IDPR-P3-CORE-01

## Typed Deformation Architecture, Gauge Conventions, and Wall Protocol

**Programme:** Boundary Compensation — Independent Deformation and Phase-Resolved Response (BC-IDPR)  
**Branch:** P3 — Independent Deformation  
**Document code:** BC-IDPR-P3-CORE-01  
**Version:** v0.1.0-draft  
**Status:** ACTIVE / INTERNAL RESEARCH CONTRACT  
**Date:** 2026-07-16  
**Author:** A. A. Malachevsky  
**Scientific role:** common contract for P3-A and P3-B

---

## 1. Purpose

This document fixes the common mathematical architecture required before the two parallel P3 research streams are allowed to diverge:

- **P3-A:** linearized categorical rigidity at fixed fusion data;
- **P3-B:** minimal generic-\(q\) operator envelope with fixed external geometry.

The purpose is not to prove rigidity, construct a final quantum-geometric model, or interpret the deformation parameter physically. The purpose is to prevent parameter mixing, gauge confusion, hidden changes of representation scale, and silent continuation through singular loci.

The central methodological rule is:

> A variation of the symbol \(q\) is not an independent deformation unless its operator or categorical effect survives the declared structural equivalence and cannot be absorbed into representation-scale, geometry, protocol, or gauge directions.

---

## 2. Programme dependency

The active dependency graph is

\[
\mathrm{P3\text{-}CORE}
\longrightarrow
\begin{cases}
\mathrm{P3\text{-}A}: \text{categorical rigidity},\\
\mathrm{P3\text{-}B}: \text{generic-}q\text{ operator envelope},
\end{cases}
\longrightarrow
\mathrm{CERT}
\longrightarrow
\mathrm{P1}.
\]

P1 phase-resolved residual analysis may use P3 outputs only after parameter separation has received a declared certificate. A visually strong phase pattern is not itself evidence of an independent \(q\)-channel.

---

## 3. Typed deformation datum

An **independent-deformation datum** is a tuple

\[
\mathfrak D
=
(\mathcal B,\mathcal H,Q,R,X,\Theta,\mathcal M,\mathcal D,\mathcal O,
\sim_{\mathrm{str}},\sim_{\mathcal O}),
\]

with the following components.

### 3.1 Base or parameter domain

\(\mathcal B\) is the declared parameter base or regular chamber. It may be an interval, a real slice, a complex domain, or a finite-dimensional manifold. It must not include singular points unless those points are treated by a separate wall/reset rule.

### 3.2 State space

\(\mathcal H\) is the finite-dimensional Hilbert space, fusion-space package, or other declared carrier on which the effective operator data are represented.

The dimension and identification of \(\mathcal H\) must remain fixed inside a regular chamber. A change in carrier dimension is a wall event, not a smooth deformation.

### 3.3 Deformation coordinate

\(Q\) is the space of target deformation coordinates. In P3-B the principal coordinate is \(q\), usually restricted to a declared regular domain in \(\mathbb C^\times\). In P3-A the deformation coordinate is an infinitesimal variation of associator or \(F\)-symbol data at fixed fusion datum.

### 3.4 Representation scale

\(R\) is the space of representation-scale data. It may include:

- level-like parameters;
- absolute label scale;
- cutoff or truncation data;
- finite representation dimension;
- mesh or resolution parameters;
- normalization maps that convert labels into dimensionless coordinates.

Representation scale is not identified with geometry unless a separate map is declared and audited.

### 3.5 Geometry data

\(X\) is split into two layers:

\[
X=X_{\mathrm{ext}}\times X_{\mathrm{int}}.
\]

- \(X_{\mathrm{ext}}\): externally declared normalized geometry, fixed by a predeclared label-to-geometry map or geometric input;
- \(X_{\mathrm{int}}\): induced quantum-geometric data that may depend on \(q\), including quantum dimensions, recoupling phases, Gram data, or other derived structures.

Fixing labels or \(X_{\mathrm{ext}}\) does not automatically fix \(X_{\mathrm{int}}\).

### 3.6 Observation protocol

\(\Theta\) contains protocol choices: spectral windows, cluster definitions, phase conventions, tolerances, normalization rules, observable selection, and data-reduction procedures.

No protocol parameter may be tuned after seeing the target phase pattern unless the analysis is explicitly labeled exploratory and excluded from the confirmatory claim set.

### 3.7 Model class

\(\mathcal M\) is the declared class of admissible categorical or operator models. It must state whether the object belongs to:

- a fixed fusion category;
- a unitary modular tensor category;
- a generic \(U_q(\mathfrak{sl}_2)\)-type representation family;
- a finite recoupling block;
- an abstract finite-dimensional operator family;
- another explicitly defined class.

A generic-\(q\) family must not be called standard \(SU(2)_k\) away from the root-of-unity point unless full categorical consistency has been established.

### 3.8 Operator or categorical family

\[
\mathcal D:\mathcal B\times Q\times R\times X\times\Theta
\longrightarrow \mathcal M
\]

is the principal family under study. In P3-A, \(\mathcal D\) may denote the collection of associator matrices or \(F\)-symbols. In P3-B, it denotes a finite-dimensional operator or compatible operator package.

### 3.9 Observables

\(\mathcal O\) is the predeclared observable map or family of maps. Observable identifiability is distinct from intrinsic operator nontriviality.

### 3.10 Equivalences

Two equivalences must remain separate.

1. **Structural equivalence** \(\sim_{\mathrm{str}}\): basis changes, gauge transformations, relabelings, or other transformations that preserve the declared mathematical object.
2. **Observational equivalence** \(\sim_{\mathcal O}\): equality of the recorded observables at the declared resolution.

P3 studies nontriviality modulo \(\sim_{\mathrm{str}}\). CERT studies distinguishability modulo \(\sim_{\mathcal O}\).

---

## 4. Exact independent path

Let

\[
c(s)=\bigl(q(s),\rho(s),\xi_{\mathrm{ext}}(s),\theta(s)\bigr)
\]

be a differentiable path in a regular chamber.

It is an **exact independent \(q\)-path** at \(s_0\) if

\[
\dot q(s_0)\neq 0,
\qquad
\dot\rho(s_0)=0,
\qquad
\dot\xi_{\mathrm{ext}}(s_0)=0,
\qquad
\dot\theta(s_0)=0,
\]

and the induced tangent is not structurally trivial.

No condition of the form \(\dot\xi_{\mathrm{int}}=0\) is imposed automatically. Instead, the induced internal-geometry response must be measured and entered into the leakage ledger.

---

## 5. Nuisance and gauge tangent spaces

At a base point \(m_0=\mathcal D(c(s_0))\), define the target tangent

\[
V_q=D_q\mathcal D[\dot q].
\]

The declared nuisance tangent space is

\[
\mathcal N_{m_0}
=
\overline{\operatorname{span}}
\left\{
D_\rho\mathcal D[\delta\rho],
D_{\xi_{\mathrm{ext}}}\mathcal D[\delta\xi],
D_\theta\mathcal D[\delta\theta],
\mathcal G_{m_0}
\right\},
\]

where \(\mathcal G_{m_0}\) is the tangent space to the structural gauge orbit.

For an operator family under unitary conjugation,

\[
\mathcal G_{m_0}
=
\{[K,m_0]:K^\dagger=-K\}.
\]

For categorical data, \(\mathcal G_{m_0}\) is generated by infinitesimal basis changes in the fusion spaces, with conventions specified in P3-A.

The ambient tangent space, scalar product, and closure operation must be declared. In finite matrix models, the default audit norm is the Hilbert--Schmidt norm, with operator-norm checks added where wall stability is relevant.

---

## 6. Intrinsic deformation margin

The local intrinsic margin is

\[
m_{\mathrm{int}}(m_0)
=
\left\|P_{\mathcal N_{m_0}^{\perp}}V_q\right\|.
\]

Interpretation:

- \(m_{\mathrm{int}}=0\): the target tangent is locally absorbed by declared nuisance and gauge directions;
- \(m_{\mathrm{int}}>0\): a genuine operator-level deformation direction exists inside the declared model and norm;
- the value alone does not imply observable identifiability;
- the value is valid only inside the current regular chamber and under the declared parameterization.

A scale-free companion diagnostic should be used when possible:

\[
\widehat m_{\mathrm{int}}
=
\frac{\|P_{\mathcal N^\perp}V_q\|}{\|V_q\|},
\qquad V_q\neq0.
\]

---

## 7. Tolerance-certified independent path

For a path \(c:[s_0,s_1]\to\mathcal B\), define the integrated leakage budget

\[
E_{\mathrm{leak}}
=
\int_{s_0}^{s_1}
\left(
L_\rho\|\dot\rho\|
+L_\xi\|\dot\xi_{\mathrm{ext}}\|
+L_\theta\|\dot\theta\|
\right)ds,
\]

with predeclared local or global Lipschitz bounds.

A tolerance-certified path requires a positive separation margin, for example

\[
\|\Delta\mathcal O_q\|-E_{\mathrm{leak}}
\ge m_{\mathrm{cert}}>0.
\]

The symbol \(\gg\) is forbidden in certificate statements. Numerical thresholds, norm choices, path lengths, and uncertainty sources must be explicit.

---

## 8. Regular chambers and singular walls

For a fixed finite label skeleton \(J\), define the singular set

\[
\Sigma_J
=
\{q:\text{a required denominator, normalization, carrier dimension, rank, or categorical construction fails}\}.
\]

A **regular chamber** is a connected domain

\[
U\subset\mathbb C^\times\setminus\Sigma_J
\]

on which the declared carrier dimension, model class, normalization, and required ranks remain stable.

The following events are walls:

- denominator or quantum-factorial zero;
- carrier-dimension change;
- fusion-rule or admissible-label change;
- loss of semisimplicity required by the model;
- rank drop or support change;
- cluster collision invalidating the selected branch protocol;
- failure of self-adjointness or positivity assumptions;
- gauge chart singularity;
- loss of a declared frame constant or identifiability margin.

At a wall, the status is

`CERTIFICATE_RESET`

unless a separate transition theorem has been proved. Silent continuation is forbidden.

---

## 9. P3-A interface: linearized categorical rigidity

P3-A fixes a fusion datum and studies a base associator \(F^{(0)}\). For

\[
F(t)=F^{(0)}+t\dot F+O(t^2),
\]

linearization of the pentagon equations gives

\[
D\mathcal P_{F^{(0)}}[\dot F]=0.
\]

Infinitesimal fusion-space basis changes generate a gauge image

\[
\operatorname{im}D\mathcal G_{F^{(0)}}.
\]

The local categorical deformation space is

\[
\mathcal T_{\mathrm{cat}}
=
\ker D\mathcal P_{F^{(0)}}
/
\operatorname{im}D\mathcal G_{F^{(0)}}.
\]

P3-A must report:

- the fixed object set and fusion coefficients;
- all multiplicity conventions;
- the independent \(F\)-variables;
- the independent pentagon equations used;
- the gauge generators;
- ranks, nullities, and numerical/symbolic exactness status;
- whether the result is local, global, generic, or specific to one small level.

Allowed statuses:

- `LOCALLY_RIGID`;
- `GAUGE_ONLY_DEFORMATION`;
- `NONTRIVIAL_TANGENT_FOUND`;
- `UNDERDETERMINED_BY_SELECTED_EQUATIONS`;
- `CATEGORY_DATA_INCOMPLETE`;
- `COMPUTATION_NOT_CERTIFIED`.

---

## 10. P3-B interface: minimal generic-\(q\) operator envelope

P3-B fixes a finite label skeleton \(J\), an external geometry map, a gauge convention, and a regular domain \(U\). It constructs

\[
q\longmapsto\mathcal D_J(q)
\]

from declared \(q\)-numbers, \(q\)-factorials, recoupling coefficients, or other explicitly defined data.

P3-B must report:

- the exact \(q\)-convention;
- branch choices for complex powers and square roots;
- the finite label skeleton;
- the regular domain and singular set;
- self-adjoint or real-slice conditions;
- the external geometry held fixed;
- the induced internal-geometry channels allowed to vary;
- the gauge and nuisance tangent construction;
- \(m_{\mathrm{int}}\) and its uncertainty or exactness status;
- wall distance and chamber validity.

Allowed statuses:

- `REGULAR_GENERIC_Q_FAMILY`;
- `INTRINSIC_DIRECTION_CERTIFIED`;
- `TARGET_TANGENT_GAUGE_TRIVIAL`;
- `TARGET_TANGENT_SCALE_DEGENERATE`;
- `GEOMETRY_LEAKAGE_UNCONTROLLED`;
- `SINGULAR_WALL_REACHED`;
- `MODEL_CLASS_MISMATCH`;
- `COMPUTATION_NOT_CERTIFIED`.

---

## 11. Shared anchor experiment

P3-A and P3-B must share at least one minimal anchor case, provisionally \(k=2\) or \(k=3\), selected only after checking that the categorical and operator data are nontrivial enough to test the distinction.

The key comparison is

\[
\mathcal T_{\mathrm{cat}}=0
\quad\text{with possibly}\quad
\partial_q\mathcal D_J\neq0.
\]

This is not a contradiction. It means that an analytic operator family varies outside the moduli of the fixed categorical equivalence class.

---

## 12. Claim firewall

The following claims are forbidden at P3-CORE stage:

- that \(q\) is physical time, RG time, or a dynamical variable;
- that a generic-\(q\) family is standard \(SU(2)_k\) away from the root-of-unity point;
- that fixed labels imply fixed quantum geometry;
- that a nonzero operator derivative proves observable identifiability;
- that local rigidity proves a universal global no-go theorem;
- that a root-of-unity wall is a physical phase transition;
- that numerical rank alone proves a theorem without conditioning and exactness audit;
- that phase modulation observed after exploratory tuning is confirmatory evidence.

---

## 13. Reproducibility obligations

Every P3-A/P3-B computation must preserve:

- source code or symbolic notebook;
- exact input data;
- software and package versions;
- numerical precision;
- normalization and gauge conventions;
- singular-value spectrum or rank threshold used;
- generated tables and figures;
- machine-readable result summary;
- negative and failed runs;
- provenance links to external research reports used only as advisory inputs.

No serious result may remain only inside a chat history.

---

## 14. DOI and self-citation protocol

When a BC publication is cited, the canonical DOI registry must be checked first. If the work is known to be published on Zenodo and the DOI is not present in the registry, the workflow enters

`AUTHOR_DOI_REQUIRED`.

The author is asked only for the missing DOI. The DOI is then added to the canonical registry for future reuse. DOI values must not be guessed from record numbers.

---

## 15. Gate P3-G1

P3-G1 is passed when at least one of the following is obtained in a reproducible declared case:

1. a local categorical rigidity certificate
   \[
   \dim\mathcal T_{\mathrm{cat}}=0;
   \]
2. a regular generic-\(q\) family with
   \[
   m_{\mathrm{int}}>0
   \]
   under fixed external geometry and declared nuisance space.

The preferred milestone contains both and explains their compatibility.

P3-G1 does not yet authorize P1 confirmatory phase analysis. The intermediate CERT layer must still establish observable separation, leakage control, and protocol stability.

---

## 16. Immediate execution plan

### CORE-Task 1 — convention freeze

Freeze the \(q\)-convention, label convention, external geometry map, norm, and gauge notation.

### CORE-Task 2 — anchor selection

Audit \(k=2\) and \(k=3\) as candidate shared anchor cases. Select the first case that supports both a nontrivial pentagon system and a nontrivial finite operator block.

### CORE-Task 3 — P3-A data sheet

Produce the finite list of objects, admissible triples, fusion spaces, independent \(F\)-variables, pentagon equations, and gauge generators.

### CORE-Task 4 — P3-B data sheet

Produce the finite label skeleton, explicit \(q\)-functions, singular set, base point, operator block, and nuisance basis.

### CORE-Task 5 — paired minimal computation

Run the first rigidity and operator-tangent computations on the same anchor case and compare their statuses without forcing agreement.

---

## 17. Current programme status

**P3-CORE:** ACTIVE  
**P3-A:** READY AFTER CONVENTION FREEZE  
**P3-B:** READY AFTER CONVENTION FREEZE  
**CERT:** BLOCKED BY P3 OUTPUT  
**P1 CONFIRMATORY SCAN:** BLOCKED BY CERT  
**Exploratory P1 diagnostics:** allowed only when clearly labeled exploratory and excluded from confirmatory claims.
