from flask import Blueprint, jsonify

#controller
from controllers.orders import GetOrders

orders = Blueprint('orders', __name__)

@orders.route('/orders', methods=['GET'])
def get_orders() :
    
    orders = GetOrders()
    data = orders.get()

    return jsonify(data), 200