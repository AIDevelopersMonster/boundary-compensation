# P5 research prompt: analytical mechanism of the calibration-selected mode 5

## Role

Act as an adversarial mathematical researcher in finite quantum 6j recoupling, analytic matrix families, discrete frame theory, and certified numerical analysis. Your task is not to explain the observed mode by analogy. Your task is to prove, disprove, or sharply localize possible analytical mechanisms behind the calibration-selected predictor mode `m=5` in BC-IDPR P1 / RC02.

## Frozen facts

The P1 predictor is indexed by mode `m`, not by derivative order:

\[
\Phi_m(\theta)
=\partial_\theta^2\log\frac{\sin(m\theta)}{\sin\theta}
=-m^2\csc^2(m\theta)+\csc^2\theta.
\]

On the frozen grid, let `P_3` be the discrete orthogonal projector onto the declared cubic nuisance space and define

\[
\psi_m=\frac{(I-P_3)\Phi_m}{\|(I-P_3)\Phi_m\|_2}.
\]

Calibration compared integer modes `m=2,...,10` against a frozen one-to-one half-integer control pairing and selected `m=5`, paired with control `9.5`. Confirmation then used eight sealed families and 106 ordered carriers. The confirmatory result is frozen and may not be rerun or retuned.

## Core question

Can the dominance of normalized predictor mode `m=5` be predicted a priori from the declared finite q-Racah carrier class, observable, wall geometry, nuisance projection, and family aggregation, rather than merely recovered from calibration data?

## Mandatory distinctions

Do not confuse:

- mode index `m=5` with fifth derivative order;
- parameter-space phase with physical time evolution;
- predictor curvature with spacetime, Berry, or categorical curvature;
- a wall-distance upper derivative estimate with a positive lower response bound;
- local recoupling matrices with pentagon, braiding, modular, or global TQFT coherence;
- carrier-level observations with independent family-level evidence.

## Work package A: exact predictor geometry

1. Derive exact symbolic formulas for `Phi_m`, its derivatives needed for regularity bounds, and its singularity set on the declared chamber.
2. Compute or bound the discrete Gram matrices of:
   - cubic-residualized integer atoms;
   - cubic-residualized half-integer controls;
   - paired projector differences.
3. Determine which aspects of the geometry distinguish mode 5 before any carrier response is used.
4. Prove all domain and wall-margin assumptions explicitly.

Required output: exact identities plus interval-certified numerical bounds on all finite matrices.

## Work package B: response decomposition

For each ordered carrier `J`, express the primary residual response, where possible, in the form

\[
r_J=\sum_{m=2}^{10} a_{Jm}\psi_m+r_J^\perp,
\]

or provide an alternative exact finite decomposition adapted to the q-Racah formula.

Determine whether coefficient structure, symmetries, admissibility ranges, or cancellations force a systematic preference for mode 5 across the declared family class.

Required output: either a uniform coefficient theorem, a stratified theorem by carrier family, or an explicit counterexample showing that no such theorem can hold without extra hypotheses.

## Work package C: lower-frame and separation bounds

Seek a bound of the form

\[
\mathcal E_{J,5}-\mathcal E_{J,9.5}
\ge L_J(\delta_{\rm wall},\Gamma_J,\sigma_{\min},\mathcal B_3),
\]

where every term is defined independently of confirmatory outcomes. Then determine whether a family-level bound

\[
\operatorname{median}_{J\in f}
(\mathcal E_{J,5}-\mathcal E_{J,9.5})>0
\]

can be certified uniformly for a declared class of families.

Cauchy estimates alone are insufficient. A positive result must combine upper regularity control with a non-cancellation or lower singular-value/frame argument.

## Work package D: falsification of simple explanations

Formally test and, if appropriate, refute the following hypotheses:

1. `m=5` is selected because it is the fifth derivative.
2. `m=5` is selected because the pentagon identity has five terms or a 4-simplex has five facets.
3. The selected mode minimizes distance to the nearest q-number wall.
4. The selected mode obeys a universal rule `m=k/2` at the anchor.
5. The raw magnitude of `Phi_m` or of a higher derivative predicts normalized residual energy.
6. Mode 5 remains dominant under every reasonable smooth-envelope space.

For each hypothesis provide one of: theorem, counterexample, finite certified disproof, or `INCONCLUSIVE_WITH_EXACT_OBLIGATION`.

## Work package E: nuisance-space robustness

Without touching the sealed confirmatory decision, preregister a separate robustness analysis over a finite declared family of envelope spaces, for example:

- polynomial degrees 2 through 6;
- fixed-knot B-spline spaces;
- low-frequency trigonometric nuisance spaces.

Use projector-distance bounds to distinguish genuine instability from minor nuisance-space perturbation. Do not choose the nuisance class after observing which one preserves mode 5.

## Forbidden imports

Do not use Kuramoto synchronization, physical coupling strength, phase attractors, dynamics, decoherence, Leech-lattice numerology, Turaev--Viro invariance, Berry holonomy, or coherent-state curvature as explanations unless each object is explicitly constructed and connected by a proved map to the RC02 statistic.

Do not treat the two supplied external reports as evidence. They are hypothesis sources only.

## Decision statuses

Return exactly one primary status:

- `MODE5_UNIFORM_MECHANISM_CERTIFIED`
- `MODE5_FAMILY_STRATIFIED_MECHANISM`
- `MODE5_PROTOCOL_RELATIVE_ONLY`
- `SIMPLE_MODE5_EXPLANATIONS_FALSIFIED`
- `MODE5_MECHANISM_INCONCLUSIVE`

## Required deliverables

1. notation and domain table;
2. exact symbolic derivations;
3. theorem/counterexample ledger;
4. interval-certified bound package;
5. response-independent versus response-dependent dependency graph;
6. claim and non-claim matrix;
7. reproducible code and hashes;
8. explicit handoff stating whether P2 global gluing receives any usable uniform constant.

## Claim ceiling

A successful result may explain or bound the mode-5 preference within a declared finite or uniformly controlled carrier class. It may not infer arbitrary-level universality, category coherence, global gluing, continuum physics, time dynamics, mass, matter, or gravity.