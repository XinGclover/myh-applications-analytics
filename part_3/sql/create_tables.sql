CREATE SCHEMA IF NOT EXISTS curated;

DROP TABLE IF EXISTS curated.yh_applications;

CREATE TABLE curated.yh_applications (
    application_id SERIAL PRIMARY KEY,

    -- source metadata
    source_year VARCHAR(4) NOT NULL,
    source_file TEXT NOT NULL,
    source_sheet TEXT NOT NULL,

    -- yh_application info
    diarienummer TEXT NOT NULL,
    utbildningsnamn TEXT NOT NULL,
    utbildningsomrade TEXT NOT NULL,

    -- decision
    beslut TEXT NOT NULL,
    beslut_normalized TEXT NOT NULL,

    -- geography
    kommun TEXT NOT NULL,
    lan TEXT NOT NULL,

    -- education details
    yh_poang INTEGER NOT NULL,
    studieform TEXT NOT NULL,
    studietakt_procent INTEGER NOT NULL,

    -- provider info
    utbildningsanordnare TEXT NOT NULL,
    huvudmannatyp TEXT NOT NULL,

    -- SUN / classification fields
    sun5_inriktning TEXT,
    sun5_inriktning_namn TEXT,
    seqf_niva TEXT,
    smalt_yrkesomrade TEXT,

    -- metadata
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- excute after creating table

CREATE INDEX idx_applications_year
ON curated.yh_applications(source_year);

CREATE INDEX idx_applications_region
ON curated.yh_applications(lan);

CREATE INDEX idx_applications_provider
ON curated.yh_applications(utbildningsanordnare);

CREATE INDEX idx_applications_decision
ON curated.yh_applications(beslut_normalized);