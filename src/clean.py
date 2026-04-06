import pandas as pd
from fetch import fetch_all_movies

# TODO: map genre_ids to genre names using TMDB /genre/movie/list endpoint


def clean_data(theme):

    raw = fetch_all_movies(theme)
    df = pd.DataFrame(raw)
    df = df[["title", "release_date", "vote_average", "vote_count", "genre_ids"]]
    df.to_csv(f"data/{theme}_raw.csv", index=False)
