# P3-B-M5 Research Audit — Nonuniform-Spin Unequal-Area Carrier

**Date:** 2026-07-16  
**Verdict:** `NONUNIFORM_SPIN_UNEQUAL_AREA_CARRIER_CERTIFIED`

## 1. Reviewed construction

The module replaces the four-spin-one carrier of M4 with

\[
(j_1,j_2,j_3,j_4)=\left(\tfrac12,1,2,\tfrac52\right).
\]

The common invariant channels are

\[
e\in\left\{\tfrac12,\tfrac32\right\},\qquad f\in\{2,3\},
\]

so both recoupling bases have dimension two. Direct Clebsch–Gordan construction gives a basis Gram residual below \(5\times10^{-16}\).

## 2. Genuine unequal-area geometry

An explicit closed set of outward face-area vectors is constructed with magnitudes

\[
(0.5,1,2,2.5).
\]

These are exactly proportional to the selected spins. The area-vector closure residual and the vertex-reconstruction residual are zero at displayed precision. The reconstructed tetrahedron has positive volume

\[
V=0.44582686998428134
\]

and edge spread

\[
2.818688293234257,
\]

so it is not an equifacial or regular surrogate.

## 3. q-recoupling audit

The two-by-two q-recoupling matrix is built from the direct q-Racah formula. Its sign gauge is fixed once by comparison with the direct SU(2) overlap matrix in the small-theta limit. The gauge-match residual is approximately

\[
1.76\times10^{-14}.
\]

On the 33-point interval grid \([\pi/15,\pi/10]\), the maximum orthogonality residual is below

\[
3.16\times10^{-16}.
\]

## 4. Coherent-state and response audit

The tensor product of four spin-j coherent states is projected into the invariant carrier. The resulting channel probabilities are approximately

\[
(0.3643410853,0.6356589147),
\]

with zero displayed normalization residual.

At the anchor \(\theta_0=\pi/12\), the declared normalized pair-Casimir symbol is

\[
(-0.0379765852,-0.0923514679).
\]

Its differential response is

\[
\partial_\theta S(\theta_0)=(0,0.0686871452),
\]

with finite-difference step radius below \(4.97\times10^{-8}\). The first coordinate is a q-independent negative control. The endpoint symbol separation on the declared interval is approximately

\[
0.00871584254.
\]

## 5. What has been closed

The following obligations are closed:

- nonuniform external spins;
- a finite invariant carrier with explicitly enumerated channels;
- a genuine unequal-area Euclidean tetrahedron;
- common area-to-spin calibration;
- fixed-geometry nonzero q-response;
- q-recoupling orthogonality on the declared grid.

## 6. What remains open

The construction does not establish absolute lower-symbol accuracy, asymptotic semiclassical control, or a phase law. It supplies a new carrier on which a new calibration-quotient certificate and a separately preregistered P1 pilot may be attempted.

The prior negative P1-PILOT-01 result remains valid for its original equal-spin protocol. It must not be overwritten or reinterpreted as evidence for this carrier.

## 7. Claim firewall

Do not infer:

- physical evolution of q;
- unique quantization;
- a universal tetrahedron-to-operator map;
- empirical observability;
- a confirmed trigonometric residual law;
- continuum separation outside the declared interval.

No statement from the Gemini advisory report is used as evidence.

## 8. Reproducibility

Eight dedicated M5 tests pass locally. They check status, carrier dimension, exact area pattern, closure, vertex reconstruction, basis orthonormality, recoupling orthogonality, and nonzero differential response.

## 9. Next step

Proceed to `BC-IDPR-CERT-03 / Nonuniform-Carrier Calibration-Quotient Separation`. It must freeze the nuisance group and observable package before evaluation. Only after a positive CERT-03 may a second P1 pilot be preregistered.
