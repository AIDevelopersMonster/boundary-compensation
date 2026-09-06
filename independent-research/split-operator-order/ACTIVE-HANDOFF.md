# Split Operator Order — active handoff

**Branch:** `research/split-operator-order-article-II-v0.1`  
**Checkpoint date:** 2026-09-06  
**Author:** Malachevsky, A.A.  
**ORCID:** 0009-0008-6009-3196

## Rule for future chats
Read this file first, then the cited control notes. Do not reconstruct the programme from chat memory. After every nontrivial theorem, obstruction, audit repair, manuscript promotion, source-build change, or publication-status change, update this file before continuing.

## Article I
The published Article-I core is frozen. Post-publication research established the sharp first-order Coxeter tomography theorem. Do not rewrite the frozen Article-I publication core.

**Zenodo DOI:** `10.5281/zenodo.22289201`.

## Article II — published
Directory: `article-II-open-systems/`.

Publication source package: `article-II-open-systems/publication-v0.2.1/`.

Title: *Context Reduction in Open Quantum Systems: Multiplicativity Defects, Lindblad Order Holonomy, and Sharp Coxeter Tomography*.

**Zenodo DOI:** `10.5281/zenodo.22421827`  
**Canonical URL:** https://doi.org/10.5281/zenodo.22421827  
**Publication status:** `PUBLISHED`.

The audited publication package contains `main.tex`, `sharp-proof-appendix.tex`, canonical build entrypoint `article.tex`, and release-control `README.md`. Workflow: `.github/workflows/article-ii-publication.yml`.

## Main theorem
In the bounded finite-dimensional matrix-valued first-order Coxeter-face measurement model,

`L_d^Cox=floor(d^2/2)` for every `d>=3`.

The quotient dimension is `N_d=(d^2-1)^2`; one matrix-valued face supplies at most `2d^2` real coordinates. The theorem is algebraic and does not extrapolate from low-dimensional numerical ranks.

## Audited proof chain
1. Structural scalar-one restriction quotient `R_res(d)=(d^2-1)(d+1)^2+2`.
2. Extension-ready minimal-design criterion and parity ceiling.
3. Centered odd-dimensional tangent formulas.
4. Complete one-anchor regular kernel and finite H-anchor compression.
5. Cycle factorization of compressed dependency determinant `D_n`.
6. Binder-compatible transversality inside the reverse-cycle-zero subspace.
7. Exact no-go for the old one-parameter native tilt.
8. Reverse-cycle transverse detector and finite reconstruction coefficient.
9. Extension-ready minimal designs in every odd dimension.
10. Odd-to-even transfer rebuilt directly in centered scalar-one coordinates and directly in `SL_n(C)`.
11. Return to genuine unitary Coxeter faces by `SU(n)` Zariski density and engineered contextual-square realization.

Critical proof repairs remain recorded in `article-I/research/BINDER-COMPATIBLE-TRANSVERSALITY-REPAIR-v0.1.md` and `article-I/research/ODD-TO-EVEN-TRANSFER-AUDIT-REPAIR-v0.1.md`. The invalid post hoc determinant normalization is withdrawn and is not used in the publication source.

## d=2 boundary
No two-face design is extension-ready under scalar-one embedding `M_2 -> M_3`. This does not prove native two-face tomography impossible. The sharp theorem is intentionally `d>=3`.

## Perspective bridge — published
Directory: `perspective-bridge-I/`.

Title: *Choosing the Road: From Contextual Flatness to Measurable Context Loss in Open Quantum Systems*.

Subtitle: *A Mathematical-Physics Perspective between Articles I–II and Stable Coxeter Tomography*.

**Zenodo DOI:** `10.5281/zenodo.22442536`  
**Canonical URL:** https://doi.org/10.5281/zenodo.22442536  
**Publication status:** `PUBLISHED`.

The post-audit Perspective separates proved mathematics, supported interpretation, and explicit research targets. Its long-range programme remains interrogative:

`context loss -> stable loop observables -> environmental information -> effective geometry?`

Do not promote the question mark into a physical-curvature claim.

## Article III — active research
The strict next problem is stable/robust Coxeter tomography.

Primary control notes:

- `article-II-open-systems/ARTICLE-III-NORMALIZED-FRAME-FORMULATION-v0.1.md` — normalized Hilbert/frame formulation;
- `article-II-open-systems/ARTICLE-III-FIRST-CONDITIONING-EXPERIMENT-v0.1.md` — first real singular-value experiment.

### Normalized frame layer
Let `Q_d` be the dissipative quotient with real dimension `(d^2-1)^2`. For a design `D`, the normalized measurement operator is

`M_D: Q_d -> direct_sum_f M_d`,

with averaged normalized Hilbert-Schmidt output metric. The frame operator is

