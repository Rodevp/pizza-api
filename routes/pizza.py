from flask import Blueprint, jsonify

from controllers.pizza import PizzaController

pizzas = Blueprint('pizza', __name__)

@pizzas.route('/pizzas', methods=['GET'])
def get_all() :
    pizzas = PizzaController()
    return jsonify( pizzas.get_pizzas() ), 200