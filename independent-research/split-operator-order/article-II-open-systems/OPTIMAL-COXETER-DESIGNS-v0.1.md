# Information-theoretically minimal Coxeter tomography in dimensions 3, 4, and 5

**Article II research note — v0.1**  
**Author:** Malachevsky, A.A.  
**ORCID:** 0009-0008-6009-3196  
**Status:** `EXACT_CERTIFICATES_D3_D4_D5 / ALL_D_CONJECTURE_OPEN`

## 1. Lower bound

For `M_d(C)` the dissipative generator modulo Hamiltonian derivations has real dimension

`N_d=(d^2-1)^2`.

A matrix-valued first-order Coxeter-face coefficient belongs to `M_d(C)` and therefore provides at most `2d^2` real scalar coordinates. Hence any face-only universally identifying design needs at least

`L_d := ceil( N_d / (2d^2) )`

faces.

The first values are

- `d=3`: `N_3=64`, `L_3=4`;
- `d=4`: `N_4=225`, `L_4=8`;
- `d=5`: `N_5=576`, `L_5=12`.

## 2. Exact rank certificates

The Article-II measurement operator is the real-linear map from Hermitian Kossakowski coordinates to all real and imaginary matrix entries of the first-order reduced face coefficients.

For each of `d=3,4,5` we exhibit exactly `L_d` contextual braid faces whose stacked measurement matrix has full column rank.

### Theorem 2.1 — exact minimal qutrit design

For `d=3`, four explicitly declared braid/square faces from the qutrit gate tuple recorded in `GENERAL-RANK-CRITERION-v0.1.md` yield a `72 x 64` rational measurement matrix with

`rank_Q M_3 = 64`.

The rank is certified by reduction modulo `1000003`.

Thus four faces are sufficient and, by the dimension lower bound, necessary.

### Theorem 2.2 — exact minimal d=4 design

Let the four gates be

`X_4` = cyclic shift,

`D_4 = diag(1,i,-1,-i)`,

`R_12(3/5,4/5)`,

`R_23(3/5,4/5)`.

Use the following eight braid faces, where `b01=(s_1 s_2)^3` and `b12=(s_2 s_3)^3` and the tuple denotes the starting ordering of the four declared gates:

1. `(0,1,2,3), b01`;
2. `(0,1,2,3), b12`;
3. `(0,1,3,2), b01`;
4. `(0,2,3,1), b01`;
5. `(1,0,2,3), b12`;
6. `(1,2,3,0), b01`;
7. `(2,0,1,3), b12`;
8. `(3,0,1,2), b12`.

All gate entries lie in `Q(i)`. The full real/imag measurement matrix has size `256 x 225`.

Under the two finite-field embeddings

`i -> +350504`, `i -> -350504 (mod 1000033)`,

the real and imaginary rational parts are recovered by averaging/differencing the two embedded matrices. Exact modular row reduction gives

`rank_{F_1000033} M_4 = 225`.

Therefore `rank_Q M_4=225`.

Since seven faces provide at most `7*32=224<225` real coordinates, eight faces are information-theoretically minimal.

### Theorem 2.3 — exact minimal d=5 design

For `d=5`, construct each gate from a finite product of

- diagonal phases in `{1,i,-1,-i}`;
- rational Givens rotations with cosine/sine `(3/5,4/5)` or `(5/13,12/13)`.

The deterministic design generator is fixed by seed `0` and depth `6` in `examples/exact_face_rank_certificate_d5_v010.py`. It produces twelve braid faces. All entries lie in `Q(i)`.

The stacked real/imag measurement matrix has size `600 x 576`. Using the same two embeddings modulo `p=1000033`, exact finite-field row reduction gives

`rank_{F_p} M_5 = 576`.

Therefore `rank_Q M_5=576`.

Since eleven faces provide at most `11*50=550<576` real coordinates, twelve faces are information-theoretically minimal.

## 3. Genericity

For a fixed face template, every selected minor of the measurement matrix is a real-analytic function of the gate entries on the connected unitary parameter manifold.

### Corollary 3.1 — generic minimal identifiability for d=3,4,5

For each of `d=3,4,5`, the corresponding minimal face count `L_d` achieves full dissipative rank on a nonempty open dense subset of the relevant gate-design manifold.

#### Proof

The exact certificates above show that at least one maximal minor is nonzero for each dimension. Hence that minor is not the zero real-analytic function. Its nonzero set is open and dense on each connected analytic component of the design manifold. QED.

## 4. Current all-d barrier

The finite sequence strongly suggests the following statement, but it is **not yet proved**.

### Conjecture 4.1 — information-theoretically optimal Coxeter tomography

For every `d>=3`, there exists a contextual Coxeter-face design with exactly

`L_d = ceil((d^2-1)^2/(2d^2))`

matrix-valued faces whose first-order holonomy measurement operator has rank `(d^2-1)^2`.

Equivalently, generic face designs should attain the information-theoretic lower bound.

If true,

`L_d = d^2/2 + O(1)`,

so contextual-loop tomography would be asymptotically optimal in the number of matrix-valued loop families.

## 5. What has and has not been proved

Proved:

- exact rank criterion in arbitrary finite dimension;
- exact minimal face-only designs for `d=3,4,5`;
- generic open-dense full-rank consequence in those three dimensions;
- complete qubit dissipative identification by one braid plus two backtracks.

Not proved:

- Conjecture 4.1 for all `d`;
- a closed-form universal gate tuple attaining `L_d` in every dimension;
- uniform conditioning bounds as `d -> infinity`;
- sample complexity under noisy state-preparation/measurement access.

## 6. Next proof strategy

The most promising route to Conjecture 4.1 is an induction in `d` that embeds a full-rank `M_d` face design into `M_{d+1}` and adds only `O(d)` new braid faces to resolve the new Kossakowski directions. Since

`N_{d+1}-N_d = 4d^3 + 6d^2 - 2d - 1`,

while each new `(d+1) x (d+1)` face contributes at most `2(d+1)^2` real coordinates, only `O(d)` additional faces are dimensionally required at each induction step. Summing over dimensions would give an `O(d^2)` construction.
