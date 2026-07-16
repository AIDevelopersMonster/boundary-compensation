# P3-B Jet Calculus — Preprint Readiness Gate

**Date:** 2026-07-16  
**Current state:** `THEOREM_AUDIT_COMPLETE_INTERVAL_CERTIFICATION_REQUIRED`

## Publication thesis

The bounded preprint may claim a recursive truncated-Taylor calculus for the declared finite two-channel q-6j class, analytic formulas through matrix derivative order three, and numerical validation on the frozen new-label atlas. A rigorous common nonvanishing complex disk remains conditional on interval-certified arithmetic.

## Gate status

### G1. Integrated manuscript — `CLOSED_AT_V0.1.0_DRAFT`

A coherent 12-page English manuscript and bibliography source are present under:

`bc_idpr/p3/operator_envelope/manuscript/finite_q6j_jet_calculus_v0.1.0/`

### G2. Theorem-level proof audit — `CONDITIONAL_PASS_ONE_PUBLICATION_BLOCKER`

The following parts passed:

- doubled-spin channel combinatorics and parity;
- finite q-Racah argument ordering;
- truncated-Taylor reciprocal and square-root recurrences;
- generator recurrence;
- formal logarithm recurrence;
- slope and curvature corollaries;
- bounded validation ceiling and claim firewall.

Required clarifications concern the exact q-6j convention, root-of-unity admissibility, the algebraic carrier class, orthogonality domain, analytic logarithm language, critical q-index derivation, square-root branches and the exact Cauchy-tail formula.

The publication blocker is the uniform-conditioning theorem. The present radius implementation uses ordinary floating-point arithmetic and pytest self-consistency checks. It does not yet provide outward-rounded interval enclosures. Therefore the claimed positive lower bound on the full complex disk is not a rigorous computer-assisted theorem in its current form.

Full audit:

`manuscript/finite_q6j_jet_calculus_v0.1.0/G2_THEOREM_LEVEL_AUDIT.md`

### G2-R. Rigorous interval conditioning — `OPEN_NEXT`

Preferred closure path:

1. implement interval or ball arithmetic with directed outward rounding;
2. enclose all q-number, q-factorial, square-root, Racah and angular-speed operations;
3. certify the order-50 remainder and every one of the 283 carrier margins;
4. publish per-carrier interval margins and precision metadata;
5. rerun the theorem audit against the interval certificate.

Fallback path: downgrade the theorem to an explicitly numerical conditioning experiment and remove rigorous `inf`, `>=` and `computer-assisted proof` language.

### G3. Clean reproducibility package — `OPEN`

Record exact Python, NumPy, pytest and interval-library versions, repository commit, commands, runtimes, generated-certificate hashes and equality with committed outputs.

### G4. Bibliography and related-work boundary — `PARTIALLY_CLOSED`

The initial primary-source set exists. Remaining work includes DOI and metadata verification, a direct reference for the exact finite q-Racah convention and a final audit of the asymptotic-geometry boundary.

### G5. Publication hygiene — `PARTIALLY_CLOSED`

Draft compilation and visual audit passed. Final version metadata, theorem corrections, clean build, bibliography audit, license, Zenodo metadata and release PDF audit remain open.

## Readiness decision

The analytic jet-calculus core is publication-worthy. The preprint is not yet upload-ready while the uniform-disk result is presented as a rigorous theorem without interval-certified arithmetic.

After G2-R is closed, the remaining tasks are one corrected manuscript cycle and one clean reproducibility/release cycle. A realistic estimate is **1–3 focused working days if interval certification succeeds without forcing a smaller radius**. A smaller rigorously certified radius is acceptable and preferable to retaining an uncertified larger one.

No statement from the Gemini advisory report is used as evidence.