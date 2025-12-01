"""Public API surface for optiseed.

Keep exports minimal and stable; prefer importing from submodules internally.
"""

from .strategies import greedy_farthest_sample, lhs_sample, sobol_sample

__all__ = ["sobol_sample", "lhs_sample", "greedy_farthest_sample"]
