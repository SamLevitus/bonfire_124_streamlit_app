import plotly.express as px
from pathlib import Path
import streamlit as st
import pandas as pd
import os

# Establish a filepath to the oracle_cards.csv file
filepath = os.path.join(Path(__file__).parents[1], 'data/oracle_cards.csv')
df = pd.read_csv(filepath, low_memory=False)

# Take in a user input:
vis_to_use = ['scatterplot', 'histogram', 'bar chart']
type_vis = st.selectbox('Select the type of Visualization you would like to see:', options=vis_to_use)

if type_vis == 'scatterplot':
    answer = st.selectbox('Select a Column to Visualize on the X-axis:', options=sorted(list(df.columns)))
    answer2 = st.selectbox('Select a column to visualize on the Y-axis:', options = sorted(list(df.columns)))
# answer = st.selectbox('Select a Column to Visualize:', options=list(df.columns))
    if answer:
        try:
            st.plotly_chart(px.scatter(df, x=answer, y=answer2, hover_data=['name']), use_container_width=True)
        except BaseException:
            print("Error visualizing this column")