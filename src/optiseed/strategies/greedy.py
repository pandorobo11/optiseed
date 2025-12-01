"""Greedy farthest-point sampling strategy (maximin selection from a candidate set)."""

from __future__ import annotations

from typing import Sequence, Tuple

import numpy as np
from scipy.stats import qmc

Bounds = Sequence[Tuple[float, float]]


def greedy_farthest_sample(
    n: int,
    dims: int,
    *,
    candidate_multiplier: int = 50,
    seed: int | None = None,
    bounds: Bounds | None = None,
) -> np.ndarray:
    """
    Select samples greedily by maximizing the minimum distance to existing points.

    A Sobol candidate pool is generated, and points are selected one-by-one by
    choosing the farthest point from the already selected set (Euclidean metric).

    Args:
        n: Number of samples to select.
        dims: Dimensionality of the search space.
        candidate_multiplier: Multiplier for the candidate pool size relative to n.
            Larger values improve coverage but increase cost (O(n * candidates)).
        seed: Optional RNG seed for the Sobol candidate generator.
        bounds: Optional (low, high) bounds per dimension. If provided, length
            must equal dims.

    Returns:
        Array of shape (n, dims) with values in [0, 1] if no bounds are given,
        otherwise scaled to the provided bounds.

    Raises:
        ValueError: On invalid inputs or if candidate pool is too small.
    """
    if n <= 0:
        raise ValueError("n must be positive")
    if dims <= 0:
        raise ValueError("dims must be positive")
    if candidate_multiplier <= 0:
        raise ValueError("candidate_multiplier must be positive")
    if bounds is not None and len(bounds) != dims:
        raise ValueError("bounds length must match dims")

    candidate_size = max(n * candidate_multiplier, n + 1)
    sampler = qmc.Sobol(d=dims, scramble=True, seed=seed)
    candidates = sampler.random(candidate_size)

    if bounds is not None:
        lower, upper = zip(*bounds)
        lower_arr = np.array(lower, dtype=float)
        upper_arr = np.array(upper, dtype=float)
        if np.any(upper_arr <= lower_arr):
            raise ValueError("each upper bound must be greater than its lower bound")
        candidates = qmc.scale(candidates, lower_arr, upper_arr)

    if candidates.shape[0] < n:
        raise ValueError("candidate pool must be at least as large as n")

    selected = np.empty((n, dims), dtype=float)

    # Pick the first point deterministically from the candidate set.
    selected[0] = candidates[0]
    remaining = candidates[1:]

    # Track the minimum distance from each candidate to the selected set.
    min_dists = np.linalg.norm(remaining - selected[0], axis=1)

    for i in range(1, n):
        idx = int(np.argmax(min_dists))
        selected[i] = remaining[idx]

        # Update distances after adding the new point.
        new_dists = np.linalg.norm(remaining - selected[i], axis=1)
        min_dists = np.minimum(min_dists, new_dists)

    return selected
