# G3 Clean-Checkout Reproducibility Report

**Date:** 2026-07-16  
**Repository:** `AIDevelopersMonster/boundary-compensation`  
**Pinned reviewed commit:** `3a53966637ec41a309e4d6f6551e903ba60af644`  
**Verdict:** `G3_CLOSED_WITH_DOCUMENTED_CONNECTOR_EXPORT_SUBSTITUTION`

## 1. Checkout boundary

A normal network `git clone` was attempted first and failed because the execution container could not resolve `github.com`. No claim of a literal network clone is made.

The fallback was an isolated connector-export checkout pinned to the reviewed commit. Every executable manuscript dependency used in the run was verified against its Git blob SHA. The reviewed manuscript source tree and PDF were additionally verified against the commit's 16-entry SHA-256 manifest. Previously generated local files were used only as byte transport after their hashes matched the GitHub commit; they were not treated as independent authority.

## 2. Environment

- Python `3.13.5`
- NumPy `2.3.5`
- pytest `9.0.2`
- python-flint `0.9.0`
- FLINT `3.6.0`
- pdfTeX `1.40.26`
- TeX Live `2025/dev`
- git `2.47.3`

## 3. Source identity

The following Git blob identities matched the pinned repository objects:

| Artifact | Git blob SHA |
|---|---|
| unified jet source | `12155b425b5ff09fe3846acc3dede6650be55fd3` |
| unified jet tests | `4dcc0c43a3adf06c40ebabd8321a8de4fde04e56` |
| unified jet certificate | `904c3d18c65e1ec6c02c9136dfc5e973a6672d2a` |
| G2-R Arb source | `ce39e102e51c9206aeb8e48d233d5655ff0a7d91` |
| G2-R tests | `bf91bfd1b16827cb1cfbd2f761796593b7898647` |
| G2-R certificate | `b5c492b993e7d9965d04c0ca98262af383561c63` |

## 4. Consolidated manuscript test suite

Command:

```bash
python -m pytest -q \
  bc_idpr/p3/operator_envelope/tests/test_finite_q6j_jet_calculus.py \
  bc_idpr/p3/operator_envelope/tests/test_g2r_interval_conditioning.py
```

Result:

```text
22 passed in 14.08s
```

External wall time was `19.20 s`; maximum resident memory was `371884 KiB`.

The unified jet suite covers the M10-M12 analytic response chain through matrix derivative order three and log-speed order two. The G2-R suite covers the outward-rounded common-disk theorem at 192 and 256 bits.

## 5. Certificate regeneration

### Unified jet synthesis

- Status reproduced: `FINITE_Q6J_RECURSIVE_JET_CALCULUS_CERTIFIED_THROUGH_LOG_ORDER_2`.
- Test atlas reproduced: 208 ordered carriers in 15 held-out families.
- Builder wall time: `6.73 s`.
- Generated JSON was canonically identical to the committed certificate.

### G2-R interval conditioning

- Status reproduced: `RIGOROUS_ARB_UNIFORM_CONDITIONING_CERTIFIED`.
- Strict lower endpoint reproduced: `0.16025264148217666`.
- Builder internal runtime: `8.713462829589844 s`.
- Builder external wall time: `11.00 s`.
- Generated JSON was canonically identical to the committed certificate after excluding the intentionally volatile `runtime_seconds` field and the manually recorded test-count metadata.

## 6. Supplementary carrier set

The published `declared_carriers_283.json` was compared directly with the exact algebraic generator in the G2-R source:

- ordered carrier sets equal: `true`;
- carrier count: `283`;
- unordered family sets equal: `true`;
- family count: `24`.

## 7. Clean manuscript build

The reviewed 16-entry source/PDF SHA-256 ledger passed without mismatch.

The source-only manuscript tree was copied to an empty directory and built with:

```bash
SOURCE_DATE_EPOCH=1784226293
FORCE_SOURCE_DATE=1
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Four passes are required for the table of contents and cross-references to reach the committed visual state. The clean output has:

- pages: `15`;
- SHA-256: `62de23bfe0ca978fd78b74d1fc65ee1973ea038154ecd770494d2ace2e4722d2`;
- unresolved references: `0`;
- undefined citations: `0`;
- overfull boxes: `0`;
- underfull boxes: `0`.

A second source-only build produced the same PDF byte for byte. The clean deterministic PDF differs in binary hash from the reviewed PDF because the reviewed PDF used a different creation timestamp, but a 150-dpi render comparison found `0` changed pages across all 15 pages.

PDF preflight confirmed that the clean document is openable, unencrypted, text-based, uses embedded fonts, and contains 28 outline entries.

## 8. Gate decision

- `G3_SOURCE_IDENTITY`: `CLOSED`;
- `G3_TEST_SUITE`: `CLOSED`;
- `G3_CERTIFICATE_REGENERATION`: `CLOSED`;
- `G3_SUPPLEMENT_CONSISTENCY`: `CLOSED`;
- `G3_DETERMINISTIC_PDF_BUILD`: `CLOSED`;
- `G3_OVERALL`: `CLOSED_WITH_DOCUMENTED_CONNECTOR_EXPORT_SUBSTITUTION`.

The substitution is operational, not mathematical: the normal clone transport was unavailable, while all used bytes were tied to the pinned GitHub commit by Git blob or SHA-256 identity.

The next gate is final G4 bibliography verification and G5 release packaging.

No statement from the Gemini advisory report is used as evidence.
