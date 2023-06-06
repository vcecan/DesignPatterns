# from abc import ABC, abstractmethod
# from typing import List
# import sys
# sys.path.insert(0, 'D:/univer/tmps/tmps_proiect/creational')
# from factory_prototype import MargherittaPizzaPrototype,PepperoniPizzaPrototype,CapriciosaPizzaPrototype
# from builder import Pizza
#
# from typing import List
#
#
# def find_numbers_in_array(strings):
#
#
#     for text in strings:
#         if text.isdigit():
#             return text
#
#
# class PizzaDecorator(Pizza, ABC,):
#     def __init__(self, pizzas):
#         self.pizzas = pizzas
#
#     def get_discount(self) -> float:
#         pass
#
#     @abstractmethod
#     def is_eligible_for_discount(self,pizzas) -> None:
#         pass
#
#
# class DiscountDecorator(PizzaDecorator):
#     @property
#     def is_eligible_for_discount(self,pizzas) -> bool:
#         if len(pizzas)>=3:
#             return True
#
#     def get_discount(self,pizzas) -> float:
#         total_price = 0
#         for i in range(len(self.pizzas)):
#             components = self.pizzas[i].components
#             price = find_numbers_in_array(components)
#             components.remove(price)
#             total_price += int(price)
#         if self.is_eligible_for_discount(pizzas) == True:
#             total_price = total_price * 0.9
#         return total_price
