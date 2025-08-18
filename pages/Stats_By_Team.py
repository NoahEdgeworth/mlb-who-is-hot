import streamlit as st
from data.data_clean import batting_df
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import numpy as np

st.write('Coming Soon...')


team_df = (
    batting_df.groupby("Tm")
    .agg({
        "PA": "sum",
        "AB": "sum",
        "H": "sum",
        "2B": "sum",
        "3B": "sum",
        "HR": "sum",
        "R": "sum",
        "RBI": "sum",
        "SB": "sum",
        "BB": "sum",
        "HBP": "sum",
        "SF": "sum"
    })
    .reset_index()
)

# Temp remove rows that have multiple teams listed in the team column for a single player
team_df = team_df[~team_df['Tm'].str.contains(',', na=False)]

# Calculate singles
team_df["1B"] = team_df["H"] - team_df["2B"] - team_df["3B"] - team_df["HR"]

# Calculate AVG, OBP, SLG, OPS
team_df["AVG"] = team_df["H"] / team_df["AB"]
team_df["OBP"] = (team_df["H"] + team_df["BB"] + team_df["HBP"]) / (
    team_df["AB"] + team_df["BB"] + team_df["HBP"] + team_df["SF"]
)
team_df["SLG"] = (
    team_df["1B"] + 2*team_df["2B"] + 3*team_df["3B"] + 4*team_df["HR"]
) / team_df["AB"]
team_df["OPS"] = team_df["OBP"] + team_df["SLG"]


stat_options = ["AVG", "OBP", "SLG", "OPS", "HR", "R", "RBI", "SB"]
selected_stat = st.selectbox("Choose a stat to sort teams by:", stat_options)
team_df = team_df.sort_values(selected_stat, ascending=False)
top_team = team_df.sort_values(selected_stat, ascending=False).iloc[0]
team_name = top_team['Tm']
stat = top_team[selected_stat].round(3)
st.write(f'🏆 League Leader: {team_name} {stat} {selected_stat}')
st.dataframe(team_df, hide_index=True)
