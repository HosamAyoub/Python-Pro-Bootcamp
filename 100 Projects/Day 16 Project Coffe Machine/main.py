from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

drinks = Menu()
options = drinks.get_items()
info = CoffeeMaker()
money_machine = MoneyMachine()

while (True):
    order = input(f"What would you like? {options}: ").lower()
    if (order == 'off'):
        break
    elif (order == 'report'):
        info.report()
        money_machine.report()
    else:
        drink = drinks.find_drink(order)
        if (drink and info.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost)):
            info.make_coffee(drink)