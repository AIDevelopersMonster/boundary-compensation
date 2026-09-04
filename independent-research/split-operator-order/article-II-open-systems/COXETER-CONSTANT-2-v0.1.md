# All-d Coxeter tomography with 2 d^2 square faces

**Article II research note — v0.1**  
**Author:** Malachevsky, A.A.  
**ORCID:** 0009-0008-6009-3196  
**Status:** `PROVED_ALL_D_UPPER_2D2 / SHARP_LOWER_BOUND_OPEN`

## 1. Result

Let `L_d^Cox` denote the minimum number of matrix-valued first-order adjacent-transposition Coxeter-face coefficients needed for universal identification of a bounded unital *-preserving generator on `M_d(C)` modulo Hamiltonian derivations.

The previous all-d construction gave

`L_d^Cox <= 3d^2-1`.

This note improves the constructive bound to

`L_d^Cox <= 2d^2`.

The information-theoretic lower bound simplifies exactly to

`L_d^Cox >= floor(d^2/2)`.

Hence

`floor(d^2/2) <= L_d^Cox <= 2d^2`.

The asymptotic factor gap is now at most `4`.

## 2. Backtracking defect and the Hermitian loop identity

For a bounded unital *-preserving map `D:M_d(C)->M_d(C)` and a unitary `U`, define

`R_D(U) := D(U^*)U + U^*D(U)`.

Equivalently,

`R_D(U) = -Gamma_D(U^*,U)`.

For any exact flat unitary loop

`T_m ... T_1 = I`,

let

`P_j := T_j ... T_1`, `P_0=I`,

and let

`K_D(T_1,...,T_m)`

be the first-order coefficient of

`exp(tD)(T_m) ... exp(tD)(T_1)` at `t=0`.

### Lemma 2.1 — Hermitian part of a flat-loop coefficient

`K_D + K_D^* = sum_(j=1)^m P_(j-1)^* R_D(T_j) P_(j-1)`.

#### Proof

The `j`-th derivative term is

`T_m...T_(j+1) D(T_j) P_(j-1)`.

Flatness gives

`T_m...T_(j+1) = P_(j-1)^* T_j^*`.

Adding the adjoint therefore gives

`P_(j-1)^* [ T_j^*D(T_j)+D(T_j^*)T_j ] P_(j-1)`.

Summing over `j` proves the identity. QED.

## 3. Engineered square and the sign-flip law

Use the engineered Coxeter square from the previous note. For arbitrary target first two transports `U,V in SU(d)` its four contextual edge transports can be chosen as

`T_1=U`,

`T_2=V`,

`T_3=U^*`,

`T_4=C:=U^*V^*U`.

The loop product is identity.

Let `K_D(U,V)` be its first-order coefficient.

### Lemma 3.1 — square backtracking relation

If

`K_D(U,V)=0`

and

`R_D(U)=0`,

then

`R_D(U^*V^*U) = - U^* R_D(V^*) U`.

#### Proof

For the square, Lemma 2.1 gives

`K_D+K_D^*`

`= R_D(U) + U^*R_D(V)U + C R_D(U)C^* + C R_D(C)C^*`.

Under `K_D=0` and `R_D(U)=0`,

`U^*R_D(V)U + C R_D(C)C^*=0`.

Thus

`R_D(C) = -C^*U^*R_D(V)UC`.

Using `C=U^*V^*U` and the exact identity

`R_D(V^*) = V R_D(V)V^*`,

one obtains

`R_D(C) = -U^*R_D(V^*)U`. QED.

## 4. An order-three Clifford anchor for every d

Let `X,Z` be the standard finite Weyl pair satisfying

`ZX = omega XZ`, `omega=exp(2 pi i/d)`.

Consider the projective phase-space automorphism

`phi: (a,b) -> (-b, a-b)`.

Its matrix

`[[0,-1],[1,-1]]`

has order `3` modulo every integer `d`.

Equivalently, on Weyl generators one may use

`X -> Z`,

`Z -> nu X^(-1) Z^(-1)`,

where `nu` is a phase satisfying

`nu^d = (-1)^(d-1)`.

This is an order-three automorphism of the finite Heisenberg group fixing the center. By the finite Stone-von Neumann / Clifford implementation theorem, it is implemented projectively by a unitary `S`. Multiplying `S` by an overall phase if needed, take `S in SU(d)`. Then

`S^* W_g S = zeta_g W_(phi(g))`

for phases `zeta_g`, and

`S^3` is scalar.

This is standard Clifford/finite-Heisenberg infrastructure, not a novelty claim.

## 5. One anchor kills all Weyl backtracking defects

Let `{W_g : g in Z_d^2}` be determinant-corrected Weyl representatives in `SU(d)`.

Use the following square family for the anchor `S`:

`K_D(S,W_g^*)=0`

for every `g in Z_d^2`.

The case `g=0` is a degenerate square with second transport `I`, and its first-order coefficient is exactly

`R_D(S)`.

Hence the `g=0` equation gives

`R_D(S)=0`.

For `g != 0`, Lemma 3.1 gives

`R_D(S^* W_g S) = -S^* R_D(W_g) S`.

Phases do not affect `R_D`, so

`R_D(W_(phi(g))) = -S^* R_D(W_g) S`.

Iterating three times,

`R_D(W_g)`

`= (-1)^3 (S^3)^* R_D(W_g) S^3`

`= -R_D(W_g)`.

Therefore

`R_D(W_g)=0`

for every `g`.

### Theorem 5.1 — order-three backtracking collapse

The `d^2` square faces

`{ (S,W_g^*) : g in Z_d^2 }`

