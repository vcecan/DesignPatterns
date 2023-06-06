from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

class Builder(ABC):
    @property
    @abstractmethod
    def pizza(self) -> None:
        pass

    @abstractmethod
    def make_crust(self) -> None:
        pass

    @abstractmethod
    def add_sauce(self) -> None:
        pass

    @abstractmethod
    def add_mushroms(self) -> None:
        pass

    @abstractmethod
    def add_olives(self) -> None:
        pass

    @abstractmethod
    def add_pepperoni(self) -> None:
        pass

    @abstractmethod
    def add_peper(self) -> None:
        pass

    @abstractmethod
    def add_tomato(self) -> None:
        pass

    @abstractmethod
    def add_basilic(self) -> None:
        pass

    @abstractmethod
    def add_prosciutto(self) -> None:
        pass

    @abstractmethod
    def add_cheese(self) -> None:
        pass

    @abstractmethod
    def add_8(self) -> None:
        pass

    @abstractmethod
    def add_10(self) -> None:
        pass

    @abstractmethod
    def add_12(self) -> None:
        pass


class Pizza_builder(Builder):
    def __init__(self):
        self._pizza = Pizza()

    def reset(self) -> None:
        self._pizza = Pizza()

    @property
    def pizza(self) -> Pizza:
        pizza = self._pizza
        self.reset()
        return pizza

    def make_crust(self) -> None:
        self._pizza.add("thin crust")

    def add_sauce(self) -> None:
        self._pizza.add("tomato sauce")

    def add_tomato(self) -> None:
        self._pizza.add("tomatoes")

    def add_olives(self) -> None:
        self._pizza.add("olives")

    def add_mushroms(self) -> None:
        self._pizza.add("mushroms")

    def add_peper(self) -> None:
        self._pizza.add("peper")

    def add_pepperoni(self) -> None:
        self._pizza.add("pepperoni")

    def add_basilic(self) -> None:
        self._pizza.add("basilic")

    def add_prosciutto(self) -> None:
        self._pizza.add("prosciuto")

    def add_cheese(self) -> None:
        self._pizza.add("cheese")

    def add_8(self) -> None:
        self._pizza.add('8')
    def add_10(self) -> None:
        self._pizza.add('10')
    def add_12(self) -> None:
        self._pizza.add('12')





class Pizza():
    def __init__(self) -> None:
        self.components = []
        self.price = None

    def add(self, part: Any) -> None:
        self.components.append(part)


    def add_p(self,pric :Any) ->None:
        self.price.append(pric)

    def list_components(self) -> None:
        print(f"Pizza components: {', '.join(self.components)}", end="")

    @property
    def get_components(self) -> None:
        return self.components


    def clone(self) -> Pizza:
        return Pizza(components=self.components,price=self.price)


class Baker:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def bake_margheritta(self) -> None:
        self.builder.make_crust()
        self.builder.add_sauce()
        self.builder.add_tomato()
        self.builder.add_cheese()
        self.builder.add_basilic()
        self.builder.add_8()

    def bake_pepperoni(self) -> None:
        self.builder.make_crust()
        self.builder.add_sauce()
        self.builder.add_cheese()
        self.builder.add_pepperoni()
        self.builder.add_10()


    def bake_capriciosa(self) -> None:
        self.builder.make_crust()
        self.builder.add_sauce()
        self.builder.add_mushroms()
        self.builder.add_olives()
        self.builder.add_prosciutto()
        self.builder.add_cheese()
        self.builder.add_12()

    def bake_custom(self) -> None:
        self.builder.make_crust()
        self.builder.add_sauce()


if __name__ == '__main__':
    baker = Baker()
    builder = Pizza_builder()
    baker.builder = builder

    print('Standard margherita')
    baker.bake_margheritta()
    components=builder.pizza.get_components
    print(f'\nPizza components:{components[0:-1]}\n')
    print(f'\nprice:{components[-1]}\n')

    # print(f'\nprice:{builder.pizza.get_price}')

    print("\n")

    print('Capriciosa')
    baker.bake_capriciosa()
    builder.pizza.list_components()