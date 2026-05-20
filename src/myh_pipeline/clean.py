def clean_column_name(col):
    return (
        str(col)
        .strip()
        .lower()
        .replace("å", "a")
        .replace("ä", "a")
        .replace("ö", "o")
        .replace("%", "procent")
        .replace(" ", "_")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "_")
    )


def clean_string_values(df):
    df = df.copy()

    for col in df.select_dtypes(include=["object", "string"]).columns:
        df[col] = df[col].str.strip()

    return df