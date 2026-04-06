import streamlit as st
import pandas as pd
from analyse import analyse

st.title("Mono — Narrative")

war = pd.read_csv("data/war_raw.csv")
peace = pd.read_csv("data/peace_raw.csv")

war["theme"] = "war"
peace["theme"] = "peace"
df = pd.concat([war, peace])

result = analyse(df)

result.columns = ["era", "theme", "count", "mean_rating"]

chart_data = result.pivot(index="era", columns="theme", values="mean_rating")

st.subheader("Average Audience Rating by Era")
st.caption(
    "Comparing global perception of war vs. peace themed films across three eras."
)

st.line_chart(chart_data, width="stretch")

st.subheader("Number of Films by Era")
st.caption("How much content exists per theme across each era.")

count_data = result.pivot(index="era", columns="theme", values="count")
st.bar_chart(count_data, use_container_width=True)

with st.expander("View raw data"):
    st.dataframe(df)
