# BC-IDPR-P3-B-01 — Minimal Generic-q Research Audit

**Status:** internal mathematical and computational review, v0.1.0  
**Date:** 2026-07-16  
**Scope:** P3-B-M1 only; observable certification and larger-skeleton robustness remain open.

## 1. Reviewed claim

The reviewed claim is deliberately narrow:

> For the declared two-channel finite generic-q recoupling envelope, at `theta0 = pi/4`, the derivative of the ordered operator pair `(X(theta),Y(theta))` has a nonzero component orthogonal to common identity shift, common scalar normalization, and simultaneous basis conjugation, while the external equal-label ray is held fixed.

This is an operator-envelope claim. It is not a categorical-deformation claim and it is not a physical interpretation of `q`.

## 2. Exact result

The symbolic computation gives

\[
\|V_\theta\|^2=56,
\qquad
m_{\mathrm{int}}^2=8,
\qquad
\widehat m_{\mathrm{int}}^2=\frac17.
\]

Hence

\[
m_{\mathrm{int}}=2\sqrt2>0,
\qquad
\widehat m_{\mathrm{int}}=\frac1{\sqrt7}.
\]

The nuisance Gram matrix is exactly

\[
\operatorname{diag}(4,8,32),
\]

so no threshold or pseudoinverse ambiguity enters the projection.

## 3. Independent invariant check

The centered normalized correlation

\[
c(\theta)=
\frac{\operatorname{Tr}(X_cY_c)}
{\|X_c\|_{\mathrm{HS}}\|Y_c\|_{\mathrm{HS}}}
\]

is unchanged by every declared nuisance transformation. For the selected family,

\[
c(\theta_0)=0,
\qquad
c'(\theta_0)=2.
\]

Thus the nontriviality conclusion is not an artifact of the projection implementation.

## 4. Anchor and chamber audit

The matrix

\[
F(\theta)=\frac1{[2]_\theta}
\begin{pmatrix}
1&\sqrt{[3]_\theta}\\
\sqrt{[3]_\theta}&-1
\end{pmatrix}
\]

is exactly orthogonal because `[2]_theta^2 = 1 + [3]_theta`. At `theta0 = pi/4` it equals the Ising block used by P3-A.

The selected real chart is restricted to

\[
0<\theta<\pi/3,
\]

where the chosen positive square root of `[3]_theta` is regular. The anchor has wall distance `pi/12`.

The wall is a model-chart boundary, not a physical phase transition.

## 5. Relation to external literature

External literature is used only to check that the chosen mathematical ingredients belong to established recoupling/TQFT practice, not to certify the new BC projection result.

Marché and Paul study finite-dimensional TQFT curve operators on the punctured torus and four-punctured sphere and identify their semiclassical trace-function symbols through Toeplitz analysis. This supports treating ordered packages of channel operators and recoupling transformations as legitimate finite operator data, but it does not imply that the present two-channel envelope is a full TQFT away from the root point.

Primary external reference:

1. J. Marché and T. Paul, *Toeplitz operators in TQFT via skein theory*, arXiv:1108.0629.

Background consistency reference for the Ising anchor:

2. B. Field and T. Simula, *Introduction to topological quantum computation with non-Abelian anyons*, arXiv:1802.06176.

No statement from the Gemini advisory report is used as evidence in this certificate.

## 6. Reviewer concerns

### Concern A — the family may merely rescale

**Resolution:** common scale is included in the nuisance space, yet the projected derivative remains nonzero.

### Concern B — the family may merely change basis

**Resolution:** simultaneous conjugation is included explicitly. The invariant correlation derivative independently survives conjugation.

### Concern C — trace drift may create a false signal

**Resolution:** common identity shift is included. The independent check uses centered matrices.

### Concern D — the external geometry declaration is too weak

**Assessment:** valid concern. The fixed equal-label ray is a control datum, not a complete classical geometry. Therefore the result proves independent variation relative to that declared control, not relative to a fully reconstructed tetrahedral geometry. P3-B-M2 must strengthen this interface.

### Concern E — generic q is being confused with continuous SU(2)_k

**Resolution:** model class is explicitly `finite_generic_q_recoupling_envelope`; only the anchor is identified with the k=2 Ising block.

### Concern F — the operator pair is too small

**Assessment:** correct as a limitation, not a defect. M1 is a minimal existence/calibration result. It must not be generalized before a larger-skeleton test.

## 7. Verdict

**Accept P3-B-M1 with a restricted claim.**

Assign status

`INTRINSIC_DIRECTION_CERTIFIED`.

The result establishes that the P3 architecture is non-vacuous: local categorical rigidity at the fixed Ising datum can coexist with a nonzero intrinsic derivative in a larger analytic operator envelope.

## 8. Publication firewall

Do not claim from M1:

- a continuous family of standard `SU(2)_k` categories;
- a new quantum-volume operator;
- fixed complete geometry;
- observable distinguishability;
- physical significance of theta;
- generic persistence for larger labels;
- passage through the root-of-unity wall.

## 9. Required next step

Proceed to P3-B-M2, not directly to P1. Build the first larger finite label skeleton from direct q-6j/Racah evaluation, enlarge the nuisance model, and test persistence of the intrinsic margin over a compact regular subinterval.
