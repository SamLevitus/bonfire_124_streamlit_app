from base import Base
from dotenv import load_dotenv
import pymongo
import os

# Class declaration:
class ToMongo(Base):
    '''
    Designed as a class to transport the data from the Base class to a MongoDB instance
    Initializes an instance of the inherited class.

    Defined methods are as follows:
    upload_one_by_one: uploads pieces of information to a database one by one over and iterable structure
    upload_collection: upload an entire document of itmes to MongoDB
    delete_collection: drops an entire collection of data
    '''

    def __init__(self):
        # Initialize the instace of our inherited class
        Base.__init__(self)
        # Load the env variables
        load_dotenv()
        self.user = os.getenv('USERNAME')
        self.password = os.getenv("PASSWORD")
        self.mongo_url = os.getenv('NU')
        # Connect to PyMongo
        self.client = pymongo.MongoClient(self.mongo_url)
        # Create a database
        self.db = self.client.db
        # Create a colleciton
        self.cards = self.db.cards
        # Set dataframe index to the id column
        self.df.set_index('id', inplace=True)

    def upload_collection(self):
        '''
        Upload an entire collection of items to MongoDB
        BEWARE! THERE IS A MAXIMUM UPLOAD SIZE
        limitations to the amount of data that you can upload at once
        '''

        self.cards.insert_many([self.df.to_disct()])

    def upload_one_by_one(self):
        '''
        Upload all our items to MongoDB, one-by-one
        This method will take longer, but will ensure that all our data is uploaded correctly
        '''
        for i in self.df.index:
            self.cards.insert_one(self.df.loc[i].to_dict())

if __name__ == "__main__":
    c = ToMongo()
    print('Successful connection to Client Object')
    c.upload_one_by_one()
    print('Successfully uploaded to MongoDB')
