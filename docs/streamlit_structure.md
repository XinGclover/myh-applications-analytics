# Streamlit Structure

## Purpose

The Streamlit app is the frontend for the MYH applications analytics platform. It provides a multipage interface for project documentation, notebook preview, interactive analytics, and operational actions.

The app lives in:

```text
streamlit_app/
```

## Current Structure

```text
streamlit_app/
├── app.py
├── pages/
│   ├── 1_Notebook.py
│   └── 2_Dashboard.py
└── core/
    ├── api_client.py
    ├── config.py
    ├── data_loader.py
    ├── filters.py
    └── metrics.py
```

The exact page names may change as the app evolves, but the intended split is:

- `app.py` is the Streamlit entry point and landing page.
- `pages/` contains user-facing pages.
- `core/` contains reusable frontend logic.

## Core Modules

### `core/api_client.py`

Handles HTTP communication with the FastAPI backend.

Typical responsibilities:

- read `API_BASE_URL`
- call API endpoints with `requests`
- return JSON, bytes, or dataframes
- handle API errors gracefully in Streamlit

### `core/config.py`

Stores frontend constants such as:

- endpoint paths
- filter key lists
- application row limits

Keeping endpoint names here avoids scattering route strings across the UI.

### `core/data_loader.py`

Contains endpoint-specific loading functions.

Examples:

- load initial provider and application data
- load filtered dashboard data
- load provider applications
- build export parameters

### `core/filters.py`

Contains sidebar filter logic.

Current filters include:

```text
year
region
municipality
decision
provider
study_form
```

Municipality options depend on the selected region.

### `core/metrics.py`

Contains KPI calculation and formatting logic.

Dashboard KPIs include:

- total applications
- approved applications
- approval rate
- providers count

## Running the Streamlit App

Start the frontend from the project root:

```bash
python -m streamlit run streamlit_app/app.py
```

The FastAPI backend must be running separately.

The frontend communicates with the API through `API_BASE_URL`.

Default:

```text
http://localhost:8000
```

For full setup and environment commands, see:

```text
docs/deployment.md
```

## Page Responsibilities

### Landing or README Page

Explains the project as a data platform:

- project purpose
- architecture
- pipeline
- API
- dashboard
- tech stack

### Notebook Page

Displays an exported HTML notebook if available.

In the current project, notebook HTML lives under:

```text
streamlit_app/notebooks/
```

### Dashboard Page

Provides the main analytics interface:

- sidebar filters
- KPIs
- charts
- filtered application table
- provider drilldown

### Operations Page

Provides operational actions:

- refresh database
- export CSV files

Operational actions should stay simple and should show clear success or error messages.

## Development Guidelines

- Keep page files focused on Streamlit UI.
- Put reusable API and transformation logic in `streamlit_app/core/`.
- Keep endpoint constants in `core/config.py`.
- Do not duplicate API route strings across pages.
- Prefer small helper functions over large UI files.
- Handle API errors in the frontend without crashing the app.
