import pandas as pd

from sqlalchemy import text

from src.myh_db.db import engine
from part_3.api.utils.response import dataframe_to_records


def get_providers() -> list[dict]:
    """
    Return providers with total and approved application counts
    for dashboard selection lists.
    """
    query = text("""
        SELECT
            utbildningsanordnare AS provider_name,
            COUNT(*) AS application_count,
            SUM(CASE WHEN is_approved = TRUE THEN 1 ELSE 0 END) AS approved_count
        FROM curated.yh_applications
        GROUP BY utbildningsanordnare
        ORDER BY utbildningsanordnare;
    """)

    df = pd.read_sql(query, engine)

    return dataframe_to_records(df)


def get_provider_applications(provider_name: str) -> list[dict]:
    """
    Return applications matching a provider name
    for provider drilldown views.
    """
    query = text("""
        SELECT *
        FROM curated.yh_applications
        WHERE utbildningsanordnare ILIKE :provider_name
        ORDER BY source_year DESC, diarienummer;
    """)

    params = {"provider_name": f"%{provider_name}%"}

    df = pd.read_sql(query, engine, params=params)
    print(df.isna().sum()[df.isna().sum() > 0])

    return dataframe_to_records(df)
