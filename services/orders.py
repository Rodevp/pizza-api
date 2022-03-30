from repositories.order import OrderRepository

class GetOrderService :

    def __init__(self) :
        pass


    def get_orders(self) :

        order = OrderRepository()

        return  order.get_all()