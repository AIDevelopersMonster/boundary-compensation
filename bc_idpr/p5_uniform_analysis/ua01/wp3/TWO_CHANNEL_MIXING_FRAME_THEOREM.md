# BC-IDPR P5-UA01 WP3 — Uniform Two-Channel Mixing Frame Theorem

**Contract:** `BC-IDPR-P5-UA01-WP3`  
**Status:** `RIGOROUS_ARB_TWO_CHANNEL_MIXING_BOUND_CERTIFIED`  
**Declared class:** the 283 ordered carriers in the finite algebraic two-channel class `A6`  
**Deformation chamber:** `eta in [3/5, 23/20]`, with `theta = pi eta / 12`  
**Residual bundle:** centered, Hilbert--Schmidt-normalized contrasts of the two channel observables.

## 1. Operator-adapted residual bundle

For an ordered two-channel carrier `J`, let the two channel sets be

\[
E(J)=\{e_-,e_+\},
\qquad
G(J)=\{f_-,f_+\},
\]

and let `F_J(theta)` be the real transpose-orthogonal recoupling matrix in the frozen q-Racah convention.

The diagonal channel observables have two distinct eigenvalues throughout the declared chamber. The critical dimension indices are at most eight and

\[
8\theta\le \frac{23\pi}{30}<\pi,
\]

so the ordered cosine eigenvalues remain distinct. After centering and Hilbert--Schmidt normalization, their signs are fixed by the increasing channel order. Up to a simultaneous harmless sign convention, the normalized residual operators are

\[
B_{E,J}=D,
\qquad
B_{G,J}(\theta)=F_J(\theta)D F_J(\theta)^T,
\]

where

\[
D=\frac{1}{\sqrt 2}
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}.
\]

Thus the P5 residual basis is not an arbitrary abstract basis: it is the normalized centered form of the two channel operators already present in the finite q-Racah operator envelope.

## 2. Exact coordinate map

Write the first row of the orthogonal block as

\[
F_J(\theta)_{1\bullet}=(a_J(\theta),b_J(\theta)),
\qquad
a_J^2+b_J^2=1.
\]

In the Hilbert--Schmidt-orthonormal basis

\[
E_z=D,
\qquad
E_x=\frac{1}{\sqrt2}
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix},
\]

one has

\[
B_{G,J}
=
(a_J^2-b_J^2)E_z+2a_Jb_JE_x.
\]

Therefore the operator-adapted coordinate matrix may be chosen as

\[
C_J(\theta)=
\begin{pmatrix}
1&a_J^2-b_J^2\\
0&2a_Jb_J
\end{pmatrix},
\]

up to column signs that do not change its singular values.

Let

\[
c_J(\theta)
=
\langle B_{E,J},B_{G,J}(\theta)\rangle_{HS}
=
a_J^2-b_J^2.
\]

Then

\[
C_J(\theta)^T C_J(\theta)
=
\begin{pmatrix}
1&c_J(\theta)\\
c_J(\theta)&1
\end{pmatrix},
\]

and hence

\[
\sigma_{\min}(C_J(\theta))^2
=1-|c_J(\theta)|.
\]

## 3. Mixing-to-frame identity

The exact E-optimal four-state coherent design from WP1/WP2 has canonical frame operator `I_2/4`. Consequently,

\[
F_{\mathrm{frame},J}(\theta)
=\frac14 C_J(\theta)^T C_J(\theta),
\]

and

\[
\boxed{
 c_{\mathrm{frame},J}(\theta)
 =\frac14\bigl(1-|c_J(\theta)|\bigr)
 =\frac12\min\{|a_J(\theta)|^2,|b_J(\theta)|^2\}.
}
\]

Because every real `2 x 2` orthogonal matrix has the same two absolute entry values in each row and column,

\[
\boxed{
 c_{\mathrm{frame},J}(\theta)
 =\frac12\min_{i,j}|F_J(\theta)_{ij}|^2.
}
\]

This is the exact P5 reduction. A frame wall is equivalent to a zero entry of the two-channel recoupling block; no separate numerical rank convention is needed.

## 4. Analytic extremal family

For the edge family

\[
J_L=(1,L,1,L),
\qquad 1\le L\le6,
\]

the q-Racah sum reduces exactly to

\[
F_{J_L}(\theta)
=
\frac{1}{[L+1]_\theta}
\begin{pmatrix}
-1&\sqrt{[L]_\theta[L+2]_\theta}\\
\sqrt{[L]_\theta[L+2]_\theta}&1
\end{pmatrix}.
\]

