# Publication Audit — Cheshire-Cat Perspective v0.2

**Document type:** Perspective + Research Programme  
**Author:** Malachevsky, A.A. / Малачевский А.А.  
**ORCID:** 0009-0008-6009-3196  
**Date:** 2026-09-06  
**Audit mode:** `AUDIT_ONLY_BEFORE_PUBLICATION_BUILD`

## Declared claim ceiling

The paper may restate proved results from Articles I–II, derive direct norm/commutant consequences, and formulate explicitly labelled conjectures/research questions. It may not identify reduced loop defects with physical gauge/spacetime curvature, claim a universal decoherence/entropy measure, claim generic efficient Lindbladian tomography, or claim a process-tensor extension before construction.

## Findings

| ID | Severity | Location | Problem | Why it matters | Minimal repair | Claim-set effect |
|---|---|---|---|---|---|---|
| A01 | C1 | Proposition 6.2 | Positivity/equality statement is tied to a chosen GKSL representation. | A different representation can change individual noise operators. | Keep the explicit phrase “in a fixed GKSL representation” and do not promote it to a representation-independent observable. | clarifies |
| A02 | C1 | Proposition 7.1 | The `O(t^2)` remainder is pointwise for a fixed finite loop; no uniformity in dimension/design is established. | Article III will need quantitative asymptotics. | State “for a fixed finite loop as t→0”; do not infer dimension-uniform stability. | clarifies |
| A03 | C2 | Protected-sector discussion | Multiplicative domains and noiseless/correctable structures are established literature. | Broad novelty wording would be false. | Frame only a quantitative transport-restricted bound as conjectural. | narrows |
| A04 | C2 | Carré-du-champ discussion | `Gamma_L` is close to established noncommutative carré-du-champ structures. | Calling it new quantum curvature would inflate the claim. | Retain “Leibniz defect / carré-du-champ-type” language and pose loop coupling as the open question. | narrows |
| A05 | C2 | Holonomy terminology | Established channel holonomy uses a different Uhlmann/Jamiołkowski framework. | Terminology collision can imply equivalence. | Use “reduced order holonomy” only with an explicit boundary paragraph. | clarifies |
| A06 | C2 | Article III motivation | Current Lindbladian learning literature already treats sample complexity, shadows, sparse/ansatz-free learning, and hardness. | “First practical tomography” claims would be unsupportable. | Restrict novelty target to conditioning/oversampling of the specific Coxeter loop measurement model. | narrows |
| A07 | C2 | Non-Markovian section | Process tensors and multitime tomography are established. | The paper must not imply a new theory of quantum memory. | Pose only an embedding/compatibility problem for the multiplicativity-defect composition law. | narrows |
| A08 | C4 | Bibliography | Four foundational CP/GKSL references were absent from manuscript v0.2; Lidar metadata were abbreviated; one recent process-tensor Perspective was incompletely identified. | Standalone attribution and metadata consistency are required. | Add Stinespring, Choi, GKS, Lindblad; expand Lidar; omit the incompletely verified Perspective. | none |
| A09 | C4 | 2026 learning references | Birke, Romanov, Chen–Yu, Cheng–Bao are arXiv preprints. | Publication status must not be blurred. | Label all four explicitly as preprints in EN/RU. | clarifies |
| A10 | C3 | Series handoff | Pair reduction in Article I is not CP/UCP reduction in Article II. | Silent identification would break programme architecture. | Preserve the paragraph stating that the relation is conceptual, not equality of reductions. | clarifies |
| A11 | C5 | Numbering | Markdown v0.2 has mixed Proposition/Research Question labels but no final LaTeX numbering yet. | Publication hygiene. | Resolve during LaTeX conversion; assign stable proposition/conjecture/equation labels. | none |
| A12 | C5 | Metadata | Article-specific licence for the bridge paper is not yet fixed. | Zenodo/publication metadata incomplete. | `AUTHOR_DECISION_REQUIRED` before final publication package. | none |
| A13 | C5 | Rendering | No final LaTeX/PDF exists yet. | Visual audit mandatory. | Build EN/RU PDF, compile cleanly, render every page, inspect. | none |

## Mathematical audit summary

No C0 mathematical defect was found in the five direct propositions as presently stated, provided the fixed-loop and fixed-GKSL-representation qualifications are retained. The loop norm bound follows from the exact Article-II decomposition plus UCP contractivity. Multiplicative-domain flatness is immediate. Noise-commutant vanishing follows termwise from the GKSL Leibniz-defect formula. The positivity identity follows by substituting `(A*,A)`. The small-time norm bound is valid for a fixed finite loop from the Article-II first-order expansion.

## Claim firewall after audit

**Green:** exact inherited identities; direct propositions; sharp Coxeter count only in the declared matrix-valued first-order model.

**Yellow:** protected-sector quantitative bounds; robust Coxeter designs; loop-coupled carré-du-champ geometry; categorical/cohomological realization; process-tensor embedding; effective geometry.

**Red:** spacetime/gauge curvature; universal decoherence or entropy-production interpretation; equivalence with standard quantum-channel holonomy; first/general efficient Lindbladian tomography; invention of process tensors.

## Final audit block

- unresolved blocking issues: bibliography patches must be merged into final EN/RU manuscripts; article-specific licence unresolved; PDF not yet built;
- equations/theorems changed: no mathematical change, only required hypothesis/interpretation qualifiers;
- claim set changed: yes — narrowed relative to the earliest perspective draft;
- bibliography verified: **partial-to-review level**; journal/DOI metadata and recent arXiv status checked, but final bibliography must be rechecked after LaTeX conversion;
- metadata verified: partial;
- source compiled: not supplied;
- PDF visually inspected: not supplied;
- release status: `REVIEWABLE_DRAFT`.
