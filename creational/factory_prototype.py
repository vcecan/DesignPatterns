from __future__ import annotations
from multimethod import multimeta
from abc import ABC, abstractmethod
from builder import Pizza,Baker,Pizza_builder
from typing import Dict,Any
from copy import deepcopy


class PizzaPrototype(Pizza):
    def add_component(self, component: Any) -> None:
        self.components.append(component)



class PepperoniPizzaPrototype(PizzaPrototype):
    def __init__(self):
        self._pizza = self.create_pizza()

    def create_pizza(self) -> Pizza:
        builder = Pizza_builder()
        baker = Baker()
        baker.builder = builder
        baker.bake_pepperoni()
        return builder.pizza

    def clone(self) -> Pizza:
        return deepcopy(self._pizza)

    def get_price(self) -> float:
        return 7.0


class CapriciosaPizzaPrototype(PizzaPrototype):
    def __init__(self):
        self._pizza = self.create_pizza()

    def create_pizza(self) -> Pizza:
        builder = Pizza_builder()
        baker = Baker()
        baker.builder = builder
        baker.bake_capriciosa()
        return builder.pizza

    def clone(self) -> Pizza:
        return deepcopy(self._pizza)



class MargherittaPizzaPrototype(PizzaPrototype):
    def __init__(self):
        self._pizza = self.create_pizza()

    def create_pizza(self) -> Pizza:
        builder = Pizza_builder()
        baker = Baker()
        baker.builder = builder
        baker.bake_margheritta()
        return builder.pizza

    def clone(self) -> Pizza:
        return deepcopy(self._pizza)


    def get_price(self) -> float:
        return 5.0

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
