from flask import Blueprint, jsonify


orders = Blueprint('orders', __name__)

@orders.route('/orders', methods=['GET'])
def get_orders() :
    
    data = [{
        "order-id": 0,
        "order-quantity": 3
    }]

    return jsonify(data), 200