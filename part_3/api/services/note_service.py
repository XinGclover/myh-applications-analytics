from sqlalchemy import text

from src.myh_db.db import engine
from part_3.api.schemas.request_schema import (
    ApplicationNoteCreate,
    ApplicationNoteUpdate,
)


def create_note(diarienummer: str, note: ApplicationNoteCreate) -> dict:
    query = text("""
        INSERT INTO curated.application_notes (
            diarienummer,
            note_text,
            is_flagged
        )
        VALUES (
            :diarienummer,
            :note_text,
            :is_flagged
        )
        RETURNING
            note_id,
            diarienummer,
            note_text,
            is_flagged,
            created_at,
            updated_at;
    """)

    params = {
        "diarienummer": diarienummer,
        "note_text": note.note_text,
        "is_flagged": note.is_flagged,
    }

    with engine.begin() as conn:
        result = conn.execute(query, params).mappings().first()

    return dict(result)


def get_notes_by_diarienummer(diarienummer: str) -> list[dict]:
    query = text("""
        SELECT
            note_id,
            diarienummer,
            note_text,
            is_flagged,
            created_at,
            updated_at
        FROM curated.application_notes
        WHERE diarienummer = :diarienummer
        ORDER BY created_at DESC;
    """)

    with engine.begin() as conn:
        result = (
            conn.execute(
                query,
                {"diarienummer": diarienummer},
            )
            .mappings()
            .all()
        )

    return [dict(row) for row in result]


def update_note(
    diarienummer: str,
    note_id: int,
    note: ApplicationNoteUpdate,
) -> dict | None:
    query = text("""
        UPDATE curated.application_notes
        SET
            note_text = COALESCE(:note_text, note_text),
            is_flagged = COALESCE(:is_flagged, is_flagged),
            updated_at = CURRENT_TIMESTAMP
        WHERE diarienummer = :diarienummer
          AND note_id = :note_id
        RETURNING
            note_id,
            diarienummer,
            note_text,
            is_flagged,
            created_at,
            updated_at;
    """)

    params = {
        "diarienummer": diarienummer,
        "note_id": note_id,
        "note_text": note.note_text,
        "is_flagged": note.is_flagged,
    }

    with engine.begin() as conn:
        result = conn.execute(query, params).mappings().first()

    return dict(result) if result else None


def delete_note(diarienummer: str, note_id: int) -> bool:
    query = text("""
        DELETE FROM curated.application_notes
        WHERE diarienummer = :diarienummer
          AND note_id = :note_id;
    """)

    params = {
        "diarienummer": diarienummer,
        "note_id": note_id,
    }

    with engine.begin() as conn:
        result = conn.execute(query, params)

    return result.rowcount > 0
