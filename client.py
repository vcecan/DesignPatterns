import sys

sys.path.insert(0, 'D:/univer/tmps/tmps_proiect/creational')
sys.path.insert(0, 'D:/univer/tmps/tmps_proiect/structural')
sys.path.insert(0, 'D:/univer/tmps/tmps_proiect/behavioral')
from factory_prototype import PizzaManager
from adapter import PizzaIngredientRemoverAdapter,PizzaIngredientRemover
from memento import Originator,Caretaker
from chain import AddToppingHandler,RemoveToppingHandler,OrderHandler


class Order:
    def __init__(self,price,pizzas):
        self.price=price
        self.pizzas=pizzas

    def get_price(self):
        return self.price


class DiscountDecorator:
    def __init__(self, component, discount_percentage):
        self.component = component
        self.discount_percentage = discount_percentage


    def get_price(self):
        original_price = self.component.get_price()
        discounted_price = original_price - (original_price * self.discount_percentage)
        return discounted_price




def client_code(pizza_manager: PizzaManager,pizza_decorator:DiscountDecorator, ingredient_remover: PizzaIngredientRemover) -> None:
    originator = Originator("empty order")
    caretaker = Caretaker(originator)

    add_extra = AddToppingHandler()
    remove = RemoveToppingHandler()
    order = OrderHandler()

    add_extra.set_next(remove).set_next(order)

    pizzas = []
    pizza_names=[]
    pizzas_components=[]
    print("\nWelcome to the Pizza Factory!")
    while True:
        flag=0
        components=[]
        price=0
        print("\nPlease choose a pizza:")
        print("1. Margherita")
        print("2. Pepperoni")
        print("3. Capriciosa")
        print("4. To finish order")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '4':
            break


        elif choice in ['1', '2', '3']:
            pizza_name = ["Margherita", "Pepperoni", "Capriciosa"][int(choice) - 1]

            originator.add_pizza()
            caretaker.backup()

            pizza_names.append(pizza_name)
            pizza = pizza_manager.get_pizza(pizza_name)
            pizzas.append(pizza)
            base_components = pizza.get_components
            pizza.price= find_numbers_in_array(base_components)

            add_extra = input("Would you like to add extra toppings to your pizza? (y/n): ")
            if add_extra.lower() == 'y':
                originator.add_topping()
                caretaker.backup()
                flag=1
                extras = []
                while True:
                    extra_choice = input("Enter the extra topping you want to add or type 'done' to finish: ")
                    if extra_choice.lower() == 'done':
                        break
                    else:
                        extras.append(extra_choice)
                pizza_with_extras = pizza_manager.get_pizza(pizza_name, extras)
                components = pizza_with_extras.get_components
                price = find_numbers_in_array(components)
                components.remove(price)
                pizzas_components.append(components)
                print(f'\nPizza components:{components}\n')
                # print(f'\nprice:{price}\n')
                # print(pizzas)with_extras.list_components()}")


            remove_ingredient = input("Do you have any food allergies? (y/n): ")
            if remove_ingredient.lower() == 'y':
                originator.remove_topping()
                caretaker.backup()
                flag=2
                #print(flag)
                allergens = []
                while True:
                    print(f"pizza components: {components}")
                    allergen_choice = input("Enter the allergen you have or type 'done' to finish: ")
                    if allergen_choice.lower() == 'done':
                        break
                    else:
                        allergens.append(allergen_choice.lower())

                for allergen in allergens:
                    pizza = ingredient_remover.remove(pizza_with_extras, allergen)

                #print(f"{pizza.list_components()}")
                if flag != 1 and flag != 2:
                    components = pizza.get_components
                    price=find_numbers_in_array(components)
                    components.remove(price)
                    pizzas_components.append(components)
                print(f'\nPizza components:{components}\n')
                # print(f'\nprice:{price}\n')
                # print (pizzas)
        else:
            print("Invalid choice. Please try again.")



    total_price=0
    for i in range(len(pizzas)):
        components=pizzas[i].components
        if flag == 0:
            price = find_numbers_in_array(components)
            components.remove(price)
            pizzas_components.append(components)
        print(f'Pizza number {i+1}:{pizza_names[i]}')
        print(pizzas_components[i])
        print(f'price:{price}')
        total_price+=int(price)

    order = Order(total_price, pizzas)
    discounted_product=None
    if len(pizzas)<3:
        discounted_product = DiscountDecorator(order, 0)
    elif len(pizzas)>=3 and len(pizzas)<5:
        discounted_product = DiscountDecorator(order, 0.2)
    elif len(pizzas)>=5 and len(pizzas)<7:
        discounted_product = DiscountDecorator(order, 0.3)
    elif len(pizzas) >= 7 and len(pizzas) < 9:
        discounted_product = DiscountDecorator(order, 0.4)
    print(f"Total price: {discounted_product.get_price()}$")
    print(f'Ypu saved :{round(order.price-discounted_product.get_price(),3)}$')
    caretaker.show_history()

    while True:
        print("\ndo you want to do a rollback?(y/n)\n")
        answer=input()
        if answer=='y':
            caretaker.undo()
        elif answer=='n':
            break

def find_numbers_in_array(strings):


    for text in strings:
        if text.isdigit():
            return text



if __name__ == '__main__':
    pizzas=[]
    discount=0
    pizza_manager = PizzaManager()
    ingredient_remover = PizzaIngredientRemoverAdapter()
    pizza_decorator=DiscountDecorator(pizzas,discount)


    client_code(pizza_manager,pizza_decorator, ingredient_remover)