from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
"""hello  this is test typping by keeping the laptop"""
#object initialisation
coffee_maker_obj = CoffeeMaker()
menu_obj = Menu()
money_machine_obj = MoneyMachine()
#obj initialisation ends


is_on  = True

while is_on:
    user_input = input(f"Please enter your choice {menu_obj.get_items()}: ")
    if user_input == "report":
        coffee_maker_obj.report()
    elif user_input == "profit":
        money_machine_obj.report()
    elif user_input == "off":
        is_on = False
    elif menu_obj.find_drink(user_input):
        drink=menu_obj.find_drink(user_input)
        # print(f"{drink.name} is available")
        if coffee_maker_obj.is_resource_sufficient(drink):
            payment = money_machine_obj.make_payment(drink.cost)
            if payment :
                coffee_maker_obj.make_coffee(drink)
                # print(coffee_maker_obj.report())
    
    else:
        print("invalid selection")
