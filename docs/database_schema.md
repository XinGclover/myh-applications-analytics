# Database Schema

## Purpose

PostgreSQL stores the curated MYH applications dataset used by the FastAPI backend and Streamlit dashboard.

The schema is defined in:

```text
part_3/sql/create_tables.sql
```

The project uses:

- PostgreSQL
- SQLAlchemy engine connections
- raw SQL queries

---

## Database Structure

Schema:

```sql
CREATE SCHEMA IF NOT EXISTS curated;
```

### Main Tables

| Table | Purpose |
|---|---|
| `curated.yh_applications` | Store harmonized MYH application records |
| `curated.application_notes` | Store user notes linked to applications |

---

## `curated.yh_applications`

Main curated dataset table.

Each row represents one harmonized YH application record from the MYH Excel files.

### Main Usage

| Usage | Description |
|---|---|
| Filtering | Dashboard and API filters |
| Statistics | Aggregated charts and KPIs |
| Export | CSV export endpoints |
| Visualization | Streamlit dashboard tables and charts |

---

## `curated.application_notes`

Stores user-created notes connected to applications.

The notes table is separated from the curated dataset so annotations do not modify the original harmonized source data.

---

## Database Loading

Database setup and loading are handled by:

```text
src/myh_db/bootstrap_db.py
src/myh_db/load_to_db.py
```

### Loading Commands

| Command | Purpose |
|---|---|
| `python -m src.myh_db.bootstrap_db` | Create database, tables, and load curated CSV |
| `python -m src.myh_db.load_to_db` | Reload curated CSV into existing tables |

---

## Query Access

The FastAPI service layer queries PostgreSQL directly with raw SQL.

Examples:

```text
part_3/api/services/application_service.py
part_3/api/services/stats_service.py
```

This keeps SQL queries explicit and easy to inspect during development.