# BC-IDPR-P3-B-M5 — Nonuniform-Spin Carrier and Genuine Unequal-Area Holdout

**Status:** construction module, v0.1.0  
**Date:** 2026-07-16  
**Result:** `NONUNIFORM_SPIN_UNEQUAL_AREA_CARRIER_CERTIFIED`

## 1. Purpose

CERT-02 left one structural obligation open: the M4 carrier used four equal spins and therefore could not encode a genuine unequal-area tetrahedron. M5 replaces the carrier itself rather than treating this as a calibration-layer issue.

The external spins are frozen as

\[
(j_1,j_2,j_3,j_4)=\left(\tfrac12,1,2,\tfrac52\right).
\]

The admissible invariant channels are

\[
e\in\left\{\tfrac12,\tfrac32\right\},\qquad
f\in\{2,3\},
\]

so the invariant carrier is two-dimensional.

## 2. Explicit unequal-area tetrahedron

The face-area vectors are chosen with magnitudes

\[
(A_1,A_2,A_3,A_4)=(0.5,1,2,2.5),
\]

and satisfy exact vector closure in floating arithmetic. From three independent area vectors the vertex matrix is reconstructed through the cofactor identity

\[
B=\det(M)M^{-T},\qquad M=\sqrt{\det B}\,B^{-T}.
\]

The resulting tetrahedron has positive volume and nonzero edge spread. Its face areas are proportional to the four external spins with one common calibration constant.

## 3. Recoupling operator

The q-recoupling matrix is built directly from the q-Racah formula. Row and column signs are frozen by matching the small-theta limit to the direct SU(2) Clebsch–Gordan overlap matrix. Orthogonality is checked throughout

\[
\theta\in[\pi/15,\pi/10].
\]

## 4. Coherent projection and observables

A tensor product of four spin-j coherent states, with directions fixed by the outward face normals, is projected into the invariant carrier. The declared observables are the normalized pair-Casimir channels for pairings 12 and 23.

At the anchor \(\theta_0=\pi/12\), the second channel has a nonzero differential response while the first channel is a q-independent negative control.

## 5. Certified claims

M5 certifies:

- an explicit nonuniform-spin invariant carrier;
- an explicit Euclidean tetrahedron with face areas in the ratio \(1:2:4:5\);
- exact area-vector closure and successful vertex reconstruction;
- an orthogonal two-channel q-recoupling family on the declared interval;
- a normalized coherent carrier state;
- a nonzero lower-symbol q-response at fixed unequal external areas and fixed geometry.

## 6. Non-claims

M5 does not certify:

- absolute semiclassical accuracy at these finite spins;
- a unique observable map;
- physical dynamics of q;
- a phase-residual law;
- a confirmatory P1 result;
- universality beyond the declared carrier and interval.

The next P1 evaluation requires a new preregistration. Results from P1-PILOT-01 cannot be recycled as its decision rule.
