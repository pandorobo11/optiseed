"""Example: generate and print Latin Hypercube samples."""

from __future__ import annotations

from optiseed import lhs_sample


def main() -> None:
    samples = lhs_sample(n=8, dims=2, seed=123, optimize="random-cd")
    print("Example LHS samples (first 5 rows):")
    print(samples[:5])


if __name__ == "__main__":
    main()
