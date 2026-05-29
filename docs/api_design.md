# API Design

## Purpose

The FastAPI backend exposes the English curated MYH applications dataset to the Streamlit dashboard and CSV export consumers.

Main features:

- application browsing
- filtering
- statistics
- CSV export
- application notes
- refresh operations

---

## Swagger UI

FastAPI automatically generates interactive API documentation through Swagger UI.

![Swagger UI](images/swagger_ui.png)

---

## Main API Areas

| Area | Purpose |
|---|---|
| Applications | Browse, filter, and inspect curated application records |
| Statistics | Return aggregated data for dashboard charts |
| Providers | List providers and show provider-specific applications |
| Export | Download application and statistics data as CSV |
| Application notes | Store lightweight notes for individual applications |
| Refresh | Rebuild the curated dataset and reload PostgreSQL |

---

## Main Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/applications` | Return filtered application records |
| GET | `/applications/{diarienummer}` | Return a single application |
| PUT | `/applications/{diarienummer}/note` | Create or update an application note |
| GET | `/applications/{diarienummer}/note` | Return an application note |
| DELETE | `/applications/{diarienummer}/note` | Delete an application note |
| GET | `/stats/by-year` | Return yearly application statistics |
| GET | `/stats/by-education-area` | Return statistics grouped by education area |
| GET | `/providers` | Return provider list |
| GET | `/providers/{provider_name}/applications` | Return provider applications |
| GET | `/export/applications` | Export application data as CSV |
| GET | `/export/stats/by-year` | Export yearly statistics as CSV |
| POST | `/refresh` | Run the full pipeline and reload the curated database |

---

## Response Schema

API responses use the final English curated field names stored in PostgreSQL.

Example fields:

```text
application_id
education_name
education_area
decision
municipality
region
yh_credits
study_form
study_pace_percent
provider_name
provider_type
sun5_field
sun5_field_name
seqf_level
narrow_occupational_area
```

The original Excel field `diarienummer` is now stored as `application_id` in the database and response models.

Public route paths remain stable for compatibility. Routes such as `/applications/{diarienummer}` and `/applications/{diarienummer}/note` keep the path parameter name `diarienummer`, but the service layer maps that value to `application_id`.

---

## Protected Refresh Endpoint

`POST /refresh` runs the full MYH pipeline and reloads the curated PostgreSQL database.

Because this operation modifies the database, the endpoint is protected with a simple API key header.

Required request header:

```http
x-api-key: <refresh-api-key>
```

Refresh workflow:

```text
Raw MYH Excel files
    ↓
Cleaned and harmonized data
    ↓
English curated dataset
    ↓
Validation
    ↓
PostgreSQL reload
```
