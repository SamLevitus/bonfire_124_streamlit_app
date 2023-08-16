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
        self.df = pd.read_csv(f'{folder_dir}/oracle_cards.csv', low_memory=False)
        self.nnm