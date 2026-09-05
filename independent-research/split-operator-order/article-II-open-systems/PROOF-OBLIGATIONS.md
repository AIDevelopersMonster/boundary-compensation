# Article II — proof obligations and claim firewall

## Proved in the current bounded core

- Exact reduced-loop decomposition into transported multiplicativity defects.
- UCP multiplicativity-defect norm certificate.
- Multiplicative-domain flatness criterion.
- Exact composition law for multiplicativity defects under nested reductions.
- Layer-resolved defect identity for finite context-reduction chains.
- Two-sided backtracking/Schwarz-defect characterization for unitary transports.
- Stinespring defect formula and squared-leakage form of backtracking defect.
- Exact semigroup evolution equation for `Delta_t`.
- Exact Duhamel representation of `Delta_t`.
- GKSL Leibniz-defect formula for bounded Lindblad operators.
- Exact positive evolution formula for the Schwarz defect.
- Exact integral representation of reduced loop holonomy for uniformly continuous UCP semigroups.
- First-order reduced-loop expansion as a corollary of the exact integral theorem.
- Exact benchmark channel calculations for dephasing, depolarization, and amplitude damping.
- Strong finite-channel no-go: complete closed-loop holonomy data can fail to identify a UCP channel.
- Full bilinear `Gamma_L` determines a bounded generator on `M_d` modulo Hamiltonian derivations.
- General finite-dimensional rank criterion: universal first-order contextual-loop identifiability iff rank is `(d^2-1)^2`.
- Complete qubit theorem: one braid plus two backtracks identify all nine dissipative parameters modulo Hamiltonian derivations.
- Exact minimal Coxeter-face designs for `d=3,4,5`, each saturating `floor(d^2/2)`.
- Reproducible finite-field builders are present for `d=3`, `d=4`, and `d=5`; the `d=5` builder has been independently re-executed and rebuilt the full `600 x 576` matrix with rank `576` modulo `1000033`.
- Generic open-dense full-rank consequence for the certified low-dimensional templates.
- All-d Weyl generator-defect theorem and generalized flat-loop tomography of order `Theta(d^2)`.
- Engineered Coxeter squares realizing arbitrary target first-two edge transports `U,V in SU(d)`.
- Historical all-d Coxeter upper bounds `3d^2-1` and `2d^2` remain valid constructive designs.
- Exact scalar-count lower bound `L_d^Cox >= floor(d^2/2)`.
- Block-extension audit: automatic extension-readiness is false.
- Local-plane sharp induction is false.
- Structural embedded-rank theorem with scalar-one ceiling `(d^2-1)(d+1)^2 + 2*1_(d even)`.
- Global binding lemma for sharp completion.
- Binder-compatible centered tangent theorem for every odd `n>=3`.
- Native-tilt closure and extension-ready minimal designs in every odd dimension.
- Repaired odd-to-even transfer carried out directly in centered scalar-one coordinates and directly in `SL_(d+1)(C)`.
- Therefore extension-ready minimal Coxeter designs exist in every dimension `d>=3`.
- Consequently

  `L_d^Cox = floor(d^2/2)`

  for every `d>=3` in the bounded finite-dimensional matrix-valued first-order Coxeter-face model.

## Publication consolidation completed

The sharp theorem chain has been consolidated into:

- `manuscript-v0.2.0-en.md` — publication-consolidation manuscript;
- `publication-v0.2.1/main.tex` — numbered LaTeX publication master;
- `publication-v0.2.1/sharp-proof-appendix.tex` — publication-compressed sharp-proof chain;
- `LITERATURE-NOVELTY-AUDIT-v0.2.md` — targeted source/claim-boundary audit;
- `LEGACY-STATUS-v0.2.md` — historical-result control map.

The former typography defect in the even-dimensional face-count proof has been corrected in the LaTeX source to

`((d-1)^2-1)/2 + d = d^2/2`.

A deterministic GitHub Actions LaTeX build workflow is present at

`.github/workflows/article-ii-publication.yml`.

## Immediate open obligations

The existence/count proof problem is closed. Only publication/render and longer-range robustness obligations remain:

1. Obtain a clean compiled PDF from the v0.2.1 LaTeX package.
2. Inspect the LaTeX log for output-affecting warnings/errors.
3. Visually inspect every PDF page for clipping, overfull equations, broken glyphs, orphan headings, bad references, and bibliography defects.
4. Repair any C5 source/render defects and rebuild.
5. After a clean render audit, promote the paper to `PUBLICATION_READY`.
6. Prepare the article-specific Zenodo metadata/deposit package only after the final rendered version is frozen; do not invent a DOI beforehand.
7. Establish conditioning/noise/sample-complexity bounds only as a separate later research problem.

## Longer-range analytical obligations

1. Universal monotonicity of reduced curvature under successive CP reductions is not proved.
2. Infinite-dimensional extension with unbounded GKSL generators remains open.
3. Equality with any standard decoherence/information-loss monotone is not established.
4. A general operational interpretation in terms of channel capacity, entropy production, or recoverability is not established.
5. No physical gauge/spacetime curvature claim is made.
6. Non-Markovian/process-tensor generalization is deferred.

## Claim firewall

Do not state without proof that:

- finite closed-loop holonomies identify an arbitrary UCP channel;
- local Lindblad identifiability contradicts the finite-time channel no-go;
- `||H||`, `||H-I||`, or `||Delta||` is monotone under further UCP reductions;
- reduced order holonomy is a decoherence monotone;
- every minimal full-rank design is extension-ready;
- the structural embedded-rank ceiling is automatically attained by every minimal design;
- local two-level square faces alone suffice for sharp induction;
- the sharp face-count theorem implies good conditioning or noise robustness;
- the sharp Coxeter count is a universal lower bound for arbitrary process tomography or arbitrary Lindbladian-learning protocols;
- numerical full rank is required for the all-d theorem beyond the exact proof chain;
- the even-dimensional Clifford implementation can be treated by the simplified odd-dimensional `SL(2,Z_d)` parametrization without the standard central-extension convention;
- the construction defines physical gauge or spacetime curvature.

## Sharp-theorem audit references

The publication-proof control chain is:

- `article-I/research/BINDER-COMPATIBLE-TRANSVERSALITY-REPAIR-v0.1.md`;
- `article-I/research/NATIVE-TILT-CLOSURE-ALL-ODD-ER-v0.1.md`;
- `article-I/research/ODD-TO-EVEN-TRANSFER-AUDIT-REPAIR-v0.1.md`;
- `article-I/research/SHARP-COXETER-PUBLICATION-AUDIT-2026-09-05.md`.

Current release status for the theorem/publication package:

`PUBLICATION_READY_PENDING_RENDER_AUDIT`.
