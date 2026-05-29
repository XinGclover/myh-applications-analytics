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
    application_id VARCHAR(50) PRIMARY KEY,
    education_name VARCHAR(200) NOT NULL,
    education_area VARCHAR(50) NOT NULL,

    -- decision
    decision VARCHAR(20) NOT NULL,
    decision_normalized VARCHAR(20) NOT NULL,
    is_approved BOOLEAN NOT NULL,

    -- geography
    municipality VARCHAR(100) NOT NULL,
    county VARCHAR(100) NOT NULL,

    -- education details
    yh_credits SMALLINT NOT NULL,

    education_length VARCHAR(20) NOT NULL,

    study_form VARCHAR(20) NOT NULL,
    study_form_normalized VARCHAR(20) NOT NULL,

    study_pace_percent SMALLINT NOT NULL,

    -- provider info
    provider_name VARCHAR(200) NOT NULL,
    provider_type VARCHAR(20) NOT NULL,

    -- SUN classification
    sun5_field VARCHAR(20),
    sun5_field_name VARCHAR(200),

    seqf_level NUMERIC(3,1),

    narrow_occupational_area VARCHAR(10),

    sector_category VARCHAR(50) NOT NULL,

    -- metadata
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =========================
-- Indexes
-- =========================

CREATE INDEX idx_applications_year
ON curated.yh_applications(source_year);

CREATE INDEX idx_applications_county
ON curated.yh_applications(county);

CREATE INDEX idx_applications_provider
ON curated.yh_applications(provider_name);

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

    application_id VARCHAR(50) NOT NULL UNIQUE,

    note_text TEXT NOT NULL,

    is_flagged BOOLEAN NOT NULL DEFAULT FALSE,

    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP,

    CONSTRAINT fk_notes_application_id
        FOREIGN KEY (application_id)
        REFERENCES curated.yh_applications(application_id)
);

CREATE INDEX IF NOT EXISTS idx_notes_application_id
ON curated.application_notes(application_id);