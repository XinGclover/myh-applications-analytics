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
- maintain full control over generated queries