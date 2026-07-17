# BC-IDPR P5-UA01 WP1 — Physical Residual-Frame Matrix Protocol

**Contract:** `BC-IDPR-P5-UA01-PHYSICAL-RESIDUAL-FRAME-MATRIX`  
**Status:** `CANONICAL_PHYSICAL_PROTOCOL_FROZEN / N15_INGESTION_OPEN`  
**Upstream:** BC-Spec L1-P04-P/N15 operator-adapted residual-frame construction.

## 1. Physical object

For each declared level/family case, use the actual residual plane

\[
\mathcal U_{r,\lambda}=\operatorname{span}\{\mathcal R_{\rm bulk},W\}
\]

and the registered projected-torus coherent states `|psi_z>` with their frozen chart and quadrature weights. This is the gate-closing observation protocol. Arbitrary pure states in channel-coordinate space are not substituted for it.

For generators `U_i`, define

\[
(G_{\rm HS})_{ij}=\operatorname{Tr}(U_i^*U_j),
\qquad
(G_{\mathcal S})_{ij}=\sum_a w_a
\langle\psi_a,U_i\psi_a\rangle^*
\langle\psi_a,U_j\psi_a\rangle.
\]

The physical residual lower-frame constant is

\[
\alpha_{\mathcal U}=\lambda_{\min}(G_{\mathcal S},G_{\rm HS})
\]

on the quotient by Hilbert--Schmidt-null generator combinations.

## 2. Measurement-matrix form

Set

\[
M_{ai}=\sqrt{w_a}\,\langle\psi_a,U_i\psi_a\rangle.
\]

If

\[
G_{\rm HS}=Q_r\Lambda_rQ_r^*,
\qquad \Lambda_r>0,
\]

then the whitened physical matrix is

\[
\widehat M=M Q_r\Lambda_r^{-1/2}.
\]

Hence

\[
\boxed{\alpha_{\mathcal U}=\sigma_{\min}(\widehat M)^2},
\qquad
\boxed{\beta_{\mathcal U}=\sigma_{\max}(\widehat M)^2}.
\]

This identity is basis-invariant and reproduces the N15 generalized-Gram definition.

## 3. Frozen input contract

Every physical case package must contain:

- `generators`: the exact or audited matrices `R_bulk` and `W`;
- `coherent_states`: the registered projected-torus coherent-state vectors;
- `weights`: the original quadrature weights, without silent renormalization;
- level, family, chart, support, wall and ordering metadata;
- hashes of the source arrays and implementation.

The adapter rejects non-Hermitian generators, unnormalized states, negative weights and dimension mismatches.

## 4. Gate sequence

1. Ingest one frozen N15 case and reproduce its published `alpha_U`.
2. Reproduce all 20 N15 cases within a declared tolerance.
3. Freeze the exact physical candidate pool and quadrature measure.
4. Only then study design improvement or uniform lower bounds.
5. Separate the inherited physical frame constant from the auxiliary ideal-projective benchmark `1/4`.

## 5. Current consequence

The previous two-channel `1/4` theorem remains valid as an auxiliary coefficient-space benchmark, but it closes no physical P5 gate. The exact mixing/Arb calculations likewise become optional appendices until their channel-contrast bundle is connected to `span{R_bulk,W}` and the projected-torus lower-symbol map.

The immediate next executable obligation is `N15_PHYSICAL_CASE_INGESTION_AND_REPRODUCTION`.

## 6. Claim firewall

No physical uniform-frame, phase-transfer, energy-transfer or P2 handoff claim is permitted before the N15 physical matrix has been reconstructed and audited. RC02 remains frozen and is not reused for tuning.
