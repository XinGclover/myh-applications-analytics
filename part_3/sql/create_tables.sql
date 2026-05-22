CREATE SCHEMA IF NOT EXISTS curated;

DROP TABLE IF EXISTS curated.yh_applications;

CREATE TABLE curated.yh_applications (

    application_id SERIAL PRIMARY KEY,

    -- source metadata
    source_year INTEGER NOT NULL,
    source_file TEXT NOT NULL,
    source_sheet TEXT NOT NULL,
    record_source TEXT NOT NULL,

    -- application info
    diarienummer TEXT NOT NULL,
    utbildningsnamn TEXT NOT NULL,
    utbildningsomrade TEXT NOT NULL,

    -- decision
    beslut TEXT NOT NULL,
    decision_normalized TEXT NOT NULL,
    is_approved BOOLEAN NOT NULL,

    -- geography
    kommun TEXT NOT NULL,
    lan TEXT NOT NULL,

    -- education details
    yh_poang INTEGER NOT NULL,
    education_length TEXT NOT NULL,

    studieform TEXT NOT NULL,
    study_form_normalized TEXT NOT NULL,

    studietakt_procent INTEGER NOT NULL,

    -- provider info
    utbildningsanordnare TEXT NOT NULL,
    huvudmannatyp TEXT NOT NULL,

    -- SUN / classification fields
    sun5_inriktning TEXT,
    sun5_inriktning_namn TEXT,

    seqf_niva DOUBLE PRECISION,

    smalt_yrkesomrade TEXT,
    sector_category TEXT NOT NULL,

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