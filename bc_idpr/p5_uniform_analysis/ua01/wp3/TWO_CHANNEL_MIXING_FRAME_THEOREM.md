# BC-IDPR P5-UA01 Appendix B — Uniform Two-Channel q-Racah Mixing Bound

**Artifact:** `BC-IDPR-P5-UA01-AUX-Q-RACAH-MIXING-A6`  
**Status:** `RIGOROUS_AUXILIARY_MIXING_BOUND_CERTIFIED / PHYSICAL_RESIDUAL_FRAME_GATE_OPEN`  
**Declared class:** 283 ordered carriers in the finite algebraic two-channel class `A6`  
**Deformation chamber:** `eta in [3/5,23/20]`, with `theta=pi eta/12`.

## 1. Auxiliary channel-contrast bundle

For an ordered two-channel carrier `J`, let `F_J(theta)` be the frozen real q-Racah recoupling block. On the abstract channel space define the normalized centered contrast

\[
D=\frac1{\sqrt2}\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\qquad
B_E=D,
\qquad
B_G(\theta)=F_J(\theta)DF_J(\theta)^T.
\]

This bundle is mathematically natural inside the finite q-Racah envelope, but it is not automatically the N15 physical residual plane

\[
\operatorname{span}\{R_{\rm bulk},W\}.
\]

Nor does it by itself specify the inherited projected-torus coherent-state lower-symbol map.

## 2. Exact mixing identity

Writing the first row of `F_J` as `(a_J,b_J)`, one has

\[
B_G=(a_J^2-b_J^2)E_z+2a_Jb_JE_x.
\]

Thus the coordinate Gram matrix of the two abstract contrasts is

\[
C_J^TC_J=
\begin{pmatrix}
1&c_J\\c_J&1
\end{pmatrix},
\qquad
c_J=a_J^2-b_J^2,
\]

and therefore

\[
\sigma_{\min}(C_J)^2=1-|c_J|
=2\min\{|a_J|^2,|b_J|^2\}.
\]

A mixing wall is equivalent to a zero entry of the two-channel recoupling block.

## 3. Analytic extremal family

For

\[
J_L=(1,L,1,L),\qquad1\le L\le6,
\]

the recoupling block reduces to

\[
F_{J_L}(\theta)=\frac1{[L+1]_\theta}
\begin{pmatrix}
-1&\sqrt{[L]_\theta[L+2]_\theta}\\
\sqrt{[L]_\theta[L+2]_\theta}&1
\end{pmatrix}.
\]

The identity

\[
[L+1]_\theta^2=1+[L]_\theta[L+2]_\theta
\]

follows from the sine-product formula. For `L=6`, the smallest entry magnitude is

\[
b_*=rac1{[7]_{\pi/20}}
=\frac{\sin(\pi/20)}{\sin(7\pi/20)}.
\]

## 4. Finite-class Arb certificate

An outward-rounded Arb computation over all 283 ordered `A6` carriers and the full frozen chamber certified

\[
\min_{i,j}|F_J(\theta)_{ij}|\ge b_*>0.
\]

The two analytic extremizers are `(1,6,1,6)` and `(6,1,6,1)` at `eta=3/5`. Hence the abstract channel-contrast coordinate map has the sharp floor

\[
\sigma_{\min}(C_J)^2
\ge 2b_*^2
\]

on the declared class.

Numerically,

\[
b_*\approx0.1755705045849463,
\qquad
\frac12b_*^2\approx0.0154125010401063.
\]

The last number equals the frame floor only under the auxiliary ideal-projective design of Appendix A. It is not the physical N15 residual-frame constant.

## 5. Programme role

This appendix closes a useful representation-theoretic statement:

> finite `A6` two-channel q-Racah blocks stay uniformly away from signed permutation walls on the frozen deformation chamber.

It may later contribute to a physical P5 theorem after an explicit bridge is proved from the N15 residual generators and projected-torus symbol matrix to this channel-contrast bundle.

Current gate status:

```text
AUXILIARY q-RACAH MIXING: CERTIFIED
N15 PHYSICAL MEASUREMENT MATRIX: OPEN
PHYSICAL LOCAL FRAME GATE: OPEN
PHYSICAL UNIFORM FRAME GATE: OPEN
P2 HANDOFF: BLOCKED
```

## 6. Claim firewall

This result is restricted to the finite `A6` class, real two-channel q-Racah blocks and the frozen eta chamber. It does not prove a lower bound for the physical N15 generalized Gram eigenvalue, phase concentration, energy advantage, arbitrary labels, higher-channel sectors, global gluing, a continuum limit or dynamics.
