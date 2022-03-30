from services.orders import GetOrdersService


class GetOrders :

    def __init__(self):
        pass

    def get(self) :

        order_service = GetOrdersService()

        return  order_service.get_orders()