force all Weyl backtracking defects to vanish for the difference of any two generators producing identical face data.

No separate Weyl backtracking faces are required.

## 6. Choosing a second anchor densely with S

We need a second unitary `T` such that

`closure <S,T> = SU(d)`.

This can be proved directly.

### Lemma 6.1 — a maximal torus in generic position with S

For every non-scalar unitary `S`, there exists a maximal torus `Torus` of `SU(d)` such that the Lie algebras

`t = Lie(Torus)`

and

`Ad_S(t)`

generate `su(d)`.

#### Proof

Choose an orthonormal basis in which every matrix entry of `S` is nonzero. Such a basis exists: for each matrix position the condition that the corresponding entry vanish is a proper real-analytic condition on the basis manifold, and a finite union of proper analytic zero sets cannot cover the whole manifold when `S` is non-scalar.

Let `Torus` be the diagonal maximal torus in this basis. Any common invariant subspace of the diagonal algebra is a coordinate subspace. If a nontrivial coordinate subspace were also invariant under `S Torus S^*`, then `S` would map one coordinate subspace onto another, forcing a nontrivial zero block in `S`, contrary to the all-nonzero choice.

Thus the two maximal abelian *-algebras act irreducibly. The compact Lie algebra generated by their traceless Hermitian parts contains the full diagonal Cartan. In a Lie subalgebra of `su(d)` containing that Cartan, root spaces occur in a symmetric bracket-closed set. Irreducibility forces the root graph to be connected, and bracket closure along paths then produces every root space. Hence the generated Lie algebra is all of `su(d)`. QED.

Choose `T in Torus` whose powers are dense in `Torus` (Kronecker). Then the closure of `<S,T>` contains both `Torus` and `S Torus S^*`, so its Lie algebra is `su(d)`. Therefore

`closure <S,T> = SU(d)`.

## 7. Second anchor forces full conjugation invariance modulo derivations

Now add the second square family

`K_D(T,W_g^*)=0`

for every `g in Z_d^2`.

Again, the `g=0` equation is the degenerate square giving

`R_D(T)=0`.

Section 5 already gave

`R_D(W_g)=0`

for every Weyl element.

Therefore the square-to-conjugation lemma from the previous Article-II note applies to both anchors `S` and `T`: for every Weyl basis element, vanishing of the square coefficient implies exact Leibniz consistency under conjugation by the anchor.

By linearity, the class `[D]` modulo Hamiltonian derivations is fixed by both `Ad_S` and `Ad_T`, hence by the dense subgroup they generate, and therefore by all of `PSU(d)`.

The earlier invariant-quotient lemma then gives

`D = lambda P_0 + delta_H`,

where

`P_0(X)=X-tr(X)I/d`

is the depolarizing direction and `delta_H` is Hamiltonian.

But every nonidentity Weyl operator is traceless and Section 5 gives `R_D(W_g)=0`, whereas

`R_(lambda P_0)(W_g)=2 lambda I`.

Hence `lambda=0`.

Thus `D` is Hamiltonian.

## 8. Main theorem

### Theorem 8.1 — all-d 2d^2 Coxeter tomography

For every `d>=2`, there exists a family of exactly

`2d^2`

matrix-valued adjacent-transposition Coxeter square faces whose first-order reduced holonomy data identify every bounded unital *-preserving generator on `M_d(C)` modulo Hamiltonian derivations.

A valid family is

`{ (S,W_g^*) : g in Z_d^2 }`

union

`{ (T,W_g^*) : g in Z_d^2 }`,

with `S` the order-three Clifford anchor and `T` chosen as in Section 6.

Each target pair is realized by an actual adjacent-transposition Coxeter square via Gotô commutator surjectivity, as proved in the preceding engineered-square note.

Therefore

`L_d^Cox <= 2d^2`.

## 9. Exact lower bound simplification

The general scalar-count lower bound is

`ceil((d^2-1)^2/(2d^2))`.

Since

`(d^2-1)^2/(2d^2) = d^2/2 -1 + 1/(2d^2)`,

one gets for every `d>=2`

`ceil((d^2-1)^2/(2d^2)) = floor(d^2/2)`.

Hence

`floor(d^2/2) <= L_d^Cox <= 2d^2`.

For `d=3,4,5` the lower bound itself is already known to be attained by exact certificates.

## 10. Computational evidence beyond the proved theorem

Independent generic square-face calculations give full rank at the exact lower-bound count also for

- `d=6`: `18` generic squares, rank `1225=(36-1)^2`;
- `d=7`: `24` generic squares, rank `2304=(49-1)^2`.

These are numerical evidence only at the present stage; unlike `d=3,4,5`, no exact finite-field certificate has yet been frozen for `d=6,7`.

A block-embedding experiment also shows a striking near-triangular pattern:

- embedded minimal `d=4` design inside `d=5`: rank `377`, leaving deficiency `199`, while four new faces have capacity `200`;
- embedded minimal `d=6` design inside `d=7`: rank `1717`, leaving deficiency `587`, while six new faces have capacity `588`.

This strongly motivates a sharp block-extension lemma but is not yet used as a theorem premise.

## 11. Remaining sharp problem

The only unresolved asymptotic-constant question is now

`L_d^Cox ?= floor(d^2/2)`

for all `d>=3`.

The present note reduces the previous factor-six gap between the constructive `3d^2-1` bound and the lower bound `~d^2/2` to a factor-four gap.

The most promising next route is a block-extension theorem showing that a lower-bound-saturating design in `M_d` can be embedded into `M_(d+1)` and completed with exactly

`floor((d+1)^2/2)-floor(d^2/2)`

new generic-mixing squares.
