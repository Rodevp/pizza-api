from pymongo import MongoClient


def init_db():
    try:
        
        client = MongoClient('localhost', 27017)
        
        print('***connect***')

        return client

    except Exception as err:
        print(err)


