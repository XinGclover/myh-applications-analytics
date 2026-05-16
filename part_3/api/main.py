from fastapi import FastAPI, HTTPException, Query
from .queries import (
    get_applications,
    get_application_by_id,
    get_stats_by_year,
)

app = FastAPI(
    title="Applications API",
    description="A small internal API for browsing and analyzing curated education application data.",
    version="1.0.0",
)
print("RUNNING PART_3 API MAIN")

@app.get("/")
def root():
    return {"message": "Applications API is running", "docs": "/docs"}


@app.get("/applications")
def applications(
    year: int | None = None,
    county: str | None = None,
    study_form: str | None = None,
    limit: int = Query(default=100, ge=1, le=1000),
):
    return get_applications(
        year=year,
        county=county,
        study_form=study_form,
        limit=limit,
    )


@app.get("/applications/by-id")
def application_by_id(diarienummer: str):
    application = get_application_by_id(diarienummer)

    if application is None:
        raise HTTPException(status_code=404, detail="Application not found")

    return application


@app.get("/stats/by-year")
def stats_by_year():
    return get_stats_by_year()
