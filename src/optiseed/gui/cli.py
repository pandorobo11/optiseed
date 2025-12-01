"""CLI entrypoint to launch the Streamlit GUI."""

from __future__ import annotations

import sys
from pathlib import Path

from streamlit.web import cli as stcli


def main() -> None:
    script_path = Path(__file__).with_name("app.py")
    sys.argv = ["streamlit", "run", str(script_path)]
    sys.exit(stcli.main())


if __name__ == "__main__":
    main()