`S_D = M_D^* M_D = (1/L) sum_f C_f^* C_f`.

Define

`A_D=lambda_min(S_D)=sigma_min(M_D)^2`,

`B_D=lambda_max(S_D)=sigma_max(M_D)^2`,

`kappa(D)=sqrt(B_D/A_D)`.

Proved invariances:

- orthonormal coordinate invariance;
- unitary conjugation invariance;
- exact replication invariance `S_{rD}=S_D`;
- `A_D>0` iff `M_D` is injective iff rank is `(d^2-1)^2`.

Thus Article II solved the binary wall `A_D=0` versus `A_D>0`; Article III studies the size and scaling of `A_D` and `kappa`.

### First conditioning experiment
The Article-II real/complex builders were reconstructed rather than reading metric information from modular certificates.

For an orthonormal traceless-Hermitian basis and Hermitian Kossakowski coordinates, the induced domain Gram form was numerically identified as

`G_d(C,D)=Tr(CD)+Tr(C)Tr(D)+(1/2) tau(K_C^0 K_D^0)`.

Its spectrum was found to machine precision for `d=2,3,4,5` as

`spec(G_d)={1,d^2/2,d^2}`

with multiplicities

`d^4-3d^2+1`, `d^2-1`, `1`.

This is now the next analytic theorem target; it is numerical evidence until proved.

Baseline normalized conditioning data:

- `d=3`, four-face Article-II design: `sigma_min≈0.1217388`, `kappa≈37.78097`, `A≈0.0148203`;
- `d=4`, eight-face Article-II design: `sigma_min≈0.05355124`, `kappa≈81.25384`, `A≈0.00286774`;
- `d=5`, twelve-square Article-II design: `sigma_min≈0.03978665`, `kappa≈121.74003`, `A≈0.00158298`.

No asymptotic conclusion is licensed from three points.

Inside a fixed 72-face Coxeter pool:

- `d=3`: local/random sharp redesign improved `kappa` from about `37.78` to about `21.52` in the best sampled four-face design;
- `d=4`: one sharp face exchange improved `kappa` from about `81.25` to about `56.45`.

Hence the Article-II rank witnesses are not conditioning-optimal even at small dimension.

Genuine geometric oversampling, with averaged output normalization so duplication gives no gain, produced strong preliminary improvements:

- `d=3`: from `L=4`, `A≈0.03585`, `kappa≈26.16`, to `L=7`, `A≈0.33024`, `kappa≈7.37`;
- `d=4`: from `L=8`, `A≈0.005592`, `kappa≈56.45`, to `L=11`, `A≈0.031720`, `kappa≈23.99`.

This is first numerical evidence for a possible robustness/redundancy gap, not a theorem.

### Immediate next hit
Prove the exact Gram-spectrum theorem

`spec(G_d)={1,d^2/2,d^2}`

with multiplicities

`d^4-3d^2+1`, `d^2-1`, `1`,

preferably by decomposing `Herm(su(d))` under the adjoint `SU(d)` action and identifying the scalar, adjoint, and orthogonal sectors of `C -> K_C^0`.

After this proof, construct dimension-scalable normalized face pools and test whether sharp designs admit polynomial conditioning or whether a provable redundancy barrier appears.

## Claim firewall
Do not inflate the current results into finite-time arbitrary UCP-channel identifiability, universal CP-reduction monotonicity, entropy/decoherence monotones, infinite-dimensional unbounded GKSL results, established physical spacetime/gauge curvature, process-tensor results, asymptotic conditioning theorems, or experimental/sample-complexity optimality.

## Reproducibility
The `d=5` builder was independently re-executed during Article-II consolidation:

`prime=1000033 shape=600x576 rank=576`

`CERTIFIED_FULL_COLUMN_RANK_OVER_Q`.

The new Article-III metric experiments reconstruct the real/complex matrices and explicitly do not infer singular values from finite-field residues.

## Publication audit
Successful audited Article-II workflow run: `33995974451` at head `26b2e9488b823b225f0c8312e78cb8c6c431c3e5`.

Artifact:
- `article-II-v0.2.1-pdf`;
- id `9978084171`;
- SHA-256 `d474fa8cc1ab94aa7bf6a184d647fb2536597780ebbfbc693b4456aafc4c7488`.

PDF audit: 16 pages, PDF 1.5, text-based, unencrypted; no visible publication blocker.

## Current branch status
Published sequence is now:

1. Article I — DOI `10.5281/zenodo.22289201`;
2. Article II — DOI `10.5281/zenodo.22421827`;
3. Perspective bridge — DOI `10.5281/zenodo.22442536`;
4. Article III — active normalized stability/conditioning research.

Do not reopen Article-I/II theorem existence unless a concrete defect is found. The active mathematical front is Article III.
