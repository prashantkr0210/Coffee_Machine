MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 100,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 120,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 150,
    }
}

resources = {
    "water": 500,
    "milk": 500,
    "coffee": 500,
}


should_continue = True
money_collected = 0

def print_report():
    print(f' Water: {resources["water"]}ml')
    print(f' Milk: {resources["milk"]}ml')
    print(f' Coffee: {resources["coffee"]}g')
    print(f' Money: Rs.{money_collected}')


def process_coffee(coffee_type):

    for items in MENU[coffee_type]["ingredients"]:
        if MENU[coffee_type]["ingredients"][items] > resources[items]:
            print(f"Sorry there is not enough {items}.")
            return 0

    given_money = 0
    print("Please insert coins. ")
    ten = int(input("How many Rs.10 coins? "))
    five = int(input("How many Rs.5 coins? "))
    two = int(input("How many Rs.2 coins? "))
    one = int(input("How many Rs.1 coins? "))
    given_money = (ten * 10) + (five * 5) + (two * 2) + one
    if given_money >= MENU[coffee_type]["cost"]:
        global money_collected   
        print(f'Here is Rs.{given_money - MENU[coffee_type]["cost"]} in change. ')
        print(f"Here is your {coffee_type} ☕. Enjoy!")
        money_collected += MENU[coffee_type]["cost"]
        for items in MENU[coffee_type]["ingredients"]:
            resources[items] -= MENU[coffee_type]["ingredients"][items]
    else:
        print("Sorry that's not enough money. Money refunded. ")


while should_continue:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input == "report":
        print_report()
    elif user_input == "off":
        should_continue = False
    else:
        process_coffee(user_input)
