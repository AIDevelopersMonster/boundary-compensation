# Minimal qubit holonomy design and conditioning

**Article II research note — v0.1**  
**Author:** Malachevsky, A.A.  
**ORCID:** 0009-0008-6009-3196  
**Status:** `PROVED_FOR_ARTICLE-I-QUBIT-DESIGN`

This note sharpens the finite qubit identifiability theorem in `IDENTIFIABILITY-v0.1.md`.

## 1. Measurement blocks

For the Article-I contextual braid tuple, let `B(C)` denote the full first-order braid coefficient matrix and let `R_j(C),L_j(C)` denote the right/left first-order backtracking coefficient matrices of edge `j`.

Each is a real-linear map from the six-dimensional space `Sym_3(R)` of canonical unital qubit Kossakowski matrices to `M_2(C)`.

Direct exact/numerical rank evaluation gives:

- `rank(B)=4`;
- every single right or left backtracking block has rank `1`;
- the span of all twelve backtracking blocks has rank `5`;
- `rank(B + all backtracking blocks)=6`.

## 2. Minimal number of loop families

### Proposition 2.1 — braid plus two backtracks is minimal for this design

For the Article-I three-gate qubit transport design, full six-parameter dissipative identification from matrix-valued first-order loop coefficients requires at least three loop families if one of them is the contextual braid face.

Moreover, one braid loop together with two suitable backtracking loops is sufficient.

#### Proof

The braid block has rank `4`. A single backtracking block has rank at most `1`, so braid plus one backtrack has rank at most `5` and cannot identify all six parameters.

Exhaustive rank evaluation over the twelve oriented backtracking blocks shows that there exist pairs whose addition to the braid block raises the rank to `6`; for example `(R_1,R_2)` is full rank. Hence three loop families suffice, and fewer cannot suffice within this braid-plus-backtracking architecture. QED.

For the frozen design, 36 of the 66 unordered pairs of oriented backtracking blocks complete the braid block to rank `6`.

## 3. Conditioning

The six-scalar reconstruction matrix used in Theorem 5.1 of `IDENTIFIABILITY-v0.1.md` is

```text
M = [ -6  -8  -8   0   0   2
       0   0   2   0   4  -2
       0   2   0   4   0  -2
      -4   0  -4   0   0   0
      -4  -4   0   0   0   0
      -2  -2  -2   2   2   2 ]
```

Its singular values are approximately

`(15.01844, 5.31605, 5.12311, 3.18181, 3.12311, 2.01549)`,

so

`kappa_2(M) = sigma_max/sigma_min ≈ 7.45149`.

This is a moderate condition number. The present theorem is still algebraic rather than statistical, but the chosen six-scalar coordinate system is not near a rank singularity.

For comparison, using the *full matrix entries* of the braid block together with right backtracks `(R_1,R_2)` gives condition number approximately `12.447` for the corresponding overdetermined measurement operator. Other pairs can be substantially worse; for example `(R_5,R_6)` gives approximately `41.856`.

Thus identifiability and conditioning are distinct design objectives.

## 4. Exact inverse of the six-scalar map

Let `m=(m_1,...,m_6)^T` be the six measured scalars from `IDENTIFIABILITY-v0.1.md`, and let

`c=(c_xx,c_yy,c_zz,c_xy,c_xz,c_yz)^T`.

Then `c=M^{-1}m`, where

```text
M^{-1} =
[  1/8    1/32    1/32  -13/64  -13/64   -1/16
  -1/8   -1/32   -1/32   13/64   -3/64    1/16
  -1/8   -1/32   -1/32   -3/64   13/64    1/16
   0     -1/16    3/16   -3/32    1/32    1/8
   0      3/16   -1/16    1/32   -3/32    1/8
  -1/8   -5/32   -5/32    1/64    1/64    5/16 ]
```

Hence the Kossakowski coefficients are reconstructed explicitly without optimization or iterative fitting.

## 5. Design problem opened

The next finite-dimensional problem is no longer mere identifiability. It is the experiment/design problem

`maximize sigma_min(M_design)`

over admissible unitary tuples, loop families, and selected scalar matrix elements, subject to a declared cost budget.

This optimization should remain separate from the current theorem until a stable objective and admissible design class are fixed.
