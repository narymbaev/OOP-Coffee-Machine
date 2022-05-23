from MENU import machine
from MENU import menu

machine["money"] = 0


def content():
    water = machine["water"]
    milk = machine["milk"]
    coffee = machine["coffee"]
    money = machine["money"]
    return f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money} "


def insert_coins():
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    total_money = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
    return round(total_money, 2)


def sufficient_resources(type_of_coffee):
    if machine["water"] - menu[type_of_coffee]["ingredients"]["water"] < 0:
        return "water"
    if type_of_coffee != "espresso":
        if machine["milk"] - menu[type_of_coffee]["ingredients"]["milk"] < 0:
            return "milk"
    if machine["coffee"] - menu[type_of_coffee]["ingredients"]["coffee"] < 0:
        return "coffee"
    return ""


def change_coins(inserted_money, type_of_coffee):
    change = inserted_money - menu[type_of_coffee]["cost"]
    return change


def machine_change(type_of_coffee):
    machine["water"] -= menu[type_of_coffee]["ingredients"]["water"]
    if type_of_coffee != "espresso":
        machine["milk"] -= menu[type_of_coffee]["ingredients"]["milk"]
    machine["coffee"] -= menu[type_of_coffee]["ingredients"]["coffee"]
    machine["money"] += menu[type_of_coffee]["cost"]


def start():
    type_of_coffee = input("What would u like (espresso/cappuccino/latte): ").lower()
    if type_of_coffee == "report":
        status = content()
        print(status)
        start()
    resource = sufficient_resources(type_of_coffee)
    ''' "resource" returns name of missing resource
        if there are sufficient resources it returns free space "" '''
    if resource:
        print(f"There is no enough {resource} in machine!")
        start()
    print("Please insert coins")
    inserted_money = insert_coins()
    change = change_coins(inserted_money, type_of_coffee)
    if change < 0:
        print("Sorry that is not enough money. Money Refunded!")
        start()
    machine_change(type_of_coffee)
    print(f"Here is ${change} in change")
    print(f"Here is your {type_of_coffee}, enjoy!")
    start()


start()


# profit = 0
#
#
# def is_resource_sufficient(order_ingredients):
#     """Returns True when order can be made, False if ingredients are insufficient."""
#     for item in order_ingredients:
#         if order_ingredients[item] > resources[item]:
#             print(f"​Sorry there is not enough {item}.")
#             return False
#     return True
#
#
# def process_coins():
#     """Returns the total calculated from coins inserted."""
#     print("Please insert coins.")
#     total = int(input("how many quarters?: ")) * 0.25
#     total += int(input("how many dimes?: ")) * 0.1
#     total += int(input("how many nickles?: ")) * 0.05
#     total += int(input("how many pennies?: ")) * 0.01
#     return total
#
#
# def is_transaction_successful(money_received, drink_cost):
#     """Return True when the payment is accepted, or False if money is insufficient."""
#     if money_received >= drink_cost:
#         change = round(money_received - drink_cost, 2)
#         print(f"Here is ${change} in change.")
#         global profit
#         profit += drink_cost
#         return True
#     else:
#         print("Sorry that's not enough money. Money refunded.")
#         return False
#
#
# def make_coffee(drink_name, order_ingredients):
#     """Deduct the required ingredients from the resources."""
#     for item in order_ingredients:
#         resources[item] -= order_ingredients[item]
#     print(f"Here is your {drink_name} ☕️. Enjoy!")
#
#
# is_on = True
#
# while is_on:
#     choice = input("​What would you like? (espresso/latte/cappuccino): ")
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#         print(f"Water: {resources['water']}ml")
#         print(f"Milk: {resources['milk']}ml")
#         print(f"Coffee: {resources['coffee']}g")
#         print(f"Money: ${profit}")
#     else:
#         drink = MENU[choice]
#         if is_resource_sufficient(drink["ingredients"]):
#             payment = process_coins()
#             if is_transaction_successful(payment, drink["cost"]):
#                 make_coffee(choice, drink["ingredients"])