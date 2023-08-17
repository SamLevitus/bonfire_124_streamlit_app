import streamlit as st
from pathlib import Path
import sys
import os

filepath = os.path.join(Path(__file__).parents[1])
sys.path.insert(0, filepath)

from model import dummy_func, Model
m = Model()

st.title('Recommended Cards:')

card_name = st.text_input(
    "Please enter the full name of the card you would like recommedations for:"
)
if st.button('Submit Card'):
    try:
        st.image(m.img_return(card_name))
        img_list = m.recommended_cards(card_name)
        st.write(
            f'Here are the {len(img_list)} cards that would be recommended based off the card: {card_name.title()}'
        )
        col1,col2,col3 = st.columns(3)
        col1.image(img_list[0:3])
        col2.image(img_list[3:6])
        col3.image(img_list[6:10])
    except BaseException:
        st.error(f'''
                 {card_name.title()} is an invalid card name.
                 Please try again with a valid card name. If the 
                 card name is valid, please try typing it the EXACT way
                 it appears on the face of the card.
                 ''')