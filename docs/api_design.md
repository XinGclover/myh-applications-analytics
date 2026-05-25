# API Design

## Purpose

The FastAPI backend exposes the curated MYH applications dataset to dashboard users and other consumers. It provides record browsing, filtering, provider drilldowns, aggregated statistics, CSV exports, notes, and an operational refresh endpoint.

The API code lives in `part_3/api/`.

## Structure

```text
part_3/api/
├── main.py
├── routers/
├── services/
├── schemas/
└── utils/
```

Responsibilities:

- `main.py` creates the FastAPI app and includes routers.
- `routers/` defines HTTP endpoints and request parameters.
- `services/` contains database query logic and business logic.
- `schemas/` contains Pydantic models for validation and response shape.
- `utils/response.py` contains shared response helpers.

## Design Choices

The API intentionally uses SQLAlchemy engine connections and raw SQL instead of ORM models.

This keeps query behavior explicit and makes the project easier to inspect while learning and debugging:

- SQL is visible in service functions.
- Filters are built directly from API query parameters.
- Aggregation queries are easy to compare with database output.
- Pydantic models still define the API contract.

## Main Endpoint Groups

### Applications

Defined in `part_3/api/routers/application_router.py`.

Examples:

```text
GET /applications
GET /applications/{diarienummer}
```

Supported `/applications` filters include:

```text
year
decision
region
municipality
provider
study_form
limit
```

Example:

```bash
curl "http://localhost:8000/applications?year=2025&decision=approved&limit=20"
```

### Providers

Defined in `part_3/api/routers/provider_router.py`.

Examples:

```text
GET /providers
GET /providers/{provider_name}/applications
```

Example:

```bash
curl "http://localhost:8000/providers"
```

### Statistics

Defined in `part_3/api/routers/stats_router.py`.

Examples:

```text
GET /stats/by-year
GET /stats/by-education-area
```

The current Streamlit frontend uses these endpoints for dashboard charts.

Example:

```bash
curl "http://localhost:8000/stats/by-year"
```

### Exports

Defined in `part_3/api/routers/export_router.py`.

Examples:

```text
GET /export/applications
GET /export/stats/by-year
```

Example:

```bash
curl -o applications.csv "http://localhost:8000/export/applications"
```

### Refresh

Defined in `part_3/api/routers/refresh_router.py`.

```text
POST /refresh
```

This endpoint runs the pipeline, validates the result, truncates the current curated table, and reloads the refreshed dataset.

Example:

```bash
curl -X POST "http://localhost:8000/refresh"
```

Expected response fields:

```json
{
  "status": "success",
  "rows_inserted": 1234,
  "validation_checks": 5
}
```

## Running the API Locally

From the project root:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m uvicorn part_3.api.main:app --reload
```

Open the interactive docs:

```text
http://localhost:8000/docs
```

## Error Handling

Routers raise `HTTPException` for missing records or failed operations. The Streamlit API client catches HTTP and network errors and shows user-friendly error messages in the frontend.

## API Contract Notes

- Response models are defined with Pydantic in `part_3/api/schemas/response_schema.py`.
- Service functions return plain dictionaries or lists of dictionaries.
- Pandas dataframes are converted to JSON-compatible records before returning.
- Endpoint names should remain stable because the Streamlit frontend depends on them through constants in `streamlit_app/core/config.py`.
