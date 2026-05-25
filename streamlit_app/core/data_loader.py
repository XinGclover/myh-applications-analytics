from urllib.parse import quote

try:
    from core.api_client import load_dataframe
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
except ImportError:
    from core.api_client import load_dataframe
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

    return {
        "year_stats": load_dataframe(
            STATS_BY_YEAR_ENDPOINT,
            params=build_query_params(
                selected_filters={},
                allowed_keys=STATS_BY_YEAR_FILTER_KEYS,
            ),
        ),
        "providers": load_dataframe(PROVIDERS_ENDPOINT),
        "all_applications": load_dataframe(
            APPLICATIONS_ENDPOINT,
            params=all_applications_params,
        ),
    }


def load_provider_applications(provider_name: str):
    """
    Load application records for a selected provider
    using the provider drilldown endpoint.
    """
    provider_endpoint = f"{PROVIDERS_ENDPOINT}/{quote(provider_name, safe='')}/applications"
    return load_dataframe(provider_endpoint)


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
    return {
        "year_stats": load_dataframe(
            STATS_BY_YEAR_ENDPOINT,
            params=build_query_params(
                selected_filters,
                STATS_BY_YEAR_FILTER_KEYS,
            ),
        ),
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
