# P3-B Jet Calculus Synthesis Audit v0.1.0

## Verdict

`CERTIFIED_WITH_EXPLICIT_IMPLEMENTATION_CEILING`

## Findings

The synthesis removes duplicated derivative code from M10–M12 by using normalized Taylor coefficients. Product, inverse, square-root, and logarithm recurrences are algebraic and extend to every finite order inside a regular chamber.

The numerical certificate is deliberately narrower: it validates matrix order 3 and log-speed order 2 on the 208-carrier, 15-family new-label atlas. This distinction prevents an arbitrary-order formal lemma from being confused with an arbitrary-order numerical stability theorem.

The unified engine reproduces the three prior residual scales:

- speed: `2.03e-9`;
- log-speed slope: `1.85e-9`;
- log-speed curvature: `8.64e-9`.

All twelve local tests pass. No fitted parameter, regression coefficient, or carrier-specific calibration is used.

## Integrity note

The M12 Markdown file had encoding corruption and was briefly replaced by a partial editorial update. The full document was restored before synthesis completion. The M12 source, certificate, numerical values, and verdict were never changed.

## Claim firewall

The general recurrence proves finite-order constructibility only under regularity of all denominators and square-root branches. It does not provide uniform wall bounds, physical q dynamics, semiclassical universality, or low-dimensional compression.

No statement from the Gemini advisory report is used as evidence.
