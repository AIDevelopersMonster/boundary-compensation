"""Optional Streamlit GUI for BC-Origin Shadow Lab.

Run:
    streamlit run bc_origin/lab/streamlit_app.py
"""
from __future__ import annotations

from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

HERE = Path(__file__).resolve().parent / "python"
sys.path.insert(0, str(HERE))
from bc_origin_visual_core import signed_shadow

st.set_page_config(page_title="BC-Origin Shadow Lab", layout="wide")
st.title("BC-Origin Shadow Lab")
st.caption("Interactive signed-shadow model: orientation-controlled localization, admissibility horizon, and coupling-induced shadow gap.")

with st.sidebar:
    st.header("Parameters")
    n1 = st.slider("n1 winding", -5, 5, 1, 1)
    n2 = st.slider("n2 winding", -5, 5, 1, 1)
    d1 = st.slider("d1 denominator", 0.2, 10.0, 3.0, 0.1)
    d2 = st.slider("d2 denominator", 0.2, 10.0, 5.0, 0.1)
    gamma = st.slider("gamma signed shift", 0.0, 8.0, 1.0, 0.1)
    kappa = st.slider("kappa coupling", 0.0, 5.0, 1.0, 0.1)
    mu = st.slider("mu effective", 0.1, 5.0, 1.0, 0.1)

res = signed_shadow(n1, n2, d1, d2, gamma, kappa, mu)

c1, c2, c3, c4 = st.columns(4)
c1.metric("orientation s", res.orientation)
c2.metric("lambda-", f"{res.lambda_minus:.4f}")
c3.metric("lambda+", f"{res.lambda_plus:.4f}")
c4.metric("gap", f"{res.gap:.4f}")

c5, c6, c7 = st.columns(3)
c5.metric("scale- ell/L", "horizon" if not np.isfinite(res.scale_minus) else f"{res.scale_minus:.4f}")
c6.metric("scale+ ell/L", "horizon" if not np.isfinite(res.scale_plus) else f"{res.scale_plus:.4f}")
c7.metric("localized", str(res.localized_minus and res.localized_plus))

x = np.linspace(-8, 14, 600)
fig, ax = plt.subplots(figsize=(10, 4.5))
ax.axvspan(0, max(res.lambda_minus, 0), alpha=0.18)
ax.axvline(0, linewidth=1)
ax.axvline(res.lambda_minus, linewidth=2, label="lambda-")
ax.axvline(res.lambda_plus, linewidth=2, linestyle="--", label="lambda+")
ax.set_xlim(-8, 14)
ax.set_yticks([])
ax.set_xlabel("observable inverse-scale denominator lambda")
ax.set_title("Signed observable shadow spectrum")
ax.legend()
st.pyplot(fig)

st.subheader("Admissibility horizon map for opposite orientation")
gammas = np.linspace(0, 8, 220)
kappas = np.linspace(0, 5, 160)
z = np.zeros((len(kappas), len(gammas)))
for i, k in enumerate(kappas):
    for j, g in enumerate(gammas):
        z[i, j] = signed_shadow(1, -1, d1, d2, g, k, mu).lambda_minus
fig2, ax2 = plt.subplots(figsize=(10, 4.8))
im = ax2.imshow(z, origin="lower", aspect="auto", extent=[gammas.min(), gammas.max(), kappas.min(), kappas.max()])
ax2.contour(gammas, kappas, z, levels=[0], linewidths=2)
ax2.set_xlabel("gamma")
ax2.set_ylabel("kappa")
ax2.set_title("lambda- phase map: zero contour is the admissibility horizon")
fig2.colorbar(im, ax=ax2, label="lambda-")
st.pyplot(fig2)

st.subheader("Signed matrix")
st.code(f"""s = sign(n1*n2) = {res.orientation}
D_signed = [[{d1 + gamma*res.orientation:.4f}, {kappa:.4f}],
            [{kappa:.4f}, {d2 + gamma*res.orientation:.4f}]]
""")
