# Deferred research backlog extracted from the external review

**Source date:** 2026-07-17  
**Upstream publication:** `Recursive Jet Calculus and Rigorous Uniform Conditioning for Finite Quantum 6j Recoupling Matrices`, v0.1.2  
**DOI:** `10.5281/zenodo.21401141`  
**Status:** `PARKED / NOT PART OF RC01 / REQUIRES NEW CONTRACT`

## Triage decision

The review contains four worthwhile future directions, but none may be imported into the frozen RC01 pilot, calibration or confirmatory stages. They are parked as independent obligations.

## D1. Multi-anchor and multi-level wall geometry

Study anchors

\[
\theta_k=\frac{\pi}{k+2}
\]

for multiple integer levels and finite label cutoffs. A useful exact preliminary target is the distance from the anchor to the nearest q-number zero. If all indices `1 <= n <= k` are admitted, the candidate half-margin is

\[
R_{\mathrm{wall}}(k)=\frac12\min_{1\le n\le k}
\frac{\operatorname{dist}(n\theta_k,\pi\mathbb Z)}{n}
=\frac{\pi}{k(k+2)}.
\]

Thus the `O(k^{-2})` scaling suggested in the review has a plausible exact elementary form. This is a wall-geometry bound, not yet a uniform lower bound for the recoupling angular speed.

**Future route:** P5 uniform analysis or a separate P3 multi-anchor extension.

## D2. Holomorphic transpose orthogonality versus Hermitian unitarity

The review correctly notices that

\[
F(z)F(z)^T=I
\]

is holomorphic, whereas

\[
F(z)F(z)^*=I
\]

is not a holomorphic identity in `z`. This is a potentially useful boundary lemma.

For a real orthogonal anchor with real derivative and

\[
K=F'F^T,
\]

the imaginary displacement `z=theta_0+i epsilon` formally gives

\[
F(z)F(z)^*=I+2i\epsilon K+O(\epsilon^2).
\]

Hence nonzero `K` generically produces a first-order Hermitian-unitarity defect off the real slice while transpose orthogonality remains analytically continued.

**Important correction:** this does not by itself prove the review's proposed global no-go theorem, nor does it show that unitarity exists only at isolated roots of unity. A future theorem must state its domain, real/unit-circle slice, gauge assumptions and category-level meaning precisely.

**Future route:** separate `COMPLEX_SLICE_UNITARITY_DEFECT` lemma or technical note.

## D3. Full coherence and modular-data extension

The present publication proves statements for a declared finite recoupling subsystem. It does not certify the full modular tensor category. A future extension could register independent residuals for:

- pentagon coherence;
- braiding `R` data;
- modular `S` and `T` data;
- gauge compatibility across all admissible fusion spaces.

**Important correction:** transpose orthogonality is not the pentagon identity. The review conflates them in one passage. A future coherence programme must treat them as separate obligations.

**Future route:** P2 global gluing/category compatibility, after P1 and P5.

## D4. Arbitrary finite `(k,N)` theorem

Generalize the truncated-Taylor construction from `(k,N)=(10,6)` to a declared finite class at arbitrary integral level `k` and label cutoff `N`, with typed conditions for:

1. admissible fusion channels;
2. critical q-index ledger below the first wall;
3. common regularity chamber;
4. recursive jets at arbitrary finite formal order;
5. explicit or certified lower bounds for the selected observable.

The existing work supplies the finite-order algebraic engine, but not the required uniform lower bounds or full category theorem.

**Future route:** P5, then P2.

## Rejected or corrected review claims

- The DOI is not absent: the publication DOI is `10.5281/zenodo.21401141`.
- The work does not prove local structural stability of the full `SU(2)_10` modular category; it certifies a finite recoupling class.
- `FF^T=I` is transpose orthogonality, not the pentagon identity.
- Non-holomorphicity of `FF^*=I` is not alone a global impossibility proof.
- Venue rankings and the numerical score `7/10` are editorial opinions, not scientific evidence.

## Firewall

Nothing in this backlog changes RC01 observables, grids, family split, predictors, thresholds or outcome logic. Each deferred item requires a new contract identifier before computation.

No statement from the Gemini advisory report is used as evidence.
