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


check_connection()
