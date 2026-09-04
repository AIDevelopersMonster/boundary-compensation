# Article II — exact channel examples v0.1

This note extends the v0.1.0 analytical core from dephasing to qubit depolarization and amplitude damping on the same six-edge contextual braid loop inherited from Article I.

## 1. Common loop

Use

`U_1 = sigma_x`,

`U_2 = (sigma_x+sigma_y)/sqrt(2)`,

`U_3 = (sigma_x+sigma_z)/sqrt(2)`

and the closed adjacent-swap path

`123 -> 213 -> 231 -> 321 -> 312 -> 132 -> 123`.

Let

`T_k = W_{sigma_k} W_{sigma_{k-1}}^*`.

Then, exactly,

`T_6 T_5 T_4 T_3 T_2 T_1 = I`.

For a channel `Phi`, define

`H_Phi = Phi(T_6)...Phi(T_1)`.

The unreduced loop is flat; all formulas below measure only the failure of the channel to preserve the multiplicative context.

## 2. Dephasing reference result

For

`Phi_eta([[a,b],[c,d]])=[[a,eta b],[eta c,d]]`,

`0<=eta<=1`,

we already obtained

`H_eta = [[eta^4, b_eta],[-b_eta,eta^4]]`,

where

`b_eta = eta^3(1-eta^2)/2`.

Therefore

`||H_eta-I|| = sqrt((1-eta^4)^2 + eta^6(1-eta^2)^2/4)`.

For `eta=e^{-gamma t}`,

`||H_t-I|| = sqrt(17) gamma t + O(t^2)`.

## 3. Qubit depolarizing channel

Let

`Phi_eta(A)=eta A+(1-eta) tr(A) I/2`,

with `0<=eta<=1`.

A direct exact multiplication gives

`H_eta^dep = [[a_eta,b_eta],[-conj(b_eta),a_eta]]`,

with

`a_eta = eta^5(eta+1)/2`,

`b_eta = eta^4(1-eta)[2 eta + i(1+eta)]/4`.

The matrix `H_eta^dep-I` is normal, hence

`||H_eta^dep-I||`

`= sqrt( (1-a_eta)^2 + |b_eta|^2 )`,

where

`|b_eta|^2 = eta^8(1-eta)^2(5 eta^2+2 eta+1)/16`.

Thus

`||H_eta^dep-I||`

`= sqrt( (1-eta^5(eta+1)/2)^2`

`        + eta^8(1-eta)^2(5 eta^2+2 eta+1)/16 )`.

For the semigroup parameterization `eta=e^{-gamma t}`,

`||H_t^dep-I|| = (sqrt(123)/2) gamma t + O(t^2)`.

This differs from the dephasing coefficient `sqrt(17) gamma`, so the reduced braid holonomy distinguishes these two channels already at first order on the same contextual loop.

## 4. Amplitude damping — Heisenberg picture

Let `q in [0,1]` be the survival parameter of the standard amplitude-damping channel. The Schrödinger-picture channel is trace preserving but not unital; its Heisenberg dual is UCP and acts by

`Phi_q([[a,b],[c,d]])`

`= [[a, sqrt(q)b],`

`   [sqrt(q)c, q d+(1-q)a]]`.

For the same contextual braid loop, define

`c_q = q^2[(1+q)+i(q-1)]/2`.

Then exact multiplication gives

`H_q^AD =`

`[[ c_q, (1/2) q^(3/2)(1-q)(2q-1) ],`

` [ q^(3/2)(1-q)(1/2+i q), (2q-1)c_q ]]`.

Unlike the dephasing and depolarizing examples, this reduced holonomy is generally non-normal. Its operator norm is nevertheless closed-form through the standard 2x2 singular-value identity.

Let

`M_q = H_q^AD-I`,

`tau(q)=tr(M_q^* M_q)`

`=(q-1)^2(4q^6+8q^5+8q^4+13q^3+12q^2+8q+4)/2`,

and

`delta(q)=|det M_q|^2`

`=(q-1)^4(100q^8+220q^7+329q^6+408q^5+400q^4`

`           +296q^3+160q^2+64q+16)/16`.

Then

`||H_q^AD-I||^2`

`= [ tau(q) + sqrt(tau(q)^2-4 delta(q)) ]/2`.

For the Markov parameterization `q=e^{-gamma t}`,

`H_t^AD-I = -gamma t D_AD + O(t^2)`

with

`D_AD = [[5/2+i/2,-1/2],[-1/2-i,9/2+i/2]]`,

so

`||H_t^AD-I||`

`= (1/2)sqrt(57+2sqrt(314)) gamma t + O(t^2)`.

Numerically the linear coefficient is approximately `4.80728848 gamma`.

## 5. Comparison of first-order channel fingerprints

For the same exactly flat six-edge contextual loop:

| Channel | Semigroup parameter | First-order coefficient of `||H_t-I||/(gamma t)` |
|---|---|---:|
| dephasing | `eta=e^{-gamma t}` | `sqrt(17) ~= 4.1231` |
| depolarizing | `eta=e^{-gamma t}` | `sqrt(123)/2 ~= 5.5453` |
| amplitude damping (Heisenberg) | `q=e^{-gamma t}` | `sqrt(57+2sqrt(314))/2 ~= 4.8073` |

These are not claimed as universal channel invariants. They are loop-resolved fingerprints relative to the declared Article-I transport loop.

## 6. Interpretation boundary

The differences above show that reduced order holonomy is sensitive to the structure of the UCP reduction, not merely to a scalar amount of contraction. They do **not** establish equivalence to decoherence rate, entropy production, channel capacity loss, or any standard open-system monotone.

## 7. Next analytical question

The next structural target is no longer “find a nonzero channel example”; that is now closed. The sharper question is:

> For a fixed transport algebra and a family of channels, which part of the channel is actually visible to the collection of elementary Coxeter-loop holonomies?

This leads to a potential identifiability theorem: characterize the quotient of UCP reductions determined by all square/braid reduced holonomies of a given operator family.
