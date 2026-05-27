from __future__ import annotations

import os
import requests
from dotenv import load_dotenv
import pandas as pd
import streamlit as st

load_dotenv()


REQUEST_TIMEOUT_SECONDS = 10
REFRESH_TIMEOUT_SECONDS = 120
EXPORT_TIMEOUT_SECONDS = 30


def get_api_base_url() -> str:
    """
    Read the FastAPI base URL from environment variables
    and normalize trailing slashes.
    """

    api_base_url = os.getenv("API_BASE_URL")

    if not api_base_url:
        raise ValueError("API_BASE_URL is not configured.")

    return api_base_url.rstrip("/")


def get_error_message(endpoint: str, exc: requests.RequestException) -> str:
    """
    Format request failures into Streamlit-friendly messages
    with endpoint and response details when available.
    """
    response = getattr(exc, "response", None)
    if response is None:
        return f"Could not call {endpoint}: {exc}"

    try:
        detail = response.json().get("detail", response.text)
    except ValueError:
        detail = response.text

    return f"Could not call {endpoint}: {response.status_code} {detail}"


@st.cache_data(ttl=60)
def get_json(endpoint: str, params: dict | None = None) -> tuple[list | dict | None, str | None]:
    """
    Fetch JSON data from the FastAPI backend
    and return either parsed data or an error message.
    """
    url = f"{get_api_base_url()}{endpoint}"

    try:
        response = requests.get(url, params=params, timeout=REQUEST_TIMEOUT_SECONDS)
        response.raise_for_status()
    except requests.RequestException as exc:
        return None, get_error_message(endpoint, exc)

    try:
        return response.json(), None
    except ValueError:
        return None, f"Could not parse JSON from {endpoint}."


def post_json(
    endpoint: str,
    payload: dict | None = None,
    headers: dict | None = None,
) -> tuple[dict | None, str | None]:
    """
    Send a POST request to the API
    and return either parsed JSON or an error message.
    """
    url = f"{get_api_base_url()}{endpoint}"

    try:
        response = requests.post(
            url,
            json=payload,
            headers=headers,
            timeout=REFRESH_TIMEOUT_SECONDS,
        )
        response.raise_for_status()

    except requests.RequestException as exc:
        return None, get_error_message(endpoint, exc)

    try:
        return response.json(), None

    except ValueError:
        return None, f"Could not parse JSON from {endpoint}."


def get_file(endpoint: str, params: dict | None = None) -> tuple[bytes | None, str | None]:
    """
    Download binary content from an API endpoint
    for Streamlit download buttons.
    """
    url = f"{get_api_base_url()}{endpoint}"

    try:
        response = requests.get(url, params=params, timeout=EXPORT_TIMEOUT_SECONDS)
        response.raise_for_status()
    except requests.RequestException as exc:
        return None, get_error_message(endpoint, exc)

    return response.content, None


def load_dataframe_with_error(
    endpoint: str,
    params: dict | None = None,
) -> tuple[pd.DataFrame, str | None]:
    """
    Load an API response into a dataframe
    without rendering Streamlit error messages.
    """
    data, error = get_json(endpoint, params=params)

    if error or not data:
        return pd.DataFrame(), error

    if isinstance(data, dict):
        return pd.DataFrame([data]), None

    return pd.DataFrame(data), None


def load_dataframe(endpoint: str, params: dict | None = None) -> pd.DataFrame:
    """
    Load list-style API responses into a dataframe
    and show API errors inside Streamlit.
    """
    df, error = load_dataframe_with_error(endpoint, params=params)

    if error:
        st.error(error)
        return df

    return df


def put_json(
    endpoint: str,
    payload: dict | None = None,
) -> tuple[dict | None, str | None]:
    """
    Send a PUT request to the API
    and return either parsed JSON or an error message.
    """
    url = f"{get_api_base_url()}{endpoint}"

    try:
        response = requests.put(
            url,
            json=payload,
            timeout=REFRESH_TIMEOUT_SECONDS,
        )
        response.raise_for_status()

    except requests.RequestException as exc:
        return None, get_error_message(endpoint, exc)

    try:
        return response.json(), None

    except ValueError:
        return None, f"Could not parse JSON from {endpoint}."


def delete_json(endpoint: str) -> tuple[bool, str | None]:
    """
    Send a DELETE request to the API
    and return success status or an error message.
    """
    url = f"{get_api_base_url()}{endpoint}"

    try:
        response = requests.delete(url, timeout=REFRESH_TIMEOUT_SECONDS)
        response.raise_for_status()
        return True, None

    except requests.RequestException as exc:
        return False, get_error_message(endpoint, exc)
