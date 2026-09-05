# Split Operator Order — active handoff

**Branch:** `research/split-operator-order-article-II-v0.1`  
**Checkpoint date:** 2026-09-06  
**Author:** Malachevsky, A.A.  
**ORCID:** 0009-0008-6009-3196

## Rule for future chats

Read this file first, then the cited control notes. Do not reconstruct the programme from chat memory. After every nontrivial theorem, obstruction, audit repair, manuscript promotion, or publication-status change, update this file before continuing.

## Article I

The published Article-I core is frozen. The post-publication research line developed sharp first-order Coxeter tomography / extension-ready minimal designs. Do not rewrite the frozen publication core to absorb these later results.

## Article II — current publication state

Directory:

`article-II-open-systems/`

Current publication-consolidation manuscript:

`article-II-open-systems/manuscript-v0.2.0-en.md`

Working title:

*Context Reduction in Open Quantum Systems: Multiplicativity Defects, Lindblad Order Holonomy, and Sharp Coxeter Tomography*.

Current release level:

`REVIEWED_CLEAN / RENDER_AUDIT_PENDING`.

Primary control files:

- `article-II-open-systems/PROOF-OBLIGATIONS.md`;
- `article-II-open-systems/LITERATURE-NOVELTY-AUDIT-v0.2.md`;
- `article-II-open-systems/LEGACY-STATUS-v0.2.md`;
- `article-I/research/SHARP-COXETER-PUBLICATION-AUDIT-2026-09-05.md`.

## Bounded analytical core

Established results include:

- exact reduced-loop decomposition by multiplicativity defects;
- UCP norm certificate and multiplicative-domain flatness;
- exact nested-reduction composition law;
- Stinespring leakage formula;
- exact semigroup evolution and Duhamel representation;
- bounded GKSL Leibniz defect;
- exact Lindblad loop-holonomy integral;
- exact dephasing, depolarizing, and amplitude-damping braid-loop examples;
- finite-time closed-loop channel-identifiability no-go;
- first-order generator identifiability modulo Hamiltonian derivations;
- exact qubit, qutrit, `d=4`, and `d=5` certificates.

## Sharp Coxeter theorem

In the declared bounded finite-dimensional matrix-valued first-order Coxeter-face measurement model,

`L_d^Cox=floor(d^2/2)`

for every `d>=3`.

The quotient dimension is

`N_d=(d^2-1)^2`,

and one matrix-valued face supplies at most `2d^2` real coordinates, giving the matching lower bound.

The all-dimensional theorem is algebraic; it does not extrapolate from low-dimensional numerical rank data.

## Audited proof chain

1. Structural scalar-one restriction quotient:

   `R_res(d)=(d^2-1)(d+1)^2+2`.

2. Extension-ready minimal-design criterion and parity ceiling.
3. Centered odd-dimensional tangent formulas.
4. Complete one-anchor regular kernel and finite `H`-anchor compression.
5. Cycle factorization of the compressed dependency determinant `D_n`.
6. Binder-compatible transversality inside the reverse-cycle-zero subspace.
7. Exact no-go for the old one-parameter native tilt.
8. Reverse-cycle transverse detector and finite reconstruction coefficient `kappa_(n,r)(t)`.
9. Nonzero native projection and extension-ready minimal designs in every odd dimension.
10. Odd-to-even transfer rebuilt directly in the exact centered scalar-one convention and directly in `SL_n(C)`.
11. Return to genuine unitary Coxeter faces by `SU(n)` Zariski density and engineered contextual-square realization.

## Two critical audit repairs

### Binder-subspace repair

The ambient-space Zariski argument did not imply intersection with the proper reverse-cycle-zero binder subspace. This genuine gap is repaired in:

`article-I/research/BINDER-COMPATIBLE-TRANSVERSALITY-REPAIR-v0.1.md`.

### Determinant-normalization repair

