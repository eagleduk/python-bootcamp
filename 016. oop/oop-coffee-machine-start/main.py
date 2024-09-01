from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
coffee_menu = Menu()
money = MoneyMachine()

is_run = True

while is_run:
    answer = input(f"What would you like? ({coffee_menu.get_items()}): ")

    if answer == "off":
        is_run = False
        print("Have a nice day!")
    elif answer == "report":
        coffee_machine.report()
        money.report()
    else:
        coffee_item = coffee_menu.find_drink(answer)
        if (coffee_item is not None and
                coffee_machine.is_resource_sufficient(coffee_item) and
                money.make_payment(coffee_item.cost)):
            coffee_machine.make_coffee(coffee_item)
