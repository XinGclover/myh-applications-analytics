# API Design

## Purpose

The FastAPI backend exposes the curated MYH applications dataset to the Streamlit dashboard.

Main features:

- application browsing
- filtering
- statistics
- CSV export
- notes
- refresh operations

---

## Swagger UI

FastAPI automatically generates interactive API documentation through Swagger UI.

![Swagger UI](images/swagger_ui.png)

---

## Main Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/applications` | Return filtered application records |
| GET | `/applications/{diarienummer}` | Return a single application |
| POST | `/applications/{diarienummer}/notes` | Create an application note |
| GET | `/applications/{diarienummer}/notes` | Return application notes |
| PUT | `/applications/{diarienummer}/notes/{note_id}` | Update an application note |
| DELETE | `/applications/{diarienummer}/notes/{note_id}` | Delete an application note |
| GET | `/stats/by-year` | Return yearly application statistics |
| GET | `/stats/by-education-area` | Return statistics grouped by education area |
| GET | `/export/applications` | Export application data as CSV |
| GET | `/export/stats/by-year` | Export yearly statistics as CSV |
| POST | `/refresh` | Rebuild and reload the curated dataset |
| GET | `/providers` | Return provider list |
| GET | `/providers/{provider_name}/applications` | Return provider applications |

---

## Local Development

Run the API with:

```bash
python -m uvicorn part_3.api.main:app --reload
```

For full setup instructions, see:

```text
docs/deployment.md
```