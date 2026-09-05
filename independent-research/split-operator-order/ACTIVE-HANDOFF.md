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
9. The centered tangent compressed dependency determinant is now proved nonzero for a suitable finite complete compression in every odd dimension `n>=3`.

Relevant notes under `article-I/research/`:

- `GLOBAL-BINDING-LEMMA-v0.1.md`
- `ODD-TO-EVEN-EXTENSION-READY-v0.1.md`
- `D2-EXTENSION-READY-OBSTRUCTION-v0.1.md`
- `CENTERED-TANGENT-ODD-ER-v0.1.md`
- `CENTERED-TANGENT-COMPRESSION-AUDIT-v0.1.md`
- `CENTERED-TANGENT-CYCLE-FACTOR-v0.1.md`
- `ODD-ER-TRANSVERSALITY-CLOSURE-v0.1.md`
- `ODD-D-EXTENSION-READY-v0.1.md` (audited; old all-odd claim withdrawn)

## Exact current bottleneck

The compressed row-dependency determinant barrier is CLOSED for every odd `n>=3`.

The centered tangent route now has exactly one remaining obstruction:

`native tilt scalar tau_n != 0`

(or the first nonzero higher-order centered coefficient) for the unique non-derivation kernel line left after embedded regular rank is lifted.

At the tangent base the extra line lies in the native hyperplane

`N={F:F(I)=0}`.

The next task is to prove that the finite centered perturbation moves this line transversely out of `N` for some minimal odd-dimensional design.

## Next permitted attack

Work only on the native tilt barrier. Preferred routes:

- derive the extra kernel line explicitly in cycle/path coordinates and compute its first variation under the same `H -> H+tS` perturbation;
- or prove by algebraic transversality that the native hyperplane condition is not identically preserved on the already-open embedded-full-rank locus;
- if the linear tilt vanishes structurally, identify and prove the first nonzero higher-order coefficient.

Once native tilt is closed for all odd `n>=3`, all-odd extension-ready existence follows. Combined with the proved odd-to-even transfer and even-to-odd global binding lemma, this closes the sharp all-dimensional equality. Do not claim that equality before native tilt is proved.

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

**Next single obligation:** prove native tilt `tau_n !=0` (or the first nonzero higher-order coefficient) for the unique extra non-derivation kernel line.
