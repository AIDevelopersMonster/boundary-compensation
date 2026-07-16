# G2 Theorem-Level Audit

**Date:** 2026-07-16  
**Manuscript:** `Recursive Jet Calculus and Uniform Conditioning for Finite Quantum 6j Recoupling Matrices`  
**Verdict:** `CONDITIONAL_PASS_ONE_PUBLICATION_BLOCKER`

## Executive decision

The doubled-spin conventions, finite q-Racah formula, truncated-Taylor algebra, generator recurrence and formal logarithm recurrence survive theorem-level inspection. The finite 208-carrier validation is correctly a numerical verification on a declared atlas.

One publication blocker remains. The manuscript states a rigorous computer-assisted lower-bound theorem for the uniform complex disk, but the present radius code uses ordinary binary floating-point arithmetic. It does not use interval arithmetic, directed rounding, rational enclosures or independently checked error bounds. Therefore the positive number reported as a lower bound is currently a high-precision numerical certificate, not yet a rigorous enclosure.

No statement from the Gemini advisory report is used as evidence.

## 1. Critical error

### CE-1. The conditioning theorem overstates the rigor of the current computation

**Location:** Section `Uniform regularity and conditioning`, theorem `Computer-assisted uniform conditioning` and its proof.

**Current claim:** for every declared carrier and every point of the closed complex disk,

`|omega_J(z)| >= 0.16025264148217636`.

**Audit finding:** the code builds Taylor coefficients and Cauchy-tail majorants in NumPy/Python floating point. The extremal search and all intermediate products, quotients, square roots and sums are rounded without certified outward enclosure. The pytest file checks self-consistency of the same floating-point builder; it does not prove that rounding error cannot invalidate the sign of the final lower envelope.

**Required correction:** choose one of two publication paths.

1. **Rigorous path:** replace the relevant calculation by interval or ball arithmetic with outward rounding, record precision, and certify every carrier margin.
2. **Numerical path:** downgrade the theorem to a `Numerical uniform-conditioning certificate`, replace `inf` and `>=` by an explicitly numerical statement, and remove the phrase `computer-assisted proof`.

Because the preprint thesis currently includes a certified common nonvanishing disk, the preferred path is interval certification.

## 2. Missing assumptions

### MA-1. Exact quantum-group convention

The manuscript defines the trigonometric q-number but should state explicitly which normalized quantum 6j convention is used and how it relates to the chosen phase and dimension factors. The finite formula is internally consistent, but convention dependence must be visible to the reader.

### MA-2. Root-of-unity admissibility

At `theta_0=pi/12`, the deformation is a root-of-unity specialization. The manuscript should state that the declared labels and intermediate channels stay in the nontruncated admissible range for the chosen convention, or else define the work purely as a trigonometric finite Racah model rather than silently importing a full modular-category interpretation.

### MA-3. Orthogonality domain

The text states orthogonality for real theta in the chamber. This should be an explicit assumption or a cited identity for the exact convention. Numerical orthogonality at the anchor is not by itself a proof throughout the real interval.

### MA-4. Carrier definition mixes mathematics and numerical filters

The declared class currently includes numerical conditions such as orthogonality tolerance and nonzero speed. Separate the algebraic carrier class from the computationally retained atlas. This avoids defining a mathematical object through floating-point acceptance tests.

### MA-5. Analytic logarithm

The signed logarithm on a complex disk requires a holomorphic branch of `log(s_J omega_J(z))`, not the real quantity `log|omega|`. The manuscript mostly uses the correct signed analytic logarithm, but the wording should consistently distinguish the holomorphic logarithm from its real-axis restriction.

## 3. Proof gaps

### PG-1. Square-root branch argument is incomplete as written

Nonvanishing of each q-factorial proves that the triangle radicand is nonzero. On a simply connected disk this permits a holomorphic square root after fixing the anchor value, but this implication should be stated as a lemma and applied also to the dimension-amplitude square roots in the matrix entries.

