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
- Uses a `src/` layout; install dependencies and an editable build with:
  ```bash
  uv sync
  ```
- GUI (Streamlit) optional dependencies:
  ```bash
  uv sync --extra gui
  uv run streamlit run src/optiseed/gui/app.py
  ```
- Examples live under `examples/`:
  ```bash
  uv run python examples/sobol_demo.py
  ```
- Format/lint/test steps will be added as the codebase grows.
