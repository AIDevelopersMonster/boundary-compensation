Split-Interval Quantum Operator Order — benchmark notes

This directory contains the deterministic classical reordering benchmarks used by Article I. The benchmarks compare exhaustive minimax search on the adjacent-transposition permutation graph with the exact inversion-set / threshold algorithms derived in the manuscript.

Scope:
- timings start after the pairwise weights c_ij = 1/2 ||[U_i,U_j]|| are available;
- QAOA and Pauli-rotation weights are obtained analytically;
- the benchmark is not a full hardware-aware quantum compiler benchmark;
- exhaustive search is run only where the permutation graph remains computationally feasible;
- larger-n rows report only the exact threshold solver.

Run the benchmark script with the recorded Python environment and compare the generated CSV values with the frozen tables in this directory. Wall-clock timings may fluctuate; mathematical thresholds, state counts, and filtration values are deterministic.
