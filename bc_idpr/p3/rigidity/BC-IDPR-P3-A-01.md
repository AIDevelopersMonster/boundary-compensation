# BC-IDPR-P3-A-01

## Linearized Pentagon Rigidity at Fixed Fusion Data

**Programme:** Boundary Compensation — Independent Deformation and Phase-Resolved Response (BC-IDPR)  
**Track:** P3-A — strict categorical rigidity  
**Status:** `ACTIVE / v0.1.0-draft`  
**Document type:** technical research contract and first computation specification  
**Upstream:** `BC-IDPR-P3-CORE-01`  
**Downstream:** P3-B comparison, CERT parameter-separation stage

---

## 0. Scientific decision

The first strict categorical test will use the multiplicity-free `SU(2)_2` / Ising fusion datum as a calibration anchor. The purpose is not to claim a new rigidity theorem for fusion categories. Generalized Ocneanu rigidity already states that fusion categories over characteristic zero are undeformable at fixed fusion data up to equivalence. The purpose here is narrower and reproducible:

1. construct the linearized pentagon complex explicitly in a declared gauge;
2. calculate the quotient tangent space for one finite anchor;
3. separate genuine categorical deformation from basis/gauge motion;
4. establish a certified comparison point for the generic-q operator envelope of P3-B.

The anchor is chosen because it is small enough for complete enumeration while still containing a nontrivial two-dimensional associator block.

---

## 1. Fixed fusion datum

Let the simple-object set be

\[
\mathcal I=\{\mathbf 1,\sigma,\psi\}.
\]

The fusion rules are

\[
\psi\otimes\psi\cong\mathbf 1,\qquad
\psi\otimes\sigma\cong\sigma\otimes\psi\cong\sigma,
\qquad
\sigma\otimes\sigma\cong\mathbf 1\oplus\psi.
\]

All fusion multiplicities are either zero or one. The fixed discrete datum is

\[
\mathfrak F_0=(\mathcal I,N_{ab}^{c},\mathbf 1,(-)^*),
\]

with

\[
N_{ab}^{c}\in\{0,1\}.
\]

No continuous change of the object set, fusion coefficients, duality map, or admissible fusion channels is permitted inside P3-A.

---

## 2. Associator variables

For each admissible quadruple `(a,b,c;d)`, define the fusion-tree channel set

\[
E_{abc}^{d}=\{e\in\mathcal I:N_{ab}^{e}N_{ec}^{d}=1\},
\qquad
F_{abc}^{d}=\{f\in\mathcal I:N_{bc}^{f}N_{af}^{d}=1\}.
\]

The associator block is

\[
F^{abc}_{d}:\mathbb C^{E_{abc}^{d}}\longrightarrow\mathbb C^{F_{abc}^{d}}.
\]

For multiplicity-free data, each matrix entry is a scalar

\[
[F^{abc}_{d}]_{ef}.
\]

The baseline solution is denoted by `F^(0)`. A first-order deformation is

\[
F(t)=F^{(0)}+t\dot F+O(t^2).
\]

The variable space `C^2` is the direct sum of all admissible first-order matrix entries after the normalization constraints involving the tensor unit have been imposed.

---

## 3. Pentagon residual map

For every admissible five-object fusion configuration, the two composites of associators define a polynomial residual. Collect all independent residual entries into

\[
\mathcal P(F)=0.
\]

The first-order cocycle condition is

\[
D\mathcal P_{F^{(0)}}[\dot F]=0.
\]

Define

\[
Z^3_{F^{(0)}}:=\ker D\mathcal P_{F^{(0)}}.
\]

This is the space of infinitesimal pentagon-preserving directions before quotienting by gauge.

### 3.1 Reproducibility rule

The implementation must not use a hand-selected subset of pentagons without recording the selection. It must output:

- the full list of admissible pentagon instances;
- the matrix-entry residuals used;
- the deduplication rule;
- the Jacobian matrix;
- its exact or certified numerical rank;
- the basis of its kernel.

---

## 4. Gauge tangent

