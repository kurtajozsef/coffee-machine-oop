from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
while True:
    order_name = input(f"What would you like?{menu.get_items()} ")
    if order_name == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(order_name)
        if drink is None:
            continue
        if not coffee_maker.is_resource_sufficient(drink):
            continue
        print(f"You chose {drink.name}, it costs ${drink.cost}")
        if not money_machine.make_payment(drink.cost):
            continue
        coffee_maker.make_coffee(drink)