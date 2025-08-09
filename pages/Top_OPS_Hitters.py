import streamlit as st
from data.data_clean import batting_df
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import numpy as np
from data.constants import MLB_TEAM_COLORS

def bar_chart(df, stat_col, title):
    df_sorted = df.sort_values(stat_col, ascending=True)
    
    colors = [MLB_TEAM_COLORS.get(team, '#888888') for team in df_sorted['Tm']]
    
    fig, ax = plt.subplots()
    ax.barh(df_sorted['Name'] + '\n' + df_sorted['Tm'], df_sorted[stat_col], color=colors)
    
    ax.set_xlabel(stat_col)
    ax.set_title(title)
    st.pyplot(fig)


month = datetime.datetime.now()
month = month.strftime('%B')

st.subheader(f'Top OPS Hitters for {month}')

pa_cutoff = st.slider("PA percentile threshold", 0, 100, 33)
pa_threshold = np.percentile(batting_df["PA"], pa_cutoff)

eligable_avg_leaders = batting_df[batting_df['PA']> pa_threshold]
ops_leaders = eligable_avg_leaders.sort_values(by='OPS', ascending=False)
ops_leaders = ops_leaders[['Name', 'Age', 'Tm', 'OPS', 'PA']]
st.dataframe(
    ops_leaders,
    column_config={
        'Name': st.column_config.TextColumn('Player'),
        'Tm': st.column_config.TextColumn('Team'),
        'PA': st.column_config.TextColumn('PA'),
        'OPS': st.column_config.TextColumn('OPS') 
    },
    hide_index=True,
    use_container_width=True
)
st.write(bar_chart(ops_leaders.head(5), 'OPS', 'Top 5 OPS Hitters this month'))