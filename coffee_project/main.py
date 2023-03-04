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

#functions

def wybor():
    if choice == "Report":
        report()
    elif choice == "espresso":
        espresso()
    elif choice == "latte":
        latte()
    elif choice == "cappuccino":
        cappucino()
    else:
        print("Wrong choice. Try again")
        wybor()


def report():
    print(resources)

def espresso():

def latte():

def cappucino():


choice = input("What would you like? Choose 'espresso' 'latte' 'cappuccino' or 'report' ")


