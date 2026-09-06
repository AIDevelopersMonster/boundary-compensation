# Cheshire-Cat Perspective — publication plan v0.2

Author: Malachevsky, A.A. / Малачевский А.А.  
ORCID: 0009-0008-6009-3196  
Date: 2026-09-06  
Status: `REVIEWABLE_DRAFT / PRE-LATEX GATES COMPLETE`

## Editorial architecture

The bridge publication is a Perspective + Research Programme between two published theorem papers and the planned stable-tomography paper.

Published foundations:

1. Article I — *Split-Interval Representation of Quantum Operator Order: Descent Obstructions, Order Ultrametrics, and Pair-Reduced Holonomy*. DOI `10.5281/zenodo.22289201`.
2. Article II — *Context Reduction in Open Quantum Systems: Multiplicativity Defects, Lindblad Order Holonomy, and Sharp Coxeter Tomography*. DOI `10.5281/zenodo.22421827`.

Planned strict continuation:

3. Article III — *Stable Coxeter Tomography*: conditioning, singular values, oversampling, robustness, and eventually an operational measurement layer.

## Mathematical spine

Merged into the post-audit manuscript:

- loop amplification bound `||H_Phi-I|| <= (m-1) mu_Phi(S)`;
- multiplicative-domain flatness of a transport algebra;
- dissipative invisibility on the common noise commutant;
- positivity `Gamma_L(A*,A)=sum [A,V_alpha]*[A,V_alpha] >= 0` in a fixed GKSL representation;
- fixed-loop small-time bound `||H_t-I|| <= t(m-1)g_L(S)+O(t^2)`.

The next strict problem is normalized robust Coxeter tomography through `sigma_min(M_D)`, `kappa(M_D)`, and a minimal robust face count `L_d^rob(epsilon)`.

## Speculative layer

Central research target:

`context loss -> stable loop observables -> environmental information -> effective geometry?`

The question mark is mandatory. The bridge paper does not identify the Article-II loop defect with spacetime curvature, gauge curvature, entropy production, a universal decoherence measure, or non-Markovianity.

## Geometry gate

The programme will use the phrase `genuine geometry` only after specifying objects/configurations, transport, composition, a local connection/defect object, loop holonomy, covariance/gauge structure, nontrivial invariants, and an operational or representation-independent evaluation procedure.

## Literature boundary

The post-audit manuscript explicitly distinguishes the programme from established work on:

- multiplicative domains and quantum error correction;
- decoherence-free/noiseless algebras and subsystems;
- Uhlmann/Jamiołkowski channel holonomy;
- noncommutative carré du champ / quantum Markov geometry;
- Lindbladian/Liouvillian learning and process tomography;
- classical-shadow/randomized-measurement approaches;
- process tensors and multitime non-Markovian characterization.

No broad priority claim such as `first quantum curvature`, `first practical Lindblad tomography`, or `new non-Markovian process theory` is permitted.

## Completed gates

1. `DONE` — mathematical interface merged into Russian post-audit manuscript v0.2.
2. `DONE` — targeted literature/claim-boundary audit.
3. `DONE` — English parity manuscript v0.2.
4. `DONE_TO_REVIEW_LEVEL` — journal DOI metadata and 2026 preprint status checked; bibliography verification checkpoint recorded.
5. `DONE` — theorem/claim audit recorded in `AUDIT-v0.2.md`; no C0 defect found in the five direct propositions, with fixed-loop/fixed-representation qualifications retained.

## Remaining release gates

1. Patch the final RU bibliography to include the four foundational CP/GKSL references, Amato–Facchi–Konderak 2026, full Lidar metadata, and explicit `preprint` labels for 2026 arXiv items.
2. Convert EN/RU manuscripts to stable LaTeX with numbered equations, propositions, conjectures, and cross-references.
3. Fix the article-specific licence (`AUTHOR_DECISION_REQUIRED`).
4. Compile publication PDFs.
5. Run log gate, render every page, visually inspect, and clear all C5 defects.
6. Recheck final bibliography after LaTeX conversion.

## Current release status

`REVIEWABLE_DRAFT`

The scientific direction and claim firewall are mature enough to proceed to publication typesetting. The document is not yet `PUBLICATION_READY_PENDING_RENDER_AUDIT` because final LaTeX sources, licence metadata, and rendered PDFs do not yet exist.
