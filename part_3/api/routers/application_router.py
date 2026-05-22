# import pandas as pd
# from fastapi import FastAPI, HTTPException, Query
# from fastapi.responses import StreamingResponse
# from io import StringIO
# from .queries import (
#     get_applications,
#     get_application_by_id,
#     get_stats_by_year,
# )

# app = FastAPI(
#     title="Applications API",
#     description="A small internal API for browsing and analyzing curated education application data.",
#     version="1.0.0",
# )
# print("RUNNING PART_3 API MAIN")

# @app.get("/")
# def root():
#     return {"message": "Applications API is running", "docs": "/docs"}


# @app.get("/applications")
# def applications(
#     year: int | None = None,
#     county: str | None = None,
#     study_form: str | None = None,
#     limit: int = Query(default=100, ge=1, le=1000),
# ):
#     return get_applications(
#         year=year,
#         county=county,
#         study_form=study_form,
#         limit=limit,
#     )


# @app.get("/applications/{diarienummer:path}")
# def application_by_id(diarienummer: str):
#     application = get_application_by_id(diarienummer)

#     if application is None:
#         raise HTTPException(status_code=404, detail="Application not found")

#     return application


# @app.get("/stats/by-year")
# def stats_by_year():
#     return get_stats_by_year()


# @app.get("/export/applications")
# def export_applications(year: int | None = None):

#     data = get_applications(year=year)

#     df = pd.DataFrame(data)

#     output = StringIO()
#     df.to_csv(output, index=False)

#     output.seek(0)

#     return StreamingResponse(
#         output,
#         media_type="text/csv",
#         headers={"Content-Disposition": "attachment; filename=applications.csv"},
#     )


from fastapi import APIRouter, HTTPException, status

from part_3.api.schemas.application_schema import ApplicationResponse
from part_3.api.services.application_service import (
    get_applications,
    get_application_by_diarienummer,
)

router = APIRouter(
    prefix="/applications",
    tags=["Applications"],
)


@router.get(
    "",
    response_model=list[ApplicationResponse],
)
def list_applications(
    year: int | None = None,
    decision: str | None = None,
    region: str | None = None,
    municipality: str | None = None,
    provider: str | None = None,
    study_form: str | None = None,
    limit: int = 100,
):
    return get_applications(
        year=year,
        decision=decision,
        region=region,
        municipality=municipality,
        provider=provider,
        study_form=study_form,
        limit=limit,
    )


@router.get(
    "/{diarienummer:path}",
    response_model=ApplicationResponse,
)
def get_application(diarienummer: str):
    application = get_application_by_diarienummer(diarienummer)

    if not application:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Application not found",
        )

    return application
