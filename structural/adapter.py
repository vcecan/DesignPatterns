import sys

sys.path.insert(0, 'D:/univer/tmps/tmps_proiect/creational')


from factory_prototype import MargherittaPizzaPrototype,PepperoniPizzaPrototype,CapriciosaPizzaPrototype
from builder import Pizza
from typing import List


class PizzaIngredientRemover:
    def remove(self, pizza: Pizza, ingredient: str) -> Pizza:
        if ingredient in pizza.components:
            pizza.components.remove(ingredient)
        return pizza




class PizzaIngredientRemoverAdapter(PizzaIngredientRemover):
    def remove(self, pizza: Pizza, allergen: str) -> Pizza:
        if allergen == 'gluten':
            return super().remove(pizza, 'flour')
        elif allergen == 'dairy':
            return super().remove(pizza, 'cheese')
        elif allergen == 'nuts':
            return super().remove(pizza, 'nuts')
        elif allergen == 'basilic':
            return super().remove(pizza, 'basilic')
        else:
            return super().remove(pizza, allergen)
            #return pizza


class PizzaManager:
    def __init__(self):
        self._prototypes: Dict[str, PizzaPrototype] = {
            "Margherita": MargherittaPizzaPrototype(),
            "Pepperoni": PepperoniPizzaPrototype(),
            "Capriciosa": CapriciosaPizzaPrototype(),
        }

    def get_pizza(self, name: str, extras: List[str] = []) -> Pizza:
        pizza = self._prototypes[name].clone()
        for extra in extras:
            pizza.add(extra)
        return pizza

if __name__ == '__main__':
    pizza_manager = PizzaManager()
    ingredient_remover = PizzaIngredientRemoverAdapter()
    while True:
        client_code(pizza_manager, ingredient_remover)
