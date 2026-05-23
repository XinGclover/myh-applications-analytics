import pandas as pd
from sqlalchemy import text

from src.myh_db.db import engine


def get_stats_by_year() -> list[dict]:
    query = """
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
        GROUP BY source_year
        ORDER BY source_year;
    """

    df = pd.read_sql(text(query), engine)
    return df.to_dict(orient="records")


def get_stats_by_education_area() -> list[dict]:
    query = """
        SELECT
            utbildningsomrade,
            COUNT(*) AS total_applications,
            SUM(CASE WHEN is_approved THEN 1 ELSE 0 END) AS approved_applications,
            ROUND(
                SUM(CASE WHEN is_approved THEN 1 ELSE 0 END)::numeric
                / COUNT(*) * 100,
                2
            ) AS approval_rate_percent
        FROM curated.yh_applications
        GROUP BY utbildningsomrade
        ORDER BY total_applications DESC;
    """

    df = pd.read_sql(text(query), engine)
    return df.to_dict(orient="records")
