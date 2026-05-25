from __future__ import annotations

from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


APP_DIR = Path(__file__).resolve().parents[1]
NOTEBOOK_HTML_PATH = APP_DIR / "notebooks" / "part_2_curated_dataset.html"


st.title("Curated Dataset Notebook")
st.markdown(
    "This page displays the exported HTML version of the curated dataset notebook."
)

if NOTEBOOK_HTML_PATH.exists():
    components.html(
        NOTEBOOK_HTML_PATH.read_text(encoding="utf-8"),
        height=950,
        scrolling=True,
    )
else:
    st.warning(
        "Notebook preview is not available yet. Export the notebook to "
        "`notebooks/curated_dataset.html` first, then reload this page."
    )
