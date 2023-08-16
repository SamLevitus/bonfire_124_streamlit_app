# Imports
import pandas as pd
import pickle
import re
import spacy
from base import Base
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

folder_dir = f'{Path(__file__).parents[0]}\\data'

folder_dir = folder_dir[0].upper()+ folder_dir[1:]

Base().df.to_csv(f'{folder_dir}\\oracle_cards.csv', index=False)

df = pd.read_csv(f'{folder_dir}\\oracle_cards.csv', low_memory=False)
print('Created the dataframe')

df.dropna(subset=['oracle_text'], axis = 0, inplace=True)

df.drop(df.index[df['oracle_text'] == ''], inplace=True)
print('Dropped all values that were null/empty')

df['oracle_text'] = [re.sub('[^0-9a-zA-Z]+', " ",i) for i in df.oracle_text]
print('Regex was successful')

# Load in the SpaCy Dictionary:
nlp = spacy.load('en_core_web_md')
lemmas = []
for doc in df['oracle_text']:
    lemmas.append([token.lemma_.lower().strip() for token in nlp(str(doc)) if (token.is_stop != True) and (token.is_punct != True) and (token.is_space != True)])

df['lemmas'] = lemmas
print('Successfully create a lemma column in a dataframe object')
print(df)

# Save back over the csv file with the new lemma column
df.to_csv(f'{folder_dir}\\oracle_cards.csv', index=False)

def dummy_func(doc):
    return doc

vect = TfidfVectorizer(preprocessor=dummy_func,
                      token_pattern=None,
                      tokenizer=dummy_func)

vect.fit(df['lemmas'])

pickle.dump(vect, open(f'{folder_dir}\\vect', 'wb'))
pickle.dump(vect.vocabulary_, open(f'{folder_dir}\\vect_vocab', 'wb'))
print('Successfully saved the vect and the vocab')

# Create the model and save that to a file
model = NearestNeighbors(n_neighbors=10)
model.fit(vect.transform(df.lemmas))
pickle.dump(model, open(f'{folder_dir}\\model', 'wb'))
print('Model has been created and saved')
print('All required updates have been completed.')