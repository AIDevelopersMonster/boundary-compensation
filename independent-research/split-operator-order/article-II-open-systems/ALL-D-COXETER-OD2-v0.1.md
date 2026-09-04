# All-d O(d^2) Coxeter tomography via anchored square faces

**Article II research note — v0.1**  
**Author:** Malachevsky, A.A.  
**ORCID:** 0009-0008-6009-3196  
**Status:** `PROVED_ALL_D_COXETER_O_D2 / SHARP_CONSTANT_OPEN`

## 1. Purpose

The Weyl-loop theorem already proved that generalized exact flat-loop tomography needs and suffices with `Theta(d^2)` matrix-valued loop families. This note converts that asymptotic result back into the adjacent-transposition Coxeter geometry of Article I.

The result is constructive at the level of face types: for every finite `d`, one can identify any bounded dissipative generator on `M_d(C)` modulo Hamiltonian derivations using at most

`3d^2-1`

matrix-valued **Coxeter faces**: degenerate braid faces implementing backtracks and genuine commuting-transposition square faces.

The information-theoretic lower bound remains

`ceil((d^2-1)^2/(2d^2))`,

so the sharp constant is still open, but the all-d Coxeter order is now exactly `Theta(d^2)`.

## 2. Infrastructure

Two classical group facts are used only as infrastructure.

1. **Gotô commutator surjectivity.** Every element of a compact connected semisimple group is a single group commutator. In particular, every element of `SU(d)` can be written as

   `BA B^* A^*`.

2. **Dense two-generation.** A connected semisimple Lie group admits pairs of elements generating a dense subgroup. Thus one may choose anchors `S_1,S_2 in SU(d)` whose projective inner automorphisms generate a dense subgroup of `PSU(d)`.

No novelty is claimed for these group-theoretic facts.

## 3. Realizing an arbitrary target backtrack as a Coxeter braid

Let `U in SU(d)`. By Gotô, choose `A,B in SU(d)` with

`U = B A B^* A^*`.

Use the three-gate tuple `(A,B,I)` and the standard adjacent-transposition braid loop

`123 -> 213 -> 231 -> 321 -> 312 -> 132 -> 123`.

Because the third gate is the identity, the six contextual edge transports are

`U, I, I, U^*, I, I`

up to the ordering convention of the path. Therefore the first-order reduced braid coefficient is exactly the two-edge backtracking coefficient

`R_L(U) := L(U^*)U + U^*L(U)`.

Hence every unitary backtrack needed below can be measured by a (degenerate) Coxeter braid face.

## 4. Realizing arbitrary first two edge transports by a genuine square face

Let `U,V in SU(d)` be arbitrary target edge transports.

Choose `A,B in SU(d)` with

`G_AB := B A B^* A^* = U`.

Set

`M := (BA)^* V (BA) in SU(d)`.

Choose `C,D in SU(d)` with

`G_CD := D C D^* C^* = M`.

Now use the four-gate word `ABCD` and the commuting adjacent-transposition square

`1234 -> 2134 -> 2143 -> 1243 -> 1234`,

corresponding to `(s_1 s_3)^2=e`.

### Lemma 4.1 — engineered contextual square

The four exact contextual edge transports of this square are

`T_1 = U`,

`T_2 = V`,

`T_3 = U^*`,

`T_4 = U^* V^* U`.

In particular,

`T_4 T_3 T_2 T_1 = I`.

#### Proof

The first edge has transport `G_AB=U`. The second has prefix `BA`, hence

`T_2 = BA G_CD (BA)^* = V`.

The third reverses the first swap, so `T_3=G_AB^{-1}=U^*`.

For the fourth,

`T_4 = AB G_CD^{-1} (AB)^*`.

From `U=BA(AB)^*` one has `BA=U AB`, and therefore

`G_CD=(AB)^* U^* V U (AB)`.

Substitution gives

`T_4=U^*V^*U`.

The product is then immediate. QED.

Thus every abstract square probe used below is an actual adjacent-transposition Coxeter square of Article I.

## 5. Square coefficient and infinitesimal conjugation consistency

