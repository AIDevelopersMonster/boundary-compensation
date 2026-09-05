# Sharp Coxeter theorem — publication proof audit

**Date:** 2026-09-05  
**Author:** Malachevsky, A.A.  
**ORCID:** 0009-0008-6009-3196  
**Document type:** publication audit  
**Claim ceiling under audit:** `L_d^Cox=floor(d^2/2)` for every `d>=3` in the bounded finite-dimensional first-order Coxeter tomography model.

## Audit summary

The sharp theorem proof chain has now undergone two adversarial repairs.

First, the odd-dimensional centered-tangent proof contained a genuine parameter-space gap: nonempty Zariski-open conditions were proved in the full sample space but later intersected with the proper reverse-cycle-zero binder subspace. That gap was repaired by `BINDER-COMPATIBLE-TRANSVERSALITY-REPAIR-v0.1.md`, which proves all required good-locus conditions directly on the restricted irreducible affine space.

Second, the original odd-to-even transfer used centered scalar-one language but compressed several coordinate and determinant-normalization steps. The audit confirmed that the post hoc scalar-rescaling argument is invalid after scalar-one embedding: `diag(cA,1)` is not a scalar multiple of `diag(A,1)`. The transfer has therefore been re-derived from the exact normalized coordinate and rebuilt directly in `SL_n(C)` in `ODD-TO-EVEN-TRANSFER-AUDIT-REPAIR-v0.1.md`. No post hoc determinant normalization is used.

The mathematical existence blockers A1–A4 are now closed at research-proof level. The remaining work is manuscript consolidation, source support, numbering, metadata, and render audit.

## Mandatory findings

| ID | Severity | Location | Problem | Why it matters | Repair / disposition | Claim-set effect |
|---|---|---|---|---|---|---|
| A1 | C0 | odd native-tilt intersection step | Ambient nonempty Zariski-open conditions were intersected with a proper binder subspace without proving restricted nonemptiness. | Ambient density does not imply intersection with a fixed proper subspace. | **CLOSED.** `BINDER-COMPATIBLE-TRANSVERSALITY-REPAIR-v0.1.md` proves complete compression, cycle pivot, all `theta_e`, binder genericity and dual-identity nonvanishing directly on the reverse-cycle-zero irreducible space. | none |
| A2 | C1 | old odd-to-even carrier, Sections 4–8 | Centered scalar-one and uncentered symbols were mixed. | This was the same failure mode that invalidated the earlier all-odd draft. | **CLOSED.** `ODD-TO-EVEN-TRANSFER-AUDIT-REPAIR-v0.1.md` derives the master branch formula from `D(diag(X,a))=F(X-aI)` and re-derives the carrier and scalar directions in that convention. | clarifies |
| A3 | C1 | old odd-to-even local/binding reduction | Two-tail reduction and two perturbation scales were imported by “same argument” shorthand. | The parity transfer depends on the exact exceptional kernel and Schur coefficients. | **CLOSED.** The repair note gives the typed two-tail determinant, exact first-scale determinant-one perturbation, exact second-scale determinant-one cross-plane perturbation, and graph binding. | clarifies |
| A4 | C1/C0 | old odd-to-even unitary return | Post hoc scalar determinant normalization was treated as rank harmless after scalar-one embedding. | That covariance is false in the embedded centered problem. | **CLOSED BY REPLACEMENT.** The rescaling step is withdrawn. Carrier and local families are parameterized directly in `SL_n(C)` before rank calculation; only then is `SU(n)` Zariski density invoked, followed by engineered-square realization. | clarifies |
| A5 | C2 | control wording | Sharp equality was called a research theorem before transfer audit. | Publication wording had to stay below the audited claim ceiling. | **CLOSED mathematically.** The theorem may now be promoted in the research control plane; manuscript promotion still waits for formal/source audit. | expands presentation to audited theorem |
| A6 | C5 | `PROOF-OBLIGATIONS.md`, older optimal/upper-bound notes | Older control files still describe the sharp count as open. | They now contradict the audited proof chain. | **OPEN FORMAL REPAIR.** Update control files and mark older bounds/conjecture sections superseded, without deleting historical notes. | none |
| A7 | C5/C4 | main Article-II manuscript and references | Main manuscript does not yet contain the sharp theorem chain; bibliography/related-work boundary has not been re-audited for this larger claim. | Publication package must expose dependencies and distinguish new theorem from standard infrastructure. | **OPEN PUBLICATION TASK.** Prepare a new manuscript version with compact theorem chain and appendices/research-note dependency map, then audit bibliography and metadata. | none |

## Mathematical chain accepted after audit

The following components are accepted at research-proof level:

1. scalar-one centered tangent formulas for the four embedded sectors;
2. complete one-anchor regular kernel and finite complete `H`-anchor compression;
3. cycle-factor reduction and binder-compatible nonvanishing of `D_n` for every odd `n>=3`;
4. exact no-go for the old one-parameter native tilt;
5. reverse-cycle first-order holonomy detector;
6. singular-lift reconstruction and nonzero native-projection coefficient;
7. extension-ready minimal designs in every odd dimension `n>=3`;
8. corrected odd-to-even extension-ready transfer, built directly in `SL_n(C)` with explicit two-tail local and graph-binding reductions;
9. return to genuine unitary Coxeter faces via `SU(n)` Zariski density plus the engineered contextual-square realization theorem;
10. the information-theoretic lower bound `L_d^Cox>=floor(d^2/2)`.

Therefore, within the declared finite-dimensional first-order Coxeter tomography model,

`L_d^Cox=floor(d^2/2)`

is mathematically supported for every `d>=3`.

The `d=2` obstruction remains only an obstruction to **extension-readiness** of two-face designs under scalar-one embedding; it is not a statement that native two-face tomography in `d=2` is impossible.

## Publication boundary

The sharp theorem does not imply conditioning, noise robustness, finite-time UCP-channel identifiability, monotonicity of reduced curvature under arbitrary CP reductions, or any physical spacetime/gauge-curvature interpretation.

Older `2d^2` and `3d^2-1` constructions remain valid historical upper bounds and independent constructive designs; they are no longer the best face-count theorem.

## Release gate

Unresolved blocking mathematical issues: **none currently identified**.

Unresolved publication issues: A6, A7; full related-work/bibliography audit; source compilation and PDF visual inspection.

Equations/theorems changed: the odd-to-even transfer proof was replaced by a centered determinant-one repair; the old scalar-normalization justification is withdrawn.

Claim set changed: **yes**, from `RESEARCH_THEOREM_PENDING_TRANSFER_AUDIT` to mathematically audited sharp theorem in the declared model.

Bibliography verified: partial.

Metadata verified: partial.

Source compiled: not supplied.

PDF visually inspected: not supplied.

**Release status:** `REVIEWABLE_DRAFT`

## Next single obligation

Reconcile the Article-II control files and prepare a publication-clean theorem section in a new manuscript version. Then run bibliography/related-work, numbering, metadata, source compilation and PDF render audit before any Zenodo release.
