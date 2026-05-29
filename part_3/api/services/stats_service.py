import pandas as pd
from sqlalchemy import text

from src.myh_db.db import engine
from part_3.api.utils.response import dataframe_to_records


def build_stats_filters(
    year=None,
    region=None,
    municipality=None,
    decision=None,
    provider=None,
    study_form=None,
) -> tuple[str, dict]:
    """
    Build reusable SQL filter clauses
    for statistics endpoints.
    """
    filters = []
    params = {}

    if year:
        filters.append("source_year = :year")
        params["year"] = year

    if region:
        filters.append("region ILIKE :region")
        params["region"] = f"%{region}%"

    if municipality:
        filters.append("municipality ILIKE :municipality")
        params["municipality"] = f"%{municipality}%"

    if decision:
        filters.append("decision_normalized ILIKE :decision")
        params["decision"] = f"%{decision}%"

    if provider:
        filters.append("provider_name ILIKE :provider")
        params["provider"] = f"%{provider}%"

    if study_form:
        filters.append("study_form_normalized ILIKE :study_form")
        params["study_form"] = f"%{study_form}%"

    where_clause = ""
    if filters:
        where_clause = "WHERE " + " AND ".join(filters)

    return where_clause, params


def get_stats_by_year(
    region=None,
    municipality=None,
    decision=None,
    provider=None,
    study_form=None,
) -> list[dict]:
    """
    Return yearly application statistics
    with approval counts and rates.
    """
    where_clause, params = build_stats_filters(
        region=region,
        municipality=municipality,
        decision=decision,
        provider=provider,
        study_form=study_form,
    )

    query = f"""
        SELECT
            source_year,
            COUNT(*) AS total_applications,
            SUM(CASE WHEN is_approved THEN 1 ELSE 0 END) AS approved_applications,
            ROUND(
                SUM(CASE WHEN is_approved THEN 1 ELSE 0 END)::numeric
                / COUNT(*) * 100,
                2
            ) AS approval_rate_percent
        FROM curated.yh_applications
        {where_clause}
        GROUP BY source_year
        ORDER BY source_year;
    """

    df = pd.read_sql(text(query), engine, params=params)
    return dataframe_to_records(df)

def get_stats_by_education_area(
    year=None,
    region=None,
    municipality=None,
    decision=None,
    provider=None,
    study_form=None,
) -> list[dict]:
    """
    Return education-area statistics
    filtered by active dashboard selections.
    """
    where_clause, params = build_stats_filters(
        year=year,
        region=region,
        municipality=municipality,
        decision=decision,
        provider=provider,
        study_form=study_form,
    )

    query = f"""
        SELECT
            education_area,
            COUNT(*) AS total_applications,
            SUM(CASE WHEN is_approved THEN 1 ELSE 0 END) AS approved_applications,
            ROUND(
                SUM(CASE WHEN is_approved THEN 1 ELSE 0 END)::numeric
                / COUNT(*) * 100,
                2
            ) AS approval_rate_percent
        FROM curated.yh_applications
        {where_clause}
        GROUP BY education_area
        ORDER BY total_applications DESC;
    """

    df = pd.read_sql(text(query), engine, params=params)
    return dataframe_to_records(df)