Let `D:M_d(C)->M_d(C)` be complex-linear, unital and *-preserving. For unitaries `U,V`, define the backtracking defects

`R_D(U)=D(U^*)U+U^*D(U)`,

`R_D(V)=D(V^*)V+V^*D(V)`.

Let `C=U^*V^*U`, and let `K_D(U,V)` be the first-order coefficient of the engineered square of Lemma 4.1:

`K_D(U,V)`

`= D(C)U^*VU`

`  + C D(U^*) VU`

`  + C U^* D(V) U`

`  + C U^* V D(U)`.

Define the derivation-consistency defect for the conjugation identity `C=U^*V^*U` by

`E_D(U,V)`

`:= D(U^*V^*U)`

` - D(U^*)V^*U`

` - U^*D(V^*)U`

` - U^*V^*D(U)`.

### Lemma 5.1 — square-to-conjugation conversion

If

`R_D(U)=R_D(V)=0`,

then

`K_D(U,V)=E_D(U,V) C^*`.

Hence under the two backtracking equalities,

`K_D(U,V)=0`

if and only if `D` obeys the Leibniz rule on the triple product `U^*V^*U`.

#### Proof

Multiply `E_D(U,V)` on the right by `C^*=U^*VU`. The three non-leading terms become, respectively,

`-D(U^*)U`,

`-U^*D(V^*)VU`,

`-U^*V^*D(U)U^*VU`.

Using

`D(U^*)U=-U^*D(U)`,

`D(V^*)V=-V^*D(V)`,

which are exactly the two backtracking hypotheses, these terms coincide with the last, third, and second terms of `K_D(U,V)`. QED.

## 6. Anchored squares make the generator class conjugation-invariant

Let

`{W_g : g in Z_d^2}`

be a determinant-corrected Weyl unitary basis in `SU(d)`. Central phase corrections do not affect spanning or inner conjugation. There are

`q=d^2-1`

nonidentity Weyl elements.

Choose two anchors `S_1,S_2 in SU(d)` whose projective classes generate a dense subgroup of `PSU(d)`.

Assume two bounded unital *-preserving generators `L_1,L_2` produce identical data for the following faces, and put `D=L_1-L_2`.

The data are:

1. backtracking braid faces for every nonidentity `W_g`;
2. backtracking braid faces for `S_1,S_2`;
3. engineered square faces `(S_j,W_g)` for `j=1,2` and every nonidentity `W_g`.

Then

`R_D(W_g)=0`, `R_D(S_j)=0`, `K_D(S_j,W_g)=0`.

By Lemma 5.1,

`D(S_j^* W_g^* S_j)`

`= D(S_j^*)W_g^*S_j`

` + S_j^*D(W_g^*)S_j`

` + S_j^*W_g^*D(S_j)`.

Since the Weyl operators form a basis, linearity extends this identity to every `X in M_d(C)`:

`D(S_j^* X S_j)`

`= D(S_j^*)X S_j + S_j^*D(X)S_j + S_j^*X D(S_j)`.

### Lemma 6.1 — quotient invariance

Let `Ad_S(X)=SXS^*`. Under `R_D(S)=0`, the preceding identity is equivalent to

`Ad_S o D o Ad_(S^*) = D - ad_{H_S}`,

where

`H_S := D(S)S^*`

is skew-adjoint and `ad_{H_S}(X)=[H_S,X]` is a Hamiltonian derivation.

Therefore the class `[D]` modulo Hamiltonian derivations is fixed by conjugation with `S`.

#### Proof

Conjugate the preceding identity by `S` on the left and `S^*` on the right. The backtracking condition implies

`S D(S^*)=-D(S)S^*=-H_S`.

The result follows. Skew-adjointness of `H_S` is another rewriting of `R_D(S)=0`. QED.

Since `S_1,S_2` generate a dense subgroup, `[D]` is fixed by all of `PSU(d)`.

## 7. The only invariant quotient direction is depolarizing

Let

`V=Herm_0(d)`

be the real vector space of traceless Hermitian matrices, of dimension `q=d^2-1`. The adjoint action of `PSU(d)` on `V` is irreducible.

