# General finite-dimensional holonomy rank criterion

**Article II research note — v0.1**  
**Author:** Malachevsky, A.A.  
**ORCID:** 0009-0008-6009-3196  
**Status:** `PROVED_FINITE_DIMENSIONAL_CORE / QUTRIT_CERTIFICATE_COMPLETE`

## 1. Dissipative parameter space modulo Hamiltonian derivations

Let `A=M_d(C)` and let `q=d^2-1`. Consider bounded complex-linear, *-preserving, unital generators `L:A->A`, so `L(I)=0`.

The real vector space of such linear maps has dimension

`d^2(d^2-1)`.

Hamiltonian derivations

`D_H(X)=i[H,X]`

with self-adjoint `H`, modulo scalar multiples of `I`, form a real vector space of dimension

`d^2-1=q`.

Therefore the quotient by Hamiltonian derivations has dimension

`d^2(d^2-1)-(d^2-1)=(d^2-1)^2=q^2`.

Equivalently, after fixing a traceless Hermitian operator basis `F_1,...,F_q`, the dissipative class can be represented by a Hermitian Kossakowski matrix `C in Herm_q`, which also has real dimension `q^2`.

The bilinear Leibniz defect

`Gamma_L(X,Y)=L(XY)-L(X)Y-X L(Y)`

is invariant under adding a derivation. Conversely, if two bounded *-preserving unital maps have the same `Gamma`, their difference is a derivation. Thus `Gamma_L` is a complete coordinate on the quotient by Hamiltonian derivations.

## 2. First-order contextual-loop measurements

Fix a finite transport design `D` consisting of exact contextual loops. For a loop

`ell=(T_1,...,T_m)`, `T_m...T_1=I`,

write

`P_{k-1}=T_{k-1}...T_1`.

For the semigroup `Phi_t=exp(tL)`, the first-order reduced loop coefficient is

`K_ell(L) := d/dt|_{t=0} [ Phi_t(T_m)...Phi_t(T_1) ]`

and Article II gives

`K_ell(L) = - sum_{k=2}^m T_m...T_{k+1} Gamma_L(T_k,P_{k-1})`.

For a backtracking loop based on a unitary `U`,

`K_U^R(L)=-Gamma_L(U^*,U)`

and similarly for the opposite orientation.

Each coefficient depends real-linearly on the dissipative class `[L]`.

Choose finitely many real-linear scalar readouts `lambda_r` of the matrix coefficients `K_ell(L)` (for example real and imaginary matrix entries or state expectation values). They define a real-linear measurement operator

`M_D : G_d / Der(M_d) -> R^N`.

After choosing a real basis of the quotient, this is an `N x q^2` real measurement matrix.

## 3. Rank criterion

### Theorem 3.1 — exact finite-dimensional holonomy identifiability criterion

The following are equivalent:

1. the selected first-order holonomy readouts identify every bounded dissipative generator on `M_d(C)` modulo Hamiltonian derivations;
2. `ker M_D={0}`;
3. `rank M_D=(d^2-1)^2`.

#### Proof

The first-order coefficients are linear in `Gamma_L`, and `Gamma_L` depends only on the class modulo derivations. Therefore the complete readout map is the finite-dimensional real-linear map `M_D`. Injectivity is equivalent to trivial kernel, and by rank-nullity this is equivalent to full column rank `q^2`. QED.

### Corollary 3.2 — physical non-identifiability when rank is deficient

If `rank M_D<q^2`, then the design is not universally identifiable even on the interior of the physical Kossakowski cone.

#### Proof

Let `0 != K in ker M_D` be Hermitian in Kossakowski coordinates. Choose `C_0=lambda I_q` with `lambda>0`. For sufficiently small `epsilon>0`, both

`C_+=C_0+epsilon K`, `C_-=C_0-epsilon K`

remain positive definite. They define two distinct physical dissipators with identical selected first-order holonomy data because their difference lies in the kernel. QED.

Thus full rank is not merely sufficient; it is necessary for universal physical identifiability.

## 4. Information-theoretic measurement lower bounds

A general matrix-valued face coefficient in `M_d(C)` carries at most `2d^2` real scalar coordinates. A backtracking Schwarz coefficient is Hermitian and carries at most `d^2` real coordinates.

Therefore:

- a design using only general face matrices needs at least

  `ceil((d^2-1)^2/(2d^2))`

  loop families;

- a design using only full Hermitian backtracking matrices needs at least

  `ceil((d^2-1)^2/d^2)`

  loop families.

These are dimension-count lower bounds; algebraic symmetries may force more loops.

## 5. Corrected complete qubit result

For `d=2`, the full dissipative quotient has dimension

`(2^2-1)^2=9`.

The earlier six-parameter note treated only the real-symmetric Kossakowski subclass. The complete Hermitian `3 x 3` Kossakowski matrix has nine real parameters.

For the Article-I spin tuple

`U_1=sigma_x`,

`U_2=(sigma_x+sigma_y)/sqrt(2)`,

`U_3=(sigma_x+sigma_z)/sqrt(2)`,

use the six-edge contextual braid loop

