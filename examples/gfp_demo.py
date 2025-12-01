"""Example: generate and print greedy farthest-point samples."""

from __future__ import annotations

from optiseed import greedy_farthest_sample


def main() -> None:
    samples = greedy_farthest_sample(n=8, dims=2, seed=123, candidate_multiplier=50)
    print("Example Greedy Farthest samples (first 5 rows):")
    print(samples[:5])


if __name__ == "__main__":
    main()
