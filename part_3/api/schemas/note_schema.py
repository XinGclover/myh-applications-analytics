from datetime import datetime

from pydantic import BaseModel, Field


class ApplicationNoteCreate(BaseModel):
    note_text: str = Field(..., min_length=1)
    is_flagged: bool = False


class ApplicationNoteUpdate(BaseModel):
    note_text: str | None = Field(default=None, min_length=1)
    is_flagged: bool | None = None


class ApplicationNoteResponse(BaseModel):
    note_id: int
    diarienummer: str
    note_text: str
    is_flagged: bool
    created_at: datetime
    updated_at: datetime | None = None
