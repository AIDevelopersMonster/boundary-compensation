# P3-B Jet Calculus — Preprint Readiness Gate

**Date:** 2026-07-16  
**Current state:** `INTEGRATED_DRAFT_READY_FOR_THEOREM_AUDIT`

## Publication thesis

The preprint may claim that, inside the declared finite two-channel regular chamber, the finite q-6j recoupling matrix admits a recursive truncated-Taylor jet calculus; the anchor speed, its logarithmic slope and its logarithmic curvature are reproduced analytically on an independent new-label atlas; and a uniform complex disk supports common nonvanishing and Cauchy conditioning bounds.

## Closed mathematical gates

1. Exact finite q-6j derivative construction through matrix order three.
2. Recursive jet calculus replacing three hand-expanded derivative chains.
3. Independent validation on 208 ordered carriers in 15 new-label families.
4. Full declared conditioning class: 283 ordered carriers in 24 families.
5. Uniform q-wall and branch separation.
6. Uniform nonvanishing of the angular speed on a common disk.
7. Confirmatory sharp-radius certificate with
   \[
   R_{\rm cert}=0.1R_{\rm wall}.
   \]
8. Claim firewall excluding physical interpretation and universal continuum claims.

## Publication gates

### G1. Integrated manuscript — `CLOSED_AT_V0.1.0_DRAFT`

A coherent 12-page English manuscript has been assembled with:

- problem, scope and non-claims;
- doubled-spin and channel conventions;
- the finite q-Racah formula;
- truncated-Taylor algebra lemma;
- recoupling-generator recurrence;
- log-speed jet corollaries;
- independent validation atlas and numerical protocol;
- computer-assisted uniform-conditioning theorem;
- related-work boundary;
- reproducibility protocol;
- claim firewall and appendices.

The sectioned LaTeX project is stored under:

`bc_idpr/p3/operator_envelope/manuscript/finite_q6j_jet_calculus_v0.1.0/`

### G2. Theorem-level proof audit — `OPEN_NEXT`

Check every assumption and index convention, especially:

- doubled-spin conventions and parity;
- correspondence between channel order and q-6j arguments;
- phase and gauge conventions;
- branch selection for all square roots;
- regularity of the finite Racah expression;
- proof of coefficient recurrences;
- distinction between formal all-order recurrence and validated orders;
- exact status of the order-50 Taylor–Cauchy remainder;
- classification of analytic versus computer-assisted claims.

### G3. Reproducibility package — `OPEN`

Run all manuscript-relevant tests from a clean checkout and record:

- Python, NumPy and pytest versions;
- deterministic commands;
- repository commit;
- generated certificates;
- hashes of source, tests and outputs;
- wall-clock runtime;
- proof that regenerated certificates equal the committed certificates.

### G4. Bibliography and related-work boundary — `PARTIALLY_CLOSED`

The draft contains an initial primary-source set covering:

- angular-momentum recoupling;
- quantum-group q-6j formulae;
- Turaev–Viro state sums;
- Ponzano–Regge and tetrahedral asymptotics;
- analytic perturbation;
- Cauchy estimates.

Remaining work:

- verify every bibliographic field and DOI;
- add a direct primary reference for the precise finite q-Racah convention if needed;
- verify the Taylor–Woodward publication metadata;
- audit wording that separates the present finite local-jet result from asymptotic geometry.

### G5. Publication hygiene — `PARTIALLY_CLOSED`

Closed at draft level:

- title, abstract and keywords;
- author and affiliation metadata;
- numbered definitions, lemmas, theorem, proposition, corollaries and equations;
- successful two-pass LaTeX compilation;
- 12-page PDF render and visual audit;
- no unresolved references, undefined citations or box warnings.

Still open:

- theorem-audit corrections;
- final version/date/DOI metadata;
- clean release build and hash manifest;
- final bibliography consistency audit;
- Zenodo metadata, license and repository archive link;
- final PDF visual audit after corrections.

## Readiness decision

The mathematical research phase required for a bounded preprint is complete, and the integrated v0.1.0 manuscript draft is complete. The next blocking task is the theorem-level proof audit, not additional exploratory research.

The preprint becomes upload-ready when G2 and G3 are closed and the remaining portions of G4 and G5 are finalized. At the current pace, the realistic remaining workload is:

1. one theorem-level audit cycle;
2. one corrected manuscript cycle;
3. one clean reproducibility and release cycle.

Operational estimate: **1–3 focused working days** from the present state, provided the theorem audit does not reveal a structural defect in the order-50 conditioning proof.

No statement from the Gemini advisory report is used as evidence.