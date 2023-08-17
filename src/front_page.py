import streamlit as st

st.title("Bonfire-124 MTG Tracer Application")
st.text("My first application that uses Pandas, Streamlit, Scikitlearn, SpaCy, MongoDB, and Python to create a MTG Recommendation System")

st.header('Here are the different pages of my application:')
st.subheader('Image Return')
st.text('Image Return: Return an image of the requested card')

st.subheader("Summary")
st.text('Summary page explaining all the inner workings of the app and the "why" behind each decision made')

st.subheader('Query')
st.text('Query: Allow a user to enter a card name and return all information about it from our database')

st.subheader('Recommender')
st.text('A recommendation system that we will build to allow users to see recomended cards')