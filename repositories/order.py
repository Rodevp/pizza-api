from db import init_db
from bson import json_util
import json

class OrderRepository :

    _client = init_db()

    def __init__(self) :
        pass

    def get_all(self) :

        db = self._client['pizzadb']
        collection = db['orders']
        list_orders = []

        for item in collection.find() :
            list_orders.append(item)


        return json.loads( json_util.dumps(list_orders) )