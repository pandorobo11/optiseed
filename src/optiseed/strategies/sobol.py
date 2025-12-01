"""Sobol sequence sampling strategy."""

from __future__ import annotations

from typing import Sequence, Tuple

import numpy as np
from scipy.stats import qmc


Bounds = Sequence[Tuple[float, float]]


def sobol_sample(
    n: int,
    dims: int,
    *,
    scramble: bool = True,
    seed: int | None = None,
    bounds: Bounds | None = None,
) -> np.ndarray:
    """
    Generate Sobol quasi-random samples.

    Args:
        n: Number of samples to draw.
        dims: Dimensionality of the search space.
        scramble: Whether to use Owen scrambling for better uniformity.
        seed: Optional RNG seed for reproducibility when scrambling.
        bounds: Optional sequence of (low, high) bounds per dimension. If
            provided, its length must equal `dims`.

    Returns:
        Array of shape (n, dims) with values in [0, 1] if no bounds are given,
        otherwise scaled to the provided bounds.

    Example:
        >>> sobol_sample(n=4, dims=2, seed=0).shape
        (4, 2)
    """
    if n <= 0:
        raise ValueError("n must be positive")
    if dims <= 0:
        raise ValueError("dims must be positive")
    if bounds is not None and len(bounds) != dims:
        raise ValueError("bounds length must match dims")

    sampler = qmc.Sobol(d=dims, scramble=scramble, seed=seed)
    samples = sampler.random(n)

    if bounds is None:
        return samples

    lower, upper = zip(*bounds)
    lower_arr = np.array(lower, dtype=float)
    upper_arr = np.array(upper, dtype=float)
    if np.any(upper_arr <= lower_arr):
        raise ValueError("each upper bound must be greater than its lower bound")

    return qmc.scale(samples, lower_arr, upper_arr)
