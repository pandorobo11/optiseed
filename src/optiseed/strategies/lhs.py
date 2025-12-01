"""Latin Hypercube sampling strategy."""

from __future__ import annotations

from typing import Sequence, Tuple

import numpy as np
from scipy.stats import qmc

Bounds = Sequence[Tuple[float, float]]


def lhs_sample(
    n: int,
    dims: int,
    *,
    strength: int = 1,
    optimize: str | None = "random-cd",
    seed: int | None = None,
    bounds: Bounds | None = None,
) -> np.ndarray:
    """
    Generate Latin Hypercube samples.

    Args:
        n: Number of samples to draw.
        dims: Dimensionality of the search space.
        strength: Sample strength (1 = standard LHS). See scipy.stats.qmc docs.
        optimize: Optional optimization method name for space-filling improvement
            (e.g., "random-cd"). Passed to scipy.stats.qmc.LatinHypercube via the
            constructor.
        seed: Optional RNG seed for reproducibility.
        bounds: Optional sequence of (low, high) bounds per dimension. If
            provided, its length must equal `dims`.

    Returns:
        Array of shape (n, dims) with values in [0, 1] if no bounds are given,
        otherwise scaled to the provided bounds.

    Example:
        >>> lhs_sample(n=4, dims=2, seed=0).shape
        (4, 2)
    """
    if n <= 0:
        raise ValueError("n must be positive")
    if dims <= 0:
        raise ValueError("dims must be positive")
    if bounds is not None and len(bounds) != dims:
        raise ValueError("bounds length must match dims")

    sampler = qmc.LatinHypercube(
        d=dims,
        strength=strength,
        seed=seed,
        optimization=optimize,  # type: ignore[arg-type]
    )
    samples = sampler.random(n)

    if bounds is None:
        return samples

    lower, upper = zip(*bounds)
    lower_arr = np.array(lower, dtype=float)
    upper_arr = np.array(upper, dtype=float)
    if np.any(upper_arr <= lower_arr):
        raise ValueError("each upper bound must be greater than its lower bound")

    return qmc.scale(samples, lower_arr, upper_arr)
