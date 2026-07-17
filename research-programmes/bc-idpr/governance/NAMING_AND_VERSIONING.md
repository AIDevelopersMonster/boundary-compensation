# BC-IDPR Naming and Versioning Rules

## Canonical identifiers

Programme: `BC-IDPR`

Workstream identifiers:

- `BC-IDPR-P3` — Independent Deformation.
- `BC-IDPR-CERT` — Parameter-Separation Certification.
- `BC-IDPR-P1` — Phase-Resolved Response.
- `BC-IDPR-SYN` — Synthesis, rigidity, universality, or null-result article.

## File naming

Use lowercase ASCII paths in GitHub:

`bc-idpr-<workstream>-<artifact>-v<major>.<minor>.<patch>-<status>.<ext>`

Examples:

- `bc-idpr-p3-contract-v0.1.0-draft.md`
- `bc-idpr-p1-preregistration-v0.1.0-frozen.yaml`
- `bc-idpr-cert-leakage-report-v0.1.1-reviewed.md`

Google Drive display names may use title case, but must retain the same identifier and version.

## Allowed status suffixes

- `skeleton`
- `draft`
- `internal-review`
- `reviewed`
- `clean`
- `preregistered`
- `frozen`
- `publication-ready`
- `published`
- `superseded`

Do not use `final` before publication. After publication, record DOI and immutable release tag instead of relying on the word final.

## Version rule

- Patch: editorial, metadata, citation, rendering, or non-claim-changing correction.
- Minor: new theorem, experiment, section, benchmark, or materially extended argument inside the declared claim ceiling.
- Major: changed programme contract, object class, or claim ceiling.

## Cross-surface identity

Every substantive artifact must carry:

1. canonical identifier;
2. title;
3. version;
4. status;
5. date;
6. author and ORCID where publication-facing;
7. GitHub path or release;
8. Drive file ID or link when mirrored;
9. predecessor and successor relations;
10. current release gate.