A gauge transformation is a change of basis in each nonzero trivalent fusion space. In the multiplicity-free case it is specified by nonzero scalars

\[
u_{ab}^{c}\in\mathbb C^{\times}
\]

for all admissible triples. Write

\[
u_{ab}^{c}(t)=\exp(t\chi_{ab}^{c})=1+t\chi_{ab}^{c}+O(t^2).
\]

The induced first-order variation of an F-entry is

\[
(\delta_{\chi}F)^{abc}_{d;ef}
=
F^{(0)abc}_{d;ef}
\left(
\chi_{ab}^{e}+\chi_{ec}^{d}-\chi_{bc}^{f}-\chi_{af}^{d}
\right),
\]

subject to the declared unit normalizations.

Let

\[
D\mathcal G_{F^{(0)}}:C^1\to C^2
\]

be the corresponding linear map and define

\[
B^3_{F^{(0)}}:=\operatorname{im}D\mathcal G_{F^{(0)}}.
\]

The local deformation quotient is

\[
H^3_{\mathrm{lin}}(F^{(0)})
:=
Z^3_{F^{(0)}}/B^3_{F^{(0)}}.
\]

This notation is operational for this finite calculation. Identification with a standard categorical cohomology theory requires a separate convention audit and must not be asserted merely from notation.

---

## 5. Rigidity certificate

The finite anchor receives status `LOCALLY_RIGID_IN_DECLARED_COMPLEX` when all of the following are verified:

1. `D P o D G = 0` to exact arithmetic or declared tolerance;
2. `rank(DG)` and `rank(DP)` are certified;
3. `im(DG) = ker(DP)`;
4. therefore

\[
\dim H^3_{\mathrm{lin}}(F^{(0)})=0.
\]

The certificate is relative to:

- the fixed fusion datum;
- the selected associator normalization;
- the declared gauge group;
- the enumerated pentagon equations;
- the arithmetic/tolerance protocol.

It is not by itself a global theorem about all categories, all levels, or generic-q analytic families.

---

## 6. Calibration subproblem: the nontrivial Ising block

After standard unit normalizations, the most visible nontrivial associator block is the two-channel map for three sigma objects fusing to sigma:

\[
F^{\sigma\sigma\sigma}_{\sigma}:
\operatorname{span}\{\mathbf 1,\psi\}
\to
\operatorname{span}\{\mathbf 1,\psi\}.
\]

A common gauge representative is

\[
F^{\sigma\sigma\sigma}_{\sigma}
=
\frac{1}{\sqrt 2}
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix}.
\]

The full computation must nevertheless include every admissible scalar and matrix block needed by the pentagon equations. The 2x2 block alone is not a complete categorical deformation calculation.

---

## 7. Two arithmetic modes

### 7.1 Exact algebraic mode

Preferred field:

\[
K=\mathbb Q(\sqrt 2)
\]

or an equivalent exact algebraic-number representation.

Outputs:

- exact Jacobian;
- exact ranks;
- exact kernel and image bases;
- exact quotient-dimension certificate.

### 7.2 Certified numerical mode

Fallback mode uses high precision with singular-value thresholds declared before the final rank decision.

Required outputs:

- working precision;
- singular values of `DP` and `DG`;
- threshold rule;
- smallest retained singular value;
- largest discarded singular value;
- stability under precision increase.

A bare floating-point rank call is not a rigidity certificate.

---

## 8. Minimal software architecture

The first implementation package shall contain:

```text
bc_idpr/p3/rigidity/
  BC-IDPR-P3-A-01.md
  data/
    ising_fusion_rules.json
    ising_F_baseline.json
  src/
    enumerate_fusion_trees.py
    build_pentagon_residuals.py
    build_gauge_tangent.py
    linearized_rigidity.py
  tests/
    test_fusion_associativity.py
    test_baseline_pentagon.py
    test_gauge_is_cocycle.py
    test_rank_stability.py
  outputs/
    variable_registry.json
    pentagon_registry.json
    jacobian_summary.json
    rigidity_certificate.json
```

