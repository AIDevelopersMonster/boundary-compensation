from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

out = Path(__file__).resolve().parent / "figures"
out.mkdir(exist_ok=True)

g1, g2, gamma_rate, tau, eta = 0.5, 0.7, 0.4, 0.05, 0.02
t = np.linspace(0.0, 2.0, 200001)
gamma_abs = np.abs(np.cos(2 * g1 * t) * np.cos(2 * g2 * t))
lambda_minus = (1.0 - gamma_abs) / 2.0
d_coarse = 0.5 * np.abs(gamma_abs - np.exp(-gamma_rate * t))


def first_crossing(y: np.ndarray, level: float) -> float:
    idxs = np.where(y >= level)[0]
    if len(idxs) == 0:
        raise RuntimeError(f"no crossing for level {level}")
    idx = int(idxs[0])
    if idx == 0:
        return float(t[0])
    t0, t1 = t[idx - 1], t[idx]
    y0, y1 = y[idx - 1], y[idx]
    return float(t0 + (level - y0) * (t1 - t0) / (y1 - y0))


t_tau = first_crossing(lambda_minus, tau)

fig, ax = plt.subplots(figsize=(6.8, 4.0))
ax.plot(t, lambda_minus, label=r"$\lambda_-(t)$")
ax.axhline(tau, linestyle="--", label=r"$\tau$")
ax.axhline(tau - eta, linestyle=":", label=r"$\tau-\eta$")
ax.axhline(tau + eta, linestyle=":", label=r"$\tau+\eta$")
ax.axvline(t_tau, linestyle="--", label=r"$t_\tau$")
ax.set_xlim(0.0, 0.6)
ax.set_ylim(0.0, 0.12)
ax.set_xlabel(r"$t$")
ax.set_ylabel("normalized Choi eigenvalue")
ax.legend(loc="best", fontsize=8)
fig.tight_layout()
fig.savefig(out / "choi_threshold_margin.pdf")
fig.savefig(out / "choi_threshold_margin.png", dpi=200)
plt.close(fig)

fig, ax = plt.subplots(figsize=(6.8, 4.0))
ax.plot(t, d_coarse, label=r"$D_{\rm coarse}(t)$")
ax.axvline(t_tau, linestyle="--", label="threshold crossing")
ax.set_xlim(0.0, 0.6)
ax.set_ylim(0.0, 0.025)
ax.set_xlabel(r"$t$")
ax.set_ylabel("coarse distance")
ax.legend(loc="best", fontsize=8)
fig.tight_layout()
fig.savefig(out / "coarse_markovian_distance.pdf")
fig.savefig(out / "coarse_markovian_distance.png", dpi=200)
plt.close(fig)

rows = []
for level in [tau - eta, tau, tau + eta]:
    tc = first_crossing(lambda_minus, level)
    ga = float(abs(np.cos(2 * g1 * tc) * np.cos(2 * g2 * tc)))
    lm = float((1.0 - ga) / 2.0)
    dc = float(0.5 * abs(ga - np.exp(-gamma_rate * tc)))
    rows.append((level, tc, lm, dc))

max_before = float(d_coarse[t <= t_tau].max())
for level, tc, lm, dc in rows:
    print(f"level={level:.3f}, t={tc:.6f}, lambda_minus={lm:.6f}, D_coarse={dc:.6f}")
print(f"max D_coarse before threshold: {max_before}")
