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
- all-`d` Coxeter tomography upper bounds, currently `L_d^Cox <= 2 d^2`;
- structural lower bound `L_d^Cox >= floor(d^2/2)`.

Primary control file: `article-II-open-systems/PROOF-OBLIGATIONS.md`.

## Sharp minimal-design programme

Target:

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
7. Conditional odd-to-even transfer: `ER_d -> ER_(d+1)` for odd `d>=3`, using exactly `d+1` new faces, and the resulting even design is extension-ready.
8. `d=2` is an unavoidable exception: no two-face minimal design is extension-ready under scalar-one embedding. Therefore the all-dimensional ER programme begins at `d=3`.
9. The centered tangent compressed dependency determinant is proved nonzero for a suitable finite complete compression in every odd dimension `n>=3`.
10. The old one-parameter native-tilt route `H -> H+tS` is proved impossible: the cycle-holonomy Schur multiplier remains an exact kernel vector for every `t`, so all native tilt coefficients along that path vanish identically.
11. A transverse perturbation of one forbidden reverse-cycle binder entry, `Y_* -> Y_*+sE_(r-1,r)`, detects the holonomy coordinate at order `ts`; at fixed `t!=0` this is first order in `s`.
12. The finite native-projection coefficient is now proved nonzero for a suitable reverse-cycle index in every odd dimension. Therefore extension-ready minimal designs exist for every odd `n>=3`.
13. Combining all-odd ER with the proved odd-to-even transfer yields extension-ready minimal designs in every dimension `d>=3` and the sharp research theorem `L_d^Cox=floor(d^2/2)`.

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
- `ODD-D-EXTENSION-READY-v0.1.md` (audited; old all-odd claim withdrawn and superseded by the new centered proof chain)

## Exact current bottleneck

The mathematical existence gate for the sharp minimal-design count is CLOSED at research-note level.

The former final coefficient

`kappa_(n,r)(t)=R_t A_(t,r)h_q`

is proved nonzero for a suitable good compression and reverse-cycle index in every odd `n>=3`.

The key mechanism is:

- each reverse-cycle diagonal spike `d_r` lies in `im M_0` because all finite `H`-anchor row dependencies live on off-diagonal output blocks;
- a diagonal-block dual-basis coefficient reconstructs a nonzero `F(I)` value for a suitable spike;
- the singular Schur-complement controlled by invertible `D_n` shows `R_t d_r -> F_r^(0)(I)` as `t->0`;
- hence `R_t d_r !=0` for sufficiently small nonzero `t`, and the transverse first-order native tilt is nonzero.

Consequences:

- all odd dimensions admit extension-ready minimal designs;
- odd-to-even transfer supplies all even dimensions;
- the lower bound and construction match: `L_d^Cox=floor(d^2/2)` for every `d>=3`.

## Next permitted attack

Do **not** reopen the existence proof under a new name unless an audit finds a concrete gap.

The next phase is publication consolidation/audit of the sharp theorem:

- audit the complete dependency chain from centered tangent formulas through finite exponential lifting;
- make the transition from tangent faces to genuine Coxeter square faces explicit and publication-clean;
- reconcile the older `2d^2` upper-bound text and `PROOF-OBLIGATIONS.md` with the newly closed sharp theorem;
- state the `d=2` extension-ready exception without confusing it with the `d>=3` sharp count;
- audit theorem numbering, hypotheses, complex-vs-real rank conventions, and all generic/Zariski-open intersection arguments;
- only after that promote the result into the Article-II manuscript/publication package.

## Checkpoint discipline

For each research step append a short entry below:

- result/status;
- exact statement or obstruction;
- file containing proof/details;
- next single obligation.

### 2026-09-05 checkpoint 0

Repository/branch recovery completed. Existing branch and all recent theorem notes were found intact. No reconstruction from the two blocked chats is required; their committed mathematical output survives on GitHub. Current work resumes from the two centered-tangent final determinants above.

### 2026-09-05 checkpoint 1

**Result:** `det D_n` barrier CLOSED for all odd `n>=3`.

**Exact statement:** the cycle-factor reduction plus an explicit symmetric skeleton and finite Zariski-open transversality argument prove existence of a single complete finite `H`-anchor compression with invertible odd-cycle pivot and all non-cycle leading coefficients `theta_e` nonzero. Therefore the compressed dependency operator `D_n` is invertible.

**Proof file:** `article-I/research/ODD-ER-TRANSVERSALITY-CLOSURE-v0.1.md`.

**Supporting structural note:** `article-I/research/CENTERED-TANGENT-CYCLE-FACTOR-v0.1.md`.

**Next single obligation:** audit the native tilt variation.

### 2026-09-05 checkpoint 2

**Result:** old native-tilt direction refuted; transverse first-order detector proved.

**Exact statement:** for the old family with only `H -> H+tS`, the path-additive cycle-holonomy Schur multiplier `h_q` satisfies every face equation exactly for every `t`; hence the non-derivation kernel line is constant and `h_q(I)=0`, so all old `tau_n` coefficients vanish. If one also perturbs a reverse-cycle binder entry `Y_* -> Y_*+sE_(r-1,r)`, then the holonomy line produces diagonal defects `-tsq` in the two paired branches. At fixed `t!=0`, holonomy is therefore activated linearly in `s`.

**Proof file:** `article-I/research/NATIVE-TILT-ORDER-AUDIT-v0.1.md`.

**Numerical sanity only:** random finite compressions in `n=3,5` showed `||h(s)(I)||` proportional to `|s|` while `s=0` remained at numerical zero.

**Next single obligation:** prove `kappa_(n,r)(t)=R_t A_(t,r)h_q !=0` for at least one reverse-cycle index `r` on a complete-compression/cycle-pivot point, uniformly in every odd `n>=3`.

### 2026-09-05 checkpoint 3

**Result:** native projection CLOSED; all-odd ER CLOSED; sharp all-`d` count obtained at research-note level.

**Exact statement:** on a good finite complete `H`-anchor compression, reverse-cycle diagonal spikes lie in `im M_0`. For a suitable diagonal block, a nonzero dual identity coefficient gives an old-image preimage `F_r^(0)` with `F_r^(0)(I)!=0`. The singular-lift lemma, whose Schur complement is the already-invertible compressed dependency operator `D_n`, proves `R_t d_r -> F_r^(0)(I)` as `t->0`. Therefore `R_t d_r!=0` for small nonzero `t`, so `kappa_(n,r)(t)=-tqR_t d_r!=0`. The transverse perturbation moves the unique non-derivation kernel line out of `F(I)=0`, giving native full rank and extension-readiness in every odd dimension.

**Proof file:** `article-I/research/NATIVE-TILT-CLOSURE-ALL-ODD-ER-v0.1.md`.

**Consequence:** together with the proved odd-to-even transfer and the lower bound, `L_d^Cox=floor(d^2/2)` for all `d>=3` at research-note level.

**Next single obligation:** publication proof audit and manuscript consolidation; do not add new existence machinery unless the audit identifies a specific defect.
