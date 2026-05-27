import streamlit as st

from core.api_client import post_json
from core.config import REFRESH_ENDPOINT

def render_refresh_section() -> None:
    st.subheader("🔄 Refresh database")
    st.markdown(
        "Trigger the backend refresh endpoint to rebuild and reload the curated dataset."
    )

    refresh_api_key = st.text_input(
        "Refresh API key",
        type="password",
        help="Required to run the protected refresh endpoint.",
    )

    if st.button("Refresh Database", type="primary"):
        if not refresh_api_key:
            st.warning("Please enter the refresh API key first.")
        else:
            with st.spinner("Refreshing database..."):
                refresh_result, refresh_error = post_json(
                    REFRESH_ENDPOINT,
                    headers={"x-api-key": refresh_api_key},
                )

            if refresh_error:
                st.error(refresh_error)
            elif refresh_result:
                st.cache_data.clear()
                st.success(
                    "Refresh completed: "
                    f"status={refresh_result.get('status')}, "
                    f"rows_inserted={refresh_result.get('rows_inserted')}, "
                    f"validation_checks={refresh_result.get('validation_checks')}"
                )