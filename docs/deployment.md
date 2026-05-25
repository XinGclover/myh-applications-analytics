# Deployment

## Cloud Deployment

The project is deployed using managed cloud services.

### Deployment Overview

| Layer | Service |
|---|---|
| Frontend | Streamlit Community Cloud |
| Backend API | Render |
| Database | Neon PostgreSQL |

Live application:

```text
🔗 https://myh-applications-analytics.streamlit.app/
```

The Streamlit frontend communicates with the FastAPI backend hosted on Render, which connects to PostgreSQL hosted on Neon.

---

## Local Setup

### Python Version

| Requirement | Version |
|---|---|
| Python | 3.12 or newer |

Check installed version:

```bash
python --version
```

---

## Local Run Commands

### Environment Setup

| Step | Command |
|---|---|
| Create virtual environment | `python -m venv .venv` |
| Activate environment | `source .venv/bin/activate` |
| Install dependencies | `pip install -r requirements.txt` |

---

## Environment Variables

Create a `.env` file in the project root.

### Example

```bash
DB_NAME=myh_applications
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
DATABASE_URL=postgresql+psycopg2://postgres:your_password@localhost:5432/myh_applications
API_BASE_URL=http://localhost:8000
```

### Variable Usage

| Variable | Purpose |
|---|---|
| `DATABASE_URL` | PostgreSQL connection for SQLAlchemy |
| `API_BASE_URL` | FastAPI backend URL used by Streamlit |

---

## Database Loading

| Command | Purpose |
|---|---|
| `python -m src.myh_db.bootstrap_db` | Create database, tables, and load curated CSV |
| `python -m src.myh_db.load_to_db` | Reload curated CSV into existing tables |

---

## Notebook HTML Export

The notebook is exported to HTML so it can be displayed inside Streamlit as a read-only report.

### Export Command

```bash
python -m jupyter nbconvert \
  --to html \
  --output-dir streamlit_app/notebooks \
  part_2/notebooks/part_2_curated_dataset.ipynb
```

---

## Run Services

| Service | Command |
|---|---|
| FastAPI backend | `python -m uvicorn part_3.api.main:app --reload` |
| Streamlit frontend | `python -m streamlit run streamlit_app/app.py` |

---

## API Documentation

FastAPI automatically provides Swagger UI documentation:

```text
http://localhost:8000/docs
```
