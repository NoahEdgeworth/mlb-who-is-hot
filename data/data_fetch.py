from pybaseball import batting_stats_range
from datetime import date, timedelta
import pandas as pd
import streamlit as st

@st.cache_data
def get_monthly_batting_stats():
    today = date.today()
    first_of_month = today.replace(day=1)

    if today.day <= 6:
        # Use last full month if we are in the first week of new month
        last_month = first_of_month - timedelta(days=1)
        start_date = last_month.replace(day=1)
        end_date = last_month
    else:
        # Else, use current month
        start_date = first_of_month
        end_date = today
    return batting_stats_range(start_dt=str(start_date), end_dt=str(end_date))

