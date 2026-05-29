# Data Pipeline

## Purpose

The data pipeline transforms raw MYH Excel files into one English curated dataset used by PostgreSQL, FastAPI, Streamlit, and CSV exports.

---

## Pipeline Overview

```text
Excel Files
    ↓
Load Data
    ↓
Clean Data
    ↓
Harmonize Swedish Columns
    ↓
Combine Years
    ↓
Enrich Dataset
    ↓
Translate Columns
    ↓
Validate Dataset
    ↓
Curated CSV / PostgreSQL Load
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
| 3 | Harmonize columns across years using Swedish-normalized names |
| 4 | Combine yearly dataframes |
| 5 | Add enrichment fields |
| 6 | Translate columns into the English curated schema |
| 7 | Validate the curated dataset |
| 8 | Export the curated CSV |

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
| `harmonize.py` | Standardize yearly files into Swedish-normalized columns |
| `enrich.py` | Add analysis-ready fields |
| `translate_columns.py` | Translate Swedish-normalized columns into English curated analytics fields |
| `validate.py` | Create validation checks |
| `pipeline.py` | Coordinate the full process |

---

## Column Translation Layer

The project keeps a clear separation between source fields, intermediate fields, and final analytics fields.

| Layer | Purpose |
|---|---|
| Raw Excel fields | Preserve the original MYH source layout and Swedish names |
| Swedish-normalized harmonized fields | Support traceability, debugging, and cross-year harmonization |
| English curated fields | Provide stable names for PostgreSQL, FastAPI, Streamlit, exports, and analytics |

Important examples:

| Source / Harmonized Field | English Curated Field |
|---|---|
| `diarienummer` | `application_id` |
| `utbildningsnamn` | `education_name` |
| `utbildningsomrade` | `education_area` |
| `beslut` | `decision` |
| `kommun` | `municipality` |
| `län` / `lan` | `region` |
| `yh_poang` | `yh_credits` |
| `studieform` | `study_form` |
| `studietakt_procent` | `study_pace_percent` |
| `utbildningsanordnare` | `provider_name` |
| `huvudmannatyp` | `provider_type` |
| `sun5_inriktning` | `sun5_field` |
| `sun5_inriktning_namn` | `sun5_field_name` |
| `seqf_niva` | `seqf_level` |
| `smalt_yrkesomrade` | `narrow_occupational_area` |

The Swedish field `län` describes a Swedish regional administrative area. The curated schema uses `region` because it matches the dashboard language and avoids confusing this value with a national field.

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

