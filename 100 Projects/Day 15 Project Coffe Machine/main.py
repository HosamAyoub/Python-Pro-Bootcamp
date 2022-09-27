MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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

profit = 0.0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(order):
    """Check if the resources was enough for the order or not, returns bool"""
    for gradient in MENU[order]['ingredients']:
        if (resources[gradient] >= MENU[order]['ingredients'][gradient]):
            pass
        else:
            print(f"Sorry there is not enough {gradient}.")
            return False
    return True


def calc_money():
    """Calculate the total inserted coins for each order, returns the total inserted money"""
    inserted_money = 0
    inserted_money += int(input("how many quarters?: ")) * 0.25
    inserted_money += int(input("how many dimes?: ")) * 0.10
    inserted_money += int(input("how many nickles?: ")) * 0.05
    inserted_money += int(input("how many penny?: ")) * 0.01
    return inserted_money


def calc_transaction(inserted_money, order):
    """Check if the inserted money was enough for the order and calculates the in change money, returns bool"""
    in_change = 0
    if (inserted_money >= MENU[order]['cost']):
        in_change = inserted_money - MENU[order]['cost']
        print(f"Here is ${in_change:.2f} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False        


def calc_resources(order):
    """calculate the remaining resources and make the order, has no return"""
    global profit
    for gradient in MENU[order]['ingredients']:
        resources[gradient] -=  MENU[order]['ingredients'][gradient]
    profit +=  MENU[order]["cost"]
    print(f"Here is your {order} ☕️. Enjoy!")


def coffee_machine():
    """The logic of the coffee machine"""
    global resources
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if (choice in MENU):
        if (check_resources(choice)):
            print("Please insert coins.")
            money = calc_money()
            if calc_transaction(money, choice):
                calc_resources(choice)
    elif (choice.lower() == 'off'):
        return False
    elif (choice.lower() == 'report'):
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit:.2f}")
    else:
        print("Invalid input")
    return True


while(coffee_machine()):
    pass