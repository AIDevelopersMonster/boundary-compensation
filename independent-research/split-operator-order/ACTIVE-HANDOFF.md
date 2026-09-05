# Split Operator Order — active handoff

**Branch:** `research/split-operator-order-article-II-v0.1`  
**Checkpoint date:** 2026-09-05  
**Author:** Malachevsky, A.A.  
**ORCID:** 0009-0008-6009-3196

## Rule for future chats

Read this file first, then the cited active notes. Do not reconstruct the programme from chat memory. After every nontrivial theorem, obstruction, counterexample, or change of target, update this handoff in the same branch before continuing.

## Article I

Publication core is frozen. The post-publication research line now studies sharp first-order Coxeter tomography / extension-ready minimal designs. Do not rewrite the published Article-I core to absorb these later results.

## Article II — open systems / context reduction

Directory: `article-II-open-systems/`.

Bounded analytical core already proved:

- exact reduced-loop decomposition by multiplicativity defects;
- multiplicative-domain flatness criterion;
- nested-reduction composition law;
- Stinespring leakage formula;
- exact semigroup/Duhamel defect formula;
- GKSL Leibniz defect and exact Lindblad loop-holonomy integral;
- exact dephasing, depolarizing and amplitude-damping braid-loop formulas;
- finite-channel closed-loop identifiability no-go;
- first-order generator identifiability modulo Hamiltonian derivations;
- full qubit and exact minimal `d=3,4,5` tomography certificates;
- all-`d` Coxeter tomography upper bounds, currently `L_d^Cox <= 2 d^2` in the publication-controlled notes;
- structural lower bound `L_d^Cox >= floor(d^2/2)`.

Primary control file: `article-II-open-systems/PROOF-OBLIGATIONS.md`.

## Sharp minimal-design programme

Research target:

`L_d^Cox = floor(d^2/2)` for every `d>=3`.

Important proved structure:

1. Embedded old faces factor through `B=M_d(C) direct-sum C`.
2. Restriction-quotient ceiling:

   `R_res(d)=(d^2-1)(d+1)^2+2`.

3. Embedded minimal-design ceiling:

   `rank M_d^up <= (d^2-1)(d+1)^2 + 2*1_(d even)`.

4. Automatic extension-readiness is false.
5. Local two-level sharp induction is false.
6. Global binding lemma: if an **even** `d` design is extension-ready, exactly `d` new global square faces give a sharp minimal full-rank design in `d+1`.
7. Conditional odd-to-even transfer: `ER_d -> ER_(d+1)` for odd `d>=3`, using exactly `d+1` new faces, and the resulting even design is extension-ready — **publication audit still pending on centered-coordinate consistency**.
8. `d=2` is an unavoidable exception: no two-face minimal design is extension-ready under scalar-one embedding. Therefore the all-dimensional ER programme begins at `d=3`.
9. The centered tangent compressed dependency determinant is proved nonzero for a suitable finite complete compression in every odd dimension `n>=3`.
10. The old one-parameter native-tilt route `H -> H+tS` is proved impossible: the cycle-holonomy Schur multiplier remains an exact kernel vector for every `t`, so all native tilt coefficients along that path vanish identically.
11. A transverse perturbation of one forbidden reverse-cycle binder entry, `Y_* -> Y_*+sE_(r-1,r)`, detects the holonomy coordinate at order `ts`; at fixed `t!=0` this is first order in `s`.
12. The finite native-projection coefficient is proved nonzero for a suitable reverse-cycle index in every odd dimension. Therefore extension-ready minimal designs exist for every odd `n>=3`.
13. A publication audit found one genuine parameter-space gap in the odd proof and it has been repaired: the `det D_n` good locus is now proved nonempty **inside the reverse-cycle-zero binder subspace itself**, not merely in the ambient sample space.
14. The sharp all-`d` equality remains a **research theorem pending transfer audit**, not yet publication-certified.

Relevant notes under `article-I/research/`:

