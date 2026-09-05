# Split Operator Order — active handoff

**Branch:** `research/split-operator-order-article-II-v0.1`  
**Checkpoint date:** 2026-09-05  
**Author:** Malachevsky, A.A.  
**ORCID:** 0009-0008-6009-3196

## Rule for future chats

Read this file first, then the cited active notes. Do not reconstruct the programme from chat memory. After every nontrivial theorem, obstruction, counterexample, audit repair, or change of target, update this handoff before continuing.

## Article I

Publication core is frozen. The post-publication research line studies sharp first-order Coxeter tomography / extension-ready minimal designs. Do not rewrite the published Article-I core to absorb these later results.

## Article II — open systems / context reduction

Directory: `article-II-open-systems/`.

The bounded analytical core is established: exact reduced-loop decomposition by multiplicativity defects; multiplicative-domain flatness; nested reduction law; Stinespring leakage; exact semigroup/Duhamel formulas; GKSL Leibniz defect; exact Lindblad loop-holonomy integral; explicit channel examples; finite-channel loop-only no-go; first-order generator identifiability modulo derivations; qubit and exact `d=3,4,5` certificates; generalized and Coxeter all-d `O(d^2)` constructions.

Primary control file:

`article-II-open-systems/PROOF-OBLIGATIONS.md`.

## Sharp minimal-design theorem

The information-theoretic lower bound is

`L_d^Cox >= floor(d^2/2)`.

The sharp existence theorem is now mathematically audit-closed at research-proof level:

`L_d^Cox = floor(d^2/2)`

for every `d>=3` in the bounded finite-dimensional first-order Coxeter tomography model.

Key proof chain:

1. Structural scalar-one restriction ceiling and extension-ready definition.
2. Global binding lemma for sharp completion.
3. Correct centered tangent formulas in odd dimension.
4. Finite complete `H`-anchor compression.
5. Cycle factorization and `det D_n` reduction.
6. Binder-compatible transversality repair proving the good locus inside the reverse-cycle-zero subspace actually required later.
7. Exact no-go for the old one-parameter native tilt.
8. Transverse reverse-cycle native detector and singular-lift reconstruction.
9. Native projection nonvanishing and all-odd extension-ready existence.
10. Audited odd-to-even transfer rebuilt directly in the centered scalar-one convention and directly in `SL_n(C)`.
11. Return to genuine unitary Coxeter faces through `SU(n)` Zariski density plus the engineered contextual-square realization theorem.

## Important audit corrections

### Odd-dimensional parameter-space repair

The previous ambient-space Zariski argument did not by itself imply intersection with the reverse-cycle-zero binder subspace. This was a real C0 gap and is repaired by:

`article-I/research/BINDER-COMPATIBLE-TRANSVERSALITY-REPAIR-v0.1.md`.

### Odd-to-even determinant-normalization repair

The original transfer note used a post hoc scalar determinant-normalization argument. That step is invalid after scalar-one embedding because

`diag(cA,1)`

is not a scalar multiple of

`diag(A,1)`.

The transfer was re-derived and repaired without that step. Carrier and local families are constructed directly in `SL_n(C)` before rank calculation. Repair note:

`article-I/research/ODD-TO-EVEN-TRANSFER-AUDIT-REPAIR-v0.1.md`.

This repair also gives the explicit two-tail local determinant, the determinant-one first binding scale, the determinant-one cross-plane second binding scale, and the graph-binding Schur lift.

## Current theorem/audit status

Mathematical existence blockers: **none currently identified**.

The sharp theorem package has audit status:

`REVIEWABLE_DRAFT`.

It is not yet `PUBLICATION_READY` because bibliography/related-work, manuscript consolidation, theorem/formula numbering, metadata, source compilation, and PDF visual inspection remain.

Publication audit file:

`article-I/research/SHARP-COXETER-PUBLICATION-AUDIT-2026-09-05.md`.

## Relevant notes

- `GLOBAL-BINDING-LEMMA-v0.1.md`
- `ODD-TO-EVEN-EXTENSION-READY-v0.1.md` — historical proof, superseded at its audited weak points by the repair note
- `ODD-TO-EVEN-TRANSFER-AUDIT-REPAIR-v0.1.md`
- `D2-EXTENSION-READY-OBSTRUCTION-v0.1.md`
- `CENTERED-TANGENT-ODD-ER-v0.1.md`
- `CENTERED-TANGENT-COMPRESSION-AUDIT-v0.1.md`
- `CENTERED-TANGENT-CYCLE-FACTOR-v0.1.md`
- `ODD-ER-TRANSVERSALITY-CLOSURE-v0.1.md`
- `BINDER-COMPATIBLE-TRANSVERSALITY-REPAIR-v0.1.md`
- `NATIVE-TILT-ORDER-AUDIT-v0.1.md`
- `NATIVE-TILT-CLOSURE-ALL-ODD-ER-v0.1.md`
- `SHARP-COXETER-PUBLICATION-AUDIT-2026-09-05.md`
- `ODD-D-EXTENSION-READY-v0.1.md` — old all-odd claim withdrawn; historical only

## `d=2` boundary

`d=2` remains a low-dimensional exception only for **minimal extension-readiness** under scalar-one embedding: no two-face design reaches the extension-ready restriction ceiling. This does not by itself rule out native two-face tomography.

The sharp theorem stated above is for `d>=3`.

## Next permitted attack

Do not add new existence machinery unless a later audit identifies a concrete mathematical defect.

The next phase is publication consolidation:

1. prepare a new Article-II manuscript version containing the sharp theorem chain in compact form;
2. mark older `2d^2`, `3d^2-1`, and “sharp conjecture open” notes as historical/superseded without deleting them;
3. audit related work and bibliography for the enlarged claim;
4. verify theorem/formula numbering, real-vs-complex rank conventions, DOI/version/date, ORCID, licence and repository metadata;
5. compile and visually inspect the final PDF before Zenodo.

## Checkpoints

### 2026-09-05 checkpoint 0

Repository/branch recovery completed.

### checkpoint 1

`det D_n` barrier closed for all odd `n>=3`.

### checkpoint 2

Old native-tilt path refuted; transverse first-order detector proved.

### checkpoint 3

Native projection closed; all-odd ER obtained at research-note level.

### checkpoint 4

Adversarial publication audit found and repaired the binder-subspace transversality gap. All-d promotion remained blocked pending odd-to-even transfer audit.

### checkpoint 5

**Result:** odd-to-even transfer audit CLOSED.

**Critical finding:** post hoc scalar determinant normalization in the old transfer proof is invalid in the scalar-one embedded problem.

**Repair:** `ODD-TO-EVEN-TRANSFER-AUDIT-REPAIR-v0.1.md` rebuilds the carrier and both binding scales directly in `SL_n(C)`, derives the exact centered scalar-one formulas, and certifies the unitary return through Zariski density plus engineered-square realization.

**Consequence:** mathematical blockers A1–A4 in the sharp theorem audit are closed. The sharp equality

`L_d^Cox=floor(d^2/2)`, `d>=3`,

is now mathematically audit-supported in the declared model.

**Next single obligation:** manuscript consolidation and publication/source audit, not further existence research.
