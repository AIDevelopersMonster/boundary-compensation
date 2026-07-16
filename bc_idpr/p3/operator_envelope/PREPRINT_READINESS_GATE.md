# P3-B Jet Calculus - Preprint Readiness Gate

**Date:** 2026-07-16  
**Current state:** `G3_REPRODUCIBILITY_CLOSED_G4_G5_RELEASE_PACKAGING_NEXT`

## Publication thesis

The bounded preprint supports a recursive truncated-Taylor calculus for the declared finite two-channel trigonometric q-6j class, numerical cross-validation through matrix derivative order three and logarithmic-speed order two, and an Arb-certified common complex disk on which the angular speed is nonzero and admits a holomorphic logarithm.

## Gate status

### G1. Integrated manuscript - `CLOSED`

The corrected 15-page English manuscript is present under:

`bc_idpr/p3/operator_envelope/manuscript/finite_q6j_jet_calculus_v0.1.1-reviewed/`

### G2. Theorem-level proof audit - `CLOSED`

All classified G2 findings were resolved, including the exact q-6j convention, root-of-unity scope, algebraic carrier class, critical q-index ledger, transpose orthogonality, holomorphic square-root and logarithm branches, explicit Taylor-Cauchy remainder, and bounded formal-versus-tested order claims.

### G2-R. Rigorous interval conditioning - `CLOSED`

The outward-rounded Arb theorem uses:

- primary precision: 192 bits;
- control precision: 256 bits;
- outer radius: `pi/120`;
- certified radius: `pi/1200`;
- Taylor order: 50;
- exact class: 283 ordered carriers in 24 families;
- rigorous worst-carrier lower bound: `0.16025264148217666`;
- worst family: `(1,1,1,1)`.

### Corrected manuscript cycle v0.1.1 reviewed - `CLOSED`

- pages: 15;
- unresolved references: 0;
- undefined citations: 0;
- overfull boxes: 0;
- underfull boxes: 0;
- PDF metadata: present;
- fonts: embedded;
- visual audit: pass;
- exact 283-carrier supplement: present.

### G3. Clean-checkout reproducibility package - `CLOSED_WITH_DOCUMENTED_CONNECTOR_EXPORT_SUBSTITUTION`

A normal network clone was attempted but the execution container could not resolve `github.com`. G3 therefore used an isolated connector-export checkout pinned to reviewed commit:

`3a53966637ec41a309e4d6f6551e903ba60af644`

Every executable dependency was verified by Git blob SHA, and the manuscript tree was verified by its 16-entry SHA-256 manifest. No previous local work product was used as authority.

Environment:

- Python `3.13.5`;
- NumPy `2.3.5`;
- pytest `9.0.2`;
- python-flint `0.9.0`;
- FLINT `3.6.0`;
- pdfTeX `1.40.26`;
- TeX Live `2025/dev`.

Execution results:

- consolidated manuscript tests: `22 passed in 14.08s`;
- unified jet certificate: canonically identical to committed output;
- G2-R certificate: canonically identical after excluding volatile runtime and manually recorded test metadata;
- supplementary carrier set: exact match, 283 carriers in 24 families;
- clean deterministic PDF: 15 pages;
- clean PDF SHA-256: `62de23bfe0ca978fd78b74d1fc65ee1973ea038154ecd770494d2ace2e4722d2`;
- repeated clean build: byte-identical;
- reviewed-versus-clean render comparison: 0 changed pages at 150 dpi;
- PDF preflight: pass, embedded fonts, 28 outline entries.

Artifacts:

- `g3/G3_RELEASE_MANIFEST.json`;
- `g3/G3_REPRODUCIBILITY_REPORT.md`;
- `g3/G3_SOURCE_BLOBS.json`;
- `g3/requirements-g3.txt`;
- `g3/reproduce_g3.sh`;
- `g3/G3_SHA256SUMS.txt`.

### G4. Bibliography and related-work boundary - `OPEN_NEXT`

Required closure items:

1. verify every bibliographic field and DOI against primary publisher or archival sources;
2. verify the exact finite q-Racah convention citation;
3. verify the tetrahedral-symmetry citation;
4. confirm the wording separating this finite local result from asymptotic geometry;
5. freeze the final bibliography for release.

### G5. Release hygiene - `OPEN_NEXT`

Required closure items:

- final release version/date/DOI metadata;
- license and `CITATION.cff`;
- Zenodo title, abstract, keywords, communities and related identifiers;
- repository archive link;
- final release PDF and source archive;
- final visual and metadata audit.

## Readiness decision

The mathematical, theorem-audit, interval-certification, manuscript-review and reproducibility phases are complete. No further exploratory research is required for the bounded preprint.

The only remaining blocking task is the combined G4/G5 release cycle. Operational estimate: one focused release-packaging cycle.

No statement from the Gemini advisory report is used as evidence.
