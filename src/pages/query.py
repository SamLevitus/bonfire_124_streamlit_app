from pathlib import Path
import streamlit as st
import sys
import os

# Grab the filepath:
filepath = os.path.join(Path(__file__).parents[1])
print(filepath)

# Insert the filepath into the system:
sys.path.insert(0, filepath)

# Import the ToMongo Class now:
from to_mongo import ToMongo

# Instantiate the class:
c = ToMongo()
st.header('Query Page')
st.write('This page will search our database for any card name you input. Spelling currently must be exact.')
# Now we query the database
# '''
# This is to return information about a card from our database to a user in a friendly format.

# Query the database based off a user input, then display that information back to them.

# Why is this important?

# When a user wants to query(or search) information, and we don't have a local file to reference, we will want to be able to
# plug and play into a database. 

# Also, when build dashboards and applications, knowing how to allow a user to retreive information is critical.

# How will we go about this?
# First, we will use the texct_input function to allow a user to input a card name:
# When we find a match, we will return all info about the card to the user
# The .find() function will give us everythin we need!
# '''

answer = st.text_input('Enter a card name:', value = 'Sol Ring')
st.write(list(c.cards.find({'name': answer})))