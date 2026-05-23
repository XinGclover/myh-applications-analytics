## Architecture

This API follows a layered architecture with clear separation of concerns:

- FastAPI for the API layer
- Pydantic models for request/response validation
- Service layer for business logic
- PostgreSQL as the database
- SQLAlchemy Core for database connection and transaction management
- Raw SQL for explicit query control and transparency

The project intentionally uses raw SQL instead of a full ORM approach in order to:

- strengthen SQL fundamentals
- keep database behavior explicit
- simplify debugging
- maintain full control over generated queries∏


### POST /refresh is an operational endpoint that triggers the full curated dataset pipeline.

When called, the endpoint:
- reads all configured Excel source years from YEAR_CONFIG,
- cleans and harmonizes the raw data,
- applies enrichment logic,
- validates the final curated dataset,
- truncates the existing curated database table,
- reloads the refreshed curated dataset into PostgreSQL.

This makes the API more operational and reusable, because the database can be refreshed from source files without manually running the notebook.