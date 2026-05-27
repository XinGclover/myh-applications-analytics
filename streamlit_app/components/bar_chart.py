import pandas as pd
import streamlit as st


def render_bar_chart(
    title: str,
    df: pd.DataFrame,
    index_column: str,
    value_column: str,
    empty_message: str,
    error_message: str | None = None,
    limit: int | None = None,
) -> None:
    st.subheader(title)

    if error_message:
        st.warning(error_message)
        return

    if df.empty:
        st.info(empty_message)
        return

    chart_df = df.copy()

    if limit:
        chart_df = chart_df.head(limit)

    chart_data = chart_df.set_index(index_column)[value_column]
    st.bar_chart(chart_data)