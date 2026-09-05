# Odd-dimensional extension-ready minimal Coxeter designs

**Article I post-publication research note — v0.1**  
**Author:** Malachevsky, A.A.  
**ORCID:** 0009-0008-6009-3196  
**Status:** `PROVED_ODD_D_EXTENSION_READY_EXISTENCE / EVEN_D_REMAINS`

## 1. Result

Let

`L_d = floor(d^2/2)`

be the information-theoretic lower bound for matrix-valued Coxeter-face tomography, and let a minimal design be called **extension-ready** when

1. it has exactly `L_d` faces;
2. its native rank on `M_d(C)` is `(d^2-1)^2`;
3. after block embedding into `M_(d+1)(C)`, its rank attains the structural restriction ceiling.

For odd `d`, that ceiling is

`R_d^up = (d^2-1)(d+1)^2`.

### Theorem 1.1 — odd-dimensional extension-ready existence

For every odd integer `d>=3`, there exists an extension-ready minimal Coxeter square design with exactly

`L_d=(d^2-1)/2`

faces.

Equivalently, for every odd `d>=3` there is a real unitary face design whose native first-order dissipative rank is

`(d^2-1)^2`

and whose block embedding into dimension `d+1` has rank

`(d^2-1)(d+1)^2`.

The proof proceeds in the complexification, constructs one explicit nonunitary `SL_d(C)` witness with a full structural minor, and then returns to actual unitary faces by Zariski density of `SU(d)` in `SL_d(C)`.

## 2. Complexified branch pairing

Let `F:M_d(C)->M_(d+1)(C)` denote the complexified restriction variable. For one real square face with first two unitary transports `(A,B)`, the real matrix output complexifies into the two ordered branches

`(A,B)`

and

`(B^{-1},A^{-1})`.

The four output sectors are the complexified block-module coboundaries

- regular:

  `delta_reg F(A,B)=F(AB)-F(A)B-AF(B)`;

- left:

  `delta_L F(A,B)=F(AB)-A F(B)`;

- right:

  `delta_R F(A,B)=F(AB)-F(A)B`;

- scalar:

  `delta_0 F(A,B)=F(AB)`.

Thus one real face contributes two complex branch equations.

For odd `d`, `L_d=(d^2-1)/2`, so a minimal real design contributes exactly

`d^2-1`

complex branches.

## 3. Weyl basis and face count

Let

`X^d=Z^d=I`, `ZX=omega XZ`, `omega=exp(2 pi i/d)`,

and use the Weyl basis

`W_(p,q)=X^p Z^q`, `(p,q) in Z_d^2`.

Put

`m=(d-1)/2`.

Reserve the four root labels

`+/-e_x=(+/-1,0)`, `+/-e_z=(0,+/-1)`.

The design has two seed faces, one with product `X` and one with product `Z`.

### Axis forest

For `k=2,...,m`, use the face

`(X, X^(k-1))`,

whose paired branch is

`(X^(-(k-1)), X^(-1))`.

This resolves the pair of target powers `X^k` and `X^(-k)`.

Do the same with `Z`.

### Mixed forest

For every inverse pair

`{(p,q),(-p,-q)}`

with `p!=0` and `q!=0`, choose one representative and use

`(X^p, Z^q)`.

The paired branch automatically has factors

`(Z^(-q), X^(-p))`

and product `(X^p Z^q)^(-1)`.

The number of faces is

`2 + 2(m-1) + (d-1)^2/2`

`=2+(d-3)+(d-1)^2/2`

`=(d^2-1)/2=L_d`.

The non-seed branches form a triangular multiplicative forest: every target value `F(W_g)` occurs with coefficient one and all factor values belong to earlier axis/root variables. Therefore those rows are automatically independent in all four sectors.

After eliminating the forest rows, only the five input roots

`I, X, X^(-1), Z, Z^(-1)`

remain.

## 4. Seed faces

The `Z` seed is

`B_Z=I+t Z^2`,

`A_Z=Z B_Z^(-1)`.

The `X` seed carries the cross perturbation

`B_X(s)=I+t X^2+s(Z+eta Z^2)`,