No generated output is to be treated as canonical until its input hashes, conventions, and software revision are recorded.

---

## 9. Required machine-readable certificate

```json
{
  "contract": "BC-IDPR-P3-A-01",
  "anchor": "SU(2)_2 / Ising fusion datum",
  "status": "UNRUN",
  "fusion_datum_hash": null,
  "baseline_F_hash": null,
  "field": "Q(sqrt(2))",
  "n_variables": null,
  "n_pentagon_residuals": null,
  "rank_DP": null,
  "dim_kernel_DP": null,
  "rank_DG": null,
  "dim_quotient": null,
  "complex_condition_verified": false,
  "claim_status": "OPEN_OBLIGATION"
}
```

---

## 10. Failure statuses

- `BASELINE_PENTAGON_FAILURE`
- `GAUGE_MAP_INCONSISTENT`
- `COMPLEX_CONDITION_FAILURE`
- `RANK_UNCERTIFIED`
- `EQUATION_SET_INCOMPLETE`
- `NORMALIZATION_DEPENDENT_RESULT`
- `NONTRIVIAL_TANGENT_FOUND`
- `LOCALLY_RIGID_IN_DECLARED_COMPLEX`
- `INCONCLUSIVE`

A nontrivial quotient tangent is not to be discarded as a software defect without an explicit audit. It may indicate an omitted constraint, an oversized variable class, a wrong gauge map, or a genuine deformation direction.

---

## 11. Interface to P3-B

P3-B will construct a generic-q finite operator family `D_J(q)` near an anchor value `q_2`. The comparison must distinguish:

\[
\dot F_{\mathrm{cat}}
\quad\text{from}\quad
\partial_q D_J(q_2).
\]

Possible outcome:

\[
H^3_{\mathrm{lin}}(F^{(0)})=0,
\qquad
\partial_qD_J(q_2)\ne0.
\]

This is not a contradiction. It means that the varying operator family leaves the equivalence class of the fixed fusion category or changes auxiliary analytic data not represented by a categorical deformation at fixed fusion datum.

---

## 12. First milestone

`P3-A-M1` is complete only when the repository contains:

1. a validated fusion-rule registry;
2. a complete baseline F-symbol registry in one gauge;
3. an enumerated pentagon registry;
4. an explicit Jacobian `DP`;
5. an explicit gauge tangent `DG`;
6. verification of `DP DG = 0`;
7. a machine-readable quotient-dimension certificate;
8. an independent manual or second-implementation spot check.

---

## 13. Claim firewall

This draft does not claim:

- a new proof of generalized Ocneanu rigidity;
- a classification of `SU(2)_k` fusion categories;
- rigidity of arbitrary braided or modular structures;
- equivalence of modular data and categorical equivalence;
- impossibility of generic-q operator variation;
- physical consequences of categorical rigidity.

The controlled prospective claim is narrower:

> The BC-IDPR pipeline can make local categorical rigidity computationally explicit and auditable for a finite fixed fusion datum, thereby providing a strict negative-control channel for independent q-deformation studies.

---

## 14. Primary background references

1. P. Etingof, D. Nikshych, V. Ostrik, *On fusion categories*, Annals of Mathematics 162 (2005), arXiv:math/0203060. Used for generalized Ocneanu rigidity and finiteness at fixed fusion data.
2. B. Bartlett, *Fusion categories via string diagrams*, Communications in Contemporary Mathematics 18 (2016), arXiv:1502.02882. Used as an explicit graphical route to Ocneanu rigidity and fusion-category identities.
3. W. Aboumrad, *Quantum computing with anyons: an F-matrix and braid calculator*, arXiv:2212.00831. Used as software-related precedent for solving pentagon equations in multiplicity-free root-of-unity anyon systems.

---

## 15. Immediate next operation

Populate the Ising fusion and baseline-F registries, enumerate all admissible fusion trees, and freeze the convention ledger before deriving the Jacobians. Until then the document status remains

`ACTIVE / OPEN_OBLIGATION`.
