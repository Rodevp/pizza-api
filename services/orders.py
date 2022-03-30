from repositories.order import OrderRepository

class GetOrdersService :

    def __init__(self) :
        pass


    def get_orders(self) :

        orders = OrderRepository()

        return  orders.get_all()