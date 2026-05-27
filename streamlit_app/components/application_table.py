from __future__ import annotations

import pandas as pd
import streamlit as st


PREFERRED_APPLICATION_COLUMNS = [
    "source_year",
    "diarienummer",
    "utbildningsnamn",
    "utbildningsomrade",
    "decision_normalized",
    "is_approved",
    "kommun",
    "lan",
    "study_form_normalized",
    "utbildningsanordnare",
]


def render_application_table(applications_df: pd.DataFrame) -> str | None:
    st.subheader("Filtered applications")

    if applications_df.empty:
        st.info("No applications match the current filters.")
        return None

    visible_columns = [
        column
        for column in PREFERRED_APPLICATION_COLUMNS
        if column in applications_df.columns
    ]

    selected = st.dataframe(
        applications_df[visible_columns],
        use_container_width=True,
        hide_index=True,
        on_select="rerun",
        selection_mode="single-row",
    )

    selected_rows = selected.selection.rows

    if not selected_rows:
        return None

    selected_row = applications_df.iloc[selected_rows[0]]
    return selected_row["diarienummer"]