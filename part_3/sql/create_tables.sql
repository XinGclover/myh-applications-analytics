CREATE SCHEMA IF NOT EXISTS curated;

-- =========================
-- Drop existing tables
-- =========================

DROP TABLE IF EXISTS curated.application_notes;

DROP TABLE IF EXISTS curated.yh_applications;

-- =========================
-- Main applications table
-- =========================

CREATE TABLE curated.yh_applications (

    -- source metadata
    source_year SMALLINT NOT NULL,
    source_file VARCHAR(100) NOT NULL,
    source_sheet VARCHAR(20) NOT NULL,
    record_source VARCHAR(50) NOT NULL,

    -- application info
    diarienummer VARCHAR(50) PRIMARY KEY,
    utbildningsnamn VARCHAR(200) NOT NULL,
    utbildningsomrade VARCHAR(50) NOT NULL,

    -- decision
    beslut VARCHAR(20) NOT NULL,
    decision_normalized VARCHAR(20) NOT NULL,
    is_approved BOOLEAN NOT NULL,

    -- geography
    kommun VARCHAR(100) NOT NULL,
    lan VARCHAR(100) NOT NULL,

    -- education details
    yh_poang SMALLINT NOT NULL,

    education_length VARCHAR(20) NOT NULL,

    studieform VARCHAR(20) NOT NULL,
    study_form_normalized VARCHAR(20) NOT NULL,

    studietakt_procent SMALLINT NOT NULL,

    -- provider info
    utbildningsanordnare VARCHAR(200) NOT NULL,
    huvudmannatyp VARCHAR(20) NOT NULL,

    -- SUN / classification fields
    sun5_inriktning VARCHAR(20),
    sun5_inriktning_namn VARCHAR(200),

    seqf_niva NUMERIC(3,1),

    smalt_yrkesomrade VARCHAR(10),

    sector_category VARCHAR(50) NOT NULL,

    -- metadata
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- indexes

CREATE INDEX idx_applications_year
ON curated.yh_applications(source_year);

CREATE INDEX idx_applications_region
ON curated.yh_applications(lan);

CREATE INDEX idx_applications_provider
ON curated.yh_applications(utbildningsanordnare);

CREATE INDEX idx_applications_decision
ON curated.yh_applications(decision_normalized);

CREATE INDEX idx_applications_sector
ON curated.yh_applications(sector_category);

CREATE INDEX idx_applications_approved
ON curated.yh_applications(is_approved);


-- =========================
-- Application notes
-- =========================

CREATE TABLE IF NOT EXISTS curated.application_notes (
    note_id SERIAL PRIMARY KEY,

    diarienummer VARCHAR(50) NOT NULL UNIQUE,

    note_text TEXT NOT NULL,

    is_flagged BOOLEAN NOT NULL DEFAULT FALSE,

    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP,

    CONSTRAINT fk_notes_diarienummer
        FOREIGN KEY (diarienummer)
        REFERENCES curated.yh_applications(diarienummer)
);

CREATE INDEX IF NOT EXISTS idx_notes_diarienummer
ON curated.application_notes(diarienummer);