`A_X(s)=X B_X(s)^(-1)`,

where `t!=0`, `eta!=0`, and `s` is eventually chosen sufficiently small and nonzero.

At `s=0` both seeds lie in the corresponding cyclic Weyl algebras.

All matrices are invertible outside a proper algebraic exceptional set. Individual determinant-one normalization is harmless: replacing

`A -> lambda^(-1) A`, `B -> lambda B`

leaves all four coboundary blocks unchanged. Hence the complex witness may be normalized into `SL_d(C)` face by face.

## 5. Scalar sector

The forest products cover every nonzero Weyl label except the four roots. The two seed faces contribute the four remaining products

`X, X^(-1), Z, Z^(-1)`.

Therefore the scalar branch matrix is simply evaluation on all nonidentity Weyl basis elements and has rank

`d^2-1`.

This is the odd-`d` scalar ceiling.

## 6. Left and right sectors at `s=0`

The forest equations propagate four root module values.

For the left sector write

`F(X)=X u_+`, `F(X^(-1))=X^(-1) u_-`, `v_0=F(I)`.

The positive/negative axis forest gives

`F(X^k)=X^k u_+`, `F(X^(-k))=X^(-k) u_-`

for the corresponding representatives.

For the `X` seed at `s=0`, `B=I+tX^2`, `A=XB^(-1)`. The first branch gives

`F(X)=A F(B)`.

After multiplication by `A^(-1)=B X^(-1)`, this becomes

`(I+tX^2)u_+ = v_0+tX^2 u_*`,

where `u_*` is either `u_+` or `u_-` according to whether `X^2` is the positive or negative root class.

The paired branch gives

`t X (u_- - u_+)=0`.

Hence `u_-=u_+`, and the first equation reduces to

`u_+=v_0`.

Thus the two `X` branches eliminate exactly the two `X` root defects. The same argument applies to `Z`.

Consequently the left kernel is exactly

`F(Y)=Y v_0`,

of complex dimension `d`. Hence

`rank delta_L = d(d^2-1)`.

For the right sector write

`F(X)=u_+ X`, `F(X^(-1))=u_- X^(-1)`.

The first branch is equivalent to

`u_+ A=F(A)`.

For odd `d`,

`B^(-1)=(1/(1+t^d)) sum_(k=0)^(d-1) (-t)^k X^(2k)`

and

`A=X B^(-1)`.

Because `2` is invertible modulo odd `d`, `A` has a nonzero identity coefficient, namely the term with `2k+1=0 mod d`. Therefore comparison of the identity coefficient in `u_+A=F(A)` gives

`u_+=v_0`.

The paired branch uses `B^(-1)`, whose identity coefficient is also nonzero, and gives

`u_-=v_0`.

The same argument applies to `Z`, so

`rank delta_R = d(d^2-1)`.

Full left/right row rank is an open condition, hence it persists for all sufficiently small nonzero `s`.

## 7. Regular cyclic closure lemma

The regular sector requires one additional step.

### Lemma 7.1 — one cyclic seed has full residual row rank

Let `U` have simple spectrum consisting of the `d`-th roots of unity, with odd `d`. Use the positive/negative power forest and the seed

`B=I+tU^2`, `A=UB^(-1)`.

After forest elimination, the two seed branches have full row rank `2d^2` for generic nonzero `t`.

#### Proof

Diagonalize `U`. For one matrix entry `(i,j)` with eigenvalues `alpha,beta`, the unresolved values are

`r=F(I)_(ij)`, `p=F(U)_(ij)`, `q=F(U^(-1))_(ij)`.

The power forest expresses every other `F(U^k)_(ij)` in these three variables. The two seed branches give a `2 x 3` scalar system depending rationally on `t`.

At `t=0`, the leading parts are

`K_1=-alpha r+O(t)`,

`K_2=-beta^(-1) r+O(t)`.

The combination

`K_1-alpha beta K_2`

has zero constant term. Its first nonzero coefficient is:

- for `d=3`,

  `beta(alpha-beta)p-(2alpha+beta)q`,

  whose two coefficients cannot vanish simultaneously for third roots `alpha,beta`;

- for `d=5`, the coefficient of `p` is

  `-alpha^2(1+beta/alpha)^2`,

  which is nonzero because `-1` is not a fifth root of unity;

- for every odd `d>=7`,

  `-alpha^2 (p+alpha beta q)`,

  whose `p` coefficient is nonzero.

Thus the two seed rows are not identically dependent for any spectral pair `(alpha,beta)`. Since there are only finitely many pairs, one may choose `t` outside a finite algebraic exceptional set so that all `d^2` entrywise systems have rank `2`. Summing over the entries gives residual seed rank `2d^2`. QED.

It follows that the complete cyclic subsystem has rank

`(d-1)d^2`

and kernel dimension `d^2`.

For `alpha!=beta`, that one-dimensional entrywise kernel is the restriction of an inner derivation. For `alpha=beta`, the remaining direction has nonzero `F(I)_(ii)`. Therefore evaluation at the identity maps the non-derivation part of the cyclic kernel isomorphically onto the commutant of `U`.

## 8. The unperturbed regular defect is exactly `(d-1)^2`

Set `s=0`.

The `X` cyclic subsystem has kernel dimension `d^2`; modulo restricted inner derivations its extra identity data lie in the maximal abelian algebra

`C_X=C[X]`.

Likewise the `Z` subsystem has extra identity data in

`C_Z=C[Z]`.

Because the two restrictions share the same `F(I)`, the common identity defect lies in

`C_X intersect C_Z = C I`.

Modulo that one scalar defect, a regular kernel element is represented by two independent restricted inner derivations

`delta_(H_X)` on `C_X`,

`delta_(H_Z)` on `C_Z`.

The mixed forest extends them to normal-form Weyl products. Hence the `s=0` regular kernel has dimension

`1 + 2(d^2-d)`

`=2d^2-2d+1`

`=d^2+(d-1)^2`.

Since the regular domain has dimension `d^4`, the unperturbed regular rank is

`d^4-[d^2+(d-1)^2]`

`=d^4-2d^2+2d-1`.

The full regular row count is

`d^2(d^2-1)=d^4-d^2`,

so the exact row-rank defect is

`(d-1)^2`.

The extra defect modulo global derivations is naturally

`E = M_d(C)/(C_X+C_Z)`,

which has dimension

`d^2-(2d-1)=(d-1)^2`.

In the Weyl basis it is represented by the mixed modes

`W_(p,q)`, `p!=0`, `q!=0`.

## 9. Two-frequency cross perturbation removes the entire regular defect

Differentiate the `X` seed in `s` at `s=0`. For a mismatch representative, subtract a global derivation and take `H_Z=0`, `H=H_X-H_Z`.

On a normal-form monomial the remaining base-kernel map is the `X`-partial derivation determined by `H`.

For a cross frequency `Z^r`, let

`sigma_r(f(X)) = f(omega^r X)`.

The first `X`-seed branch produces, after forest and cyclic elimination, the residual operator

`T_r([H,Z^r])`,

where

`T_r(Y)=Y-sigma_r(B_0^(-1)) Y B_0`,

`B_0=I+tX^2`.

Multiplying by the invertible matrix `sigma_r(B_0)` gives

`sigma_r(B_0) T_r(Y)`

`= t(omega^(2r) X^2 Y - Y X^2)`.

For a Weyl mode `Y=W_(p,s)`, this vanishes exactly when

`omega^(2r)=omega^(2s)`.

Because `d` is odd, multiplication by `2` is invertible modulo `d`; hence

`T_r(W_(p,s))=0 iff s=r`.

Also

`[W_(p,q),Z^r]=(1-omega^(pr)) W_(p,q+r)`.

For `r=1` and `r=2`, the factor `1-omega^(pr)` is nonzero for every `p!=0`, again because `1` and `2` are units modulo odd `d`.

After the natural identification of the base cokernel with the mixed Weyl blocks, the first-order Schur map induced by a single `Z^r` perturbation therefore has the block form

`E_q -> C_(q+r)`

