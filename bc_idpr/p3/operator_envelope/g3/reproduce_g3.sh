#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-$(pwd)}"
cd "$ROOT"

export PYTHONHASHSEED=0
export SOURCE_DATE_EPOCH=1784226293
export FORCE_SOURCE_DATE=1

python --version
python - <<'PY'
import numpy, pytest, flint
print('numpy', numpy.__version__)
print('pytest', pytest.__version__)
print('python-flint', flint.__version__)
print('FLINT', flint.__FLINT_VERSION__)
PY
pdflatex --version | head -n 2

python -m pytest -q \
  bc_idpr/p3/operator_envelope/tests/test_finite_q6j_jet_calculus.py \
  bc_idpr/p3/operator_envelope/tests/test_g2r_interval_conditioning.py

mkdir -p generated
python bc_idpr/p3/operator_envelope/src/finite_q6j_jet_calculus.py \
  --output generated/finite_q6j_jet_calculus_certificate.json
python bc_idpr/p3/operator_envelope/src/g2r_interval_conditioning.py \
  --output generated/g2r_interval_conditioning_certificate.json

python - <<'PY'
import json
from pathlib import Path
base=Path('bc_idpr/p3/operator_envelope/outputs')
gen=Path('generated')
expected=json.loads((base/'finite_q6j_jet_calculus_certificate.json').read_text())
actual=json.loads((gen/'finite_q6j_jet_calculus_certificate.json').read_text())
assert expected == actual
expected=json.loads((base/'g2r_interval_conditioning_certificate.json').read_text())
actual=json.loads((gen/'g2r_interval_conditioning_certificate.json').read_text())
expected.pop('tests',None)
actual.pop('runtime_seconds',None)
assert expected == actual
print('canonical certificate equality: PASS')
PY

MAN=bc_idpr/p3/operator_envelope/manuscript/finite_q6j_jet_calculus_v0.1.1-reviewed
BUILD=generated/manuscript
rm -rf "$BUILD"
mkdir -p "$BUILD/sections" "$BUILD/supplementary"
cp "$MAN/main.tex" "$MAN/references.tex" "$MAN/finite_q6j_jet_calculus.bib" "$BUILD/"
cp "$MAN"/sections/*.tex "$BUILD/sections/"
cp "$MAN/supplementary/declared_carriers_283.json" "$BUILD/supplementary/"
(
  cd "$BUILD"
  for pass in 1 2 3 4; do
    pdflatex -interaction=nonstopmode -halt-on-error main.tex > "pass-${pass}.log"
  done
  sha256sum main.pdf
)
