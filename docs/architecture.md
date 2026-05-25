# Architecture

## Purpose

This project is a data engineering and analytics platform for Swedish YH application data from Myndigheten for yrkeshögskolan (MYH).

The system transforms historical Excel files into a curated PostgreSQL dataset, exposes the data through a FastAPI backend, and presents the results in a multipage Streamlit dashboard.

---

## High-Level Flow

```text
Excel Files
    ↓
Pandas Harmonization Pipeline
    ↓
Curated Dataset
    ↓
PostgreSQL Database
    ↓
FastAPI Backend
    ↓
Streamlit Dashboard
```

---

## Project Structure

```text
project_root/
├── docs/
├── part_2/
├── src/
├── part_3/api/
├── streamlit_app/
└── requirements.txt
```

---

## Main Components

### Data Preparation

- `part_2/`
  Contains notebook-based exploration and harmonization work.

- `part_2/data/raw/`
  Stores the original MYH Excel files.

- `part_2/data/curated/`
  Stores curated CSV outputs.

- `src/myh_pipeline/`
  Contains reusable pipeline modules for:
  - loading
  - cleaning
  - harmonization
  - enrichment
  - validation

---

### Database Layer

PostgreSQL stores the curated analytics dataset.

Main responsibilities:

- store harmonized application data
- support filtering and aggregation
- provide data for the API layer

Key files:

```text
src/myh_db/db.py
src/myh_db/bootstrap_db.py
src/myh_db/load_to_db.py
part_3/sql/create_tables.sql
```

---

### API Layer

The FastAPI backend lives in:

```text
part_3/api/
```

Structure:

```text
api/
├── routers/
├── services/
├── schemas/
└── main.py
```

Responsibilities:

- `routers/`
  Define HTTP endpoints.

- `services/`
  Contain SQL queries and business logic.

- `schemas/`
  Define Pydantic request and response models.

- `main.py`
  Creates the FastAPI application.

The API exposes:

- applications
- statistics
- providers
- export endpoints
- refresh operations

---

### Streamlit Layer

The frontend lives in:

```text
streamlit_app/
```

Structure:

```text
streamlit_app/
├── app.py
├── pages/
└── core/
```

Responsibilities:

- `pages/`
  Contains multipage Streamlit views.

- `core/`
  Contains reusable frontend logic such as:
  - API client functions
  - filters
  - metrics
  - configuration
  - data loading

The frontend communicates with FastAPI through HTTP requests.

---

## Design Choices

### Raw SQL Instead of ORM

The project uses:

- SQLAlchemy engine connections
- raw SQL queries
- Pydantic models

instead of ORM models.

This keeps SQL explicit and easier to debug and inspect during development.

### Thin Router Pattern

Routers are intentionally lightweight.

Business logic and SQL queries are placed in the service layer to keep the API structure modular and maintainable.

### Multipage Streamlit Structure

The Streamlit frontend is separated into pages and reusable core modules to avoid large monolithic dashboard files as the project grows.

---

## Local Development

For environment setup, database loading, notebook HTML export, and run commands, see:

```text
docs/deployment.md
```
```
