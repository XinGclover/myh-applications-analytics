# Local Run Commands

This project runs locally with PostgreSQL, FastAPI, and Streamlit. It does not use `uv`; use normal `python -m ...` commands.

## 1. Create a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate
```

## 2. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

## 3. Configure Environment Variables

Create a `.env` file in the project root:

```bash
DB_NAME=myh_applications
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
DATABASE_URL=postgresql+psycopg2://postgres:your_password@localhost:5432/myh_applications
API_BASE_URL=http://localhost:8000
```

`DATABASE_URL` is used by SQLAlchemy. `API_BASE_URL` is used by the Streamlit app.

## 4. Create Database, Tables, and Load Data

Make sure PostgreSQL is running, then run:

```bash
python -m src.myh_db.bootstrap_db
```

This command:

- creates the PostgreSQL database if it does not exist
- runs `part_3/sql/create_tables.sql`
- loads `part_2/data/curated/curated_applications.csv`

## 5. Reload Only the Curated CSV

If the database and tables already exist, reload only the curated applications data:

```bash
python -m src.myh_db.load_to_db
```

This truncates `curated.yh_applications` and loads the curated CSV again.

## 6. Export Notebook to HTML

The Streamlit notebook page displays the notebook as a static HTML document instead of rendering the `.ipynb` file directly.

Reasons for converting the notebook to HTML:

- Streamlit does not natively render Jupyter notebooks cleanly.
- HTML export preserves:
  - markdown formatting
  - tables
  - charts
  - code cells
  - outputs
- The exported file loads faster and is easier to embed inside Streamlit.
- Users can view the notebook as a read-only report without requiring Jupyter installed.

Convert the notebook using:

```bash
python -m jupyter nbconvert \
  --to html \
  --output-dir streamlit_app/notebooks \
  part_2/notebooks/part_2_curated_dataset.ipynb
```

## 7. Run the FastAPI Backend

```bash
python -m uvicorn part_3.api.main:app --reload
```

API docs:

```text
http://localhost:8000/docs
```

## 8. Run the Streamlit App

Open a second terminal, activate the virtual environment, then run:

```bash
source .venv/bin/activate
python -m streamlit run streamlit_app/app.py
```

