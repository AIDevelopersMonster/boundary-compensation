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
10. The old one-parameter native-tilt route `H -> H+tS` is now proved impossible: the cycle-holonomy Schur multiplier remains an exact kernel vector for every `t`, so all native tilt coefficients along that path vanish identically.
11. A transverse perturbation of one forbidden reverse-cycle binder entry, `Y_* -> Y_*+sE_(r-1,r)`, detects the holonomy coordinate at order `ts`; at fixed `t!=0` this is first order in `s`.

Relevant notes under `article-I/research/`:

- `GLOBAL-BINDING-LEMMA-v0.1.md`
- `ODD-TO-EVEN-EXTENSION-READY-v0.1.md`
- `D2-EXTENSION-READY-OBSTRUCTION-v0.1.md`
- `CENTERED-TANGENT-ODD-ER-v0.1.md`
- `CENTERED-TANGENT-COMPRESSION-AUDIT-v0.1.md`
- `CENTERED-TANGENT-CYCLE-FACTOR-v0.1.md`
- `ODD-ER-TRANSVERSALITY-CLOSURE-v0.1.md`
- `NATIVE-TILT-ORDER-AUDIT-v0.1.md`
- `ODD-D-EXTENSION-READY-v0.1.md` (audited; old all-odd claim withdrawn)

## Exact current bottleneck

The compressed row-dependency determinant barrier is CLOSED for every odd `n>=3`.

The old native tilt scalar `tau_n` along the same `H+tS` path is not merely unproved: it is identically zero to all orders.

The true remaining obstruction is now the finite-compression native projection coefficient

`kappa_(n,r)(t)=R_t A_(t,r) h_q`,

where:

- `M_t` is a full-row-rank embedded regular measurement map at fixed `t!=0`;
- `E(F)=F(I)=R_t M_t(F)` is the uniquely reconstructed native-normalization functional on the rowspace;
- `h_q` is the surviving cycle-holonomy kernel line;
- `A_(t,r)` is the derivative produced by the reverse-cycle perturbation `Y_* -> Y_*+sE_(r-1,r)`.

The intrinsic Schur/binder calculation is already transverse: `A_(t,r)h_q` contains explicit diagonal spikes of size `-tq`. What remains is to prove that at least one such spike reconstructs to a nonzero `F(I)` value under `R_t`.

## Next permitted attack

Work only on the finite native-projection coefficient `kappa_(n,r)(t)`.

Preferred routes:

- prove that `R_t` cannot annihilate all reverse-cycle diagonal spike vectors simultaneously, using the exact dimension/sector structure of the native hyperplane;
- identify a dual row functional whose pairing with one spike is explicitly nonzero;
- or produce one exact algebraic witness, after which nonvanishing is Zariski-open and can be intersected with the already-proved complete-compression/cycle-pivot locus.

Do not search for second- or higher-order tilt along the old one-parameter path; that route is now proved dead.

Once `kappa_(n,r)(t)!=0` is proved for every odd `n>=3`, all-odd extension-ready existence follows. Combined with the proved odd-to-even transfer and even-to-odd global binding lemma, this closes the sharp all-dimensional equality. Do not claim that equality before `kappa` is closed.

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
