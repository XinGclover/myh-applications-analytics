from __future__ import annotations

import os

import pandas as pd
import requests
import streamlit as st


DEFAULT_API_BASE_URL = "http://localhost:8000"
REQUEST_TIMEOUT_SECONDS = 10
REFRESH_TIMEOUT_SECONDS = 120
EXPORT_TIMEOUT_SECONDS = 30


def get_api_base_url() -> str:
    return os.getenv("API_BASE_URL", DEFAULT_API_BASE_URL).rstrip("/")


def get_error_message(endpoint: str, exc: requests.RequestException) -> str:
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


def post_json(endpoint: str) -> tuple[dict | None, str | None]:
    url = f"{get_api_base_url()}{endpoint}"

    try:
        response = requests.post(url, timeout=REFRESH_TIMEOUT_SECONDS)
        response.raise_for_status()
    except requests.RequestException as exc:
        return None, get_error_message(endpoint, exc)

    try:
        return response.json(), None
    except ValueError:
        return None, f"Could not parse JSON from {endpoint}."


def get_file(endpoint: str, params: dict | None = None) -> tuple[bytes | None, str | None]:
    url = f"{get_api_base_url()}{endpoint}"

    try:
        response = requests.get(url, params=params, timeout=EXPORT_TIMEOUT_SECONDS)
        response.raise_for_status()
    except requests.RequestException as exc:
        return None, get_error_message(endpoint, exc)

    return response.content, None


def load_dataframe(endpoint: str, params: dict | None = None) -> pd.DataFrame:
    data, error = get_json(endpoint, params=params)

    if error:
        st.error(error)
        return pd.DataFrame()

    if not data:
        return pd.DataFrame()

    return pd.DataFrame(data)
