from services.pizzas import GetAllPizzasServices


class PizzaController: 

    def __init__(self):
        pass


    def get_pizzas(self) :

        #TODO: manejar error
        pizza_service = GetAllPizzasServices()
        return pizza_service.get()