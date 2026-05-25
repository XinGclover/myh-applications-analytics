# Data Pipeline

## Purpose

The data pipeline transforms raw MYH Excel files into one harmonized curated dataset used by PostgreSQL, FastAPI, and the Streamlit dashboard.

---

## Pipeline Overview

```text
Excel Files
    ↓
Load Data
    ↓
Clean Data
    ↓
Harmonize Columns
    ↓
Combine Years
    ↓
Enrich Dataset
    ↓
Validate Dataset
    ↓
Curated CSV
```

---

## Notebook and Reusable Pipeline

The project uses the same pipeline logic in two forms:

| Component | Purpose |
|---|---|
| Notebook | Exploration, inspection, and documentation |
| `src/myh_pipeline/` | Reusable execution for database loading and API refresh |

The notebook explains the cleaning and harmonization process step by step, while the reusable modules support automated execution.

---

## Source and Output

| Type | Location |
|---|---|
| Raw Excel files | `part_2/data/raw/` |
| Curated CSV output | `part_2/data/curated/curated_applications.csv` |

---

## Notebook Workflow

The notebook in `part_2/notebooks/` demonstrates:

| Step | Description |
|---|---|
| 1 | Inspect Excel files and sheets |
| 2 | Clean yearly datasets |
| 3 | Harmonize columns across years |
| 4 | Combine yearly dataframes |
| 5 | Add enrichment fields |
| 6 | Validate the curated dataset |
| 7 | Export the curated CSV |

The notebook acts both as data processing code and project documentation.

---

## Reusable Pipeline Modules

The reusable pipeline lives in:

```text
src/myh_pipeline/
```

Main pipeline entry point:

```text
build_curated_dataset()
```

### Main Modules

| Module | Responsibility |
|---|---|
| `load.py` | Read Excel files |
| `clean.py` | Apply initial cleaning |
| `harmonize.py` | Standardize columns across years |
| `enrich.py` | Add analysis-ready fields |
| `validate.py` | Create validation checks |
| `pipeline.py` | Coordinate the full process |

---

## Enrichment

The pipeline adds fields that simplify dashboard filtering and API queries.

Examples:

```text
decision_normalized
is_approved
study_form_normalized
sector_category
```

---

## Validation

Validation checks help confirm that the curated dataset is ready for PostgreSQL loading and API usage.

Examples include:

| Validation Goal | Example |
|---|---|
| Required fields exist | Missing critical columns |
| Consistent normalization | Decision values aligned |
| Database compatibility | Text fields fit schema limits |
| Data completeness | Important fields are not empty |

---

## API Refresh Process

The API exposes:

```text
POST /refresh
```

This reruns the reusable pipeline directly from the backend.

### Refresh Workflow

| Step | Action |
|---|---|
| 1 | Run `build_curated_dataset()` |
| 2 | Create validation summary |
| 3 | Truncate `curated.yh_applications` |
| 4 | Insert refreshed curated data |
| 5 | Return status and validation results |

This allows the database to be refreshed without manually rerunning the notebook.



