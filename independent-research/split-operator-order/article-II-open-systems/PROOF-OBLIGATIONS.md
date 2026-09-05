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
- Reproducible finite-field builders are present for `d=3`, `d=4`, and `d=5`; the `d=4` builder has been independently executed and rebuilt the full `256 x 225` matrix with rank `225` modulo `1000033`.
- Generic open-dense full-rank consequence for the certified low-dimensional templates.
- All-d Weyl generator-defect theorem and generalized flat-loop tomography of order `Theta(d^2)`.
- Engineered Coxeter squares realizing arbitrary target first-two edge transports `U,V in SU(d)`.
- Historical all-d Coxeter upper bounds `3d^2-1` and `2d^2` remain valid constructive designs.
- Exact scalar-count lower bound `L_d^Cox >= floor(d^2/2)`.
- Block-extension audit: automatic extension-readiness is false.
- Local-plane sharp induction is false.
- Structural embedded-rank theorem: every old-face family embedded through `M_d direct-sum C subset M_(d+1)` factors through the normalized restriction quotient, with ceiling `(d^2-1)(d+1)^2 + 2*1_(d even)`.
- Exact parity-dependent deficiency whenever that ceiling is attained.
- Global binding lemma: an extension-ready even stage admits sharp minimal completion to the next odd native-full stage.
- Binder-compatible centered tangent theorem: for every odd `n>=3`, the finite compressed dependency determinant `D_n` is invertible on the reverse-cycle-zero parameter space actually used by the native-tilt proof.
- Native-tilt closure: a transverse reverse-cycle perturbation moves the unique non-derivation kernel line out of `F(I)=0`, yielding extension-ready minimal designs in every odd `n>=3`.
- Repaired odd-to-even transfer: for every odd `d>=3`, `ER_d -> ER_(d+1)` using exactly `d+1` new faces. The proof is carried out directly in the centered scalar-one convention and directly in `SL_(d+1)(C)`; the earlier post hoc scalar determinant-normalization argument is withdrawn.
- Therefore extension-ready minimal Coxeter designs exist in every dimension `d>=3`.
- Consequently the sharp first-order Coxeter face count is

  `L_d^Cox = floor(d^2/2)`

  for every `d>=3` in the bounded finite-dimensional model of this programme.

## Immediate open obligations

The sharp existence/count problem is closed. The remaining immediate obligations are publication and robustness tasks:

1. Consolidate the sharp theorem chain into a publication-clean Article-II manuscript version with explicit dependency map and theorem numbering.
2. Mark older `2d^2`, `3d^2-1`, and “sharp conjecture open” notes as historical/superseded in their status text without deleting them.
3. Audit the full sharp construction against Lindbladian learning, process tomography, quantum-control identifiability, and channel-holonomy literature.
4. Verify all bibliography entries, DOI/version/date metadata, ORCID, licence, and repository links.
5. Compile the final source and visually inspect the PDF.
6. Execute the committed `d=5` builder in a clean environment and record reproducibility output alongside the already re-run `d=4` certificate.
7. Establish exact finite-field certificates for retained `d=6,7` examples only if they remain in the publication package as independent computational illustrations; they are no longer needed for the all-d existence theorem.
8. Establish conditioning/noise bounds. Identifiability and numerical stability remain separate claims.

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
- numerical full rank is required for the all-d theorem beyond the exact proof chain;
- the even-dimensional Clifford implementation can be treated by the simplified odd-dimensional `SL(2,Z_d)` parametrization without the standard central-extension convention;
- the construction defines physical gauge or spacetime curvature.

## Sharp-theorem audit references

The publication-proof control chain is:

- `article-I/research/BINDER-COMPATIBLE-TRANSVERSALITY-REPAIR-v0.1.md`;
- `article-I/research/NATIVE-TILT-CLOSURE-ALL-ODD-ER-v0.1.md`;
- `article-I/research/ODD-TO-EVEN-TRANSFER-AUDIT-REPAIR-v0.1.md`;
- `article-I/research/SHARP-COXETER-PUBLICATION-AUDIT-2026-09-05.md`.

Current audit release status for the theorem package: `REVIEWABLE_DRAFT` pending manuscript/source/bibliography/render consolidation.
