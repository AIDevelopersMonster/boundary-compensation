# BC-IDPR Stage Gates

## Gate G0 — Architecture registered

Required:

- programme identifier and dependency graph;
- anti-duplication note against existing BC branches;
- claim firewall;
- naming and versioning rules;
- initial theorem-obligation graph.

Auditor: `BC Project Steward`.

## Gate G1 — P3 object defined

Required:

- typed definitions of `q`, `rho`, `xi`, and `vartheta`;
- admissible parameter domain;
- equivalence and gauge conventions;
- exact statement of what is fixed and what varies;
- one exact benchmark and one confounded negative control.

Failure status: `P3_OBJECT_NOT_WELL_TYPED`.

## Gate G2 — Independence certified

Required:

- exact or tolerance-based independence certificate;
- geometry leakage bound;
- representation-scale leakage bound;
- protocol and branch-identity stability;
- wall-distance and reset rules.

Failure statuses include `GEOMETRY_LEAKAGE`, `SCALE_LEAKAGE`, `BRANCH_IDENTITY_FAILURE`, and `CERTIFICATE_RESET`.

P1 work may not pass beyond protocol design until G2 is satisfied.

## Gate G3 — P1 preregistration frozen

Required:

- dense parameter grid;
- phase predictors;
- signed and complex observables;
- branch tracking;
- exclusions and wall policy;
- null models;
- model-selection hierarchy;
- held-out tests;
- multiple-testing controls;
- immutable preregistration checksum or tagged commit.

Failure status: `PREREGISTRATION_NOT_FROZEN`.

## Gate G4 — Experiment complete

Required:

- machine-readable outputs;
- environment and code version;
- full run log;
- negative controls;
- deviation log from preregistration;
- result classification, including valid null result.

Auditor: `BC Project Steward` for structural conformity, then `BC Publication Auditor` for scientific and publication review.

## Gate G5 — Manuscript reviewed clean

Required:

- theorem and assumption audit;
- formula and notation audit;
- source and bibliography audit;
- metadata and DOI audit;
- LaTeX and PDF render audit;
- final claim-set comparison against the registered ceiling.

Only `BC Publication Auditor` may recommend `PUBLICATION_READY`.

## Automatic invocation rule

Invoke `BC Project Steward` whenever creating, renaming, moving, splitting, merging, versioning, or registering any BC-IDPR artifact, issue, branch, folder, dataset, script, experiment, or manuscript. Invoke `BC Publication Auditor` at review, corrected-manuscript, PDF, Zenodo, arXiv, release, and publication stages.
