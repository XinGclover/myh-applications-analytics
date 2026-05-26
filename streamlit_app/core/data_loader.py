from core.api_client import load_dataframe, load_dataframe_with_error
from core.config import (
    APPLICATION_FILTER_KEYS,
    APPLICATIONS_ENDPOINT,
    PROVIDERS_ENDPOINT,
    STATS_BY_EDUCATION_AREA_FILTER_KEYS,
    STATS_BY_EDUCATION_AREA_ENDPOINT,
    STATS_BY_YEAR_FILTER_KEYS,
    STATS_BY_YEAR_ENDPOINT,
)
from core.filters import build_query_params


def load_initial_data():
    """
    Load unfiltered data needed to populate dashboard filters
    before user selections are applied.
    """
    all_applications_params = build_query_params(
        selected_filters={},
        allowed_keys=APPLICATION_FILTER_KEYS,
        include_limit=True,
    )

    year_stats, year_stats_error = load_dataframe_with_error(
        STATS_BY_YEAR_ENDPOINT,
        params=build_query_params(
            selected_filters={},
            allowed_keys=STATS_BY_YEAR_FILTER_KEYS,
        ),
    )

    return {
        "year_stats": year_stats,
        "year_stats_error": year_stats_error,
        "providers": load_dataframe(PROVIDERS_ENDPOINT),
        "all_applications": load_dataframe(
            APPLICATIONS_ENDPOINT,
            params=all_applications_params,
        ),
    }


def build_export_applications_params(selected_filters: dict) -> dict:
    """
    Build export query parameters from active dashboard filters
    without adding the table display limit.
    """
    return build_query_params(
        selected_filters=selected_filters,
        allowed_keys=APPLICATION_FILTER_KEYS,
        include_limit=False,
    )


def load_filtered_data(selected_filters: dict):
    """
    Load filtered applications and chart data
    for the main dashboard view.
    """
    year_stats, year_stats_error = load_dataframe_with_error(
        STATS_BY_YEAR_ENDPOINT,
        params=build_query_params(
            selected_filters,
            STATS_BY_YEAR_FILTER_KEYS,
        ),
    )

    return {
        "year_stats": year_stats,
        "year_stats_error": year_stats_error,
        "education_area_stats": load_dataframe(
            STATS_BY_EDUCATION_AREA_ENDPOINT,
            params=build_query_params(
                selected_filters,
                STATS_BY_EDUCATION_AREA_FILTER_KEYS,
            ),
        ),
        "applications": load_dataframe(
            APPLICATIONS_ENDPOINT,
            params=build_query_params(
                selected_filters,
                APPLICATION_FILTER_KEYS,
                include_limit=True,
            ),
        ),
    }
