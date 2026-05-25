from pydantic import BaseModel


class ApplicationResponse(BaseModel):
    application_id: int
    source_year: int
    diarienummer: str
    utbildningsnamn: str
    utbildningsomrade: str
    beslut: str
    decision_normalized: str
    is_approved: bool
    kommun: str
    lan: str
    studieform: str
    study_form_normalized: str
    utbildningsanordnare: str

    

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
    utbildningsomrade: str
    total_applications: int
    approved_applications: int
    approval_rate_percent: float