The original odd-to-even transfer used post hoc scalar determinant normalization. That is invalid after scalar-one embedding because

`diag(cA,1)`

is not a scalar multiple of

`diag(A,1)`.

The old normalization step is withdrawn. The transfer is rebuilt directly in `SL_n(C)` in:

`article-I/research/ODD-TO-EVEN-TRANSFER-AUDIT-REPAIR-v0.1.md`.

## `d=2` boundary

No two-face design is extension-ready under scalar-one embedding `M_2 -> M_3`. This is only an extension-readiness obstruction. It does not state that native two-face tomography in `d=2` is impossible.

The sharp theorem is intentionally `d>=3`.

## Literature / novelty boundary

Targeted audit is recorded in:

`article-II-open-systems/LITERATURE-NOVELTY-AUDIT-v0.2.md`.

Standard infrastructure is not claimed as new: Stinespring dilation, Choi Schwarz/multiplicative-domain theory, GKSL/Lindblad generators, noncommutative carre-du-champ methods, and general Lindbladian/Liouvillian learning.

The reduced product defect is explicitly distinguished from Jamiołkowski/Uhlmann-type channel holonomy.

Safe wording: `we derive`, `we prove in the present operator-order setting`, and `the contribution is the coupling of these structures`. Do not use universal priority language such as `first` or `new invariant` without a stronger specialist priority audit.

## Reproducibility

The repository contains deterministic checks for the braid-loop examples and exact low-dimensional rank certificates.

The `d=5` builder reconstructs a `600 x 576` finite-field matrix modulo `1000033` and certifies rank `576`. It has been independently re-executed during publication consolidation with output:

`prime=1000033 shape=600x576 rank=576`

`CERTIFIED_FULL_COLUMN_RANK_OVER_Q`.

This is a reproducibility check, not part of the all-dimensional proof.

## Historical notes

Older `3d^2-1` and `2d^2` all-dimensional constructions remain valid but are historical upper bounds. Older notes saying the sharp count is open are retained as research history and must not be used as current control statements.

See:

`article-II-open-systems/LEGACY-STATUS-v0.2.md`.

## Current publication gate

Mathematical existence blockers: **none currently identified**.

Targeted related-work/claim-boundary audit: complete.

Author/ORCID: verified.

Repository licence: MIT at repository level.

Article-specific Zenodo DOI: not yet assigned; do not invent one.

Final LaTeX/source compilation: pending.

PDF visual inspection: pending.

A small manuscript preflight item remains: in Theorem 16.1 the even-dimensional face-count line is typographically written as

`(d-1)^2-1 over 2 + d`.

The intended and algebraically correct expression is

`((d-1)^2-1)/2 + d = d^2/2`.

Correct this in the final source; it does not change the theorem.

## Next permitted attack

Do not reopen the existence proof unless a concrete new mathematical defect is found.

Next phase:

1. prepare publication LaTeX/source from `manuscript-v0.2.0-en.md`, applying the small Theorem-16 typography correction;
2. perform equation/theorem/cross-reference and bibliography formatting audit;
3. compile PDF and visually inspect it;
4. only after render audit promote to `PUBLICATION_READY_PENDING_RENDER_AUDIT` / `PUBLICATION_READY` as appropriate;
5. prepare article-specific Zenodo metadata only when the final version and DOI workflow are ready.

## Checkpoint 6 — 2026-09-06

**Result:** Article-II publication consolidation completed at manuscript level.

**New manuscript:** `article-II-open-systems/manuscript-v0.2.0-en.md`.

**Literature audit:** `article-II-open-systems/LITERATURE-NOVELTY-AUDIT-v0.2.md`.

**Legacy-control map:** `article-II-open-systems/LEGACY-STATUS-v0.2.md`.

**README:** promoted to v0.2 publication state.

**Reproducibility:** exact `d=5` finite-field certificate re-run successfully.

**Current release status:** `REVIEWED_CLEAN`; render/source audit remains.
