from db import init_db
from bson import json_util
import json

from models.pizza import PizzaModel

class PizzaRepository :

    _client = init_db()
    _db = _client['pizzadb']

    def __init__(self):
        pass

    
    def get_all(self) :
        
        pizzas = json.loads( json_util.dumps( self._db['pizza'].find() ) )
        list_pizzas = []
        
        for item in pizzas :
            pizza_model = PizzaModel(item['_id']['$oid'], item['name'], item['ingredients'])

            pizza = {
                'namePizza': pizza_model.name,
                'quantity': pizza_model.ingredients,
                'id': pizza_model.id
            }

            list_pizzas.append(pizza)
        
        return list_pizzas


    def get_one(self) :
        pass