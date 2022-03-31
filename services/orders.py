from repositories.order import OrderRepository

class GetOrderService :

    def __init__(self) :
        pass


    def get_orders(self) :

        try :
            order_repository = OrderRepository()
        except Exception as err :
            raise ValueError('server internal error')

        if len( order_repository.get_all() ) == 0 :
            return []
    
        return order_repository.get_all()


    def get_order(self, id) : 
        
        try :
            order_repository = OrderRepository()
        except Exception as err :
            raise ValueError('error')
        
        order = order_repository.get(id)

        if order == None :
            raise ValueError('Id no valido')

        return order