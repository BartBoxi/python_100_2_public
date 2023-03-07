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

monety = {
        "pennies" : 0,
        "nickles" : 0,
        "dimes" : 0,
        "quarters" : 0
    }


# functions

def wybor():
    if choice == "report":
        report()
    elif choice == "espresso":
        if resources['water'] >= MENU['espresso']['ingredients']['water'] and resources['coffee'] >= MENU['espresso']['ingredients']['coffee']:
            espresso()
        else:
            print("not enough resources")
    elif choice == "latte":
        if resources['water'] >= MENU['latte']['ingredients']['water'] and resources['coffee'] >= MENU['latte']['ingredients']['coffee'] and resources['milk'] >= MENU['latte']['ingredients']['milk']:
            latte()
        else:
            print("not enough resources")
    elif choice == "cappuccino":
        if resources['water'] >= MENU['cappuccino']['ingredients']['water'] and resources['coffee'] >= MENU['cappuccino']['ingredients']['coffee'] and resources['milk'] >= MENU['cappuccino']['ingredients']['milk']:
            cappucino()
        else:
            print("not enough resources")
    elif choice == "off":
        return 0
    else:
        print("Wrong choice. Try again")
        wybor()

def report():
    print(resources)

def money():
    if choice == "espresso":
        price = MENU['espresso']['cost']
        print(price)
    elif choice == "latte":
        price = MENU['latte']['cost']
        print(price)
    elif choice == "cappuccino":
        price = MENU['cappuccino']['cost']
        print(price)
    else:
        return 0

    pennies = int(input("How many pennies you got?"))
    total_pennies = pennies * 0.01
    suma = price - total_pennies
    print(f"You put {pennies} which is giving {total_pennies}. Remaining amount to pay is {suma} ")
    monety["pennies"] = pennies

    nickles = int(input("How many nickles you got?"))
    total_nickles = nickles * 0.05
    suma = suma - total_nickles
    print(f"You put {nickles} which is giving {total_nickles}. Remaining amount to pay is {suma} ")
    monety["nickles"] = nickles

    dimes = int(input("How many dimes you got?"))
    total_dimes = dimes * 0.1
    suma = suma - total_dimes
    print(f"You put {dimes} which is giving {total_dimes}. Remaining amount to pay is {suma} ")
    monety["dimes"] = dimes

    quarters = int(input("How many quarters you got?"))
    total_quarters = quarters * 0.25
    suma = suma - total_quarters
    print(f"You put {quarters} which is giving {total_quarters}. Remaining amount to pay is {suma} ")
    monety["quarters"] = quarters

    if suma == price:
        print("Thanks for payment")
    elif suma < 0:
        print(f"You pay too much. Your change will be {suma - price}")
    elif suma > 0:
        print(f"You paid not enough. Still missing {price - suma}")
        pennies = int(input("How many pennies you got?"))
        total_pennies = pennies * 0.01
        suma = price - total_pennies
        print(f"You put {pennies} which is giving {total_pennies}. Remaining amount to pay is {suma} ")
        monety["pennies"] = pennies

        nickles = int(input("How many nickles you got?"))
        total_nickles = nickles * 0.05
        suma = suma - total_nickles
        print(f"You put {nickles} which is giving {total_nickles}. Remaining amount to pay is {suma} ")
        monety["nickles"] = nickles

        dimes = int(input("How many dimes you got?"))
        total_dimes = dimes * 0.1
        suma = suma - total_dimes
        print(f"You put {dimes} which is giving {total_dimes}. Remaining amount to pay is {suma} ")
        monety["dimes"] = dimes

        quarters = int(input("How many quarters you got?"))
        total_quarters = quarters * 0.25
        suma = suma - total_quarters
        print(f"You put {quarters} which is giving {total_quarters}. Remaining amount to pay is {suma} ")
        monety["quarters"] = quarters
    else:
        return 0

# todo: "Round up the result of the suma and the price wynik teraz to suma ujemna, zrobic tak aby bylo dobrze"

def espresso():
    # print(resources['water'])
    # print(MENU['espresso']['water'])

    print(MENU['espresso']['cost'])

    resources['water'] = resources['water'] - MENU['espresso']['ingredients']['water']

    resources['coffee'] = resources['coffee'] - MENU['espresso']['ingredients']['coffee']

    print(resources)


def latte():
    resources['water'] = resources['water'] - MENU['latte']['ingredients']["water"]

    resources['coffee'] = resources["coffee"] - MENU['latte']['ingredients']['coffee']

    resources['milk'] = resources['milk'] - MENU['latte']['ingredients']['milk']
    print(resources)


def cappucino():
    resources['water'] = resources['water'] - MENU['cappuccino']['ingredients']["water"]

    resources['coffee'] = resources["coffee"] - MENU['cappuccino']['ingredients']['coffee']

    resources['milk'] = resources['milk'] - MENU['cappuccino']['ingredients']['milk']

    print(resources)



choice = input("What would you like? Choose 'espresso' 'latte' 'cappuccino' or 'report' ")
wybor()
money()
