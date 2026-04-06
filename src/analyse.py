import pandas as pd

war = pd.read_csv("data/war_raw.csv")
peace = pd.read_csv("data/peace_raw.csv")


def analyse():
    war["theme"] = "war"
    peace["theme"] = "peace"

    df = pd.concat([war, peace])

    df["year"] = df["year"].astype(int)

    bins = [1979, 1999, 2019, 2030]
    labels = ["1980-1999", "2000-2019", "2020-present"]
    df["era"] = pd.cut(df["year"], bins=bins, labels=labels)

    results = df.groupby(["era", "theme"])["vote_average"].agg(["count", "mean"])
    print(results)


analyse()