### PG-2. Critical q-index bound is asserted but not derived

The paper uses `N_crit={1,...,10}`. Add a finite combinatorial lemma showing that every q-factorial index occurring in all triangle factors, Racah numerators, denominators and dimension amplitudes for the declared class is at most 10. The software filter `zmax<=12` is not a transparent derivation of this claim.

### PG-3. Outer-disk Cauchy remainder needs a displayed formula

The theorem proof says that a Cauchy tail is added, but the manuscript should display the exact inequality, identify the outer radius, define the majorant `M_J`, and explain why the bound applies to the angular-speed series through order 50.

### PG-4. Formal orthogonality and complex continuation

The recurrence theorem correctly proves skewness if `F F^T=I` as a formal series. The manuscript should not imply that a complex-analytic continuation is unitary; transpose-orthogonality is an algebraic identity and should be stated as such for the chosen exact recoupling formula.

### PG-5. Finite-difference references are not independent implementations

The low-order analytic constructions and the unified jet engine provide useful cross-checks, but the central-difference references call the same q-Racah evaluation machinery. Replace `independent calculation` by `independent differentiation route` or `cross-validation route` unless genuinely separate code and arithmetic are used.

## 4. Wording corrections

1. Replace `first three matrix-response levels` by `matrix derivatives through order three`.
2. Replace `previously unseen representation families` by `families excluded by the frozen label-1-to-4 split`.
3. Qualify `exactly computable` as `given by a finite explicit analytic expression and recursively evaluable`.
4. State that the radius extremum is only within the frozen order-50 proof family.
5. Use `q-number walls` only after defining the term as zeros of critical trigonometric q-numbers.
6. Avoid calling pytest success a proof; tests verify implementation invariants and reproducibility.
7. In the abstract, do not call the uniform-disk statement a theorem until CE-1 is closed.

## 5. Publication enhancements

1. Add a theorem-dependency table: analytic lemma, finite enumeration, floating-point validation, interval certificate.
2. Add pseudocode for carrier enumeration and the order-50 tail calculation.
3. Publish the exact 283-carrier list and per-carrier margins as machine-readable supplementary data.
4. Add a convention table mapping manuscript symbols to source-code argument order.
5. Add a reproducibility statement distinguishing source hashes, generated certificates and independently verified enclosures.
6. Add a short limitations paragraph explaining that finite-label certification does not establish asymptotic stability as labels grow.

## 6. Items that passed

- Doubled-spin channel sets and parity rules are internally consistent.
- The four triangle factors and seven denominator arguments in the displayed Racah sum match the implemented argument order.
- The constant sign gauge is frozen with respect to theta.
- Reciprocal and square-root recurrences in the truncated algebra are correct.
- The generator recurrence is correct for normalized Taylor coefficients.
- The logarithm recurrence and the slope/curvature corollaries are correct.
- The third logarithmic derivative of the q-number has the correct sign and powers.
- The validation ceiling is explicitly bounded at matrix order three and logarithmic order two.
- The claim firewall against asymptotic geometry and physical interpretation is appropriate.

## 7. Gate decision

- `G2_ANALYTIC_CORE`: `PASS`
- `G2_CONVENTIONS`: `PASS_WITH_REQUIRED_CLARIFICATIONS`
- `G2_FINITE_VALIDATION`: `PASS_AS_NUMERICAL_VERIFICATION`
- `G2_UNIFORM_CONDITIONING`: `BLOCKED_PENDING_RIGOROUS_ROUNDING_OR_CLAIM_DOWNGRADE`
- `G2_OVERALL`: `CONDITIONAL_PASS_ONE_PUBLICATION_BLOCKER`

The next step is a rigorous interval-conditioning module or an explicit downgrade of the disk result. The manuscript should not proceed to upload-ready status while the current theorem retains rigorous lower-bound language.