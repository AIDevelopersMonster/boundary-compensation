# Sharp Coxeter theorem — publication proof audit

**Date:** 2026-09-05  
**Author:** Malachevsky, A.A.  
**ORCID:** 0009-0008-6009-3196  
**Document type:** publication audit  
**Claim ceiling under audit:** `L_d^Cox=floor(d^2/2)` for every `d>=3` in the bounded finite-dimensional first-order Coxeter tomography model.

## Audit summary

The odd-dimensional centered-tangent chain has been re-audited through the native-tilt closure. One concrete parameter-space gap was found and repaired in `BINDER-COMPATIBLE-TRANSVERSALITY-REPAIR-v0.1.md`: the previous full-space Zariski-open argument did not by itself imply nonempty intersection with the reverse-cycle-zero binder subspace required later. The repair proves the complete-compression, cycle-pivot, all-`theta_e`, binder-generic, and dual-identity conditions simultaneously on that restricted irreducible affine space.

The remaining publication blocker is the **odd-to-even transfer theorem**. Its argument is structurally strong and dimension counts are consistent, but the current note mixes centered scalar-one language with formulas written in uncentered symbols `C,D,u,v`, and the final passage from the complex witness to genuine unitary Coxeter faces is compressed. Before the sharp all-`d` equality is promoted into the main manuscript, this transfer must be rewritten in one coordinate convention from start to finish and its determinant-normalization / unitary-realization step must be explicitly checked.

## Mandatory findings

| ID | Severity | Location | Problem | Why it matters | Minimal repair | Claim-set effect |
|---|---|---|---|---|---|---|
| A1 | C0 | `NATIVE-TILT-CLOSURE-ALL-ODD-ER-v0.1.md`, intersection step | Full-space nonempty Zariski-open conditions were intersected with a proper reverse-cycle-zero binder subspace without a separate nonemptiness proof. | A dense open subset of the ambient affine space may miss a fixed proper linear subspace. | **REPAIRED** by `BINDER-COMPATIBLE-TRANSVERSALITY-REPAIR-v0.1.md`, which proves nonemptiness on the restricted irreducible parameter space. | none after repair |
| A2 | C1 | `ODD-TO-EVEN-EXTENSION-READY-v0.1.md`, Sections 4–8 | The carrier proof says it is using centered coordinates, but several formulas are expressed as `F(CD)-F(C)D-CF(D)` and `phi(CD)-phi(C)-phi(D)` while the actual scalar-one embedding depends on centered differences against the tail scalar. The note needs one explicit declaration of what `C,D` denote in each formula and a derivation from the normalized block coordinate `D(diag(A,a))=F(A-aI)`. | This is exactly the coordinate issue that invalidated the earlier odd-dimensional draft. Publication cannot rely on an implicit convention here. | Re-derive the carrier formulas directly from the scalar-one block embedding and state the centered variables explicitly. Verify all `T_+`, `T_-`, `s_ab^±`, `Delta_nn`, `Delta_NN` formulas in that convention. | clarifies; may narrow if a formula changes |
| A3 | C1 | `ODD-TO-EVEN-EXTENSION-READY-v0.1.md`, Sections 9–11 | “The same entrywise determinant argument” and the first/second binding-scale formulas are imported from earlier local/global lemmas but not re-derived for the two-dimensional scalar tail. | The transfer theorem depends on these exact relative-kernel and Schur-coefficient statements. A publication proof needs either a formal reduction lemma or an explicit calculation. | Add a typed reduction lemma mapping the two-tail variables to the earlier local-kernel calculation, then give the two short coefficient computations. | clarifies |
| A4 | C1 | `ODD-TO-EVEN-EXTENSION-READY-v0.1.md`, Section 13 | The proof moves from a complexified witness to `SU(n)` by Zariski density and then invokes the engineered-square theorem. The determinant-normalization step is stated but not checked against the centered scalar-one measurement formulas. | Scalar rescaling is harmless for the uncentered Leibniz defect, but the centered embedded formulas contain `A-I`, `B-I` terms; publication must show the selected maximal minor is a regular function on the chosen `SL_n` parameterization and that the normalization used does not alter the claimed rank locus. | Parameterize the carrier/local faces directly in `SL_n(C)` (or prove the exact rank covariance under the normalization actually used), then invoke `SU(n)` Zariski density and the engineered contextual-square lemma from `ALL-D-COXETER-OD2-v0.1.md`. | clarifies / unknown until checked |
| A5 | C2 | `ACTIVE-HANDOFF.md`, `NATIVE-TILT-CLOSURE-ALL-ODD-ER-v0.1.md` | The sharp equality is currently labeled a research theorem before the odd-to-even transfer receives the centered-coordinate audit above. | Research-note status is acceptable internally, but manuscript promotion would overstate the audited state. | Keep equality marked `RESEARCH_THEOREM_PENDING_TRANSFER_AUDIT`; do not update the main manuscript or `PROOF-OBLIGATIONS.md` to “proved all-d” until A2–A4 are closed. | narrows presentation only |
| A6 | C5 | `article-II-open-systems/PROOF-OBLIGATIONS.md`, `OPTIMAL-COXETER-DESIGNS-v0.1.md`, older upper-bound notes | Control files still say the sharp all-`d` conjecture is open and the best all-`d` upper bound is `2d^2`. | Once the proof audit passes these will become contradictory publication metadata. | Update only after A2–A4 close; retain history by marking older notes superseded rather than deleting them. | none |
| A7 | C5 | Main Article-II manuscript | The current manuscript v0.1.0 does not contain the sharp minimal-design theorem chain and still has analytical-core status. | A theorem of this size needs a dedicated theorem section, dependency statement, and related-work boundary rather than a silent insertion. | After proof audit, prepare a new manuscript version with a compact theorem chain and appendices/research-note references. | none |

## Odd-dimensional chain status

The following components are presently accepted after audit:

- correct scalar-one centered tangent formulas;
- complete one-anchor regular kernel;
- finite complete `H`-anchor compression;
- cycle-factor reduction of `D_n`;
- all-odd nonvanishing of `D_n` **on the binder-compatible restricted parameter space**, after the new repair note;
- exact no-go for the old one-parameter native tilt;
- first-order reverse-cycle holonomy detector;
- singular-lift reconstruction argument;
- nonzero native projection coefficient and all-odd extension-ready existence.

The low-dimensional `d=2` obstruction is logically separate and correctly states only failure of **extension-readiness**, not failure of native two-face tomography.

## Release gate

Unresolved blocking issues: A2, A3, A4.

Equations/theorems changed in this audit: no existing theorem text rewritten; one new repair theorem added in `BINDER-COMPATIBLE-TRANSVERSALITY-REPAIR-v0.1.md`.

Claim set changed: **no** for the odd-dimensional result after repair; **all-d promotion remains conditional on transfer audit**.

Bibliography verified: partial.

Metadata verified: partial.

Source compiled: not supplied.

PDF visually inspected: not supplied.

**Release status:** `BLOCKED_MATHEMATICAL`

## Next single obligation

Re-derive and audit `ODD-TO-EVEN-EXTENSION-READY-v0.1.md` entirely in the corrected scalar-one centered coordinate convention. Do not work on new existence machinery until that transfer theorem is either certified or repaired.
