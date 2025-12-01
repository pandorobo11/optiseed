"""Public API surface for optiseed.

Keep exports minimal and stable; prefer importing from submodules internally.
"""

from .strategies import sobol_sample

__all__ = ["sobol_sample"]
