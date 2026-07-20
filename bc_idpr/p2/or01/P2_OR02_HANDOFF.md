# P2-OR02 Handoff — Cross-Family Physical Pullback Identification

P2-OR01 localizes the remaining ambiguity to the relative U3/U4 physical
pullback. P2-OR02 must choose between the same-index and x-reversing
identifications from upstream geometry rather than numerical convenience.

Required inputs and gates:

1. derive the physical coordinate embeddings of U3 and U4 from the frozen N15
   four-gon chart;
2. define the common physical overlap as an equality or certified
   interpolation relation in physical coordinates, not grid indices;
3. compute the pullback Jacobian orientation and its uncertainty;
4. reconstruct genuine local P5 residual matrix elements on that overlap;
5. rerun the U3/U4 cross-Gram without post-hoc coordinate reversal;
6. test whether its determinant remains separated from zero.

Terminal outcomes:

- `PHYSICAL_Z2_ORIENTATION_OBSTRUCTION_CERTIFIED`;
- `ORIENTATION_SIGNAL_REMOVED_BY_CANONICAL_PULLBACK`;
- `PHYSICAL_PULLBACK_WALL_CROSSED`;
- `P2_CERTIFICATE_RESET` if an upstream convention error is proved.

