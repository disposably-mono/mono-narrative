import pandas as pd


# NOTE: search-based theme matching — genre overlap may skew averages


def analyse(df):
    df["year"] = df["year"].astype(int)

    bins = [1979, 1999, 2019, 2030]
    labels = ["1980-1999", "2000-2019", "2020-present"]
    df["era"] = pd.cut(df["year"], bins=bins, labels=labels)

    result = (
        df.groupby(["era", "theme"])["vote_average"]
        .agg(["count", "mean"])
        .reset_index()
    )

    return result
