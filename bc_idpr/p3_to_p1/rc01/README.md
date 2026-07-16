# BC-IDPR P3→P1 Research Contract 01

**Title:** Phase-Resolved Residual Modulation on the Certified Finite Quantum-6j Atlas  
**Status:** `PILOT_COMPLETED / CALIBRATION_BLOCKED / CONFIRMATORY_UNTOUCHED`  
**Date:** 2026-07-17  
**Programme:** Boundary Compensation / BC-IDPR

This package records the first prospective transition from the completed P3 independent-deformation analytic core to P1 phase-resolved residual analysis.

## RC01 decision

The pilot-only implementation was executed on exactly four preregistered pilot families, containing 64 ordered carriers. No calibration or confirmatory carrier was evaluated.

The software and contamination guards passed. However, a response-independent predictor-identifiability audit proved that the frozen positive criterion is unreachable. After cubic baseline removal, each integer q-mode is almost collinear with its paired half-integer control. The largest possible energy advantage is

\[
0.003670726619615724,
\]

while the frozen confirmatory threshold is

\[
0.02.
\]

Therefore calibration is not authorized under RC01. The confirmatory families remain sealed and untouched. Further work requires a new contract identifier with a redesigned predictor/control geometry.

## Frozen preregistration files

- `P3_CLOSURE_AND_HANDOFF_NOTE.md` — closes the bounded P3 analytic core and declares the admissible P3→P1 interface.
- `RESEARCH_CONTRACT_01.md` — human-readable scientific contract.
- `PREREGISTRATION_v0.1.0.json` — machine-readable preregistration.
- `FROZEN_FAMILY_SPLIT.json` — exact family-disjoint split and deterministic derivation rule.
- `PREREGISTRATION_SCHEMA.json` — structural schema for the preregistration record.
- `OUTCOME_DECISION_TABLE.md` — frozen A/B/C/D decision logic.
- `CHANGE_CONTROL.md` — rules for pilot fixes, calibration freeze and confirmatory unsealing.
- `validate_preregistration.py` — dependency-free structural validator.
- `PREREGISTRATION_CERTIFICATE.json` — hash and validation certificate.

## Pilot and review triage

The `pilot/` directory contains:

- the non-inferential pilot report;
- the exact predictor-identifiability audit;
- the calibration stop decision;
- the executable response-independent reachability audit;
- a deferred research backlog extracted from the external review.

The review-derived backlog is explicitly outside RC01 and requires new contracts before computation.

## Upstream authority

Published English article:

**Recursive Jet Calculus and Rigorous Uniform Conditioning for Finite Quantum 6j Recoupling Matrices**, v0.1.2, DOI `10.5281/zenodo.21401141`.

The exact carrier supplement is pinned by:

- repository path: `bc_idpr/p3/operator_envelope/manuscript/finite_q6j_jet_calculus_v0.1.1-reviewed/supplementary/declared_carriers_283.json`;
- Git blob SHA: `6485ceb3a4f34ee771d38ddf8f63a59d43b2608b`;
- SHA-256: `a8bcfb1038a288df29e4c76e4ef7ac8d711516df9d42c5da29e7f01a4fe79eb1`.

## Current transition state

```text
P3_LOCAL_FINITE_LABEL_ANALYTIC_CORE: CLOSED
P3_UNBOUNDED_LABEL_EXTENSION: OPEN
P3_CONTINUUM_INTERPRETATION: BLOCKED
P3_TO_P1_INTERFACE: PILOT_COMPLETED
RC01_CALIBRATION: NOT_AUTHORIZED
RC01_CONFIRMATORY: SEALED_AND_UNTOUCHED
NEXT_REQUIRED_ARTIFACT: BC-IDPR-P3-P1-RC02
```

No statement from the Gemini advisory report is used as evidence.