# Split Operator Order — active handoff

**Branch:** `research/split-operator-order-article-II-v0.1`  
**Checkpoint date:** 2026-09-06  
**Author:** Malachevsky, A.A.  
**ORCID:** 0009-0008-6009-3196

## Rule for future chats
Read this file first, then the cited control notes. Do not reconstruct the programme from chat memory. After every nontrivial theorem, obstruction, audit repair, manuscript promotion, source-build change, or publication-status change, update this file before continuing.

## Article I — published / frozen
Title: *Split-Interval Representation of Quantum Operator Order: Descent Obstructions, Order Ultrametrics, and Pair-Reduced Holonomy*.

**Zenodo DOI:** `10.5281/zenodo.22289201`.

Do not rewrite the frozen Article-I publication core except for genuine errata or metadata corrections.

## Article II — published / frozen
Directory: `article-II-open-systems/`.

Title: *Context Reduction in Open Quantum Systems: Multiplicativity Defects, Lindblad Order Holonomy, and Sharp Coxeter Tomography*.

**Zenodo DOI:** `10.5281/zenodo.22421827`  
**Canonical URL:** https://doi.org/10.5281/zenodo.22421827  
**Publication status:** `PUBLISHED`.

Main theorem in the declared bounded finite-dimensional matrix-valued first-order Coxeter-face model:

`L_d^Cox=floor(d^2/2)` for every `d>=3`.

The quotient dimension is `N_d=(d^2-1)^2`. The result is algebraic and does not extrapolate from low-dimensional numerical ranks.

Critical proof repairs remain recorded in:

- `article-I/research/BINDER-COMPATIBLE-TRANSVERSALITY-REPAIR-v0.1.md`;
- `article-I/research/ODD-TO-EVEN-TRANSFER-AUDIT-REPAIR-v0.1.md`.

## Perspective bridge — published
Directory: `perspective-bridge-I/`.

Title: *Choosing the Road: From Contextual Flatness to Measurable Context Loss in Open Quantum Systems*.

Subtitle: *A Mathematical-Physics Perspective between Articles I–II and Stable Coxeter Tomography*.

**Zenodo DOI:** `10.5281/zenodo.22442536`  
**Canonical URL:** https://doi.org/10.5281/zenodo.22442536  
**Publication status:** `PUBLISHED`.

Long-range programme remains interrogative:

`context loss -> stable loop observables -> environmental information -> effective geometry?`

Do not promote the question mark into a physical-curvature claim.

## Article III — active research
The active front is stable/robust Coxeter tomography.

Primary control notes:

- `article-II-open-systems/ARTICLE-III-NORMALIZED-FRAME-FORMULATION-v0.1.md`;
- `article-II-open-systems/ARTICLE-III-FIRST-CONDITIONING-EXPERIMENT-v0.1.md`;
- `article-II-open-systems/ARTICLE-III-GRAM-SPECTRUM-THEOREM-v0.1.md`.

### Normalized frame layer
For a design `D`, the normalized first-order measurement operator is

`M_D: Q_d -> direct_sum_f M_d`,

with averaged normalized Hilbert-Schmidt output metric. The frame operator is

`S_D=(1/L) sum_f C_f^* C_f`.

Define

`A_D=lambda_min(S_D)=sigma_min(M_D)^2`,

`B_D=lambda_max(S_D)=sigma_max(M_D)^2`,

`kappa(D)=sqrt(B_D/A_D)`.

Proved invariances:

- orthonormal coordinate invariance;
- unitary conjugation invariance;
- replication invariance `S_{rD}=S_D`;
- `A_D>0` iff `M_D` is injective iff rank is `(d^2-1)^2`.

Thus Article II solved only the binary wall `A_D=0` versus `A_D>0`; Article III studies quantitative stable injectivity.

### First conditioning experiment
Baseline normalized conditioning:

- `d=3`, four-face Article-II design: `sigma_min≈0.1217388`, `kappa≈37.78097`, `A≈0.0148203`;
- `d=4`, eight-face Article-II design: `sigma_min≈0.05355124`, `kappa≈81.25384`, `A≈0.00286774`;
- `d=5`, twelve-square Article-II design: `sigma_min≈0.03978665`, `kappa≈121.74003`, `A≈0.00158298`.

No asymptotic theorem follows from these three points.

Inside a fixed 72-face Coxeter pool:

- `d=3`: sampled sharp redesign improved `kappa` from about `37.78` to about `21.52`;
- `d=4`: one sharp exchange improved `kappa` from about `81.25` to about `56.45`.

