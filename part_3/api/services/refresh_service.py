from sqlalchemy import text

from src.myh_db.db import engine
from src.myh_pipeline.pipeline import build_curated_dataset


def refresh_database() -> dict:
    curated_df, validation_summary = build_curated_dataset()

    with engine.begin() as conn:
        conn.execute(text("TRUNCATE TABLE curated.yh_applications RESTART IDENTITY;"))

        curated_df.to_sql(
            "yh_applications",
            conn,
            schema="curated",
            if_exists="append",
            index=False,
            method="multi",
        )

    return {
        "status": "success",
        "rows_inserted": len(curated_df),
        "validation_checks": len(validation_summary),
    }
