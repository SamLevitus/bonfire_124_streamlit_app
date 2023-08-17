from pathlib import Path
from PIL import Image
from io import BytesIO
import pandas as pd
import requests
import pickle
import ast
import os
import re

# First step: Establish the data folder directory:
folder_dir = os.path.join(Path(__file__).parents[0], 'data')
print(folder_dir)

# Second step: For the vectorizer:
# We need to create a dummy function that takes in a doc and returns the doc
def dummy_func(doc):
    return doc

class Model:
    def __init__(self):
        # instantiating the dataframe
        self.df = pd.read_csv(f'{folder_dir}/oracle_cards.csv', low_memory=False)
        # loading in our pretrained model
        self.nnm = pickle.load(open(f'{folder_dir}/model', 'rb')) # load in saved model for nearest neighbors
        # creating our own list of stop words
        self.stop_words = ['on', 'the', 'of', 'and']
        self.cap_stop_words = [w.title() for w in self.stop_words]      

    def card_name_fix(self, card_name:str):
        # created this string object
        self.string = re.sub(
            r"[A-Za-z]+('[A-Za-z]+)?",              ## look at first word and first letter and make upper case, then check next word and make lower if word is not in stop words list. If it is, lowercase the whole word
            lambda x: x.group(0)[0].upper() +
            x.group(0)[1:].lower() if x.group(0) not in self.stop_words or self.cap_stop_words and 
            card_name.startswith(x.group(0)) else x.group(0).lower(), card_name
        )

        # split the string:
        self.split_str = self.string.split()
        print(self.split_str)
        c = 0
        for name in self.split_str:
            if '-' in name:
                name= name.title()
                c += 1
            elif name[1] == "'":
                name = name[0:3].upper() + name[3:]
                self.split_str[c] = name
                c += 1

            else:
                c +=1 # adding one to the index counter

        return ' '.join(self.split_str)
        # return self.val

    def nn(self, card_name:str):
        '''
        Input: card name - > str type object, received from the user

        Output: 9 recommended cards based on cosine similarity between each card mapped out by our model
        '''
        self.card_name = self.card_name_fix(card_name)
        self.vect = pickle.load(open(f'{folder_dir}/vect', 'rb'))
        self.names = []
        self.doc = self.vect.transform(
            self.df['lemmas'][self.df['name'] == self.card_name]
        )
        self.n_index = self.nnm.kneighbors(
            self.doc, return_distance=False
        )

        for index in self.n_index[0]:
            if index != self.df[self.df['name'] == self.card_name].index:
                self.names.append(self.df['name'][index])
        return self.names
    
    def img_return(self, card_name:str):
        '''
        input: card name as a string object

        the function will take a card string and return an image    
        output: full-detailed card image
        '''
        s=self.df[self.df['name'] == self.card_name_fix(card_name)]['image_uris']
        for k in s:
            img_dic = ast.literal_eval(k)
        img_str = img_dic['normal']
        response = requests.get(img_str)
        img = Image.open(BytesIO(response.content))
        return img
    
    def recommended_cards(self, card_name:str):
        names = self.nn(card_name)
        return [self.img_return(name) for name in names]
    

if __name__ == ('__main__'):
    c = Model()
    print(c.card_name_fix("d'vorrah"))