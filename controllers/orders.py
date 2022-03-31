from services.orders import GetOrderService


class GetOrders :

    def __init__(self):
        pass

    def get(self) :

        try :
            order_service = GetOrderService()
        except ValueError as err :
            
            raise ValueError(err)
        
        return  order_service.get_orders()
    

    def get_one(self, id) :

        try :
            order_service = GetOrderService()
        except ValueError as err :
            
            raise ValueError(err)

        return order_service.get_order(id)