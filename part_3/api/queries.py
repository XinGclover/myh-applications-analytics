import pandas as pd
from sqlalchemy import text
from src.myh_db.db import engine


def get_applications(year=None, county=None, study_form=None, limit=100):
    query = """
        SELECT *
        FROM curated.yh_applications
        WHERE 1=1
    """

    params = {}

    if year:
        query += " AND source_year = :year"
        params["year"] = year

    if county:
        query += " AND county ILIKE :county"
        params["county"] = f"%{county}%"

    if study_form:
        query += " AND study_form ILIKE :study_form"
        params["study_form"] = f"%{study_form}%"

    query += " LIMIT :limit"
    params["limit"] = limit

    return pd.read_sql(text(query), engine, params=params).to_dict(orient="records")


def get_application_by_id(diarienummer):
    query = """
        SELECT *
        FROM curated.yh_applications
        WHERE TRIM(diarienummer) = TRIM(:diarienummer)
    """

    df = pd.read_sql(text(query), engine, params={"diarienummer": diarienummer})

    if df.empty:
        return None

    return df.iloc[0].to_dict()


def get_stats_by_year():
    query = """
        SELECT
            source_year,
            COUNT(*) AS application_count,
        FROM curated.yh_applications
        GROUP BY source_year
        ORDER BY source_year
    """

    return pd.read_sql(text(query), engine).to_dict(orient="records")
