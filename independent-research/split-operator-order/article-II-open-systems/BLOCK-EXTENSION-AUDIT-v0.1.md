# Block-extension audit for sharp Coxeter tomography

**Article II research note — v0.1**  
**Author:** Malachevsky, A.A.  
**ORCID:** 0009-0008-6009-3196  
**Status:** `NAIVE_INDUCTION_REFUTED / PARITY_EXTENSION_PROGRAMME_ACTIVE`

## 1. Question

Let

`L_d = floor(d^2/2)`

be the information-theoretic lower bound on the number of matrix-valued Coxeter faces needed to identify the dissipative quotient on `M_d(C)`.

The sharp conjecture asks whether a full-rank `L_d`-face design can be extended from dimension `d` to `d+1` by adding exactly

`m_d := L_(d+1)-L_d`

new square faces.

Thus

- if `d` is even, `m_d=d`;
- if `d` is odd, `m_d=d+1`.

The naive version of the induction was:

> every minimal full-rank design in dimension `d` is automatically extension-ready after the block embedding `U -> U direct-sum 1`.

This statement is false.

## 2. Exact counterexample to automatic extension-readiness

A recursive exact finite-field chain was rebuilt over the prime

`p=1000033`

starting from the certified qutrit design.

The following ranks were recomputed from the actual measurement matrices, not from stored rank labels:

- `d=3`: 4 faces, rank `64`;
- embedded `d=3 -> 4`: rank `128`;
- after four new global rational square faces: `d=4`, 8 faces, rank `225`;
- embedded recursive `d=4 -> 5`: rank `377`;
- after four new global rational square faces: `d=5`, 12 faces, rank `576`;
- embedded recursive `d=5 -> 6`: rank `833`;
- after six new global rational square faces: `d=6`, 18 faces, rank `1225`;
- embedded recursive `d=6 -> 7`: rank `1717`.

All ranks through the embedded `d=6 -> 7` stage were verified by modular row reduction in the current research environment.

The crucial point is the `d=5` stage. A generic minimal `d=5` design can have embedded rank `864`, but the recursively constructed minimal full-rank `d=5` design above has embedded rank only

`833 < 864`.

Hence

`full rank in M_d`

does not imply

`maximal embedded rank in M_(d+1)`.

This refutes automatic extension-readiness.

## 3. Generic embedded-rank pattern

For independently generic lower-bound-saturating square designs, numerical calculations for `2 <= d <= 7` give the stable pattern

`R_d^star = (d^2-1)(d+1)^2 + 2 * 1_(d even)`.

Equivalently,

- for odd `d`, the embedded old measurement matrix has full row rank;
- for even `d`, its row-rank defect is exactly `(d+1)^2-2` relative to its total row count.

The corresponding deficiency to the full dissipative rank in dimension `d+1` is

`Delta_d^star = 2 d (d+1)^2 - (-1)^d`.

This explains the observed maximal-increment ladders:

- odd `d`: after `d` new generic faces only one dimension remains, and the `(d+1)`-st face closes it;
- even `d`: `d-1` new faces add full `2(d+1)^2` rank and the last face adds `2(d+1)^2-1`.

The formula is not yet promoted to an all-d theorem; it is the target of the representation-theoretic block decomposition.

## 4. Local-plane induction fails

A second naive proposal was to use one new square face in each two-level plane

`span{|j>, |d>}`.

This also fails as a sharp universal mechanism.

For generic `SU(2)` pairs embedded in those planes, the observed projected rank increments are

- `4 -> 5`: `48,48,48,48`, while a generic global face can contribute `50`;
- `6 -> 7`: six increments of `96`, while a generic global face can contribute `98`.

The resulting designs remain rank deficient at the lower-bound face count.

Therefore the sharp induction, if true, requires genuinely global mixing of the new level with the old block. A purely one-plane-per-face construction is not sufficient.

## 5. Parity structure

The recursive calculations reveal a more plausible invariant.

### Even stages

The recursively produced even designs at `d=4` and `d=6` are extension-ready:

- `d=4` embeds with rank `377`, equal to the generic maximum;
- `d=6` embeds with rank `1717`, equal to the generic maximum.

### Odd stages

Odd stages need not be extension-ready. The recursive `d=5` example has extension defect

`864-833=31`,

but the next odd-to-even step has enough face-capacity slack to recover full rank with exactly the lower-bound number of additional faces.

This suggests that the correct induction invariant is parity-sensitive:

1. every even stage should be chosen extension-ready;
2. odd stages may carry a controlled extension defect;
3. the odd-to-even step must use its additional slack to restore extension-readiness at the new even stage.

## 6. Exact linear-algebra extension criterion

For any design `D_d`, let `M_d^uparrow` be its measurement matrix after block embedding into `M_(d+1)`, and let

`Q_d := coker(M_d^uparrow)`.

Let `F_1,...,F_m` be the measurement blocks of the proposed new faces, projected to `Q_d`.

Then the extension is full rank if and only if

`rank [ pi(F_1); ...; pi(F_m) ] = dim Q_d`.

This is elementary, but it isolates the only remaining problem: prove a structural transversality theorem for **global** square faces on the specific parity-controlled cokernels.

## 7. Current sharp target

The remaining theorem should no longer be phrased as automatic block extension.

### Conjecture — parity-controlled sharp block extension

There exists a sequence of lower-bound-saturating designs `D_d`, `d>=3`, such that

- every `D_d` has `L_d=floor(d^2/2)` faces and full dissipative rank;
- every even `D_d` is extension-ready;
- `D_(d+1)` is obtained from the block embedding of `D_d` by adding exactly `m_d` genuinely global square faces.

If proved, this yields

`L_d^Cox = floor(d^2/2)`

for every `d>=3`.

## 8. Reproducibility correction

During this audit the previously archived `exact_face_rank_certificate_d4_v010.py` was found to be only a status-printing stub rather than a self-contained matrix builder. The declared `d=4` rank `225` was independently rebuilt and verified from the actual gates and faces, so the mathematical result survives, but the archival script must be replaced before publication.

The same publication-hygiene rule applies to all higher-dimensional certificates: a stored rank label is not a certificate; the release must contain the actual matrix builder plus modular elimination.
