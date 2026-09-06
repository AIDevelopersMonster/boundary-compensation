# Article III — Exact-Whitening Isotropy Census and the Next Normalization Door

**Author:** Malachevsky, A.A. / Малачевский А.А.  
**ORCID:** 0009-0008-6009-3196  
**Date:** 2026-09-06  
**Status:** `NUMERICAL_CENSUS / NEW_STRUCTURAL_OBSTRUCTION IDENTIFIED`

## 0. Purpose

This note continues the exact-whitening programme after the theorem

\[
G_d^{-1/2}=P_r+\frac{\sqrt2}{d}P_a+\frac1dP_s.
\]

It performs three tasks:

1. closes the full-precision `d=5` exact-whitening regression;
2. measures mean frame energy, lower-frame efficiency, and tightness defect for the fixed 72-face Coxeter pools in `d=3,4`;
3. tests whether the previously observed oversampling gain is primarily an isotropy effect or merely an energy effect.

The answer is mixed and reveals a new barrier: **the current raw Coxeter pool has strongly nonuniform single-face energy**. Therefore `eta` is useful diagnostically, but no Coxeter-specific redundancy theorem can yet be formulated without separating angular coverage from face-resource normalization.

---

## 1. Full-precision d=5 regression

The 12 engineered squares from `exact_face_rank_certificate_d5_v010.py` were reconstructed in real/complex arithmetic, exactly whitened by the theorem-level projector formula, and evaluated with averaged normalized Hilbert-Schmidt output metric.

The result is

\[
\boxed{
\sigma_{\min}=0.03978665131344871,
}
\]

\[
\boxed{
\sigma_{\max}=4.843628225780513,
}
\]

\[
\boxed{
\kappa=121.74003254562082,
}
\]

\[
\boxed{
A=0.00158297762273795,
\qquad
B=23.46073438957768.
}
\]

The exact Gram diagnostics were

\[
\|TT^*-(d^2-2)I\|_2\approx7.34\times10^{-15},
\]

\[
\|G^{-1/2}GG^{-1/2}-I\|_2\approx2.50\times10^{-15}.
\]

Thus the previous rounded `d=5` values are fully reproduced by the closed-form normalization. The regression script now stores full-double-precision references.

---

## 2. Single-face energy census

For a whitened face block `C_f`, define its normalized frame energy

\[
E_f=\operatorname{Tr}(C_f^*C_f).
\]

Because the output norm contains the factor `1/d`, the block matrices used here already include `1/\sqrt d`; hence `E_f` is directly the single-face contribution to `Tr S_D` before averaging over faces.

### d=3 pool

For the 72-face pool built from 24 permutations and the three loop types `b01`, `b12`, and `sq02`:

\[
E_{b01}\in[246.5362,307.1756],
\]

\[
E_{b12}\in[246.5362,307.1756],
\]

\[
E_{sq02}\in[108.9924,227.3684].
\]

Mean values:

\[
\bar E_{b01}=\bar E_{b12}\approx274.2038,
\]

\[
\bar E_{sq02}\approx183.0925.
\]

### d=4 pool

Likewise,

\[
E_{b01}\in[518.8157,648.3402],
\]

\[
E_{b12}\in[518.8157,648.3402],
\]

\[
E_{sq02}\in[58.4891,593.7969].
\]

Mean values:

\[
\bar E_{b01}=\bar E_{b12}\approx577.7856,
\]

\[
\bar E_{sq02}\approx378.3089.
\]

### Consequence

The present raw Coxeter pool is emphatically **not an equal-energy face class**. Even within a fixed symbolic loop type, conjugation/permutation changes the norm of the resulting first-order face coefficient. The commuting-square family is especially heterogeneous.

Therefore the equal-energy conclusion from `ARTICLE-III-FRAME-EFFICIENCY-BOUND-v0.1.md` does not apply directly to this pool.

---

## 3. Baseline frame-efficiency diagnostics

Recall

\[
\bar\lambda_D=\frac1N\operatorname{Tr}S_D,
\qquad
\eta_D=\frac{A_D}{\bar\lambda_D},
\]

and

\[
\delta_{tight}(D)
=
\frac{\|S_D-\bar\lambda_DI\|_F}{\bar\lambda_D\sqrt N}.
\]

