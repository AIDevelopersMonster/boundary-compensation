# The d=2 obstruction to minimal extension-readiness

Status: PROVED / LOW-DIMENSIONAL EXCEPTION

## Statement

Let a Coxeter design in dimension d=2 contain the minimal number

\[
L_2^{\rm Cox}=\left\lfloor \frac{2^2}{2}\right\rfloor=2
\]

of square faces. Under the scalar-one embedding

\[
M_2\hookrightarrow M_3,\qquad A\mapsto \operatorname{diag}(A,1),
\]

no such two-face design can be extension-ready.

Equivalently, for every pair of Coxeter squares the embedded restriction measurement on

\[
\mathcal B=M_2\oplus \mathbb C
\]

has rank at most

\[
R_{\rm res}(2)-1=28,
\]

where

\[
R_{\rm res}(2)=(2^2-1)3^2+2=29.
\]

Thus extension-ready minimal Coxeter designs can only begin at d=3.

## Proof

A normalized restriction map on \(\mathcal B\) may be written as

\[
D(\operatorname{diag}(X,a))=F(X-aI_2),
\]

with a complex-linear map

\[
F:M_2\to M_3.
\]

Consider the four-dimensional scalar-output sector

\[
F_\phi(X)=\phi(X)E_{33},\qquad \phi\in M_2^*.
\]

This sector contains no Hamiltonian gauge direction. Indeed, for every \(H\in M_3\),

\[
[H,\operatorname{diag}(X,0)]_{33}=0.
\]

Hence an extension-ready design must impose four independent scalar-output conditions.

Take one Coxeter square and denote its first two complexified transports by

\[
A,B\in SL_2(\mathbb C).
\]

For the branch \((A,B)\), the scalar-output defect of \(F_\phi\) is

\[
\phi\bigl((A-I)(B-I)\bigr)E_{33}.
\]

Set

\[
C=(A-I)(B-I).
\]

The paired Coxeter branch is \((B^{-1},A^{-1})\), whose scalar-output defect is

\[
\phi\bigl((B^{-1}-I)(A^{-1}-I)\bigr)E_{33}.
\]

For every \(A\in SL_2(\mathbb C)\),

\[
\operatorname{adj}(A-I)=A^{-1}-I.
\]

Since \(\operatorname{adj}(XY)=\operatorname{adj}(Y)\operatorname{adj}(X)\),

\[
(B^{-1}-I)(A^{-1}-I)=\operatorname{adj}(C).
\]

Now decompose

\[
C=sI+T,\qquad \operatorname{tr}T=0.
\]

For a \(2\times2\) matrix,

\[
\operatorname{adj}(C)=\operatorname{tr}(C)I-C=sI-T.
\]

Therefore the two scalar branch rows contributed by one face lie in

\[
\operatorname{span}\{I,T\}\subset M_2.
\]

For two faces with traceless parts \(T_1,T_2\), all four scalar branch rows lie in

\[
\operatorname{span}\{I,T_1,T_2\},
\]

which has dimension at most three. Hence the scalar-output sector has rank at most three, although extension-readiness requires rank four.

Consequently the total embedded restriction rank is at most

\[
29-1=28.
\]

This proves the obstruction. \(\square\)

## Consequence for the all-d programme

The correct strong target is therefore:

\[
\boxed{\text{minimal extension-ready Coxeter designs for every }d\ge 3,}
\]

with \(d=2\) treated as an unavoidable low-dimensional exception.

The native sharp-tomography problem in \(d=2\) is separate: failure of extension-readiness does not by itself rule out a two-face native full-rank design.

## Structural interpretation

The obstruction is specific to the paired \(SL_2\) geometry. On the scalar-output sector the inverse branch is not an independent generic row: it is the adjugate image of the forward row. The adjugate involution on \(M_2\) fixes the scalar line and negates the traceless subspace, so two Coxeter faces can supply at most one common scalar direction plus two traceless directions.

This also explains why the higher-dimensional extension-ready construction naturally starts at \(d=3\), where the triangle/non-bipartite binding mechanism becomes available.
