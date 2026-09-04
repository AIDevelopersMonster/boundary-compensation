# All-d flat-loop tomography from Weyl multiplication defects

**Article II research note — v0.1**  
**Author:** Malachevsky, A.A.  
**ORCID:** 0009-0008-6009-3196  
**Status:** `PROVED_ALL_D_O_D2 / COXETER_OPTIMALITY_STILL_OPEN`

## 1. Purpose

The exact minimal Coxeter-face conjecture remains open for arbitrary `d`. This note proves a weaker but fully general theorem with the correct asymptotic order: every bounded dissipative generator on `M_d(C)` can be identified modulo Hamiltonian derivations from `O(d^2)` matrix-valued closed flat-loop measurements.

The construction uses the finite Weyl unitary basis and multiplication loops. These loops are exact flat unitary contextual loops, but they are not asserted to be adjacent-transposition Coxeter faces. Thus the result proves the optimal order `Theta(d^2)` for generalized flat-loop tomography while leaving the sharp Coxeter constant as a separate conjecture.

## 2. Weyl unitary basis

Let

`G = Z_d x Z_d`.

Let `X,Z in U(d)` be the standard shift and phase operators,

`X|j> = |j+1 mod d>`,

`Z|j> = omega^j |j>`, `omega=exp(2 pi i/d)`.

Choose Weyl representatives

`W_(a,b) = X^a Z^b`.

Then

`W_g W_h = c(g,h) W_(g+h)`

for a phase `c(g,h)` of unit modulus. The `d^2` Weyl operators form an orthogonal basis of `M_d(C)`.

Define the genuine conjugation action

`alpha_g(A) := W_g^* A W_g`.

Projective phases cancel under conjugation, so

`alpha_(g+h) = alpha_h o alpha_g`.

## 3. Normalized Leibniz defect as a group coboundary

Let `L:M_d(C)->M_d(C)` be bounded, complex-linear, unital and *-preserving. Put

`A_g(L) := W_g^* L(W_g)`.

For `g,h in G`, define

`B_L(h,g) := (W_h W_g)^* Gamma_L(W_h,W_g)`,

where

`Gamma_L(X,Y)=L(XY)-L(X)Y-X L(Y)`.

### Lemma 3.1 — projective Weyl cocycle identity

For all `g,h in G`,

`B_L(h,g) = A_(h+g)(L) - alpha_g(A_h(L)) - A_g(L)`.

#### Proof

Let `P=W_hW_g=c(h,g)W_(h+g)`. Because `L` is complex-linear and `|c(h,g)|=1`,

`P^*L(P)=W_(h+g)^*L(W_(h+g))=A_(h+g)`.

Moreover,

`P^* L(W_h) W_g = W_g^* W_h^* L(W_h) W_g = alpha_g(A_h)`,

and

`P^* W_h L(W_g)=W_g^*L(W_g)=A_g`.

Substituting these three terms into `P^*Gamma_L(W_h,W_g)` gives the formula. QED.

## 4. Two generators suffice

Let

`e_1=(1,0)`, `e_2=(0,1)`

be the standard generators of `G`.

### Lemma 4.1 — generator relations extend to the whole group

Suppose a family `A_g in M_d(C)` with `A_0=0` satisfies

`A_(e_j+g)=alpha_g(A_(e_j))+A_g`

for `j=1,2` and every `g in G`.

Then

`A_(h+g)=alpha_g(A_h)+A_g`

for all `g,h in G`.

#### Proof

The claimed relation is preserved under addition of a generator. Indeed, if it holds for `h`, then for `h+e_j`,

`A_(h+e_j+g)`

`= alpha_(h+g)(A_(e_j)) + A_(h+g)`

`= alpha_g(alpha_h(A_(e_j))) + alpha_g(A_h)+A_g`

`= alpha_g( alpha_h(A_(e_j))+A_h ) + A_g`

`= alpha_g(A_(h+e_j))+A_g`.

Since `e_1,e_2` generate `G`, induction gives the relation for every `h`. QED.

### Lemma 4.2 — finite-group cocycles are coboundaries in this representation

If

`A_(h+g)=alpha_g(A_h)+A_g`

for all `g,h in G`, then there exists `K in M_d(C)` such that

`A_g = alpha_g(K)-K`

for every `g`.

One may take

`K = -(1/|G|) sum_(h in G) A_h`.

#### Proof

From the cocycle identity,

`alpha_g(A_h)=A_(h+g)-A_g`.

Summing over `h` and using translation invariance of the finite group gives

`sum_h alpha_g(A_h)=sum_h A_h-|G|A_g`.

Therefore, with the displayed definition of `K`,

`alpha_g(K)-K=A_g`. QED.

## 5. All-d identifiability modulo derivations

### Theorem 5.1 — Weyl generator-defect theorem

Let `L_1,L_2:M_d(C)->M_d(C)` be bounded, complex-linear, unital and *-preserving maps. Put `D=L_1-L_2`.

Assume

`B_D(e_1,g)=0`,

`B_D(e_2,g)=0`

for every `g in G`.

Then `D` is a Hamiltonian derivation:

`D(X)=i[H,X]`

