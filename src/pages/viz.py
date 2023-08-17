import plotly.express as px
from pathlib import Path
import streamlit as st
import pandas as pd
import os

filepath = os.path.join(Path(__file__).parents[1], 'data\oracle_cards.csv')
df = pd.read_csv(filepath, low_memory=False)

vist_to_use = ['scatterplot', 'histogram', 'bar char']
type_vis = st.selectbox('Select the typeof visualization you would like')

if type_vis == 'scatterplot':
    answer = st.selectbox('Selece a column to visualize on the x axis')
    answer2 = st.selectbox('Selece a column to visualize on the y axis')
   
    if answer:
        try:
            st.plotly_chart(px.scatter(df,x=answer, y=answer2, hover_data=['name'], use_containers=True))
        except BaseException:
            print('Error visualizing this column')