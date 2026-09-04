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
- All-d Coxeter tomography with constructive upper bound `3d^2-1`.
- Improved all-d Coxeter tomography with an order-three Clifford anchor and constructive upper bound `2d^2`.
- The order-three Clifford infrastructure has been audited with the even-dimensional caveat made explicit: the theorem uses the existence of a Zauner-type finite-Heisenberg implementer, not a naive odd-dimensional `SL(2,Z_d)` parametrization in every dimension.
- Exact scalar-count lower bound `L_d^Cox >= floor(d^2/2)`.
- Therefore the universal constant-factor gap is at most `4`.
- Numerical lower-bound saturation evidence extends to generic square-only designs for `d=6,7,8`.
- Block-extension audit: automatic extension-readiness is false. A recursively constructed exact minimal `d=5` design has embedded rank `833` in `M_6`, while generic minimal `d=5` designs can reach embedded rank `864`.
- Local-plane sharp induction is false: generic two-level square faces do not supply enough projected rank at the lower-bound face count.
- Exact recursive finite-field chain verified through: `d=3 rank 64`; embedded `3->4 rank 128`; `d=4 rank 225`; embedded recursive `4->5 rank 377`; `d=5 rank 576`; embedded recursive `5->6 rank 833`; `d=6 rank 1225`; embedded recursive `6->7 rank 1717`.

## Immediate open obligations

1. Replace the naive block-extension conjecture by a parity-controlled extension theorem for specially chosen extension-ready designs.
2. Prove or refute the sharp all-d Coxeter conjecture `L_d^Cox=floor(d^2/2)` for every `d>=3`.
3. Prove a structural formula for the maximal embedded rank of an extension-ready minimal design. Current generic evidence suggests
   `R_d^star=(d^2-1)(d+1)^2 + 2*1_(d even)`.
4. Characterize the cokernel of the embedded measurement map under the decomposition
   `su(d+1)=su(d) direct-sum W direct-sum R H`, and prove transversality of genuinely global square faces on that cokernel.
5. Determine a preserved induction invariant: current evidence suggests even stages should be extension-ready while odd stages may carry a controlled extension defect that is repaired in the next odd-to-even step.
6. Replace the existential second-anchor construction in the `2d^2` theorem by a publication-clean explicit deterministic family or concise standard theorem citation.
7. Execute the committed `d=5` builder in a clean environment and record the reproducibility output alongside the already re-run `d=4` certificate.
8. Establish exact finite-field certificates for any retained `d=6,7` lower-bound examples; numerical rank alone is not publication evidence.
9. Establish conditioning bounds; identifiability and numerical stability remain separate claims.
10. Audit the full construction against Lindbladian learning, process tomography, quantum-control identifiability, and channel-holonomy literature.

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
- local two-level square faces suffice for sharp induction;
- the exact lower-bound count `floor(d^2/2)` is proved for all dimensions;
- the `2d^2` upper bound is sharp;
- numerical full rank in dimensions beyond the exact certificates is already a theorem;
- a stored rank label without a matrix builder is an exact certificate;
- the even-dimensional Clifford implementation can be treated by the simplified odd-dimensional `SL(2,Z_d)` parametrization without the standard central-extension convention;
- the construction defines physical gauge or spacetime curvature.
