# Import statments
from base import Base
from dotenv import load_dotenv
import pymongo
import os

# Class Declaration:
class ToMongo(Base):
    '''
    Designed as a class to transport the data from the Base class to a MongoDB instance.
    Initializes an instance of the inherited class.
    
    Defined methods are as follows:
    upload_one_by_one: Uploads pieces of information to a database one by one over an iterable structure.
    upload_collection: upload an entire document of items to MongoDB
    delete_collection: drops an entire collection of data
    '''
    
    def __init__(self, user=os.getenv('USERNAME'), password=os.getenv('PASSWORD')):
        # Initialize the instance of our inherited class:
        Base.__init__(self)
        # Load the env variables:
        load_dotenv()
        self.user = user
        self.password = password
        self.mongo_url = os.getenv('NU')
        #Connect to PyMongo
        self.client = pymongo.MongoClient(self.mongo_url)
        # Create a database
        self.db = self.client.db
        # Create a collection:
        self.cards = self.db.cards
        # Set dataframe index to the id column:
        self.df.set_index('id', inplace=True)
        
    def upload_collection(self):
        '''
        Upload an entire collection of items to MongoDB.
        BEWARE! THERE IS A MAXIMUM UPLOAD SIZE
        Limitations to the amount of data that you can upload at once.
        '''
        self.cards.insert_many([self.df.to_dict()])
    
    def upload_one_by_one(self):
        '''
        Upload all our items to MongoDB, one-by-one. 
        This method will take longer, but will ensure all our data is uploaded correctly!
        '''
        for i in self.df.index:
            self.cards.insert_one(self.df.loc[i].to_dict())
        
if __name__ == '__main__':
    c = ToMongo()
    print('Successful Connection to Client Object')
    c.upload_one_by_one()
    print('Successfully Uploaded all Card Info to Mongo')
