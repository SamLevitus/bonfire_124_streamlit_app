import streamlit as st

st.title('My First Streamlit App')
st.text('Hello, World!')

st.title('Bonfire-124 MTG Tracer Application')
st.text('My first application that uses Pandas, Streamlit, Scikilearn, MongoDB, and Python to creat a MTG recognition system')

st.header('Here are the different pages of my application:')
st.subheader('Image Returnt ')
st.text('Image return: return an image of the requested card')

st.subheader('Summary')
st.text('Summary page explaining all the inner workings of of the app and the "why" behind each decision made')

st.subheader('Query')
st.text('Query: allow a user to enter a card name and return all information about it from our database')

st.subheader('Recommender')
st.text('A recommendation system that we will build to allow users to see recommended cards')