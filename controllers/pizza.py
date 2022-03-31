from services.pizzas import GetAllPizzasServices


class PizzaController: 

    def __init__(self):
        pass


    def get_pizzas(self) :

        try :
            pizza_service = GetAllPizzasServices()
        except ValueError as err :
            raise ValueError(err)
        
        return pizza_service.get()