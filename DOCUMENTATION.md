# Mono — Narrative
>
> Contrasting global audience perception of opposing themes in film and television over time.

## Status

🟡 In Progress — April 2026

## Stack

- Python 3.14
- pandas · requests · matplotlib · streamlit
- TMDB API · IMDb datasets (Kaggle)

## Theme Pairs

- War ↔ Peace
- Conflict ↔ Unity

## Structure

mono-narrative/
├── data/        ← raw and cleaned datasets
├── notebooks/   ← exploration and analysis
├── src/         ← Python modules
│   ├── fetch.py     ← API calls
│   ├── clean.py     ← data cleaning
│   ├── analyse.py   ← contrast logic
│   └── app.py       ← Streamlit dashboard
└── assets/      ← exports and static files

## Setup

git clone <https://github.com/disposably-mono/mono-narrative>
cd mono-narrative
python3 -m venv .venv && source .venv/bin/activate
pip install pandas requests matplotlib streamlit python-dotenv

## Usage

_To be documented as build progresses._

## Notes

_Running log of decisions and findings — updated weekly._
