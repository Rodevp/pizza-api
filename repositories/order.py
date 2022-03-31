from db import init_db
from bson import json_util
import json

from models.order import OrderModel

class OrderRepository :

    _client = init_db()

    def __init__(self) :
        pass


    def get_all(self) :

        db = self._client['pizzadb']
        collection = json.loads( json_util.dumps( db['orders'].find() ) )
        list_orders = []

        for item in collection :
            order_model = OrderModel(item['namePizza'], item['quantity'], item['_id']['$oid'])
            
            order = {
                'namePizza': order_model.name_pizza,
                'quantity': order_model.quantity,
                'id': order_model.id
            }

            list_orders.append(order)


        return list_orders