for some self-adjoint `H`.

#### Proof

By Lemma 3.1, the assumptions are exactly the generator cocycle relations for the family

`A_g=W_g^*D(W_g)`.

Lemma 4.1 extends them to all `g,h`. Lemma 4.2 gives

`A_g=alpha_g(K)-K`.

Hence

`D(W_g)=W_gA_g`

`=W_g(W_g^*KW_g-K)`

`=KW_g-W_gK=[K,W_g]`.

The Weyl operators form a basis of `M_d(C)`, so by linearity

`D(X)=[K,X]`

for every `X`.

Because `D` is *-preserving,

`[K,X^*]=[K,X]^*=-[K^*,X^*]`

for all `X`. Thus `K+K^*` is central, hence scalar. Subtracting half that scalar from `K` does not change the commutator and makes `K` skew-adjoint. Write `K=iH` with `H=H^*`. QED.

Therefore the normalized Leibniz defects on only two Weyl-generator directions already determine the full bounded generator modulo Hamiltonian motion.

## 6. Recovering B from closed-loop coefficients

The quantity `B_L(h,g)` is itself obtainable from first-order closed-loop holonomies.

Let

`P=W_hW_g`.

### Backtracking loop

For the two-edge loop

`P, P^*`,

define

`R_L(P) := d/dt|_(t=0) [ Phi_t(P^*) Phi_t(P) ]`

for `Phi_t=exp(tL)`. Then

`R_L(P)=L(P^*)P+P^*L(P)`.

### Multiplication triangle

For the exact flat loop

`W_g, W_h, P^*`,

whose ordered product is `P^*W_hW_g=I`, define

`K_L(h,g) := d/dt|_(t=0) [ Phi_t(P^*) Phi_t(W_h) Phi_t(W_g) ]`.

Then

`K_L(h,g)=L(P^*)P+P^*L(W_h)W_g+P^*W_hL(W_g)`.

### Proposition 6.1 — closed-loop extraction formula

`B_L(h,g)=R_L(P)-K_L(h,g)`.

#### Proof

Subtract the two displayed first-order expressions. The `L(P^*)P` terms cancel and the remainder is

`P^*L(P)-P^*L(W_h)W_g-P^*W_hL(W_g)`

`=P^*Gamma_L(W_h,W_g)=B_L(h,g)`. QED.

If one insists on even-length loops, traverse the multiplication triangle twice. Its six-edge first-order coefficient is `2K_L(h,g)`, so no information is lost.

## 7. O(d^2) closed-loop tomography theorem

### Theorem 7.1 — all-d quadratic loop upper bound

For every `d>=2`, a bounded unital *-preserving generator on `M_d(C)` is identifiable modulo Hamiltonian derivations from at most

`3d^2-1`

matrix-valued first-order closed-loop coefficients.

One valid design is:

1. `d^2-1` Weyl backtracking loops, one for each nonidentity `W_p`;
2. `2d^2` multiplication-triangle loops, one for each pair `(e_j,g)` with `j in {1,2}` and `g in G`.

#### Proof

The shared backtracking data and Proposition 6.1 recover

`B_L(e_1,g)` and `B_L(e_2,g)`

for all `g`. If two generators give identical declared loop data, their difference `D` has zero generator defects. Theorem 5.1 then forces `D` to be a Hamiltonian derivation. QED.

### Corollary 7.2 — optimal asymptotic order for generalized flat-loop tomography

The dissipative quotient has real dimension

`N_d=(d^2-1)^2`.

A general `d x d` complex matrix-valued loop coefficient contains at most `2d^2` real scalar coordinates. Hence any universally identifying matrix-valued closed-loop design requires at least

`ceil((d^2-1)^2/(2d^2))`

loop families.

Together with Theorem 7.1,

`ceil((d^2-1)^2/(2d^2)) <= L_d^flat <= 3d^2-1`.

Therefore

`L_d^flat = Theta(d^2)`.

This establishes the optimal asymptotic order in the number of matrix-valued flat-loop families.

## 8. Relation to the Coxeter-face conjecture

Theorem 7.1 does **not** prove the sharper Article-II conjecture that adjacent-transposition Coxeter faces alone attain the lower bound

`ceil((d^2-1)^2/(2d^2))`

for every `d`.

What is now proved is:

- generalized exact flat-loop tomography has the optimal order `Theta(d^2)` for every finite `d`;
- exact information-theoretically minimal Coxeter-face designs exist for `d=3,4,5`;
- the all-`d` exact Coxeter constant remains an open structural problem.

This separation should be preserved in the publication claim set.

## 9. Publication interpretation

The Weyl theorem gives an explicit finite-dimensional bridge between Article I and Article II:

- Article I supplies exact flat unitary transport;
- Article II measures the first-order failure of that flatness under open-system evolution;
- Weyl multiplication relations convert those loop failures into a finite group cocycle;
- vanishing of the two generator-defect families forces that cocycle to be a coboundary;
- the only remaining ambiguity is Hamiltonian derivation.

The theorem is algebraic. It does not by itself establish an experimentally sample-optimal protocol, noise robustness, or an advantage over general Lindbladian tomography.
