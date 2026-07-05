#!/usr/bin/env python3
"""BC-CI II certified residual transport demo.

Generates deterministic finite-dimensional toy outputs for the companion package
to BC-CI II. This is not a physical simulation: u is not time, and transport is
only certified continuation along a declared parameter path.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CONFIG_DIR = ROOT / "configs"
DATA_DIR = ROOT / "data"
FIG_DIR = ROOT / "figures"

STATUS_COLORS = {
    "READOUT_CERTIFIED": "#2ca02c",
    "READOUT_BELOW_THRESHOLD": "#ff7f0e",
    "CHANNEL_MERGER": "#9467bd",
    "RANK_CHANGE": "#8c564b",
    "CERTIFICATE_RESET": "#d62728",
    "CHANNEL_CERTIFIED": "#1f77b4",
}


def scenario_values(name: str, u: float, tau: float) -> dict[str, float]:
    if name == "stable_channel":
        la, lb, residual = 2.0 + 0.10 * u, 0.2, 0.80 + 0.05 * math.sin(math.pi * u)
    elif name == "readout_below_threshold":
        la, lb, residual = 2.0 + 0.10 * u, 0.2, max(0.0, 1.0 - u)
    elif name == "channel_merger":
        la, lb, residual = 1.2 + abs(u - 0.5), 1.2 - abs(u - 0.5), 0.8
    elif name == "reset_interrupted":
        la, lb, residual = 2.0, (1.95 if 0.45 <= u <= 0.55 else 0.2), 0.7
    else:
        raise ValueError(f"unknown scenario: {name}")
    alpha = la - tau
    rho = abs(la - lb)
    return {"lambda_a": la, "lambda_b": lb, "alpha": alpha, "rho": rho, "g": min(alpha, rho), "residual_norm": residual}


def rank_above_threshold(la: float, lb: float, tau: float) -> int:
    return int(la > tau) + int(lb > tau)


def classify(v: dict[str, float], tau: float, eta: float, delta_read: float, expected_rank: int = 1) -> str:
    if v["rho"] <= eta:
        return "CHANNEL_MERGER"
    if rank_above_threshold(v["lambda_a"], v["lambda_b"], tau) != expected_rank:
        return "RANK_CHANGE"
    if v["g"] - eta <= 0:
        return "CERTIFICATE_RESET"
    return "READOUT_CERTIFIED" if v["residual_norm"] - delta_read > 0 else "READOUT_BELOW_THRESHOLD"


def sample_scenario(config: dict) -> dict:
    name = str(config["scenario"])
    tau = float(config["tau"])
    eta = float(config["eta"])
    delta_read = float(config["delta_read"])
    samples = int(config.get("samples", 101))
    points = []
    counts: dict[str, int] = {}
    for i in range(samples):
        u = i / (samples - 1)
        v = scenario_values(name, u, tau)
        status = classify(v, tau, eta, delta_read)
        counts[status] = counts.get(status, 0) + 1
        points.append({
            "u": round(u, 6),
            "lambda_a": round(v["lambda_a"], 6),
            "lambda_b": round(v["lambda_b"], 6),
            "g_a_tau": round(v["g"], 6),
            "spectral_margin": round(v["g"] - eta, 6),
            "residual_norm": round(v["residual_norm"], 6),
            "readout_margin": round(v["residual_norm"] - delta_read, 6),
            "status": status,
        })
    return {"scenario": name, "description": config.get("description", ""), "tau": tau, "eta": eta, "delta_read": delta_read, "points": points, "status_counts": counts}


def polyline(points: list[tuple[float, float]], x0: int, y0: int, w: int, h: int, ymin: float, ymax: float) -> str:
    out = []
    for u, y in points:
        x = x0 + u * w
        yy = y0 + h - (y - ymin) / (ymax - ymin) * h
        out.append(f"{x:.1f},{yy:.1f}")
    return " ".join(out)


def write_margin_svg(result: dict) -> None:
    name = str(result["scenario"])
    pts = result["points"]
    spec = [(float(p["u"]), float(p["spectral_margin"])) for p in pts]
    read = [(float(p["u"]), float(p["readout_margin"])) for p in pts]
    ys = [y for _, y in spec + read] + [0.0]
    ymin, ymax = min(ys) - 0.1, max(ys) + 0.1
    x0, y0, w, h = 60, 30, 620, 260
    zero_y = y0 + h - (0 - ymin) / (ymax - ymin) * h
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="760" height="380" viewBox="0 0 760 380">
  <rect width="760" height="380" fill="white"/>
  <text x="60" y="22" font-family="Arial" font-size="16">BC-CI II: {name}</text>
  <line x1="{x0}" y1="{y0+h}" x2="{x0+w}" y2="{y0+h}" stroke="black"/>
  <line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y0+h}" stroke="black"/>
  <line x1="{x0}" y1="{zero_y:.1f}" x2="{x0+w}" y2="{zero_y:.1f}" stroke="#777" stroke-dasharray="4 4"/>
  <polyline points="{polyline(spec, x0, y0, w, h, ymin, ymax)}" fill="none" stroke="#1f77b4" stroke-width="3"/>
  <polyline points="{polyline(read, x0, y0, w, h, ymin, ymax)}" fill="none" stroke="#d62728" stroke-width="3"/>
  <text x="60" y="335" font-family="Arial" font-size="13">blue: spectral margin g_a^tau(B(u))-eta</text>
  <text x="60" y="355" font-family="Arial" font-size="13">red: readout margin ||R_a(u)||-delta_read</text>
</svg>\n'''
    (FIG_DIR / f"{name}_margins.svg").write_text(svg, encoding="utf-8")


def write_status_timeline(results: list[dict]) -> None:
    width, row_h = 900, 42
    height = 80 + row_h * len(results)
    lines = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">', '<rect width="100%" height="100%" fill="white"/>', '<text x="40" y="30" font-family="Arial" font-size="18">BC-CI II status timeline</text>']
    for idx, res in enumerate(results):
        y = 60 + idx * row_h
        pts = res["points"]
        lines.append(f'<text x="40" y="{y+20}" font-family="Arial" font-size="13">{res["scenario"]}</text>')
        for i, p in enumerate(pts):
            x = 260 + i * (850 - 260) / max(1, len(pts) - 1)
            color = STATUS_COLORS.get(str(p["status"]), "#999")
            lines.append(f'<rect x="{x:.1f}" y="{y}" width="6" height="24" fill="{color}"/>')
    lines.append('</svg>')
    (FIG_DIR / "status_timeline.svg").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    DATA_DIR.mkdir(exist_ok=True)
    FIG_DIR.mkdir(exist_ok=True)
    results = []
    for config_path in sorted(CONFIG_DIR.glob("*.json")):
        result = sample_scenario(json.loads(config_path.read_text(encoding="utf-8")))
        results.append(result)
        write_margin_svg(result)
    (DATA_DIR / "demo_outputs.json").write_text(json.dumps(results, indent=2), encoding="utf-8")
    write_status_timeline(results)
    print(f"Wrote {DATA_DIR / 'demo_outputs.json'}")
    print(f"Wrote SVG figures to {FIG_DIR}")


if __name__ == "__main__":
    main()
