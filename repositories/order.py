from db import init_db
from bson import json_util, ObjectId
import json

from models.order import OrderModel

class OrderRepository :

    _client = init_db()
    _db = _client['pizzadb']

    def __init__(self) :
        pass


    def get_all(self) :

        collection = json.loads( json_util.dumps( self._db['orders'].find() ) )
        list_orders = []

        for item in collection :
            order_model = OrderModel(item['quantity'], item['namePizza'], item['_id']['$oid'])
            
            order = {
                'namePizza': order_model.name_pizza,
                'quantity': order_model.quantity,
                'id': order_model.id
            }

            list_orders.append(order)


        return list_orders


    def get(self, id) :
        
        order = json.loads( json_util.dumps( self._db['orders'].find_one( {'_id': ObjectId(id) } ) ) )
        return order