- `GLOBAL-BINDING-LEMMA-v0.1.md`
- `ODD-TO-EVEN-EXTENSION-READY-v0.1.md`
- `D2-EXTENSION-READY-OBSTRUCTION-v0.1.md`
- `CENTERED-TANGENT-ODD-ER-v0.1.md`
- `CENTERED-TANGENT-COMPRESSION-AUDIT-v0.1.md`
- `CENTERED-TANGENT-CYCLE-FACTOR-v0.1.md`
- `ODD-ER-TRANSVERSALITY-CLOSURE-v0.1.md`
- `NATIVE-TILT-ORDER-AUDIT-v0.1.md`
- `NATIVE-TILT-CLOSURE-ALL-ODD-ER-v0.1.md`
- `BINDER-COMPATIBLE-TRANSVERSALITY-REPAIR-v0.1.md`
- `SHARP-COXETER-PUBLICATION-AUDIT-2026-09-05.md`
- `ODD-D-EXTENSION-READY-v0.1.md` (old all-odd claim withdrawn and superseded by the centered proof chain)

## Exact current state

### Odd dimensions

The odd-dimensional existence proof is now audit-repaired at the identified parameter-space point:

- complete compression;
- cycle pivot;
- all `theta_e != 0`;
- binder genericity with reverse-cycle zeros;
- nonzero dual identity coefficient;

are simultaneously attainable on the same irreducible restricted parameter space. The native projection closure therefore remains valid.

### All dimensions

The proposed sharp equality

`L_d^Cox=floor(d^2/2)`, `d>=3`,

still depends on the odd-to-even transfer. The transfer note is structurally promising and dimensionally consistent, but publication audit has flagged three unresolved mathematical/hypothesis issues:

1. re-derive the carrier in one exact scalar-one centered coordinate convention;
2. make the two-tail local/binding reduction explicit rather than relying on “same argument” shorthand;
3. justify determinant normalization / `SL_n(C)` / `SU(n)` realization without silently using rescaling covariance that may fail for centered formulas.

Until those are closed, do **not** promote the sharp equality into the main Article-II manuscript or `PROOF-OBLIGATIONS.md` as a publication-level theorem.

## Next permitted attack

Work only on the audit of `ODD-TO-EVEN-EXTENSION-READY-v0.1.md`.

Preferred order:

- derive all carrier formulas from `D(diag(A,a))=F(A-aI)` with explicit centered variables;
- verify the five-defect carrier rank in that convention;
- re-derive the two-tail local and graph-binding coefficients;
- parameterize directly in `SL_n(C)` or prove the exact normalization covariance needed;
- then invoke `SU(n)` Zariski density and the engineered contextual-square realization theorem.

Do not add new existence machinery unless this audit produces a real failure.

## Checkpoint discipline

For each research step append a short entry below:

- result/status;
- exact statement or obstruction;
- file containing proof/details;
- next single obligation.

### 2026-09-05 checkpoint 0

Repository/branch recovery completed. Existing branch and all recent theorem notes were found intact. Current work resumes from the centered-tangent final determinants.

### 2026-09-05 checkpoint 1

**Result:** `det D_n` barrier CLOSED for all odd `n>=3`.

**Proof files:** `CENTERED-TANGENT-CYCLE-FACTOR-v0.1.md`, `ODD-ER-TRANSVERSALITY-CLOSURE-v0.1.md`.

### 2026-09-05 checkpoint 2

**Result:** old native-tilt direction refuted; transverse first-order detector proved.

**Proof file:** `NATIVE-TILT-ORDER-AUDIT-v0.1.md`.

### 2026-09-05 checkpoint 3

**Result:** native projection CLOSED; all-odd ER CLOSED at research-note level.

**Proof file:** `NATIVE-TILT-CLOSURE-ALL-ODD-ER-v0.1.md`.

### 2026-09-05 checkpoint 4

**Result:** adversarial publication audit started. One concrete C0 gap in the odd proof was found and repaired.

**Gap:** prior transversality was proved in the ambient sample space, while the native-tilt construction requires the last sample to lie in the reverse-cycle-zero binder subspace. Ambient nonempty open does not imply nonempty intersection with a fixed proper subspace.

**Repair:** `BINDER-COMPATIBLE-TRANSVERSALITY-REPAIR-v0.1.md` proves all required odd good-locus conditions simultaneously inside the restricted irreducible affine space.

**Audit file:** `SHARP-COXETER-PUBLICATION-AUDIT-2026-09-05.md`.

**Release status:** `BLOCKED_MATHEMATICAL` for the **all-d publication claim**, due to unresolved odd-to-even transfer audit items A2–A4. The odd-dimensional theorem is not blocked by the repaired parameter-space issue.

**Next single obligation:** re-derive and certify `ODD-TO-EVEN-EXTENSION-READY-v0.1.md` in the exact centered scalar-one convention.
