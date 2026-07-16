# P3-B Jet Calculus - Preprint Readiness Gate

**Date:** 2026-07-16  
**Current state:** `V0_1_1_REVIEWED_G2_CLOSED_G3_REPRODUCIBILITY_NEXT`

## Publication thesis

The bounded preprint supports a recursive truncated-Taylor calculus for the declared finite two-channel trigonometric q-6j class, numerical cross-validation through matrix derivative order three and logarithmic-speed order two, and an Arb-certified common complex disk on which the angular speed is nonzero and admits a holomorphic logarithm.

## Gate status

### G1. Integrated manuscript - `CLOSED`

The corrected English manuscript is present under:

`bc_idpr/p3/operator_envelope/manuscript/finite_q6j_jet_calculus_v0.1.1-reviewed/`

The reviewed version has 15 pages and includes the full theorem architecture, related-work boundary, claim ledger, appendices and supplementary artifact map.

### G2. Theorem-level proof audit - `CLOSED`

All classified G2 findings were resolved in the manuscript:

- exact scalar q-6j and recoupling-matrix convention;
- explicit root-of-unity scope;
- algebraic carrier class separated from numerical validation;
- exact critical q-index ledger;
- transpose orthogonality rather than unitarity;
- holomorphic square-root and logarithm branches;
- exact Taylor-Cauchy remainder formula;
- differentiation-route cross-validation wording;
- bounded formal-versus-tested order claims.

The complete disposition is recorded in:

`manuscript/finite_q6j_jet_calculus_v0.1.1-reviewed/G2_RESPONSE_MATRIX.md`

### G2-R. Rigorous interval conditioning - `CLOSED`

The theorem uses `python-flint` Arb ball arithmetic with outward rounding:

- primary precision: 192 bits;
- control precision: 256 bits;
- outer radius: `pi/120`;
- certified radius: `pi/1200`;
- Taylor order: 50;
- exact carrier class: 283 ordered carriers in 24 families;
- canonical Arb evaluations: 24, extended by tetrahedral symmetry;
- rigorous worst-carrier lower bound: `0.16025264148217666`;
- worst family: `(1,1,1,1)`.

### Corrected manuscript cycle v0.1.1 reviewed - `CLOSED`

Build and review status:

- two-pass pdfLaTeX: successful;
- pages: 15;
- unresolved references: 0;
- undefined citations: 0;
- overfull boxes: 0;
- underfull boxes: 0;
- PDF metadata: present;
- fonts: embedded;
- 180-dpi visual audit: pass;
- exact 283-carrier supplementary JSON: present.

Review certificate:

`manuscript/finite_q6j_jet_calculus_v0.1.1-reviewed/REVIEW_CERTIFICATE.json`

### G3. Clean-checkout reproducibility package - `OPEN_NEXT`

Required closure items:

1. perform a clean checkout at the reviewed manuscript commit;
2. record Python, NumPy, pytest, python-flint and FLINT/Arb versions;
3. run all manuscript-relevant tests and certificate builders;
4. regenerate certificates and compare byte-for-byte or canonically with committed outputs;
5. compile the manuscript from the clean checkout;
6. record commands, hashes and wall-clock runtimes in a release manifest.

### G4. Bibliography and related-work boundary - `PARTIALLY_CLOSED`

The reviewed manuscript includes direct references for q-recoupling conventions, tetrahedral symmetry, asymptotic geometry, complex analysis and Arb arithmetic. Remaining work is the final field/DOI verification during the release cycle.

### G5. Release hygiene - `PARTIALLY_CLOSED`

Still required:

- final release version/date/DOI metadata;
- license and CITATION metadata;
- Zenodo title, abstract, keywords and related identifiers;
- repository archive link;
- final clean-build PDF visual audit.

## Readiness decision

The mathematical and manuscript-review phases are complete. No further exploratory research is required for this bounded preprint. The next blocking task is G3 clean-checkout reproducibility, followed by final G4/G5 release packaging.

Operational estimate: one focused reproducibility cycle plus one release-metadata cycle.

No statement from the Gemini advisory report is used as evidence.
