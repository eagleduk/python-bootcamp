MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def print_report():
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${resources["money"]}")


def insert_coin():
    print("Please insert coins.")

    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    return (quarters * 0.25)  + (dimes * 0.1) + (nickles * 0.05) + (pennies * 1)


def order_coffee(answer):
    coffee = MENU[answer]

    coffee_water = coffee["ingredients"]["water"]
    coffee_milk = coffee["ingredients"]["milk"]
    coffee_coffee = coffee["ingredients"]["coffee"]

    if resources["water"] < coffee_water:
        print("Sorry there is not enough water.")
        return

    if resources["milk"] < coffee_milk:
        print("Sorry there is not enough milk.")
        return

    if resources["coffee"] < coffee_coffee:
        print("Sorry there is not enough coffee.")
        return

    coins = insert_coin()

    coffee_cost = coffee["cost"]

    if coins < coffee_cost:
        print("Sorry that's not enough money. Money refunded.")
        return

    resources["water"] -= coffee_water
    resources["milk"] -= coffee_milk
    resources["coffee"] -= coffee_coffee
    resources["money"] += coffee_cost

    print(f"Here is ${round(coins - coffee_cost, 2)} in change.")
    print(f"Here is your {answer} Enjoy!")


is_run = True

while is_run:
    answer = input("What would you like? (espresso/latte/cappuccino): ")

    if answer == "off":
        is_run = False
    elif answer == "report":
        print_report()
    else:
        order_coffee(answer)
