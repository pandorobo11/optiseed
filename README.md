# optiseed

Seed generation utilities for optimization workflows (e.g., Bayesian optimization). Provides space-filling initial designs, discrepancy evaluation, and both CLI/GUI front ends.

## Features (planned)
- Sobol, Latin Hypercube, and greedy farthest-point initial sampling  
  - Sobol: Sobol, I.M. (1967). On the distribution of points in a cube and the approximate evaluation of integrals. USSR Comput. Math. & Math. Phys.  
  - Latin Hypercube: McKay, M.D. et al. (1979). A Comparison of Three Methods for Selecting Values of Input Variables in the Analysis of Output from a Computer Code. Technometrics.  
  - Greedy farthest-point: Kamath, C. (2022). *Intelligent sampling for surrogate modeling, hyperparameter optimization, and data analysis*. Machine Learning with Applications, 9, 100373.
- LHS supports optional optimization (e.g., `random-cd`) via SciPy’s `LatinHypercube.optimize`.
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
  uv run python examples/lhs_demo.py
  ```
- Format/lint/test steps will be added as the codebase grows.
