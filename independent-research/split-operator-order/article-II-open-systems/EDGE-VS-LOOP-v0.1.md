# Edge-resolved versus loop-only identifiability

**Article II research note — v0.1**  
**Author:** Malachevsky, A.A.  
**ORCID:** 0009-0008-6009-3196  
**Status:** `PROVED_FINITE_DIMENSIONAL_BOUNDARY`

The finite-channel no-go theorem in `IDENTIFIABILITY-v0.1.md` shows that closed-loop holonomies alone need not identify a UCP channel. This note isolates exactly where the information is lost.

## 1. Anchored edge data

Let `T` be a fixed family of contextual edge transports and define

`S_T := span_C { I, T, T^* : T in T }`.

Suppose the reduced edge operators `Phi(T)` are known individually in a fixed output representation, rather than only through products around closed loops.

### Proposition 1.1 — edge-resolved reconstruction on the transport operator system

The anchored edge data determine the restriction `Phi|_{S_T}` uniquely.

If `S_T=A` in finite dimension, then they determine the entire linear map `Phi:A->B` uniquely.

#### Proof

The values of a linear map on a spanning set determine the map on its span. QED.

Thus the general finite-channel obstruction is not caused by complete positivity itself. It is caused by reducing edge-resolved information to loop products.

## 2. Article-I qubit transport system is tomographically complete

For the Article-I braid tuple

`U_1=sigma_x`,

`U_2=(sigma_x+sigma_y)/sqrt(2)`,

`U_3=(sigma_x+sigma_z)/sqrt(2)`,

let `T_1,...,T_6` be the six exact contextual edge transports along

`123 -> 213 -> 231 -> 321 -> 312 -> 132 -> 123`.

### Proposition 2.1 — full qubit operator-system span

`span_C { I,T_1,...,T_6,T_1^*,...,T_6^* } = M_2(C)`.

In fact `I` together with only three suitable contextual edge transports already spans `M_2(C)`; for example `I,T_1,T_2,T_3` has complex rank `4`.

Therefore, for this concrete design, individually resolved channel images of three suitable edges are sufficient to reconstruct an arbitrary linear qubit channel once unitality fixes `Phi(I)=I`.

## 3. Loop quotient

Closed-loop holonomy replaces the ordered edge list

`(Phi(T_1),...,Phi(T_m))`

by products such as

`Phi(T_m)...Phi(T_1)`.

This map is nonlinear and generally many-to-one. The depolarizing sign ambiguity in `IDENTIFIABILITY-v0.1.md` is an explicit example: two distinct UCP maps have different edge images but identical products on every closed loop of the chosen graph.

Hence Article II should distinguish three information levels:

1. **edge-resolved data** — determine `Phi` on `S_T`;
2. **open-path product data** — retain anchored ordered products but not individual factors;
3. **closed-loop holonomy data** — retain only gauge-like path defects and can be strictly less informative.

## 4. Consequence for the programme

The correct inverse problem is therefore not 'does holonomy determine the channel?' in the unrestricted sense. It is:

> For a declared information level and transport design, what is the kernel of the induced measurement map on the chosen channel or generator model class?

This formulation unifies the finite-channel no-go theorem, the qubit Lindbladian rank-6 theorem, and future higher-dimensional design questions.
