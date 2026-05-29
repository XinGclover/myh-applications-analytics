import pandas as pd
from sqlalchemy import text

from src.myh_db.db import engine
from part_3.api.utils.response import dataframe_to_records


def get_applications(
    year: int | None = None,
    decision: str | None = None,
    region: str | None = None,
    municipality: str | None = None,
    provider: str | None = None,
    study_form: str | None = None,
    limit: int = 100,
) -> list[dict]:
    """
    Return filtered application records from the curated dataset.
    Supports dashboard tables and export queries.
    """
    query = """
        SELECT
            source_year,
            application_id,
            education_name,
            education_area,
            decision,
            decision_normalized,
            is_approved,
            municipality,
            region,
            study_form,
            study_form_normalized,
            provider_name
        FROM curated.yh_applications
        WHERE 1 = 1
    """

    params = {}

    if year:
        query += " AND source_year = :year"
        params["year"] = year

    if decision:
        query += " AND decision_normalized ILIKE :decision"
        params["decision"] = decision

    if region:
        query += " AND region ILIKE :region"
        params["region"] = f"%{region}%"

    if municipality:
        query += " AND municipality ILIKE :municipality"
        params["municipality"] = f"%{municipality}%"

    if provider:
        query += " AND provider_name ILIKE :provider"
        params["provider"] = f"%{provider}%"

    if study_form:
        query += " AND study_form_normalized ILIKE :study_form"
        params["study_form"] = study_form

    query += " ORDER BY source_year DESC LIMIT :limit"
    params["limit"] = limit

    df = pd.read_sql(text(query), engine, params=params)
    return dataframe_to_records(df)


def get_application_by_id(application_id: str) -> dict | None:
    """
    Return one application record by application ID
    or None when no match exists.
    """
    query = text("""
        SELECT
            source_year,
            application_id,
            education_name,
            education_area,
            decision,
            decision_normalized,
            is_approved,
            municipality,
            region,
            study_form,
            study_form_normalized,
            provider_name
        FROM curated.yh_applications
        WHERE application_id = :application_id
        LIMIT 1;
    """)

    with engine.begin() as conn:
        result = (
            conn.execute(
                query,
                {"application_id": application_id},
            )
            .mappings()
            .first()
        )

    if not result:
        return None

    return dict(result)


def application_exists(application_id: str) -> bool:
    """
    Return True when an application with the given ID exists
    in the curated dataset, otherwise False.
    """
    query = text("""
        SELECT 1
        FROM curated.yh_applications
        WHERE application_id = :application_id
        LIMIT 1;
    """)

    with engine.begin() as conn:
        result = conn.execute(
            query,
            {"application_id": application_id},
        ).first()

    return result is not None
