# Article II — Open Systems / Context Reduction

**Working title:** *Context Reduction in Open Quantum Systems: Multiplicativity Defects, Lindblad Order Curvature, and Partial Operator Context*  
**Status:** `MANUSCRIPT_SEED / BOUNDED CORE OPEN`.

This paper is the planned successor to Article I. It does **not** assume that nonunitarity by itself creates curvature. The central question is instead whether a physically admissible UCP/CP reduction preserves the multiplicative context required for the exact flat transport of Article I.

## Core objects

For a unital completely positive map `Phi: A -> B`, define

`Delta_Phi(X,Y) = Phi(XY) - Phi(X) Phi(Y)`.

For a contextual loop of unitary transports `T_m ... T_1 = I`, define the reduced product

`H_Phi = Phi(T_m) ... Phi(T_1)`.

The first paper's exact flatness is recovered whenever the relevant generated algebra lies in the multiplicative domain of `Phi`.

## Bounded results already available

The manuscript seed contains proofs of:

1. a norm bound on `||H_Phi - I||` by multiplicativity defects;
2. a multiplicative-domain sufficient condition for preserved flatness;
3. a Stinespring formula for `Delta_Phi`;
4. the GKSL/Lindblad Leibniz-defect identity;
5. a first-order formula for reduced loop holonomy under a uniformly continuous Lindblad semigroup.

## Open obligations

- classify intermediate/partial context reductions;
- test whether any useful curvature monotonicity survives under nested CP reductions;
- construct exact low-dimensional channel examples;
- separate reversible linear inverse from physically admissible CPTP reversibility;
- extend from bounded generators to infinite-dimensional/unbounded settings;
- determine which reduced-holonomy quantities have operational information-theoretic meaning.
