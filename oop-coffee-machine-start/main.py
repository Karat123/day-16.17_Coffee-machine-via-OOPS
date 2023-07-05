from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()
menu = Menu()
items = Menu.get_items(menu)

machine_on = True
while  machine_on:
    choice = (input(f"What would you like to have: {items}")).lower()
    if choice == "off":
        machine_on = False
    elif choice == "report":
        coffeemaker.report()
        moneymachine.report()
    else:
        drink_choice = menu.find_drink(choice)
        if coffeemaker.is_resource_sufficient(drink_choice) and moneymachine.make_payment(drink_choice.cost):
            coffeemaker.make_coffee(drink_choice)
