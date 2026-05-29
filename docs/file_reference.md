# File Reference

| Path | Description |
|---|---|
| `.env.sample` | Provides an example environment variable template without real secrets. |
| `.gitignore` | Defines local files and generated artifacts that Git should ignore. |
| `README.md` | Introduces the assignment/project and its overall requirements. |
| `docs/api_design.md` | Documents the FastAPI endpoint structure and API design choices. |
| `docs/architecture.md` | Explains the project architecture from Excel files to Streamlit dashboard. |
| `docs/data_pipeline.md` | Describes the MYH data pipeline and curated dataset workflow. |
| `docs/database_schema.md` | Documents the PostgreSQL schema and table responsibilities. |
| `docs/deployment.md` | Lists local and cloud deployment commands for the platform. |
| `docs/file_reference.md` | Provides a concise purpose summary for relevant project files. |
| `docs/images/dashboard.png` | Stores a dashboard screenshot used by project documentation. |
| `docs/images/swagger_ui.png` | Stores a Swagger UI screenshot used by project documentation. |
| `docs/streamlit_structure.md` | Explains the Streamlit app structure and frontend module responsibilities. |
| `part_2/data/curated/curated_applications.csv` | Stores the English curated application dataset exported by the transformation pipeline. |
| `part_2/instructions.txt` | Contains Part 2 assignment instructions and guidance. |
| `part_2/notebooks/part_2_curated_dataset.ipynb` | Shows the notebook workflow for building and validating the curated dataset. |
| `part_3/api/core/config.py` | Loads API-level configuration such as the refresh API key. |
| `part_3/api/dependencies/security.py` | Provides API key validation for protected FastAPI endpoints. |
| `part_3/api/main.py` | Creates the FastAPI app and registers all routers. |
| `part_3/api/routers/application_router.py` | Defines application browsing and detail endpoints. |
| `part_3/api/routers/export_router.py` | Defines CSV export endpoints for English curated applications and yearly statistics. |
| `part_3/api/routers/note_router.py` | Defines endpoints for reading, updating, and deleting application notes. |
| `part_3/api/routers/provider_router.py` | Defines provider listing and provider application drilldown endpoints. |
| `part_3/api/routers/refresh_router.py` | Defines the protected endpoint that triggers a full pipeline refresh. |
| `part_3/api/routers/stats_router.py` | Defines statistics endpoints used by the dashboard charts. |
| `part_3/api/schemas/request_schema.py` | Defines Pydantic request and response models for application notes. |
| `part_3/api/schemas/response_schema.py` | Defines Pydantic response models using English curated field names. |
| `part_3/api/services/application_service.py` | Queries English curated application records and checks application existence. |
| `part_3/api/services/note_service.py` | Handles database operations for application notes. |
| `part_3/api/services/provider_service.py` | Queries provider summaries and provider-specific applications. |
| `part_3/api/services/refresh_service.py` | Runs the full pipeline and reloads the curated PostgreSQL database. |
| `part_3/api/services/stats_service.py` | Builds filtered aggregate queries for dashboard statistics. |
| `part_3/api/utils/response.py` | Converts pandas dataframes into JSON-safe API records. |
| `part_3/api/utils/validation.py` | Validates that an application exists before note operations. |
| `part_3/sql/create_tables.sql` | Defines the PostgreSQL schema, tables, and indexes for English curated data. |
| `requirements.txt` | Lists Python dependencies required by the pipeline, API, and Streamlit app. |
| `src/myh_db/bootstrap_db.py` | Creates the local database schema and loads curated application data. |
| `src/myh_db/db.py` | Creates the SQLAlchemy database engine from environment variables. |
| `src/myh_db/load_to_db.py` | Loads the curated applications CSV into PostgreSQL. |
| `src/myh_pipeline/clean.py` | Cleans source column names and text values before harmonization. |
| `src/myh_pipeline/config.py` | Stores pipeline configuration for source files, selected years, and column mappings. |
| `src/myh_pipeline/enrich.py` | Adds derived analytical fields such as approval flags and sector categories. |
| `src/myh_pipeline/harmonize.py` | Maps yearly Excel dataframes into a shared Swedish-normalized schema. |
| `src/myh_pipeline/load.py` | Loads configured MYH Excel sheets and adds source traceability columns. |
| `src/myh_pipeline/pipeline.py` | Orchestrates loading, cleaning, harmonization, enrichment, column translation, and validation. |
| `src/myh_pipeline/translate_columns.py` | Translates Swedish-normalized columns into English curated analytics fields. |
| `src/myh_pipeline/validate.py` | Builds validation summaries for the English curated dataset. |
| `streamlit_app/app.py` | Renders the Streamlit landing page and project overview. |
| `streamlit_app/components/application_note.py` | Renders the application note editor in the dashboard. |
| `streamlit_app/components/application_table.py` | Renders the selectable filtered applications table. |
| `streamlit_app/components/bar_chart.py` | Renders reusable Streamlit bar chart sections. |
| `streamlit_app/components/export_button.py` | Renders CSV export controls backed by API download endpoints. |
| `streamlit_app/components/refresh_section.py` | Renders the protected database refresh control in Streamlit. |
| `streamlit_app/core/api_client.py` | Provides HTTP helpers for calling the FastAPI backend from Streamlit. |
| `streamlit_app/core/config.py` | Stores Streamlit endpoint constants, filter keys, and application limits. |
| `streamlit_app/core/data_loader.py` | Loads initial and filtered dashboard data from API endpoints. |
| `streamlit_app/core/filters.py` | Builds sidebar filter options and query parameters for the dashboard. |
| `streamlit_app/core/metrics.py` | Calculates KPI values displayed on the dashboard. |
| `streamlit_app/pages/1_Notebook.py` | Displays the exported curated dataset notebook in Streamlit. |
| `streamlit_app/pages/2_Dashboard.py` | Renders the main analytics dashboard and operations sections. |
