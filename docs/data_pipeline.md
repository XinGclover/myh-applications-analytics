# Data Pipeline

## Purpose

The data pipeline transforms raw MYH Excel files into one harmonized curated dataset.

The curated dataset is used by:

- PostgreSQL
- FastAPI
- Streamlit dashboard

---

## Main Idea

The project has two ways to run the same data logic:

```text
Notebook
    → used for explanation, inspection, and documentation

Pipeline modules
    → used for reusable execution, database loading, and API refresh
```

The notebook shows the data preparation process step by step.

The Python modules in `src/myh_pipeline/` contain the reusable version of the same logic.

---

## Source and Output

Raw Excel files are stored in:

```text
part_2/data/raw/
```

The curated output is stored in:

```text
part_2/data/curated/curated_applications.csv
```

---

## Notebook Process

The notebook in `part_2/notebooks/` is used to explain and inspect the pipeline.

It shows:

1. which Excel files are used
2. how sheets and columns are inspected
3. how yearly files are cleaned
4. how columns are harmonized across years
5. how the yearly dataframes are combined
6. which enrichment fields are added
7. how the final curated dataset is validated
8. how the curated CSV is exported

The notebook is useful because it makes the data decisions visible.

It is not only code execution, but also documentation of the cleaning and harmonization choices.

---

## Reusable Pipeline

The reusable pipeline code lives in:

```text
src/myh_pipeline/
```

The main entry point is:

```text
build_curated_dataset()
```

This function runs the full process:

```text
Load raw Excel files
    ↓
Clean each year
    ↓
Harmonize columns
    ↓
Combine all years
    ↓
Add enrichment fields
    ↓
Validate the result
    ↓
Return curated dataframe and validation summary
```

The important modules are:

```text
load.py          reads Excel files
clean.py         applies initial cleaning
harmonize.py     standardizes columns across years
enrich.py        adds analysis-ready fields
validate.py      creates validation checks
pipeline.py      coordinates the full process
```

---

## Enrichment

The pipeline adds fields that make the dataset easier to use in the API and dashboard.

Examples:

```text
decision_normalized
is_approved
study_form_normalized
sector_category
```

These fields avoid repeating the same transformation logic in every API query or dashboard chart.

---

## Validation

Validation checks are created before loading the dataset into PostgreSQL.

The validation step helps confirm that the curated dataset has the expected structure and values before it is used by the API.

Examples of validation goals:

```text
required columns exist
important fields are not empty
values are normalized consistently
text fields fit the planned database schema
```

---

## Database Loading

There are two database loading commands.

### First-time setup

```bash
python -m src.myh_db.bootstrap_db
```

This is used when setting up the project for the first time.

It can:

```text
create the database
create the tables
load the curated CSV
```

### Reload existing database

```bash
python -m src.myh_db.load_to_db
```

This is used when the database and tables already exist.

It reloads the curated CSV into the existing table.

---

## API Refresh Process

The API exposes:

```text
POST /refresh
```

This endpoint runs the reusable pipeline directly from the backend.

Refresh process:

```text
Call build_curated_dataset()
    ↓
Create a fresh curated dataframe
    ↓
Create validation summary
    ↓
Truncate curated.yh_applications
    ↓
Insert the refreshed data into PostgreSQL
    ↓
Return status, row count, and validation count
```

The refresh endpoint is useful when the source data or pipeline logic has changed and the database needs to be updated without manually running the notebook.



