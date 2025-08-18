import streamlit as st
import pandas as pd
from data.data_clean import batting_df
from data.data_fetch import get_monthly_batting_stats

st.title('Top MLB Players this Month')
st.subheader('Raw Data For Hitters This Month')
st.write(batting_df)


