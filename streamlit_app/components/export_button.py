import streamlit as st

from core.api_client import get_file


def render_export_button(
    title: str,
    description: str,
    button_label: str,
    endpoint: str,
    file_name: str,
    params: dict | None = None,
) -> None:
    st.markdown(f"#### {title}")
    st.markdown(description)

    if st.button(button_label, type="primary"):
        with st.spinner("Preparing CSV..."):
            csv_data, error = get_file(endpoint, params=params)

        if error:
            st.error(error)
        elif csv_data:
            st.download_button(
                f"Download {file_name}",
                data=csv_data,
                file_name=file_name,
                mime="text/csv",
            )