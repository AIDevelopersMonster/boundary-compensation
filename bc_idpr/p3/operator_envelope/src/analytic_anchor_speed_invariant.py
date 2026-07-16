#!/usr/bin/env python3
from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path

import numpy as np

ANCHOR = math.pi / 12
FD_STEPS = (1e-5, 5e-6)
MAXIMUM_LABEL = 6
TRAIN_MAXIMUM_LABEL = 4


def qn(n: int, theta: float) -> float:
    return 0.0 if n == 0 else math.sin(n * theta) / math.sin(theta)


def dlog_qn(n: int, theta: float) -> float:
    if n == 0:
        raise ValueError("[0]_q has no logarithmic derivative")
    return n / math.tan(n * theta) - 1.0 / math.tan(theta)


def qfac(n: int, theta: float) -> float:
    if n < 0:
        raise ValueError(n)
    out = 1.0
    for k in range(1, n + 1):
        out *= qn(k, theta)
    return out


def dlog_qfac(n: int, theta: float) ->