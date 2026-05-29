from pydantic import BaseModel


class ApplicationResponse(BaseModel):
    source_year: int
    application_id: str
    education_name: str
    education_area: str
    decision: str
    decision_normalized: str
    is_approved: bool
    municipality: str
    region: str
    study_form: str
    study_form_normalized: str
    provider_name: str


class RefreshResponse(BaseModel):
    status: str
    rows_inserted: int
    validation_checks: int


class StatsByYearResponse(BaseModel):
    source_year: int
    total_applications: int
    approved_applications: int
    approval_rate_percent: float


class StatsByEducationAreaResponse(BaseModel):
    education_area: str
    total_applications: int
    approved_applications: int
    approval_rate_percent: float
