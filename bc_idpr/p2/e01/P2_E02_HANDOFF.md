# P2-E02 Handoff

Canonical next object: `P2-E02 Oriented Cross-Overlap Edge Certification`.

The one-cycle graph is frozen:

`U1 -> U2 -> U3 -> U4 -> EQ -> U1`.

For every edge, P2-E02 must provide:

1. a declared shared comparison carrier;
2. coefficient analysis maps from both adjacent families;
3. an oriented cross-Gram matrix;
4. an explicit sign/orientation convention;
5. a lower singular-value bound for the edge comparison map;
6. a certified edge defect and uncertainty envelope.

No graph search or edge replacement is permitted before all five registered edge certificates are available.

Terminal outcomes:

- `EXACT_CYCLE_CLOSURE_CERTIFIED`;
- `NONZERO_CYCLE_DEFECT_CERTIFIED`;
- `ORIENTATION_UNIDENTIFIABLE`;
- `EDGE_CERTIFICATE_INCONCLUSIVE`.

P2-E01 does not authorize P2-G3 quantitative global positivity or P2-G4 eta-uniformity.
