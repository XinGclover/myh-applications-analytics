from sqlalchemy import text

from src.myh_db.db import engine
from part_3.api.schemas.request_schema import ApplicationNoteCreate


def upsert_note(application_id: str, note: ApplicationNoteCreate) -> dict:
    """
    Create or update the single note for one application.
    """
    query = text("""
        INSERT INTO curated.application_notes (
            application_id,
            note_text,
            is_flagged
        )
        VALUES (
            :application_id,
            :note_text,
            :is_flagged
        )
        ON CONFLICT (application_id)
        DO UPDATE SET
            note_text = EXCLUDED.note_text,
            is_flagged = EXCLUDED.is_flagged,
            updated_at = CURRENT_TIMESTAMP
        RETURNING
            note_id,
            application_id,
            note_text,
            is_flagged,
            created_at,
            updated_at;
    """)

    params = {
        "application_id": application_id,
        "note_text": note.note_text,
        "is_flagged": note.is_flagged,
    }

    with engine.begin() as conn:
        result = conn.execute(query, params).mappings().first()

    return dict(result)


def get_note_by_application_id(application_id: str) -> dict | None:
    """
    Return the single stored note for one application.
    """
    query = text("""
        SELECT
            note_id,
            application_id,
            note_text,
            is_flagged,
            created_at,
            updated_at
        FROM curated.application_notes
        WHERE application_id = :application_id;
    """)

    with engine.begin() as conn:
        result = (
            conn.execute(
                query,
                {"application_id": application_id},
            )
            .mappings()
            .first()
        )

    return dict(result) if result else None


def delete_note(application_id: str) -> bool:
    """
    Delete the single note for one application.
    """
    query = text("""
        DELETE FROM curated.application_notes
        WHERE application_id = :application_id;
    """)

    with engine.begin() as conn:
        result = conn.execute(
            query,
            {"application_id": application_id},
        )

    return result.rowcount > 0
