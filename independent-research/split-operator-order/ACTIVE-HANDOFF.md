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

Relevant notes under `article-I/research/`:

- `GLOBAL-BINDING-LEMMA-v0.1.md`
- `ODD-TO-EVEN-EXTENSION-READY-v0.1.md`
- `D2-EXTENSION-READY-OBSTRUCTION-v0.1.md`
- `CENTERED-TANGENT-ODD-ER-v0.1.md`
- `CENTERED-TANGENT-COMPRESSION-AUDIT-v0.1.md`
- `ODD-D-EXTENSION-READY-v0.1.md` (audited; old all-odd claim withdrawn)

## Exact current bottleneck

The only missing ingredient for the sharp all-`d` theorem is a rigorous source of extension-ready odd stages, beginning with `d=3` and preferably all odd `d` directly.

The centered tangent route has reduced the all-odd regular-sector problem to two nonvanishing statements:

1. compressed row-dependency determinant `det D_n != 0`, where `D_n` has size `n(n-2)`;
2. native tilt scalar `tau_n != 0` (or the first nonzero higher-order coefficient) for the unique extra kernel line after embedded regular rank is lifted.

Everything before these two determinants in the centered tangent construction is already theorem-level.

## Next permitted attack

Work on the centered tangent compression barrier, preferably by:

- identifying `D_n` with an explicit incidence / cycle operator; or
- replacing the determinant computation by a clean transversality/basis-exchange lemma that proves it cannot vanish identically; then
- compute/prove the native tilt.

A successful odd `ER_3` base plus a theorem producing odd ER stages, or an all-odd ER theorem, closes the parity induction. Do not claim the sharp all-`d` equality before this gate is closed.

## Checkpoint discipline

For each research step append a short entry below:

- result/status;
- exact statement or obstruction;
- file containing proof/details;
- next single obligation.

### 2026-09-05 checkpoint 0

Repository/branch recovery completed. Existing branch and all recent theorem notes were found intact. No reconstruction from the two blocked chats is required; their committed mathematical output survives on GitHub. Current work resumes from the two centered-tangent final determinants above.
