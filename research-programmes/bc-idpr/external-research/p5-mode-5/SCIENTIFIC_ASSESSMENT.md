# Scientific assessment of the external mode-5 reports

**Assessment status:** `ADVISORY_MATERIAL_WITH_MAJOR_CORRECTIONS`  
**Scientific authority:** supervisor decision  
**Effect on P1 claim set:** none  
**Effect on RC02:** none; rerun remains prohibited  
**Possible use:** P5 hypothesis generation and counterexample design

## 1. Central category error

Both reports identify the RC02 result `m=5` with a fifth Taylor coefficient or fifth derivative. This is not the object tested in P1.

The frozen predictor family is

\[
\Phi_m(\theta)=-m^2\csc^2(m\theta)+\csc^2\theta
=\partial_\theta^2\log\frac{\sin(m\theta)}{\sin\theta},
\]

where `m` is a mode or q-number index. RC02 calibrated over integer modes `m=2,...,10` and selected `m=5`. The derivative order remained two for every candidate mode.

Therefore a derivation based on the fifth derivative of `log[m]_q` does not explain the P1 result without an independently proved bridge between derivative order and mode index.

## 2. Claims not established by the reports

The following proposed conclusions are unsupported:

- the pentagon identity forces mode 5 because it has five terms or because a 4-simplex has five tetrahedral facets;
- every order below five cancels and every order above five destroys coherence;
- mode 5 is a topological invariant of the representation category;
- a large fifth derivative acts as a physical coupling or synchronization force;
- Kuramoto synchronization explains the family phase concentration;
- coherent-state Fubini--Study curvature or holonomy produces the RC02 phase statistic;
- Cauchy estimates or wall distance alone yield the required positive lower bound;
- the anchor `theta=pi/12` and the number 24 imply a Leech-lattice or modular-invariance mechanism;
- RC02 proves category-level, Turaev--Viro, Pachner-move, or physical phase-locking statements.

These claims cross the P1 claim ceiling and are not accompanied by the necessary constructions or proofs.

## 3. Specific mathematical defects

### 3.1 Upper bounds are used as lower bounds

Cauchy estimates control derivatives from above in terms of the analytic radius. They do not prove that a selected predictor has a nonzero response, a positive frame constant, or an energy advantage over a control. P5 requires explicit non-cancellation information or a lower singular-value/frame bound.

### 3.2 Pole cancellation is not unique to order five

For logarithmic sine derivatives, the leading homogeneous singular terms in expressions of the form

\[
m^r g^{(r)}(m\theta)-g^{(r)}(\theta)
\]

may cancel by scaling for general derivative order `r`. The reports do not prove uniqueness at `r=5`.

### 3.3 Pentagon numerology is not a deformation theorem

The number of factors or facets in a graphical realization of the pentagon identity does not imply that the fifth derivative is the first nonzero deformation coefficient. Such a theorem would require an explicit differentiated pentagon system, gauge quotient, vanishing result for lower jets, and a nonzero obstruction class at the claimed order.

### 3.4 The nearest-wall hypothesis does not predict mode 5

At the anchor `theta_0=pi/12`, among integer modes through ten the pole of mode 10 is closer than the pole of mode 5. Hence a simple nearest-wall minimization cannot explain the calibration choice.

### 3.5 The reported scalar magnitudes are not the RC02 statistic

RC02 compared normalized, cubic-residualized predictor atoms against matched controls using carrier responses and family medians. Raw values of higher derivatives at one anchor do not determine the normalized predictor energy advantage or directional resultant lengths.

## 4. Salvageable research content

The reports do motivate legitimate P5 questions after correction:

1. Can the mode-5 selection be predicted from exact q-number curvature decompositions of the finite q-Racah response?
2. Can wall margin provide uniform derivative bounds that combine with non-cancellation information to yield a positive lower frame bound?
3. How does cubic residualization change the Gram geometry of integer modes and controls?
4. Which carrier-family coefficients amplify or suppress each normalized predictor atom?
5. Can one prove that simple hypotheses such as nearest wall, `m=k/2`, or pentagon numerology fail?
6. Is mode 5 stable under a preregistered class of nuisance/envelope spaces, or is it protocol-relative?

## 5. Final decision

```text
EXTERNAL_REPORTS:
  retained_as: HYPOTHESIS_SOURCES
  evidence_status: NOT_EVIDENCE
  theorem_status: NOT_PROVED
  P1_revision_required: NO
  RC02_rerun: FORBIDDEN
  route: P5_MODE5_MECHANISM_DIAGNOSTIC
```

The useful scientific move is not to defend the reports' proposed proof. It is to convert their strongest intuitions into falsifiable P5 obligations with exact domains, norms, quantifiers, null hypotheses, and certified bounds.