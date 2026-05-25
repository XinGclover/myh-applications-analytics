from __future__ import annotations

import streamlit as st

from core.api_client import get_api_base_url, get_file, post_json
from core.config import (
    EXPORT_APPLICATIONS_ENDPOINT,
    EXPORT_STATS_BY_YEAR_ENDPOINT,
    REFRESH_ENDPOINT,
)
from core.data_loader import (
    build_export_applications_params,
    load_filtered_data,
    load_initial_data,
)
from core.filters import get_filter_options, render_sidebar_filters
from core.metrics import calculate_kpis, format_rate


st.title("MYH Applications Dashboard")
st.caption(f"API: {get_api_base_url()}")

initial_data = load_initial_data()
year_df = initial_data["year_stats"]
providers_df = initial_data["providers"]
all_applications_df = initial_data["all_applications"]

filter_options = get_filter_options(year_df, all_applications_df, providers_df)
selected_filters = render_sidebar_filters(filter_options, all_applications_df)

filtered_data = load_filtered_data(selected_filters)
year_df = filtered_data["year_stats"]
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
    st.subheader("Applications by year")
    if year_df.empty:
        st.info("No yearly statistics available.")
    else:
        chart_df = year_df.set_index("source_year")["total_applications"]
        st.bar_chart(chart_df)

with chart_cols[1]:
    st.subheader("Applications by education area")
    if education_area_df.empty:
        st.info("No education area statistics available.")
    else:
        top_areas_df = education_area_df.head(20).set_index("utbildningsomrade")[
            "total_applications"
        ]
        st.bar_chart(top_areas_df)

st.divider()

st.subheader("Filtered applications")
if applications_df.empty:
    st.info("No applications match the current filters.")
else:
    preferred_columns = [
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
    visible_columns = [
        column for column in preferred_columns if column in applications_df.columns
    ]
    st.dataframe(
        applications_df[visible_columns],
        use_container_width=True,
        hide_index=True,
    )

st.divider()


st.title("🛠️ Operations")
st.markdown(
    """
    Use the tools below to manage the curated dataset. 
    You can refresh the database to rebuild the dataset and export data for further analysis.
    """
)

st.divider()

st.subheader("🔄 Refresh database")
st.markdown(
    "Trigger the backend refresh endpoint to rebuild and reload the curated dataset."
)

if st.button("Refresh Database", type="primary"):
    with st.spinner("Refreshing database..."):
        refresh_result, refresh_error = post_json(REFRESH_ENDPOINT)

    if refresh_error:
        st.error(refresh_error)
    elif refresh_result:
        st.cache_data.clear()
        st.success(
            "Refresh completed: "
            f"status={refresh_result.get('status')}, "
            f"rows_inserted={refresh_result.get('rows_inserted')}, "
            f"validation_checks={refresh_result.get('validation_checks')}"
        )

st.divider()

st.subheader("📥 Export")
st.markdown(
    "Download the curated dataset or summary statistics as CSV for reporting and analysis."
)

export_applications_params = build_export_applications_params(selected_filters)

export_cols = st.columns(2)

with export_cols[0]:
    st.markdown("#### 📄 Export applications dataset")
    st.markdown("Download the filtered applications dataset as CSV.")

    if st.button("Export Applications CSV", type="primary"):
        with st.spinner("Preparing applications CSV..."):
            applications_csv, applications_export_error = get_file(
                EXPORT_APPLICATIONS_ENDPOINT,
                params=export_applications_params,
            )

        if applications_export_error:
            st.error(applications_export_error)
        elif applications_csv:
            st.download_button(
                "Download Applications CSV",
                data=applications_csv,
                file_name="applications.csv",
                mime="text/csv",
            )

with export_cols[1]:
    st.markdown("#### 📊 Export yearly statistics")
    st.markdown("Download yearly statistics as CSV.")

    if st.button("Export Stats By Year CSV", type="primary"):
        with st.spinner("Preparing yearly stats CSV..."):
            stats_csv, stats_export_error = get_file(EXPORT_STATS_BY_YEAR_ENDPOINT)

        if stats_export_error:
            st.error(stats_export_error)
        elif stats_csv:
            st.download_button(
                "Download Stats By Year CSV",
                data=stats_csv,
                file_name="stats_by_year.csv",
                mime="text/csv",
            )
