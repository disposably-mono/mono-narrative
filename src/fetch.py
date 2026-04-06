from dotenv import load_dotenv
import os
import requests

load_dotenv()

# TODO: move key loading into a config module later
key = os.getenv("TMDB_API_KEY")


def check_connection():
    response = requests.get(
        "https://api.themoviedb.org/3/configuration",
        headers={"Authorization": f"Bearer {key}"},
    )

    if response.status_code == 200:
        print("connection succesful!")
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return []


def fetch_movies(theme, page=1):
    response = requests.get(
        "https://api.themoviedb.org/3/search/movie",
        headers={"Authorization": f"Bearer {key}"},
        params={"query": theme, "page": page},
    )

    data = response.json()

    results = data["results"]

    print(f"Fetched {len(results)} movies for '{theme}' — page {page}")

    return results


def fetch_all_movies(theme):
    all_results = []
    for page in range(1, 6):
        results = fetch_movies(theme, page)
        all_results += results

    return all_results
