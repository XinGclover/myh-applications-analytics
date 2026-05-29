from __future__ import annotations

import pandas as pd
import streamlit as st

from core.api_client import delete_json, load_dataframe_with_error, put_json


def render_application_notes(selected_application_id: str) -> None:
    st.subheader("Application notes")

    if "note_message" in st.session_state:
        st.success(st.session_state.pop("note_message"))

    st.caption(f"Selected application: {selected_application_id}")

    note_endpoint = f"/applications/{selected_application_id}/note"

    notes_df, notes_error = load_dataframe_with_error(note_endpoint)

    note_exists = not notes_df.empty

    if notes_error:
        if "404" in notes_error:
            st.info("No note for this application yet.")
        else:
            st.error(notes_error)

    if note_exists:
        st.dataframe(
            notes_df,
            use_container_width=True,
            hide_index=True,
        )

    existing_note_text = ""
    existing_is_flagged = False

    if note_exists:
        existing_note_text = notes_df.iloc[0]["note_text"]
        existing_is_flagged = bool(notes_df.iloc[0]["is_flagged"])

    note_text = st.text_area(
        "Note text",
        value=existing_note_text,
    )

    is_flagged = st.checkbox(
        "Flag this application",
        value=existing_is_flagged,
    )

    button_label = "Update note" if note_exists else "Create note"

    col1, col2 = st.columns([1, 1])

    with col1:
        if st.button(button_label):
            if not note_text.strip():
                st.warning("Please enter a note before saving.")
            else:
                result, error = put_json(
                    note_endpoint,
                    payload={
                        "note_text": note_text,
                        "is_flagged": is_flagged,
                    },
                )

                if error:
                    st.error(error)
                else:
                    st.cache_data.clear()
                    st.success("Note saved successfully.")
                    st.dataframe(
                        pd.DataFrame([result]),
                        use_container_width=True,
                        hide_index=True,
                    )

    with col2:
        if note_exists:
            if st.button("Delete note"):
                deleted, delete_error = delete_json(note_endpoint)

                if delete_error:
                    st.error(delete_error)
                else:
                    st.cache_data.clear()
                    st.success("Note deleted successfully.")
                    st.info("No note for this application yet.")
