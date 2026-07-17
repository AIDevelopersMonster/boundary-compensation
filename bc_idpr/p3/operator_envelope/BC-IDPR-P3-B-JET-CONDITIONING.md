# BC-IDPR-P3-B — Uniform Jet Conditioning Contract

**Status:** `UNIFORM_FINITE_Q6J_JET_CONDITIONING_CERTIFIED_ON_DECLARED_DISK`  
**Date:** 2026-07-16  
**Preregistration:** `aff51a5e1f00a70ce0790bc2a4fc96af0b184780`

## 1. Objective

The recursive jet calculus proves formal finite-order propagation inside a regular chamber. This contract supplies one common complex neighbourhood for the full declared carrier class and separates the q-number, square-root and logarithmic singular sets.

## 2. Frozen wall radius

For the critical q-number indices actually used by the 283 valid ordered carriers, \(1\le n\le10\), define

\[
R_{\rm wall}=\frac12\min_n\frac{\operatorname{dist}(n\theta_0,\pi\mathbb Z)}{n},
\qquad \theta_0=\pi/12.
\]

The frozen certification radius is

\[
R_{\rm cert}=R_{\rm wall}/16.
\]

Numerically,

\[
R_{\rm wall}=2.6179939\times10^{-2},\qquad
R_{\rm cert}=1.6362462\times10^{-3}.
\]

## 3. Uniform q-number bounds

On \(|z-\theta_0|\le R_{\rm cert}\),

\[
|[n]_q(z)|\ge \frac{\sin(\delta_n-nR_{\rm cert})}{\cosh R_{\rm cert}},
\]

and

\[
|[n]_q(z)|\le \frac{\cosh(nR_{\rm cert})}{\sin(\delta_1-R_{\rm cert})}.
\]

Across the declared critical set the minimum lower bound is \(0.2572378626\). Therefore all q-factorials and all Delta radicands remain nonzero on the disk, with branches fixed by continuation from the positive real anchor.

## 4. Log-speed domain

A 16-node complex boundary scan for every declared carrier, combined with a factor-two angular Lipschitz envelope, gives

\[
\inf_{|z-\theta_0|\le R_{\rm cert}}|\omega(z)|\ge0.0993257853.
\]

Hence the locally signed branch of \(\log|\omega|\) is analytic throughout the declared disk.

## 5. Cauchy majorants

The maximum boundary Frobenius norm is \(1.4143174446\). The scaled anchor coefficients \(\|F_r\|R_{\rm cert}^r\), for orders zero through three, are

\[
1.4142135624,
\quad1.2123565\times10^{-2},
\quad1.8199699\times10^{-4},
\quad3.0287879\times10^{-6}.
\]

They all lie below the common boundary majorant, as required by the Cauchy estimate.

## 6. Decision

Closed:

- common q-number regular chamber;
- common Delta branch chamber;
- common nonzero log-speed domain;
- uniform Cauchy majorants through matrix derivative order three.

Open:

- sharp all-order constants;
- larger optimal radius;
- low-dimensional representation compression.

Physical interpretation remains blocked.

No statement from the Gemini advisory report is used as evidence.
