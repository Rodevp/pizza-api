from pymongo import MongoClient


def init_db():
    try:
        
        client = MongoClient('localhost', 27017)
        
        print('***connect***')

        print(client['test-database'])

        return client

    except Exception as err:
        print(err)


