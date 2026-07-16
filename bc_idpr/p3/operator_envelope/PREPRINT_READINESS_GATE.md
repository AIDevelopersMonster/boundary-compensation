# P3-B Jet Calculus — Preprint Readiness Gate

**Date:** 2026-07-16  
**Current state:** `G2_INTERVAL_BLOCKER_CLOSED_CORRECTED_MANUSCRIPT_NEXT`

## Publication thesis

The bounded preprint may claim a recursive truncated-Taylor calculus for the declared finite two-channel q-6j class, analytic formulas through matrix derivative order three, numerical validation on the frozen new-label atlas, and an Arb-certified common complex disk on which the angular speed is nonzero and admits a holomorphic logarithm.

## Gate status

### G1. Integrated manuscript — `CLOSED_AT_V0.1.0_DRAFT`

A coherent 12-page English manuscript and bibliography source are present under:

`bc_idpr/p3/operator_envelope/manuscript/finite_q6j_jet_calculus_v0.1.0/`

### G2. Theorem-level proof audit — `PASS_WITH_MANUSCRIPT_CORRECTIONS`

The analytic core passed:

- doubled-spin channel combinatorics and parity;
- finite q-Racah argument ordering;
- truncated-Taylor reciprocal and square-root recurrences;
- generator recurrence;
- formal logarithm recurrence;
- slope and curvature corollaries;
- bounded validation ceiling and claim firewall.

The full audit identified one critical blocker: the uniform-conditioning theorem was originally supported by ordinary `float64` arithmetic rather than outward-rounded enclosures.

Full audit:

`manuscript/finite_q6j_jet_calculus_v0.1.0/G2_THEOREM_LEVEL_AUDIT.md`

### G2-R. Rigorous interval conditioning — `CLOSED`

The replacement module uses `python-flint` Arb ball arithmetic with outward rounding:

- primary precision: 192 bits;
- control precision: 256 bits;
- outer radius: `pi/120`;
- certified radius: `pi/1200`;
- Taylor order: 50;
- algebraic carrier class: 283 ordered carriers in 24 families;
- canonical Arb evaluations: 24, extended to all ordered carriers by tetrahedral q-6j symmetry;
- rigorous worst-carrier lower bound: `0.16025264148217666`;
- worst family: `(1,1,1,1)`.

The positive lower endpoint survives both precision runs. Therefore:

- `float64_blocker`: `CLOSED`;
- `uniform_nonvanishing_theorem`: `RIGOROUSLY_CERTIFIED`;
- `holomorphic_logarithm_on_common_disk`: `CLOSED`;
- `G2_overall`: `PASS_WITH_MANUSCRIPT_CORRECTIONS`.

Artifacts:

- `BC-IDPR-P3-B-G2-R.md`;
- `src/g2r_interval_conditioning.py`;
- `tests/test_g2r_interval_conditioning.py`;
- `outputs/g2r_interval_conditioning_certificate.json`;
- `reviews/g2r_interval_conditioning_audit_v0.1.0.md`.

### Corrected manuscript cycle — `OPEN_NEXT`

Required corrections are now non-exploratory:

1. state the exact q-6j normalization and root-of-unity scope;
2. separate algebraic and certified carrier classes;
3. add the square-root and tetrahedral-symmetry lemmas;
4. derive the critical q-index maximum 10;
5. insert the exact Arb Taylor-Cauchy lower-bound formula;
6. distinguish the holomorphic logarithm from `log abs(omega)` on the real line;
7. classify finite-difference checks as an independent differentiation route;
8. update theorem and abstract wording from float64 certificate to Arb proof.

### G3. Clean reproducibility package — `OPEN`

Record exact Python, NumPy, pytest, python-flint and FLINT/Arb versions, repository commit, commands, runtimes, generated-certificate hashes and equality with committed outputs.

### G4. Bibliography and related-work boundary — `PARTIALLY_CLOSED`

The initial primary-source set exists. Remaining work includes DOI and metadata verification, a direct reference for the exact finite q-Racah convention, a primary tetrahedral-symmetry citation and final audit of the asymptotic-geometry boundary.

### G5. Publication hygiene — `PARTIALLY_CLOSED`

Draft compilation and visual audit passed. Final version metadata, theorem corrections, clean build, bibliography audit, license, Zenodo metadata and release PDF audit remain open.

## Readiness decision

The critical mathematical blocker is closed. No additional exploratory research is required for the bounded preprint. The next task is one corrected manuscript cycle, followed by clean reproducibility and release packaging.

Operational estimate from the present state: **1–2 focused working days**.

No statement from the Gemini advisory report is used as evidence.