`123 -> 213 -> 231 -> 321 -> 312 -> 132 -> 123`

plus the first two edge backtracks. The full matrix-valued braid block has rank `6`, each of these backtracking blocks adds rank `2`, and the combined three-loop design has rank `9`.

More explicitly, selecting the nine scalar rows

- braid: all four real matrix entries, `Im K_11`, `Im K_12`;
- first backtrack: `Re K_11`, `Re K_22`;
- second backtrack: `Re K_11`;

gives a `9 x 9` real matrix with exact determinant

`det M_2 = 3932160 = 2^18 * 3 * 5 != 0`.

### Theorem 5.1 — complete qubit dissipative reconstruction

For the declared Article-I transport tuple, one contextual braid loop plus two backtracking loops identify the complete bounded qubit dissipative generator modulo Hamiltonian derivations.

The previous six-parameter real-symmetric theorem remains valid as a strict subcase, but is no longer the maximal qubit statement.

## 6. Exact qutrit full-rank witness

For `d=3`, `q=8`, so the dissipative parameter dimension is

`q^2=64`.

The face-only information lower bound is

`ceil(64/18)=4`.

We now exhibit four qutrit face loops that attain this lower bound exactly.

### 6.1 Gate set

Let

`X = [[0,0,1],[1,0,0],[0,1,0]]`,

`D = diag(1,i,-1)`,

`R_12 = [[3/5,4/5,0],[-4/5,3/5,0],[0,0,1]]`,

`R_23 = [[1,0,0],[0,3/5,4/5],[0,-4/5,3/5]]`.

All four matrices are unitary and have entries in the Gaussian rationals `Q(i)`.

Write the ordered gate family as

`(U_1,U_2,U_3,U_4)=(X,D,R_12,R_23)`.

### 6.2 Four Coxeter faces

Use the following exact contextual loops:

1. at ordering `1234`, the braid `(s_1 s_2)^3`;
2. at ordering `1234`, the braid `(s_2 s_3)^3`;
3. at ordering `1234`, the square `(s_1 s_3)^2`;
4. at ordering `1243`, the braid `(s_1 s_2)^3`.

For each loop retain all real and imaginary entries of the first-order matrix coefficient. This gives `4 x 18 = 72` real readouts.

Choose the traceless Hermitian qutrit basis consisting of the six symmetric/antisymmetric matrix-unit pairs together with

`diag(1,-1,0)`, `diag(0,1,-1)`.

In the corresponding Hermitian `8 x 8` Kossakowski coordinates, the resulting measurement matrix `M_3` is a `72 x 64` rational matrix.

### Theorem 6.1 — exact minimal qutrit face design

The above four qutrit contextual faces have

`rank_Q M_3 = 64`.

Hence they identify the complete bounded qutrit dissipative generator modulo Hamiltonian derivations.

Moreover, four general face loops are information-theoretically minimal because each face matrix contributes at most `18` real scalars and `3 x 18 < 64`.

#### Exact certificate

The deterministic verification script `examples/qutrit_rank_certificate_v010.py` forms the rational matrix exactly and reduces it modulo the prime

`p=1000003`.

The modular row reduction gives

`rank_{F_p}(M_3 mod p)=64`.

All denominators are powers of `5`, so they are invertible modulo `p`. A `64 x 64` minor is therefore nonzero modulo `p`, hence its rational determinant is nonzero. Consequently `rank_Q M_3=64`. QED.

## 7. Generic qutrit consequence

The entries of the measurement matrix depend real-analytically on the four unitary gates. The nonzero `64 x 64` minor certified above is therefore a nontrivial real-analytic function on the connected manifold `U(3)^4`.

### Corollary 7.1 — generic full-rank qutrit designs for the four-face template

For the same four-face Coxeter template, full-rank dissipative identifiability holds on a nonempty open dense subset of `U(3)^4`.

#### Proof

The certified minor is nonzero at the explicit witness, so it is not identically zero. The nonzero set of a nontrivial real-analytic function is open and dense on a connected real-analytic manifold. On that set the same `64 x 64` minor remains nonzero. QED.

Thus qutrit identifiability is not a fine-tuned accident of one gate tuple.

## 8. Novelty and literature boundary

The rank-nullity criterion itself is elementary linear inverse-problem infrastructure and is not claimed as new. General Lindbladian learning/tomography is also an active independent literature, including recent 2026 work on ansatz-free and local-response Lindbladian learning.

The contribution claimed here is narrower:

1. the specific first-order measurement operator induced by exact contextual operator-order loops;
2. the separation of Hamiltonian derivations by the holonomy/Leibniz-defect construction;
3. exact finite face designs for dissipative reconstruction;
4. the complete qubit three-loop certificate;
5. the exact information-theoretically minimal four-face qutrit certificate;
6. the contrast with the finite-time closed-loop no-go theorem from the companion identifiability note.

No claim is made that this supersedes general quantum process tomography or recent scalable Lindbladian-learning protocols.

## 9. Next theorem target

The next structural problem is to determine, for general `d`, whether there exists a universal finite Coxeter-face template attaining full rank with `O(d^2)` loops, and to characterize the conditioning of such designs.
