from __future__ import annotations

import streamlit as st


st.set_page_config(
    page_title="MYH Applications Analytics Platform",
    layout="wide",
)

st.title("MYH Applications Analytics Platform")

st.header("Project Overview")
st.markdown(
    """
    This project is a full-stack data engineering and analytics platform for
    Swedish YH application data from Myndigheten for yrkeshogskolan.

    The platform turns multi-year Excel source files into a curated analytical
    dataset, stores the result in PostgreSQL, exposes it through a FastAPI
    backend, and presents the data through an interactive Streamlit interface.
    """
)
st.info(
    "The goal is to make historical YH application data easier to refresh, "
    "query, analyze, export, and explain."
)

st.header("Architecture")
st.markdown("The platform follows a simple data product architecture:")
st.code(
    """
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
""".strip(),
    language="text",
)

st.header("Features")
st.markdown(
    """
    - Multi-year Excel harmonization across MYH source files
    - Data cleaning and normalization for decisions, study forms, locations, and providers
    - Validation checks before loading curated data
    - Enrichment logic for analysis-ready fields
    - PostgreSQL loading pipeline for persistent storage
    - FastAPI endpoints for records, providers, statistics, exports, and refreshes
    - Interactive dashboard filtering by year, region, municipality, decision, provider, and study form
    """
)

st.header("Data Pipeline")
st.markdown(
    """
    The data pipeline reads raw Excel files, selects the relevant application
    tables, harmonizes changing schemas across years, applies cleaning rules,
    enriches the dataset, validates the output, and loads the curated result
    into PostgreSQL.
    """
)
st.subheader("Pipeline Responsibilities")
st.markdown(
    """
    - Read raw yearly Excel files
    - Standardize column names and value formats
    - Normalize decision and study form fields
    - Preserve source traceability
    - Run validation checks
    - Load the curated dataset into the database
    """
)

st.header("API Overview")
st.markdown(
    """
    The FastAPI backend acts as the data access layer for applications and
    dashboard consumers. It provides browsable records, provider views,
    aggregated statistics, CSV exports, and an operational refresh endpoint.
    """
)
st.subheader("Example Endpoints")
st.code(
    """
/applications
/providers
/stats/by-year
/export/applications
/refresh
""".strip(),
    language="text",
)

st.header("Dashboard Overview")
st.markdown(
    """
    The Streamlit dashboard provides a lightweight analytics interface on top
    of the API. Users can filter the dataset, inspect KPIs, compare application
    volumes over time, analyze education areas, drill into provider
    applications, export CSV data, and trigger operational refreshes.
    """
)

st.header("Tech Stack")
st.markdown(
    """
    - Python for application and pipeline code
    - Pandas for Excel processing, harmonization, and validation
    - PostgreSQL for curated data storage
    - SQLAlchemy Core and raw SQL for database access
    - FastAPI for backend API endpoints
    - Streamlit for the analytics interface
    - Requests for dashboard-to-API communication
    """
)

st.header("Future Improvements")
st.markdown(
    """
    - Add richer regional and provider-level statistics
    - Add automated pipeline tests and dashboard smoke tests
    - Add authentication for operational actions
    - Add scheduled refresh orchestration
    - Add more export formats and saved analytical views
    - Expand observability around refresh runs and validation results
    """
)
