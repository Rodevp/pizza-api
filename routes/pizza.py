from flask import Blueprint, jsonify

from controllers.pizza import PizzaController

pizzas = Blueprint('pizza', __name__)

@pizzas.route('/pizzas', methods=['GET'])
def get_all() :
    
    try :
    
        pizzas = PizzaController()
        return jsonify( pizzas.get_pizzas() ), 200
    
    except ValueError as err :
        
        return jsonify({
            'message': f'{err}'
        }), 400