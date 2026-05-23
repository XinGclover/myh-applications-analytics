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


def clean_all_years(dfs):
    standardized_dfs = {}

    for year, df in dfs.items():
        df = df.copy()

        # clean column names
        df.columns = [clean_column_name(col) for col in df.columns]

        # clean string values
        df = clean_string_values(df)

        standardized_dfs[year] = df

    return standardized_dfs