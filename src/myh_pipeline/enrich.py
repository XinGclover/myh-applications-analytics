import pandas as pd


SECTOR_KEYWORDS = {
    "data_it": [
        "data",
        "it",
        "system",
        "programmering",
        "webbutvecklare",
        "it-säkerhet",
        "mjukvara",
        "digital",
        "datavetenskap",
        "systemutveckling",
        "systemadministratör",
        "databas",
        "spel",
        "interaktionsdesign",
        "e-handel",
        "robotautomation",
        "inbyggda system",
        "telekom",
        "3d-tekniker",
        "supporttekniker",
    ],
    "ekonomi_forsaljning": [
        "ekonomi",
        "redovisning",
        "löneadministratör",
        "inköp",
        "upphandling",
        "försäljning",
        "marknadsföring",
        "affärsutvecklare",
        "bank",
        "försäkring",
        "handel",
        "logistik",
        "e-handel",
    ],
    "halso_sjukvard": [
        "vård",
        "sjukvård",
        "omsorg",
        "undersköterska",
        "tandsköterska",
        "medicinsk",
        "apotekstekniker",
        "ambulans",
        "psykiatri",
        "massageterapeut",
        "fotterapeut",
        "ortopedtekniker",
        "rehabilitering",
        "äldreomsorg",
    ],
    "bygg_fastighet_vvs": [
        "bygg",
        "fastighet",
        "vvs",
        "anläggning",
        "bygglov",
        "samhällsbyggnad",
        "ventilation",
        "kyl",
        "värmepumps",
        "trähus",
        "betong",
    ],
    "teknik_industri": [
        "automation",
        "produktionstekniker",
        "processtekniker",
        "underhållstekniker",
        "drifttekniker",
        "cad",
        "konstruktör",
        "elkraft",
        "elinstallatör",
        "elektronik",
        "mekatroniker",
        "svets",
        "cnc",
        "hydraul",
        "industri",
        "materialtekniker",
        "vindkraft",
        "solenergi",
        "energi",
        "marintekniker",
    ],
    "transport": [
        "transport",
        "lokförare",
        "järnväg",
        "trafik",
        "fordon",
        "flyg",
        "pilot",
        "skeppare",
        "sjöfart",
        "spedition",
    ],
    "hotell_turism_restaurang": [
        "hotell",
        "turism",
        "restaurang",
        "kock",
        "sommelier",
        "baransvarig",
        "konferens",
        "housekeeping",
        "food and beverage",
        "bagare",
        "konditor",
    ],
    "media_design_kultur": [
        "media",
        "design",
        "film",
        "tv",
        "musik",
        "grafisk",
        "copywriting",
        "journalistik",
        "fotograf",
        "konst",
        "modedesign",
        "spelgrafiker",
    ],
    "pedagogik_socialt_arbete": [
        "pedagog",
        "social",
        "behandlings",
        "lärarassistent",
        "skola",
        "äldreomsorg",
        "stödpedagog",
        "aktiveringspedagog",
    ],
    "natur_djur_lantbruk": [
        "trädgård",
        "skog",
        "lantbruk",
        "häst",
        "djur",
        "arborist",
        "fiske",
        "vattenbruk",
    ],
}


def classify_scope(points):
    if pd.isna(points):
        return "unknown"
    if points < 200:
        return "short"
    if points < 400:
        return "medium"
    return "long"


def classify_sector(name):
    if pd.isna(name):
        return "unknown"

    name = str(name).lower()

    for sector, keywords in SECTOR_KEYWORDS.items():
        if any(keyword in name for keyword in keywords):
            return sector

    return "other"


def enrich_dataset(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["is_approved"] = df["decision_normalized"].eq("approved")
    df["education_length"] = df["yh_poang"].apply(classify_scope)
    df["sector_category"] = df["sun5_inriktning_namn"].apply(classify_sector)
    df["record_source"] = (
        df["source_year"].astype(str) + "_" + df["source_sheet"].astype(str)
    )

    return df
