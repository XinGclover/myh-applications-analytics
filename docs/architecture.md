# Architecture

## Purpose

This project is a data engineering and analytics platform for Swedish YH application data from Myndigheten för yrkeshögskolan (MYH).

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

The FastAPI backend uses a lightweight layered structure.

| Module | Responsibility |
|---|---|
| `routers/` | API endpoints |
| `services/` | SQL queries and business logic |
| `schemas/` | Pydantic request and response models |
| `dependencies/security.py` | API key validation for protected endpoints |
| `core/config.py` | Environment-based API configuration |
| `main.py` | FastAPI application entry point |

Main API areas:

- applications
- statistics
- providers
- export
- notes
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

### Protected Operational Endpoints

The refresh endpoint is protected with an API key because it triggers a full database rebuild operation.

### Thin Router Pattern

Routers remain lightweight while query logic stays in the service layer.

### Component-Based Streamlit Structure

The frontend separates reusable Streamlit UI components from data loading and utility logic.

This keeps dashboard pages smaller and easier to maintain.

---

## Local Development

For environment setup, database loading, notebook HTML export, and run commands, see:

```text
docs/deployment.md
```
