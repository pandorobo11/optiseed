"""Streamlit app for generating initial samples."""

from __future__ import annotations

from typing import Callable, Dict

import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

from optiseed.strategies import greedy_farthest_sample, lhs_sample, sobol_sample


def _method_registry() -> Dict[str, Callable[..., np.ndarray]]:
    return {
        "Sobol": sobol_sample,
        "Latin Hypercube": lhs_sample,
        "Greedy Farthest": greedy_farthest_sample,
    }


def _scatter_matrix(samples: np.ndarray) -> None:
    """Render scatter matrix of samples."""
    dims = samples.shape[1]
    columns = [f"x{i}" for i in range(1, dims + 1)]
    df = pd.DataFrame(samples, columns=columns)
    fig = px.scatter_matrix(df, dimensions=columns, height=600)
    st.plotly_chart(fig, width="stretch")


def main() -> None:
    st.set_page_config(page_title="Optiseed Sampler", layout="wide")
    st.title("Optiseed – Initial Sampling")
    st.caption("Generate initial designs with Sobol or Latin Hypercube and inspect them.")

    methods = _method_registry()
    method_name = st.selectbox("Seeding method", list(methods.keys()), index=0)
    n_samples = st.number_input("Number of samples", min_value=1, max_value=50000, value=128, step=1)
    dims = st.number_input("Dimensions", min_value=1, max_value=64, value=3, step=1)
    seed = 0
    use_seed = False

    with st.expander("Advanced options", expanded=False):
        scramble = st.checkbox("Scramble (Sobol only)", value=True)
        lhs_strength = st.number_input("LHS strength", min_value=1, max_value=3, value=1, step=1)
        lhs_optimize = st.selectbox("LHS optimize", [None, "random-cd"], index=1, format_func=lambda x: "None" if x is None else x)
        greedy_multiplier = st.number_input(
            "Greedy candidate multiplier", min_value=10, max_value=200, value=50, step=5
        )
        use_seed = st.checkbox("Use seed", value=False)
        seed = st.number_input("Seed (optional)", min_value=0, value=0, step=1)

    generate = st.button("Generate samples")

    if generate:
        sampler = methods[method_name]
        kwargs = {"n": n_samples, "dims": dims}
        if method_name == "Sobol":
            kwargs["scramble"] = scramble
            kwargs["seed"] = seed if use_seed else None
        elif method_name == "Latin Hypercube":
            kwargs["strength"] = lhs_strength
            kwargs["optimize"] = lhs_optimize
            kwargs["seed"] = seed if use_seed else None
        elif method_name == "Greedy Farthest":
            kwargs["candidate_multiplier"] = greedy_multiplier
            kwargs["seed"] = seed if use_seed else None

        try:
            samples = sampler(**kwargs)  # type: ignore[arg-type]
        except Exception as exc:  # noqa: BLE001
            st.error(f"Failed to generate samples: {exc}")
            return

        st.success(f"Generated {samples.shape[0]} samples in {samples.shape[1]} dimensions using {method_name}.")
        st.dataframe(
            pd.DataFrame(samples, columns=[f"x{i}" for i in range(1, dims + 1)]).head(),
            width="stretch",
        )
        _scatter_matrix(samples)


if __name__ == "__main__":
    main()
