from dotenv import load_dotenv
import os
import requests

load_dotenv()
key = os.getenv("TMDB_API_KEY")


def check_connection():
    response = requests.get(
        "https://api.themoviedb.org/3/configuration",
        headers={"Authorization": f"Bearer {key}"},
    )

    if response.status_code == 200:
        print("connection succesful!")


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


fetch_movies("war")
