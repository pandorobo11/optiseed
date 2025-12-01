"""Example: generate and print Sobol samples."""

from __future__ import annotations

from optiseed import sobol_sample


def main() -> None:
    samples = sobol_sample(n=8, dims=2, seed=123)
    print("Example Sobol samples (first 5 rows):")
    print(samples[:5])


if __name__ == "__main__":
    main()
