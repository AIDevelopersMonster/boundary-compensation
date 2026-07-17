# BC-IDPR-P3-B-03 — Geometry Leakage M3 Research Audit

**Status:** internal mathematical and computational review, v0.1.0  
**Date:** 2026-07-16  
**Scope:** complete external geometry and leakage control; semantic quantization bridge remains open.

## 1. Reviewed claim

The reviewed claim is deliberately relative:

> Along the declared theta-path, a complete externally specified regular Euclidean tetrahedron, representation labels, scale calibration and protocol remain exactly fixed, while the three-channel q-Racah operator package has a nonzero nuisance-quotient derivative.

This is a parameter-separation claim. It is not yet a claim that the operator package quantizes a specified classical tetrahedral observable.

## 2. External geometry audit

The external tetrahedron is fixed by four exact algebraic vertices. The implementation independently verifies:

- six unit edge lengths;
- four face areas `sqrt(3)/4`;
- exact volume `sqrt(2)/12`;
- outward unit normals;
- exact area-vector closure;
- normal Gram matrix with diagonal `1` and off-diagonal `-1/3`;
- Gram rank three and null vector `(1,1,1,1)`;
- non-coplanarity of the normals;
- exact label-area calibration for labels `(1,1,1,1)`.

The geometry is therefore complete independently of the labels. The labels are only calibrated to the already fixed areas.

## 3. Leakage audit

Every forbidden external channel has exact derivative zero:

- vertices;
- edges;
- areas;
- normals;
- Gram data;
- volume;
- labels;
- label-area scale;
- protocol.

Hence

\[
E_{\mathrm{ext}}=0.
\]

This is stronger than a small numerical leakage estimate because the external datum is constant by definition and checked symbolically.

The internal ledger records nonzero responses in q-numbers, the q-Racah matrix, both channel operators and two quotient invariants. At the anchor,

\[
\|V_{\mathrm{int}}\|=20.3533745130361\ldots,
\]

while the nuisance-quotient margin is

\[
m_{\mathrm{int}}=2.5422533772484\ldots.
\]

## 4. Persistence and conditioning

On the 33-point compact grid:

\[
\min m_{\mathrm{int}}=1.2292366584592\ldots>0,
\]

and

\[
\min m_{\mathrm{op}}^{\mathrm{dual}}=0.53229704247649\ldots>0.
\]

The q-Racah orthogonality residual remains below `1.36e-80`. The nuisance Gram matrix remains nonsingular, with minimum eigenvalue above `0.7639` and condition number below `14.724`.

These are numerical grid bounds, not continuum minima. Continuum operator nontriviality continues to rely on the exact invariant sign theorem already established in M2.

## 5. Literature consultation

The geometric declaration is consistent with the Minkowski reconstruction principle for convex polyhedra: face normals and positive face areas satisfying closure determine a convex polyhedron up to translation under the standard nondegeneracy hypotheses. In this module, however, the vertices are already given explicitly, so no external uniqueness theorem is needed to establish the concrete tetrahedron.

The q-Racah side remains consistent with established `U_q(sl_2)` recoupling practice and with the non-Euclidean tetrahedral interpretation of quantum 6j asymptotics. These external sources justify the mathematical setting but do not supply the BC leakage certificate or the missing symbol map.

Primary consultation points:

1. Y. U. Taylor and C. T. Woodward, *6j symbols for U_q(sl_2) and non-Euclidean tetrahedra*, arXiv:math/0305113.
2. E. Bianchi, P. Dona and S. Speziale, *Polyhedra in loop quantum gravity*, arXiv:1009.3402.

No advisory Gemini statement is used as evidence.

## 6. Reviewer concerns

### Concern A — geometry fixed only by equal labels

**Resolved.** Shape is fixed independently by vertices, normals and Gram data. Equal labels enter only through an explicit area calibration.

### Concern B — the geometry might drift implicitly with q

**Resolved at the external-control level.** All external data are q-independent constants and their derivatives are exactly zero.

### Concern C — internal quantum geometry is being called leakage

**Resolved terminologically.** q-number and recoupling variation is classified as allowed internal response, not forbidden external leakage.

### Concern D — a fixed tetrahedron automatically gives physical meaning to the operators

**Not resolved and explicitly blocked.** M3 has not constructed a coherent-state or lower-symbol map proving that the q-Racah operator package represents a chosen classical observable of this tetrahedron.

### Concern E — the regular tetrahedron is too symmetric

**Valid limitation.** The exact symmetry is useful for calibration and eliminates reconstruction ambiguity, but it does not test anisotropic shape dependence. A later robustness module must include at least one scalene convex tetrahedron.

### Concern F — zero leakage is tautological

**Partly true, but methodologically useful.** The purpose of M3 is not to discover that constants have zero derivative. It is to freeze a complete geometry datum and expose exactly which channels are fixed and which are allowed to vary, thereby preventing later reinterpretation of internal q-response as an unnoticed geometry change.

## 7. Verdict

**Accept P3-B-M3 with restricted claim.**

Assign status:

`COMPLETE_EXTERNAL_GEOMETRY_AND_ZERO_LEAKAGE_CERTIFIED`.

The geometry-control objection to M2 is closed. The intrinsic q-response is no longer attributable to variation of the declared external tetrahedron, representation scale or protocol.

## 8. Why CERT remains blocked

CERT concerns observable separation and therefore requires a semantic bridge between:

\[
X_{\mathrm{ext}}
\quad\text{and}\quad
\mathcal D_J(\theta).
\]

M3 supplies both endpoints but not the map. Without a declared classical symbol, coherent-state expectation or calibrated observable correspondence, the nonzero operator derivative cannot yet be interpreted as distinguishable response of the fixed tetrahedral geometry.

## 9. Required next step

Proceed to `P3-B-M4 / Geometry-to-Operator Symbol Bridge`:

1. select a declared classical tetrahedral observable or coordinate package;
2. construct a coherent-state or lower-symbol map for the three-channel carrier;
3. calibrate it at the anchor;
4. measure and bound symbol mismatch across the compact interval;
5. separate symbol error, q-response and wall error;
6. add a nonsymmetric tetrahedron as a holdout geometry.

Only after that bridge is certified may the programme enter CERT.