### d=3 Article-II baseline

For the original four-face design,

\[
A\approx0.01482034,
\qquad
B\approx21.15458,
\qquad
\kappa\approx37.78097,
\]

\[
\operatorname{Tr}S\approx235.99566,
\qquad
\bar\lambda\approx3.687432,
\]

\[
\boxed{\eta\approx0.00401915},
\qquad
\boxed{\delta_{tight}\approx1.21854}.
\]

### d=4 Article-II baseline

For the original eight-face design,

\[
A\approx0.002867735,
\qquad
B\approx18.93332,
\qquad
\kappa\approx81.25384,
\]

\[
\operatorname{Tr}S\approx577.78560,
\qquad
\bar\lambda\approx2.567936,
\]

\[
\boxed{\eta\approx0.00111675},
\qquad
\boxed{\delta_{tight}\approx1.28803}.
\]

Both baselines are extremely far from the tight-frame benchmark `eta=1`.

---

## 4. Sharp redesign: energy and isotropy both matter

### d=3

A sampled four-face sharp design recovered the previous best lower-frame result:

\[
A\approx0.03979517,
\qquad
B\approx18.43498,
\qquad
\kappa\approx21.52317.
\]

Its energy diagnostics are

\[
\operatorname{Tr}S\approx255.07544,
\qquad
\bar\lambda\approx3.985554,
\]

\[
\boxed{\eta\approx0.00998485},
\qquad
\boxed{\delta_{tight}\approx1.05404}.
\]

Relative to the baseline,

\[
\frac{\bar\lambda_{new}}{\bar\lambda_{base}}\approx1.081,
\]

whereas

\[
\frac{\eta_{new}}{\eta_{base}}\approx2.484.
\]

Thus the improvement in `A` is not explained by energy alone: most of it is an improvement of the weakest-direction efficiency.

### d=4

A sampled eight-face design gives

\[
A\approx0.006568676,
\qquad
B\approx19.26880,
\qquad
\kappa\approx54.16121,
\]

with

\[
\bar\lambda\approx2.528964,
\qquad
\eta\approx0.00259738,
\qquad
\delta_{tight}\approx1.31276.
\]

Here the mean frame energy is actually slightly **lower** than in the baseline while `A` is more than doubled. Hence this particular sharp-design gain cannot be an energy-injection artifact.

A subsequent single exchange improved the efficiency further to

\[
A\approx0.006939435,
\qquad
\kappa\approx51.23512,
\]

\[
\boxed{\eta\approx0.00274398},
\qquad
\boxed{\delta_{tight}\approx1.23938},
\]

at essentially the same mean energy

\[
\bar\lambda\approx2.528964.
\]

This is direct numerical evidence that angular/frame allocation matters independently of total measurement energy.

---

## 5. Oversampling census

### d=3: condition-number-oriented sequence

Starting from a sharp four-face design with

\[
A\approx0.03979517,
\quad
\kappa\approx21.52317,
\quad
\bar\lambda\approx3.985554,
\quad
\eta\approx0.00998485,
\]

a greedy condition-number sequence gives:

| L | A | kappa | mean frame eigenvalue | eta | delta_tight |
|---:|---:|---:|---:|---:|---:|
| 4 | 0.039795 | 21.523 | 3.98555 | 0.009985 | 1.05404 |
| 5 | 0.121040 | 11.725 | 3.85958 | 0.031361 | 0.96467 |
| 6 | 0.215315 | 8.517 | 3.80843 | 0.056536 | 0.90609 |
| 7 | 0.260782 | 7.264 | 3.51501 | 0.074191 | 0.85520 |

The mean energy **decreases** along this sequence, while the lower-frame bound and efficiency increase sharply and the tightness defect decreases.

This is the cleanest small-dimensional evidence so far that genuine redundancy can improve angular coverage rather than merely adding frame energy.

### d=4

Starting from the efficiency-improved sharp eight-face design:

| L | A | kappa | mean frame eigenvalue | eta | delta_tight |
|---:|---:|---:|---:|---:|---:|
| 8 | 0.006939 | 51.235 | 2.52896 | 0.002744 | 1.23938 |
| 9 | 0.016324 | 33.477 | 2.50417 | 0.006519 | 1.24921 |
| 10 | 0.026052 | 26.142 | 2.53161 | 0.010291 | 1.21614 |
| 11 | 0.031720 | 23.985 | 2.54138 | 0.012481 | 1.21676 |

