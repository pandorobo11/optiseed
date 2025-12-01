# optiseed

Seed generation utilities for optimization workflows (e.g., Bayesian optimization). Provides space-filling initial designs, discrepancy evaluation, and both CLI/GUI front ends.

## Features (planned)
- Sobol, Latin Hypercube, and greedy farthest-point initial sampling
- Sample plotting for quick inspection
- Discrepancy/space-filling quality indices
- CLI and GUI entrypoints

## Getting started
- Requires Python 3.12+
- Install uv (https://github.com/astral-sh/uv) and run:
  ```bash
  uv sync
  ```

## Development
- Format/lint/test steps will be added as the codebase grows; for now you can run the default entrypoint:
  ```bash
  uv run python main.py
  ```
