# Imports for image return page
import streamlit as st
import requests
import os
import sys
from PIL import Image
from pathlib import Path
from io import BytesIO

# Create a filepath to the system where the main folder for the app lives:
filepath = os.path.join(Path(__file__).parents[1])

# Now I can insert the path and freely import my mongo class
sys.path.insert(0, filepath)
from to_mongo import ToMongo
# When I click on the page:
st.title("Image Return Page")

# We create a instance of our Mongo Class
c = ToMongo()

# Then we take an input from a user:
answer = st.text_input("Enter a Card Name:", value = 'Sol Ring')

# Transform that input into a card name!
card = list(c.cards.find({'name':answer}))[0]['image_uris']['normal']
st.image(Image.open(BytesIO(requests.get(card).content)))
