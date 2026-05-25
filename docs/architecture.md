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

| Layer | Location | Responsibility |
|---|---|---|
| Data Preparation | `part_2/` | Notebook-based exploration and harmonization |
| Pipeline Modules | `src/myh_pipeline/` | Reusable loading, cleaning, enrichment, and validation logic |
| Database | PostgreSQL | Store curated application data |
| Database Utilities | `src/myh_db/` | Database setup and loading scripts |
| API Backend | `part_3/api/` | FastAPI endpoints and business logic |
| Frontend | `streamlit_app/` | Multipage Streamlit dashboard |
| Documentation | `docs/` | Technical project documentation |

---

## API Layer

The FastAPI backend uses a lightweight layered structure:

| Module | Responsibility |
|---|---|
| `routers/` | API endpoints |
| `services/` | SQL queries and business logic |
| `schemas/` | Pydantic request and response models |
| `main.py` | FastAPI application entry point |

Main API areas:

- applications
- statistics
- providers
- export
- refresh operations

---

## Streamlit Layer

| Module | Responsibility |
|---|---|
| `app.py` | Streamlit entry point |
| `pages/` | User-facing pages |
| `core/api_client.py` | API communication |
| `core/data_loader.py` | Dashboard data loading |
| `core/filters.py` | Sidebar filters |
| `core/metrics.py` | KPI calculations |

The frontend communicates with FastAPI through HTTP requests.

---

## Design Choices

### Raw SQL Instead of ORM

The project uses:

- SQLAlchemy engine connections
- raw SQL queries
- Pydantic models

instead of ORM models.

This keeps SQL explicit and easier to inspect during development.

### Thin Router Pattern

Routers remain lightweight while query logic stays in the service layer.

### Multipage Streamlit Structure

Frontend logic is separated into reusable modules to avoid large monolithic dashboard files.

---

## Local Development

For environment setup, database loading, notebook HTML export, and run commands, see:

```text
docs/deployment.md
```
