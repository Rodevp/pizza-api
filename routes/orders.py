from flask import Blueprint, jsonify

#controller
from controllers.orders import GetOrders

orders = Blueprint('orders', __name__)

@orders.route('/orders', methods=['GET'])
def get_orders() :
    
    try :
        
        orders = GetOrders()
        data = orders.get()
        
        return jsonify(data), 200

    except ValueError as err :
        
        return jsonify({
            'message': err
        }),  500
    

@orders.route('/orders/<id>', methods=['GET'])
def get_order(id) :
    try :
        
        orders = GetOrders()
        data = orders.get_one(id)
        
        return jsonify(data), 200

    except ValueError as err :
        
        return jsonify({
            'message': f'{err}'
        }),  400