A complex-linear, unital, *-preserving map is determined on Hermitian matrices by

- a real linear functional `V -> R I`, and
- a real linear map `V -> V`.

Hence, as a real `PSU(d)`-module,

`Map_unital,* = V^* direct-sum End_R(V)`.

Hamiltonian derivations form a submodule isomorphic to `V` inside `End_R(V)`.

### Lemma 7.1 — invariant quotient is one-dimensional

Modulo Hamiltonian derivations, the `PSU(d)`-fixed subspace is one-dimensional and is represented by the depolarizing direction

`P_0(X) := X - tr(X) I/d`.

#### Proof

The adjoint representation `V` has no invariant vectors, so neither `V^*` nor the derivation copy of `V` contributes fixed directions. By Schur's lemma, the commutant of the irreducible adjoint action on `V` consists of scalar multiples of the identity. Thus the only surviving invariant class is scalar action on the traceless sector, represented by `P_0`. QED.

Therefore there exist a real scalar `lambda` and a Hamiltonian derivation `delta_H` such that

`D = lambda P_0 + delta_H`.

## 8. Weyl backtracking kills the last invariant direction

Every nonidentity Weyl operator is traceless. Hamiltonian derivations have zero backtracking defect, while

`R_(lambda P_0)(W_g)`

`= lambda W_g^*W_g + lambda W_g^*W_g`

`= 2 lambda I`.

But the design assumes `R_D(W_g)=0`. Hence

`lambda=0`.

Thus `[D]=0`: the two generators differ only by a Hamiltonian derivation.

## 9. All-d Coxeter tomography theorem

### Theorem 9.1 — all-d quadratic Coxeter upper bound

For every `d>=2`, there exists an adjacent-transposition Coxeter-face design that identifies every bounded unital *-preserving dissipative generator on `M_d(C)` modulo Hamiltonian derivations using at most

`3d^2-1`

matrix-valued face coefficients.

One valid design contains

- `d^2-1` degenerate braid faces for Weyl backtracks;
- `2` degenerate braid faces for the two dense anchors;
- `2(d^2-1)` genuine square faces coupling each anchor to each nonidentity Weyl basis element.

Total:

`(d^2-1)+2+2(d^2-1)=3d^2-1`.

#### Proof

If two generators have identical data, Sections 5--8 show that their difference is a Hamiltonian derivation. QED.

### Corollary 9.2 — optimal asymptotic Coxeter order

A general complex `d x d` face coefficient provides at most `2d^2` real scalar coordinates, while the dissipative quotient has real dimension `(d^2-1)^2`. Therefore every universal matrix-valued Coxeter design satisfies

`L_d^Cox >= ceil((d^2-1)^2/(2d^2))`.

Together with Theorem 9.1,

`ceil((d^2-1)^2/(2d^2)) <= L_d^Cox <= 3d^2-1`.

Hence

`L_d^Cox = Theta(d^2)`.

This is an all-d theorem **inside the Coxeter geometry of Article I**.

## 10. Sharp constant remains open

The theorem does not prove that the lower bound itself is always attainable. The sharper conjecture remains:

`L_d^Cox = ceil((d^2-1)^2/(2d^2))`

for every `d>=3`.

What is now known:

- exact lower-bound-saturating Coxeter designs exist for `d=3,4,5`;
- all dimensions admit Coxeter designs with at most `3d^2-1` faces;
- therefore the asymptotic order is settled exactly;
- only the optimal constant / exact minimal count remains open.

## 11. Relation to Article I

This theorem makes Article II a direct structural continuation of Article I:

1. Article I supplies the adjacent-swap contextual connection and its exact square/braid flatness before reduction.
2. Article II applies open-system evolution to those exact contextual edge transports.
3. Backtracking and square face defects test whether the reduced dynamics still obeys multiplicative/conjugation consistency.
4. Dense inner-conjugation invariance reduces the remaining ambiguity to the unique isotropic depolarizing class.
5. Weyl backtracking removes that class, leaving only Hamiltonian derivations.

No physical gauge/spacetime interpretation is implied by the word Coxeter curvature or holonomy.
