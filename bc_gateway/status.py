"""Certification status labels."""

from enum import Enum


class Status(str, Enum):
    """Finite-dimensional certification statuses."""

    CERTIFIED_STABLE = "CERTIFIED_STABLE"
    MARGIN_LOW = "MARGIN_LOW"
    CERTIFICATE_RESET = "CERTIFICATE_RESET"
    INCONCLUSIVE = "INCONCLUSIVE"