Genuine oversampling with averaged output normalization produced strong preliminary improvement:

- `d=3`: `L=4`, `A≈0.03585`, `kappa≈26.16` -> `L=7`, `A≈0.33024`, `kappa≈7.37`;
- `d=4`: `L=8`, `A≈0.005592`, `kappa≈56.45` -> `L=11`, `A≈0.031720`, `kappa≈23.99`.

This is numerical evidence for a possible robustness/redundancy gap, not a theorem.

## New theorem checkpoint — exact Kossakowski Gram spectrum
Commit: `0f795d766c04b9c9440f9e40d5762ecb96cebbee`.

The numerical Gram-spectrum pattern is now proved for every `d>=2`.

Let `q=d^2-1`, let `F_a` be any Hermitian traceless basis orthonormal for `tau(XY)=Tr(XY)/d`, and let `C in Herm(q)` parametrize the canonical dissipative Kossakowski section. Define

`K_C=sum_ab C_ab F_a F_b`,

`T(C)=K_C-Tr(C) I`.

The induced quotient Gram form is exactly

`G_d(C,D)=Tr(CD)+Tr(C)Tr(D)+(1/2) tau(T(C)T(D))`.

The Kossakowski section is exactly orthogonal to the Hamiltonian derivation sector in the normalized superoperator Hilbert geometry; no further numerical quotient projection is needed.

The key multiplication-map identity is

`T T^* = (d^2-2) I`

on traceless Hermitian matrices.

Hence `Herm(q)` splits orthogonally into:

- scalar sector `S_d = R I_q`, dimension `1`;
- canonical adjoint sector `A_d=im T^*`, dimension `d^2-1`;
- residual sector `R_d=ker T intersect {Tr C=0}`, dimension `d^4-3d^2+1`.

On these sectors the Gram operator has eigenvalues

`1`, `d^2/2`, `d^2`, respectively. Therefore

`spec(G_d)={1, d^2/2, d^2}`

with multiplicities

`d^4-3d^2+1`, `d^2-1`, `1`.

This is now theorem-level, not numerical evidence.

Exact projectors:

`P_s(C)=Tr(C)/(d^2-1) I`,

`P_a=(d^2-2)^(-1) T^* T`,

`P_r=I-P_s-P_a`.

Closed-form whitening:

`G_d^(-1/2)=P_r+(sqrt(2)/d) P_a+(1/d) P_s`.

Thus all future conditioning experiments can avoid numerical diagonalization of the domain Gram matrix.

The raw Kossakowski-coordinate distortion is exactly `d` in norm, so any worse scaling after exact whitening belongs to the measurement design rather than to unresolved domain-coordinate geometry.

### Immediate next hit
The domain-normalization barrier is closed. The next strict problem is measurement-side:

`after exact whitening, what lower frame bounds are achievable by sharp and oversampled Coxeter designs?`

Priority sequence:

1. replace numerical Gram eigendecomposition in all small-d scripts by the exact projector whitening formula;
2. re-run d=3,4,5 regression and verify agreement with previous normalized spectra;
3. construct dimension-scalable unitary face pools;
4. test whether best sharp `kappa_d` is polynomially bounded;
5. if not, seek a theorem-level redundancy barrier / lower bound for `L_d^rob(epsilon)`.

The independent face-resource normalization question remains open for comparisons across different loop lengths/control costs. Equal-face weighting is mathematically defined for the present fixed finite pools, but is not yet claimed to be the unique physical resource model.

## Claim firewall
Do not inflate current results into:

- finite-time arbitrary UCP-channel identifiability;
- universal CP-reduction monotonicity;
- entropy/decoherence monotones;
- infinite-dimensional unbounded GKSL results;
- established spacetime/gauge curvature;
- process-tensor/non-Markovian results;
- asymptotic conditioning theorems;
- statistical/sample-complexity optimality;
- experimentally canonical loop-cost normalization.

## Reproducibility
Article-II exact rank certificate remains:

`prime=1000033 shape=600x576 rank=576`

`CERTIFIED_FULL_COLUMN_RANK_OVER_Q`.

Metric claims must come from real/complex normalized operators, never from finite-field residues.

## Current sequence
1. Article I — DOI `10.5281/zenodo.22289201`;
2. Article II — DOI `10.5281/zenodo.22421827`;
3. Perspective bridge — DOI `10.5281/zenodo.22442536`;
4. Article III — active stability/conditioning research; exact domain Gram-spectrum theorem proved.

Do not reopen Article-I/II theorem existence unless a concrete defect is found. The active mathematical front is Article III measurement-side stability and redundancy.
