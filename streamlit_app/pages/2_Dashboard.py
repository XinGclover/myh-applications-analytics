from __future__ import annotations

import streamlit as st

from core.api_client import (
    get_api_base_url,
)
from core.config import (
    EXPORT_APPLICATIONS_ENDPOINT,
    EXPORT_STATS_BY_YEAR_ENDPOINT,
)
from core.data_loader import (
    build_export_applications_params,
    load_filtered_data,
    load_initial_data,
)
from core.filters import get_filter_options, render_sidebar_filters
from core.metrics import calculate_kpis, format_rate
from components.export_button import render_export_button
from components.refresh_section import render_refresh_section
from components.application_note import render_application_notes
from components.application_table import render_application_table
from components.bar_chart import render_bar_chart


st.title("MYH Applications Dashboard")
st.caption(f"API: {get_api_base_url()}")

with st.spinner("Loading dashboard filters..."):
    initial_data = load_initial_data()

year_df = initial_data["year_stats"]
providers_df = initial_data["providers"]
all_applications_df = initial_data["all_applications"]

filter_options = get_filter_options(year_df, all_applications_df, providers_df)
selected_filters = render_sidebar_filters(filter_options, all_applications_df)

with st.spinner("Loading dashboard data..."):
    filtered_data = load_filtered_data(selected_filters)

year_df = filtered_data["year_stats"]
year_stats_error = filtered_data["year_stats_error"]
education_area_df = filtered_data["education_area_stats"]
applications_df = filtered_data["applications"]

kpis = calculate_kpis(applications_df)

kpi_cols = st.columns(4)
kpi_cols[0].metric(
    "Filtered applications",
    f"{kpis['total_applications']:,}",
)
kpi_cols[1].metric("Approved applications", f"{kpis['approved_applications']:,}")
kpi_cols[2].metric("Approval rate", format_rate(kpis["approval_rate"]))
kpi_cols[3].metric("Providers count", f"{kpis['providers_count']:,}")

st.divider()

chart_cols = st.columns(2)

with chart_cols[0]:
    render_bar_chart(
        title="Applications by year",
        df=year_df,
        index_column="source_year",
        value_column="total_applications",
        empty_message="No yearly statistics available.",
        error_message=(
            "Yearly statistics are temporarily unavailable. Please refresh the page."
            if year_stats_error
            else None
        ),
    )

with chart_cols[1]:
    render_bar_chart(
        title="Applications by education area",
        df=education_area_df,
        index_column="education_area",
        value_column="total_applications",
        empty_message="No education area statistics available.",
        limit=20,
    )

st.divider()

selected_application_id = render_application_table(applications_df)

if selected_application_id:
    st.divider()
    render_application_notes(selected_application_id)


st.divider()


st.title("🛠️ Operations")
st.markdown(
    """
    Use the tools below to manage the curated dataset. 
    You can refresh the database to rebuild the dataset and export data for further analysis.
    """
)

st.divider()

render_refresh_section()

st.divider()

st.subheader("📥 Export")
st.markdown(
    "Download the curated dataset or summary statistics as CSV for reporting and analysis."
)

export_applications_params = build_export_applications_params(selected_filters)

export_cols = st.columns(2)

export_cols = st.columns(2)

with export_cols[0]:
    render_export_button(
        title="📄 Export applications dataset",
        description="Download the filtered applications dataset as CSV.",
        button_label="Export Applications CSV",
        endpoint=EXPORT_APPLICATIONS_ENDPOINT,
        file_name="applications.csv",
        params=export_applications_params,
    )

with export_cols[1]:
    render_export_button(
        title="📊 Export yearly statistics",
        description="Download yearly statistics as CSV.",
        button_label="Export Stats By Year CSV",
        endpoint=EXPORT_STATS_BY_YEAR_ENDPOINT,
        file_name="stats_by_year.csv",
    )