The identity

\[
[L+1]_\theta^2=1+[L]_\theta[L+2]_\theta
\]

is the sine-product identity

\[
\sin^2((L+1)\theta)-\sin(L\theta)\sin((L+2)\theta)=\sin^2\theta.
\]

For `L=6`, the smaller absolute matrix entry is `1/[7]_theta`. On

\[
\theta\in\left[\frac\pi{20},\frac{23\pi}{240}\right]
\subset(0,\pi/7),
\]

the q-number `[7]_theta` is strictly decreasing. Indeed,

\[
\frac{d}{d\theta}\log[n]_\theta
=n\cot(n\theta)-\cot\theta
=\frac{h(n\theta)-h(\theta)}{\theta},
\qquad
h(x)=x\cot x,
\]

and `h` is strictly decreasing on `(0,pi)`. Therefore `1/[7]_theta` is minimized at `theta=pi/20`.

The two ordered extremizers are

\[
J=(1,6,1,6),
\qquad
J=(6,1,6,1),
\]

and their extremal entry is

\[
\boxed{
 b_*
 =\frac{1}{[7]_{\pi/20}}
 =\frac{\sin(\pi/20)}{\sin(7\pi/20)}.
}
\]

## 5. Rigorous finite-class certificate

The remaining 281 ordered carriers were verified by outward-rounded Arb ball arithmetic.

The verifier:

1. reconstructs the exact algebraic class `A6` by integer enumeration;
2. obtains exactly 283 ordered carriers;
3. evaluates the frozen trigonometric q-Racah formula directly;
4. starts with 16 theta cells per nonextremal carrier;
5. adaptively bisects any cell whose entry lower bound does not yet exceed the upper Arb ball for `b_*`;
6. repeats the complete calculation at 192-bit and 256-bit precision.

Both runs checked 31,934 Arb cells, required maximum refinement depth 5, and certified every absolute recoupling entry of every nonextremal carrier strictly above `b_*`.

The smallest certified nonextremal lower ball is approximately

\[
0.1758209384959990282880320926853,
\]

which remains strictly above

\[
b_*\approx0.1755705045849462583374119092781.
\]

The machine-readable certificate and verifier are stored beside this document.

## 6. Uniform theorem

**Theorem 1 — Uniform normalized two-channel frame bound on `A6`.**  
For every ordered carrier `J` in the declared 283-carrier class `A6` and every

\[
\eta\in[3/5,23/20],
\qquad
\theta=\pi\eta/12,
\]

the normalized channel-contrast residual bundle has constant rank two and satisfies

\[
\min_{i,j}|F_J(\theta)_{ij}|\ge b_*>0.
\]

Consequently,

\[
\boxed{
 c_{\mathrm{frame},J}(\theta)
 \ge
 \underline c_{\mathrm{frame}}
 :=
 \frac12
 \left(
 \frac{\sin(\pi/20)}{\sin(7\pi/20)}
 \right)^2
 >0.
}
\]

Numerically,

\[
\underline c_{\mathrm{frame}}
\approx0.0154125010401063175602946735390.
\]

Equality is attained by the two analytic extremizers at `eta=3/5`. Thus the constant is sharp for the declared class and chamber.

## 7. Programme consequence

For this normalized two-channel residual bundle:

```text
UA01-G1 DESIGN:        PASS
UA01-G2 LOCAL_FRAME:   PASS
UA01-G3 UNIFORM_FRAME: PASS_ON_DECLARED_A6_CHAMBER
```

The direct Arb proof makes a Lipschitz-cover argument unnecessary for this finite bundle. The general WP3 jet-to-Lipschitz route remains relevant for larger carrier classes, higher channel dimension, or non-normalized residual bases.

The next unresolved gate is not frame positivity. It is the WP6 transfer problem: connect the normalized channel-contrast coefficients to the frozen complex phase statistic and predictor-versus-control energy functional without using RC02 confirmatory data for tuning.

## 8. Claim firewall

This theorem proves a sharp finite-class frame lower bound only for:

- the exact `A6` carrier list;
- two-channel real q-Racah blocks;
- the frozen eta interval;
- centered, normalized channel-contrast operators;
- the four-state coherent design already certified in WP1/WP2.

It does not prove:

- an arbitrary-label or arbitrary-level bound;
- a higher-channel frame theorem;
- a full modular-category result;
- an amplitude floor for the RC02 complex statistic;
- phase-concentration or positive energy-advantage transfer;
- global gluing, a continuum limit, or physical dynamics.
