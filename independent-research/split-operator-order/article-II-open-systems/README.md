# Article II — Open Systems / Context Reduction

**Working title:** *Context Reduction in Open Quantum Systems: Multiplicativity Defects, Lindblad Order Curvature, and Partial Operator Context*  
**Current milestone:** `v0.1.0 / ANALYTICAL_CORE_ACTIVE`  
**Author:** Malachevsky, A.A.  
**ORCID:** 0009-0008-6009-3196

This paper is the successor to Article I. It does **not** assume that nonunitarity by itself creates curvature. The central object is the failure of a physically admissible UCP reduction to preserve the multiplicative context required by the exactly flat contextual transport of Article I.

## Core object

For a UCP map `Phi: A -> B`,

`Delta_Phi(X,Y) = Phi(XY) - Phi(X)Phi(Y)`.

For a contextual loop of unitary transports

`T_m ... T_1 = I`,

the reduced loop product is

`H_Phi = Phi(T_m) ... Phi(T_1)`.

## v0.1.0 proved bounded results

The developed manuscript [`manuscript-v0.1.0-en.md`](manuscript-v0.1.0-en.md) now contains:

1. **Exact loop-defect decomposition**

   `H_Phi-I = -sum transported Delta_Phi(T_k,P_{k-1})`.

2. **UCP norm certificate** as a corollary of the exact identity.

3. **Multiplicative-domain flatness criterion**.

4. **Exact nested-reduction composition law**

   `Delta_{Psi o Phi}=Psi(Delta_Phi)+Delta_Psi(Phi(.),Phi(.))`.

5. **Layer-resolved context-loss identity** for finite chains of reductions.

6. **Backtracking/Schwarz-defect theorem** and a two-sided unitary test for membership in `MD(Phi)`.

7. **Stinespring squared-leakage formula** for backtracking defects.

8. **Exact semigroup evolution equation** for `Delta_t`.

9. **Exact Duhamel representation** of the semigroup multiplicativity defect.

10. **GKSL Leibniz-defect identity** and positive Schwarz-defect production formula.

11. **Exact integral formula for reduced Lindblad loop holonomy**; the old first-order formula is now only its linearization.

12. **Exact six-edge dephasing calculation** on the contextual braid loop inherited from Article I.

## Exact dephasing braid-loop result

For the Article-I spin triple and the closed path

`123 -> 213 -> 231 -> 321 -> 312 -> 132 -> 123`,

under qubit dephasing with coherence factor `eta`,

`H_eta = [[eta^4, eta^3(1-eta^2)/2],[-eta^3(1-eta^2)/2,eta^4]]`,

so

`||H_eta-I|| = sqrt((1-eta^4)^2 + eta^6(1-eta^2)^2/4)`.

For `eta=e^{-gamma t}`,

`||H_t-I|| = sqrt(17) gamma t + O(t^2)`.

Reproducibility files are in [`examples/`](examples/).

## Literature / novelty discipline

Classical infrastructure is explicitly separated from the proposed contribution:

- Stinespring dilation is classical;
- Choi Schwarz inequalities and multiplicative domains are classical;
- GKSL/Lindblad generator theory is classical;
- noncommutative carré du champ is classical;
- quantum-channel multiplicative-domain theory is established.

See [`LITERATURE-NOVELTY-AUDIT-v0.1.md`](LITERATURE-NOVELTY-AUDIT-v0.1.md).

The candidate new synthesis is the coupling of these structures to an exactly flat operator-order connection, including exact loop-defect, nested-reduction, semigroup-integral, and Coxeter-loop formulas. Specialist priority audit remains mandatory before publication.

## Immediate next attacks

- full amplitude-damping calculation on the six-edge contextual braid loop;
- full depolarizing calculation on the same loop;
- multiplicative-domain classification on the generated transport algebra;
- cancellation examples and converse-flatness questions;
- broader operator-algebra / QEC / channel-holonomy novelty search.

## Claim firewall

Do not claim that:

- dissipation automatically produces curvature;
- `||H-I||` is universally monotone under nested UCP reductions;
- reduced order holonomy is already a decoherence or entropy-production monotone;
- this is physical gauge or spacetime curvature.

The resolvent-boundary `R_H(E±i0)` project remains deferred to a later article.
