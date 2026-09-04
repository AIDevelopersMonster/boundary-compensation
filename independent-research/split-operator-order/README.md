# Split Operator Order — Independent Research Line

**Status:** independent research line; **not a Boundary Compensation branch**.

**Author:** Malachevsky, A.A. / Малачевский А.А.  
**ORCID:** 0009-0008-6009-3196

This directory archives a separate mathematical-physics research line that began from a split-interval representation of operator order and developed into commutator-weighted permutation geometry, exact threshold reordering algorithms, oriented lifts, contextual flatness, and pair-reduced holonomy.

## Scientific firewall

This directory is hosted inside the `boundary-compensation` repository only as an archival/reproducibility location. Its definitions, theorems, notation, publication sequence, and claims are independent of the Boundary Compensation programme. No BC theorem, branch number, or programme dependency is imported unless an explicit future document proves such a bridge.

## Publication sequence

### Article I — frozen scientific core / publication candidate

**Title:** *Split-Interval Representation of Quantum Operator Order: Descent Obstructions, Order Ultrametrics, and Pair-Reduced Holonomy*  
**Version:** v0.3.1  
**Status:** `REVIEWED_CLEAN`  
**Languages:** English and Russian mirror versions.

Core results:

1. split-interval descent obstruction;
2. exact identity `d_desc(A,B) = 1/2 ||[A,B]||`;
3. commutator-weighted minimax geometry on permutation space;
4. closed inversion-set formula for unitary tuples;
5. threshold filtration and exact precedence-reordering criterion;
6. simultaneous reduced-path optimality for all `l^p` costs;
7. additive and multiplicative oriented lifts;
8. exact contextual flatness versus pair-reduced holonomy;
9. first possible nonzero pair-reduced curvature term at fourth order;
10. QAOA / Heisenberg-XYZ computational demonstrations.

See [`article-I/`](article-I/).

### Article II — active manuscript seed

**Working title:** *Context Reduction in Open Quantum Systems: Multiplicativity Defects, Lindblad Order Curvature, and Partial Operator Context*.

The second article asks what survives when the flat contextual transport of Article I is passed through UCP/CP reductions rather than exact unitary context. The bounded setting already yields a rigorous multiplicativity-defect bound, a multiplicative-domain flatness criterion, a Stinespring defect formula, and a first-order Lindblad reduced-holonomy formula. Infinite-dimensional/domain questions, partial-context hierarchies, monotonicity, and numerical channel examples remain open obligations.

See [`article-II-open-systems/`](article-II-open-systems/).

## Repository layout

```text
split-operator-order/
├── README.md
├── AUTHOR-METADATA.md
├── ROADMAP.md
├── article-I/
│   ├── README.md
│   ├── manuscript-en.tex
│   ├── manuscript-ru.tex
│   ├── interactive-demo.html
│   ├── figures/
│   └── supplementary/
└── article-II-open-systems/
    ├── README.md
    ├── manuscript-seed-en.md
    ├── manuscript-seed-ru.md
    └── PROOF-OBLIGATIONS.md
```

## Publication rule

Article I is scientifically frozen except for genuine corrections, metadata, or publication-format changes. New open-system/context-reduction mathematics belongs to Article II rather than being appended to Article I.
