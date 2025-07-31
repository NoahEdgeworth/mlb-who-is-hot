import streamlit as st
from data.data_clean import batting_df
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import numpy as np

def bar_chart(df, stat_col, title):
    df_sorted = df.sort_values(stat_col, ascending=True)
    fig, ax = plt.subplots()
    ax.barh(df_sorted['Name'], df_sorted[stat_col])
    ax.set_xlabel(stat_col)
    ax.set_title(title)
    st.pyplot(fig)


month = datetime.datetime.now()
month = month.strftime('%B')

st.subheader(f'Top OPS Hitters for {month}')

pa_cutoff = st.slider("PA percentile threshold", 0, 100, 33)
pa_threshold = np.percentile(batting_df["PA"], pa_cutoff)

eligable_avg_leaders = batting_df[batting_df['PA']> pa_threshold]
hr_leaders = eligable_avg_leaders.sort_values(by='OPS', ascending=False)
hr_leaders = hr_leaders[['Name', 'Age', 'Tm', 'OPS', 'PA']]
st.write(hr_leaders.head(5))
st.write(bar_chart(hr_leaders.head(5), 'OPS', 'Top 5 OPS Hitters this month'))