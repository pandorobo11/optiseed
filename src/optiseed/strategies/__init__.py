"""Strategies for generating initial samples."""

from .lhs import lhs_sample
from .sobol import sobol_sample

__all__ = ["sobol_sample", "lhs_sample"]
