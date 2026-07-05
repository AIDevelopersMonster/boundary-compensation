# BC-CI II certified transport demo

This companion package illustrates the finite-dimensional status logic used in

**Boundary Compensation - Compensated Islands II: Certified Residual Transport and Propagation-Compatible Readout Channels**.

The demo is not a physical simulation. It does not implement time evolution, Hamiltonian dynamics, photons, waves, fields, or spacetime propagation. It only visualizes the certification distinction introduced in BC-CI II:

```text
spectral channel persists  !=  readout is detectable
```

Formally, the toy scenarios track two margins along a declared parameter path `u in [0,1]`:

```text
spectral margin:  s_a(u) = g_a^tau(B(u)) - eta
readout margin:   q_a(u) = ||R_a(u)|| - delta_read
```

A channel can remain spectrally certified while the residual readout falls below threshold. This is the central demonstration in `readout_below_threshold`.

## Contents

```text
configs/                    Scenario thresholds and sampling settings
certified_transport_demo.py Reproducible finite-dimensional status scanner
html/demo.html              Browser-only interactive demonstration, no dependencies
figures/*.svg               Generated margin charts
figures/status_timeline.svg Generated status timeline summary
data/demo_outputs.json      Generated sampled outputs
```

## Run

From this directory:

```bash
python certified_transport_demo.py
```

The script regenerates `data/demo_outputs.json` and SVG figures under `figures/`.

Open the interactive demo directly in a browser:

```text
html/demo.html
```

No network access and no external JavaScript libraries are required.

## Status logic

For each sample point, the status is assigned as follows:

- `CHANNEL_CERTIFIED`: spectral margin is positive but no readout data are evaluated.
- `READOUT_CERTIFIED`: spectral margin is positive and readout margin is positive.
- `READOUT_BELOW_THRESHOLD`: spectral margin is positive but readout margin is zero or negative.
- `CHANNEL_MERGER`: spectral separation margin is zero or negative.
- `RANK_CHANGE`: the threshold rank changes under the declared threshold rule.
- `CERTIFICATE_RESET`: no silent continuation is allowed after a certificate failure.

## Non-claim note

The word `transport` here means certified continuation of a channel label along a declared parameter path. It is not physical motion. The parameter `u` is not physical time.
