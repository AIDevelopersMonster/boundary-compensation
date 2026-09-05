# Odd-dimensional extension-ready minimal Coxeter designs — proof audit

**Article I post-publication research note — v0.1.1**  
**Author:** Malachevsky, A.A.  
**ORCID:** 0009-0008-6009-3196  
**Status:** `PROOF_AUDIT_OPEN / LOW_D_CORRECTED_FORMULAS_VERIFIED / DO_NOT_CITE_AS_ALL_D_THEOREM`

## 1. Audit correction

The previous v0.1 draft stated an all-odd extension-ready existence theorem. That status is withdrawn pending one specific repair.

The issue is not the restriction-quotient dimension theorem. The issue is the coordinate formula used for the embedded faces.

For the actual block embedding

`T_A = diag(A,1) in M_(d+1)(C)`,

let a normalized map on

`B=M_d(C) direct-sum C`

be represented by a complex-linear map

`F:M_d(C)->E`

through

`D(diag(A,a)) = F(A-a I)`.

Then an embedded ordered branch `(A,B)` does **not** act by the uncentered surrogate formulas used in v0.1.

Put

`A0=A-I`, `B0=B-I`, `C0=AB-I`.

The correct branch formulas are:

### Regular output sector

`K_reg(F;A,B)=F(C0)-F(A0)B-AF(B0)`.

Equivalently,

`K_reg = F(AB)-F(A)B-AF(B)+F(I)B+AF(I)-F(I)`.

### Left output sector

`K_L(F;A,B)=F(C0)-F(A0)-AF(B0)`.

Equivalently,

`K_L = F(AB)-F(A)-AF(B)+AF(I)`.

### Right output sector

`K_R(F;A,B)=F(C0)-F(A0)B-F(B0)`.

Equivalently,

`K_R = F(AB)-F(A)B-F(B)+F(I)B`.

### Scalar output sector

`K_0(F;A,B)=F(C0)-F(A0)-F(B0)`.

Equivalently,

`K_0 = F(AB)-F(A)-F(B)+F(I)`.

For a real square face, the complexified second branch is obtained from

`(A,B) -> (B^(-1),A^(-1))`.

These are the formulas that must be used in every extension-ready proof.

## 2. Why the correction matters

The previous v0.1 proof used the surrogate sector forms

`F(AB)-F(A)B-AF(B)`,

`F(AB)-AF(B)`,

`F(AB)-F(A)B`,

and `F(AB)`.

Those formulas are appropriate only after a different, singular/uncentered degeneration; they are not literally the scalar-one embedded measurement operator.

In particular, a face with one transport equal to the identity is automatically trivial for a normalized Leibniz defect. Any proof that uses such a face to detect an `F(I)` direction in the actual scalar-one embedding is invalid.

Therefore the all-odd theorem stated in v0.1 must not be cited until the centered-coordinate proof is completed.

## 3. Corrected low-dimensional audit

The proposed v0.1 face family was rebuilt with the correct formulas above.

For the same seed structure

`B_X=I+tX^2+s(Z+eta Z^2)`, `A_X=X B_X^(-1)`,

`B_Z=I+tZ^2`, `A_Z=Z B_Z^(-1)`,

together with the axis and mixed Weyl forests, direct complex rank calculations give:

### d=3

With `4` real faces (`8` complex branches):

- scalar rank: `8/8`;
- left rank: `24/24`;
- right rank: `24/24`;
- regular rank: `72/72`.

### d=5

With `12` real faces (`24` complex branches):

- scalar rank: `24/24`;
- left rank: `120/120`;
- right rank: `120/120`;
- regular rank: `600/600`.

### d=7

With `24` real faces (`48` complex branches):

- scalar rank: `48/48`;
- left rank: `336/336`;
- right rank: `336/336`;
- regular rank: `2352/2352`.

Thus the construction survives the corrected scalar-one embedding in the tested odd dimensions. These calculations are evidence and an audit of the formulas; they are not an all-`d` proof.

## 4. Correct centered-cocycle viewpoint

If

`G(A)=F(A-I)`,

then `G(I)=0` and the branch equations become

- regular:

  `G(AB)-G(A)B-A G(B)`;

- left:

  `G(AB)-G(A)-A G(B)`;

- right:

  `G(AB)-G(A)B-G(B)`;

- scalar:

  `G(AB)-G(A)-G(B)`.

This is the correct cohomological form of the embedded problem.

For Weyl products, the projective multiplication phases are essential: they couple the otherwise missing affine direction to the finite-Heisenberg multiplication relations. The old proof treated the forest as if it were ordinary uncentered evaluation, so its triangularity argument must be rewritten in this centered/projective language.

## 5. What remains to restore the theorem

The numerical audit shows that the proposed seed family is very likely the correct witness family. The missing theorem-level step is now sharply isolated:

> Prove, with the centered formulas above, that the axis/mixed forest plus the two seed faces has the declared four sector ranks for every odd `d>=3`.

The regular two-frequency Schur mechanism remains a promising route, but the left/right/scalar sectors also require centered proofs rather than the v0.1 surrogate formulas.

Until that repair is written, the correct status is:

- structural embedded-rank ceiling: **proved**;
- exact extension-ready examples in low dimensions: **supported by direct rank calculations**;
- all-odd extension-ready theorem: **open proof obligation**.

## 6. Publication firewall

Do not state from this note that

`L_d^Cox=(d^2-1)/2`

has been proved for every odd `d`.

The all-odd statement may be restored only after a centered scalar-one proof, or after an independent exact all-`d` construction, is completed.
