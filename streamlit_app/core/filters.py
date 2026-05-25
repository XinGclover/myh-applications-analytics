from __future__ import annotations

import streamlit as st

try:
    from core.config import APPLICATION_LIMIT
except ImportError:
    from core.config import APPLICATION_LIMIT


def select_filter(label: str, options: list, key: str) -> str | int | None:
    """
    Render a sidebar selectbox and convert All
    into None for API query parameters.
    """
    selected = st.sidebar.selectbox(label, ["All", *options], key=key)
    return None if selected == "All" else selected


def get_filter_options(year_df, all_applications_df, providers_df) -> dict:
    """
    Build sidebar filter options from initial API data
    for years, locations, decisions, providers, and study forms.
    """
    year_options = []
    if not year_df.empty and "source_year" in year_df:
        year_options = sorted(year_df["source_year"].dropna().astype(int).unique().tolist(), reverse=True)

    region_options = []
    if not all_applications_df.empty and "lan" in all_applications_df:
        region_options = sorted(all_applications_df["lan"].dropna().unique().tolist())

    decision_options = []
    if not all_applications_df.empty and "decision_normalized" in all_applications_df:
        decision_options = sorted(all_applications_df["decision_normalized"].dropna().unique().tolist())

    provider_options = []
    if not providers_df.empty and "provider_name" in providers_df:
        provider_options = sorted(providers_df["provider_name"].dropna().unique().tolist())

    study_form_options = []
    if not all_applications_df.empty and "study_form_normalized" in all_applications_df:
        study_form_options = sorted(all_applications_df["study_form_normalized"].dropna().unique().tolist())

    return {
        "years": year_options,
        "regions": region_options,
        "decisions": decision_options,
        "providers": provider_options,
        "study_forms": study_form_options,
    }


def get_municipality_options(all_applications_df, selected_region: str | None) -> list:
    """
    Return municipality options, narrowed to the selected region
    when a region filter is active.
    """
    if all_applications_df.empty or "kommun" not in all_applications_df:
        return []

    municipality_df = all_applications_df
    if selected_region and "lan" in all_applications_df:
        municipality_df = municipality_df[municipality_df["lan"] == selected_region]

    return sorted(municipality_df["kommun"].dropna().unique().tolist())


def render_sidebar_filters(options: dict, all_applications_df) -> dict:
    """
    Render dashboard filters and return selected values
    using keys expected by the API.
    """
    st.sidebar.header("Filters")

    selected_year = select_filter("Year", options["years"], "year")
    selected_region = select_filter("Region", options["regions"], "region")

    municipality_options = get_municipality_options(
        all_applications_df,
        selected_region,
    )

    selected_municipality = select_filter(
        "Municipality",
        municipality_options,
        "municipality",
    )

    return {
        "year": selected_year,
        "region": selected_region,
        "municipality": selected_municipality,
        "decision": select_filter("Decision", options["decisions"], "decision"),
        "provider": select_filter("Provider", options["providers"], "provider"),
        "study_form": select_filter("Study form", options["study_forms"], "study_form"),
    }


def build_query_params(
    selected_filters: dict,
    allowed_keys: list[str],
    include_limit: bool = False,
) -> dict:
    """
    Build endpoint-specific query parameters
    from selected dashboard filters.
    """
    params = {}

    if include_limit:
        params["limit"] = APPLICATION_LIMIT

    for key in allowed_keys:
        value = selected_filters.get(key)

        if value is not None and value != "":
            params[key] = value

    return params
