from services.orders import GetOrderService


class GetOrders :

    def __init__(self):
        pass

    def get(self) :

        order_service = GetOrderService()

        return  order_service.get_orders()
