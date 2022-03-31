from models.order import OrderModel
from repositories.order import OrderRepository

class GetOrderService :

    def __init__(self) :
        pass


    def get_orders(self) :

        order_repository = OrderRepository()
    
        return order_repository.get_all()