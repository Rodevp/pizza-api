from db import init_db
from bson import json_util
import json

class PizzaRepository :

    _client = init_db()
    _db = _client['pizzadb']

    def __init__(self):
        pass

    
    def get_all(self) :
        pizzas = json.loads( json_util.dumps( self._db['pizza'].find() ) )
        list_pizzas = [ item for item in pizzas ] 
        return list_pizzas


    def get_one(self) :
        pass