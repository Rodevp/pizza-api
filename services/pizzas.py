from repositories.pizza import PizzaRepository

class GetAllPizzasServices :

    def __init__(self):
        pass
    

    def get(self) :

        try :
            pizza_repository = PizzaRepository()
        except Exception as err : 
            raise ValueError(':x')

        if len( pizza_repository.get_all() ) == 0 :
            return []

        return pizza_repository.get_all()
