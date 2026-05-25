from pathlib import Path

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from src.myh_db.db import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT
from src.myh_db.load_to_db import load_data


PROJECT_ROOT = Path(__file__).resolve().parents[2]
SQL_PATH = PROJECT_ROOT / "part_3" / "sql" / "create_tables.sql"


def create_database_if_not_exists():
    """
    Create the configured PostgreSQL database
    when it is not already present.
    """
    con = psycopg2.connect(
        dbname="postgres",
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
    )
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    with con.cursor() as cursor:
        cursor.execute(
            "SELECT 1 FROM pg_database WHERE datname = %s;",
            (DB_NAME,),
        )
        exists = cursor.fetchone()

        if not exists:
            cursor.execute(f'CREATE DATABASE "{DB_NAME}";')
            print(f"Database created: {DB_NAME}")
        else:
            print(f"Database already exists: {DB_NAME}")

    con.close()


def create_tables():
    """
    Apply the curated database schema
    from the project SQL file.
    """
    con = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
    )

    with con:
        with con.cursor() as cursor:
            sql = SQL_PATH.read_text(encoding="utf-8")
            cursor.execute(sql)

    con.close()
    print("Tables created successfully.")


if __name__ == "__main__":
    create_database_if_not_exists()
    create_tables()
    load_data()