Again `bar lambda` remains nearly constant, changing by only a few percent, while `eta` increases by more than a factor four from `L=8` to `L=11`.

However `delta_tight` is not monotone: it rises slightly at `L=9` before decreasing. Therefore `eta` and `delta_tight` capture different spectral aspects. Lifting the minimum eigenvalue does not force monotone decrease of the full Frobenius spectral variance.

---

## 6. What the census establishes

The small-d data now distinguish three statements.

### Supported numerical statement A — not just energy

There exist fixed-pool sharp replacements and oversampled extensions for which

\[
A_D\uparrow,
\qquad
\eta_D\uparrow,
\]

while

\[
\bar\lambda_D
\]

stays nearly constant or decreases.

Therefore the observed gain is not reducible to an increase in average face energy.

### Supported numerical statement B — minimum-direction repair

For `d=3`, the condition-number-oriented oversampling sequence simultaneously yields

\[
\eta_D\uparrow
\quad\text{and}\quad
\delta_{tight}\downarrow,
\]

which is genuine movement toward a more isotropic frame spectrum.

### Not supported as a theorem

The data do not prove that all sharp Coxeter designs are inefficient, nor that every oversampling path improves isotropy, nor any asymptotic redundancy gap.

---

## 7. The new door: face-resource normalization

The census reveals that the next obstruction is not domain normalization. That barrier is closed.

The new issue is that the admissible face pool itself carries a nontrivial energy landscape:

\[
\boxed{
E_f=\|C_f\|_{HS}^2
}
\]

varies strongly with the face.

Consequently two different questions must now be separated.

### Raw-design stability

Use the actual `C_f` produced by the chosen unitary transports and ask how stable the resulting experiment is under equal face count/weight.

### Direction-only geometry

Normalize each nonzero face by its own Hilbert-Schmidt energy,

\[
\widehat C_f
=
\frac{C_f}{\|C_f\|_{HS}},
\]

and study

\[
\widehat S_D
=
\frac1L\sum_{f\in D}\widehat C_f^*\widehat C_f.
\]

This removes single-face amplitude and isolates angular coverage in the operator-frame sense.

But this normalization is **not yet asserted to be physically canonical**. It is a diagnostic projectivization of the face family. A physical experiment may legitimately care about the raw response amplitude because that amplitude determines signal strength.

Hence Article III should carry two parallel stability layers:

\[
\boxed{
\text{raw response stability}
}
\]

and

\[
\boxed{
\text{projective/direction-only frame geometry}.
}
\]

The comparison between them is now the next mathematical door.

---

## 8. Immediate next problem

Define for every nonzero face the projective block

\[
\widehat C_f=C_f/\|C_f\|_{HS}.
\]

Then perform the same sharp/oversampled census for

\[
\widehat A_D,
\quad
\widehat\kappa_D,
\quad
\widehat\eta_D,
\quad
\widehat\delta_{tight,D}.
\]

Because every normalized face has equal energy,

\[
\operatorname{Tr}\widehat S_D=1
\]

under the present block convention, so every improvement in

\[
\widehat A_D
\]

is necessarily pure direction-space isotropy gain.

The first sharp research question becomes:

\[
\boxed{
\sup_{|D|=\lfloor d^2/2\rfloor}
\widehat\eta_D
\stackrel{?}{\longrightarrow}0
}
\]

for scalable Coxeter face classes, versus the existence of bounded-oversampling families with `widehat eta` bounded below polynomially or uniformly.

Only after this projective layer is understood should one return to a physical resource model and decide how face amplitude, control time, and noise variance should be weighted.

---

## 9. Claim firewall

This note provides reproducible small-dimensional evidence. It does not prove:

- a Coxeter-specific sharp-design upper bound on `eta`;
- an asymptotic redundancy gap;
- physical canonicity of per-face Hilbert-Schmidt normalization;
- sample-complexity or noise-optimality claims;
- experimental cost equivalence of different loop types;
- non-Markovian or process-tensor extensions.