and is an isomorphism on the `(d-1)`-dimensional `p!=0` block whenever `q!=-r`; it vanishes only on the boundary block `q=-r`, whose target would be the excluded `q=0` sector.

Now use the perturbation

`Z + eta Z^2`, `eta!=0`.

The first-order Schur map is

`S_1 + eta S_2`.

Write a possible kernel vector as blocks `x_q`, `q=1,...,d-1`, with each `x_q` of dimension `d-1`.

The output block `C_1` receives only the `S_2` contribution from `x_(d-1)`, so

`x_(d-1)=0`.

The output block `C_2` receives only the `S_1` contribution from `x_1`, so

`x_1=0`.

Then successively

`C_3, C_4, ..., C_(d-1)`

force

`x_2=x_3=...=x_(d-2)=0`

because all interior block maps are invertible.

Therefore the first-order Schur map on `E` is injective. Since both domain and base cokernel have dimension `(d-1)^2`, it is an isomorphism.

By the standard analytic rank-perturbation lemma, a maximal regular minor has leading term

`c s^((d-1)^2)`

with `c!=0`. Hence for all sufficiently small nonzero `s`, outside an isolated exceptional set, the regular branch matrix has full row rank

`d^2(d^2-1)`.

## 10. Embedded rank

For such generic `t` and sufficiently small nonzero `s`, the four complexified restriction sectors have ranks

- regular:

  `d^2(d^2-1)`;

- left:

  `d(d^2-1)`;

- right:

  `d(d^2-1)`;

- scalar:

  `d^2-1`.

Their sum is

`(d^2-1)(d^2+2d+1)`

`=(d^2-1)(d+1)^2`,

which is exactly the odd-dimensional structural embedded ceiling.

Thus the constructed complex design attains the extension-ready rank bound.

## 11. Native rank follows from the regular sector

The unnormalized regular-domain dimension is `d^4`. Full regular row rank leaves a kernel of dimension exactly `d^2`.

All inner derivations belong to this kernel and have dimension `d^2-1`.

At `s=0` the one additional kernel direction is the common scalar identity-defect direction and has `F(I)!=0`. Under sufficiently small perturbation, the one-dimensional quotient kernel varies analytically and its evaluation at `I` remains nonzero outside a proper exceptional set.

Therefore

`ker(delta_reg) intersect {F(I)=0}`

is exactly the inner-derivation space.

But `{F(I)=0}` is precisely the complexified native unital-map domain. Hence the same face family has native quotient rank

`d^2(d^2-1)-(d^2-1)`

`=(d^2-1)^2`.

So the design is not merely embedded-ceiling-saturating: it is natively minimal and full rank.

## 12. Return from the complex witness to actual unitary faces

The relevant maximal minors are rational regular functions of the complexified face parameters in products of `SL_d(C)`. The construction above gives one point where the native and embedded minors are nonzero.

`SU(d)` is Zariski dense in `SL_d(C)`. Therefore a nonzero complexified minor cannot vanish identically on the real unitary locus.

Consequently each of the two rank conditions holds on a nonempty real-analytic open dense subset of the unitary face-parameter manifold. Their intersection is nonempty.

Thus actual unitary Coxeter square faces exist with both properties simultaneously.

This proves Theorem 1.1.

## 13. Consequences

For every odd `d>=3`, the sharp lower bound is attained:

`L_d^Cox = (d^2-1)/2`.

More strongly, an attaining design can be chosen extension-ready for the `d -> d+1` block embedding.

The previous exact certificates at `d=3` and `d=5` are now finite instances of an all-odd theorem rather than isolated low-dimensional accidents.

The remaining sharp problem is purely the even-dimensional half:

> prove the existence of extension-ready minimal designs for every even `d`.

Once that is done,

`L_d^Cox=floor(d^2/2)`

will hold for every `d>=3`.

## 14. Reproducibility status

A companion numerical probe checks the complex witness directly in `d=3,5,7`. It is not a premise of the proof; it verifies the sector ranks and the `(d-1)^2` unperturbed regular defect before the two-frequency perturbation.
