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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0.0


def check_resources(order):
    for gradient in MENU[order]['ingredients']:
        if (resources[gradient] >= MENU[order]['ingredients'][gradient]):
            pass
        else:
            print(f"Sorry there is not enough {gradient}.")
            return False
    return True


def calc_money():
    inserted_money = 0
    inserted_money += int(input("how many quarters?: ")) * 0.25
    inserted_money += int(input("how many dimes?: ")) * 0.10
    inserted_money += int(input("how many nickles?: ")) * 0.05
    inserted_money += int(input("how many penny?: ")) * 0.01
    return inserted_money