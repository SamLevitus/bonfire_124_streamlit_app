from pathlib import Path
import streamlit as st
import sys
import os

filepath = os.path.join(Path(__file__).parents[1])
print(filepath)

# Insert filepath into system
sys.path.insert(0, filepath)

# Import the two mongo classes
from to_mongo import ToMongo

# Instantiate the class
c = ToMongo()
st.header('Query Page')
st.write('This page will search our database card information. Spelling must be exact.')


# Query the database
'''
This is to return information about a card from our database to a user in a friendlier format

Query the database based off a user input, then display that information


When a user wants to query information and we don't have a local file to reference,

Also, when bulding dashboards and applications, knowing how to allow a user to retrieve information information is critical

First we will use the text_input function to allow a user to input a card name:
When we find a match, we will return all info about the card to the user

'''

answer = st.text_input('Enter a card name:', value = 'Sol Ring')
st.write(list(c.cards.find({'name': answer})))