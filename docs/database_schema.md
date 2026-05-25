# Database Schema

## Purpose

PostgreSQL stores the curated MYH applications dataset used by the FastAPI backend and Streamlit dashboard.

The schema is defined in:

```text
part_3/sql/create_tables.sql
```

The project uses:

- SQLAlchemy engine connections
- raw SQL queries
- PostgreSQL

---

## Schema

The database uses the `curated` schema:

```sql
CREATE SCHEMA IF NOT EXISTS curated;
```

Main tables:

```text
curated.yh_applications
curated.application_notes
```

---

## `curated.yh_applications`

This is the main curated dataset table.

Each row represents one harmonized YH application record from the MYH Excel files.

The table supports:

- filtering
- statistics
- exports
- dashboard visualizations

---

## `curated.application_notes`

This table stores user notes connected to applications.

The notes table is separated from the curated dataset so annotations do not modify the original harmonized data.

---

## Database Loading

Database setup and loading are handled by:

```text
src/myh_db/bootstrap_db.py
src/myh_db/load_to_db.py
```

### First-time setup

Creates the database, creates tables, and loads the curated CSV:

```bash
python -m src.myh_db.bootstrap_db
```

### Reload curated data only

Loads the curated CSV into existing tables:

```bash
python -m src.myh_db.load_to_db
```

---

## Query Access

The FastAPI service layer queries PostgreSQL directly with raw SQL.

Examples:

```text
part_3/api/services/application_service.py
part_3/api/services/stats_service.py
```

This keeps SQL queries explicit and easy to inspect during development.