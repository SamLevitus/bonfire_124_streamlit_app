import streamlit as st

st.title('Summary page for MTG Tracer')

st.text('''
        This application was designed to show our studens how to buil dna application and a dashboard using streamlit. 
        The goal is to showcase how we can use streamlit to create a multi-page application or dashboard and effectively communicate information.
        By returning images, we can grab an information from a database and have learned about how the info is stored and returned by MongoDB.
        By creating this summary page, we gained understanding on how we can create these outlines on the way we write out code
        and how we create the funcionality that we do.
        '''
        )

st.image('https://logos-download.com/wp-content/uploads/2016/09/MongoDB_logo_Mongo_DB.png')
st.write('''
         We spent last week talking over SQL and we spent this week
         of the disadvantes of using both technologies. 
         We chose to use the NoSQL format because the data was large and could fit into a tabular structure,
         however, a document oriented structure suited the data better and has proven to be
         faster.

         Also, using a database structure is faster than relying on a localized storage method.
         ''')

st.write('Other Technologies Used: streamlit, python, pandas, ML modeling')
