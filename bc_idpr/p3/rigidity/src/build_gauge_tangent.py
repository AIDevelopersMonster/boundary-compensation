#!/usr/bin/env python3
"""Exact trivalent-basis gauge tangent and rigidity quotient for the Ising anchor."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import sympy as sp

from build_pentagon_residuals import dump, f_table, instance, load, outs
from linearize_pentagon import exact_jacobian


def admissible_triples(fusion: dict[str, Any]) -> list[tuple[str, str