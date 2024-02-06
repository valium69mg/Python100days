'''
Title: Coffee machine
Author: carlostr 
Date: 06.10.2023
Desc: This is a program that simulates a coffee machine that works with coins
'''
import os
import time
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

# COINS
penny = 0.01
dime = 0.1
nickel = 0.05
quarter = 0.25

def printReport(resources):
    print("Resources report: \n" )
    for resource in resources:
        print("{} of {} left in machine.".format(resources[resource],resource))
    print("--------------------------")


def useWater(resources,quantity):
    for resource in resources:
        if (resource == 'water' and (resources[resource] - quantity) >= 0):
            resources[resource] = resources[resource] - quantity
        else:
            pass

def useMilk(resources,quantity):
    for resource in resources:
        if (resource == 'milk' and (resources[resource] - quantity) >= 0):
            resources[resource] = resources[resource] - quantity
        else:
            pass

def useCoffee(resources,quantity):
    for resource in resources:
        if (resource == 'coffee') and (resources[resource] - quantity) >= 0:
            resources[resource] = resources[resource] - quantity
        else:
            pass

def displayMenu(menu):
    
    print("WELCOME TO THE COFFEE SHOP! \nOUR MENU IS: \n")
    for item in menu:
        print(item)
        product = menu[item]
        for key in product:
            if key == 'cost':
                print("${}".format(product[key]))
            else:
                pass
    print("--------------------------")
    
def coffeeCost(menu,coffee):
    for item in menu:
        product = menu[item]
        if item == coffee:
            for key in product:
                if key == 'cost':
                    return product[key]
                else:
                    pass
        else:
            pass


def getIngredients(menu,coffe):
    for item in menu:
        product = menu[item]
        if item == coffe:
            for key in product:
                if key == 'ingredients':
                    return product[key]
                else:
                    pass
        else: 
            pass



cost_espresso = coffeeCost(MENU,'espresso')
cost_latte = coffeeCost(MENU,'latte')
cost_cappuccino = coffeeCost(MENU,'cappuccino')


gameOn = True

os.system('cls')
while gameOn:
    displayMenu(MENU)
    resources_water = resources["water"]
    resources_milk = resources["milk"]
    resources_coffee = resources["coffee"]
    water = 0
    milk = 0
    coffee = 0
    order = input("What coffee would you want: ")
    cost = coffeeCost(MENU,order)
    ingredients = getIngredients(MENU,order) #Dictionary with ingredients
    for ingredient in ingredients:
        if ingredient == 'water':
            water = ingredients['water']
        elif (ingredient == 'milk'):
            milk = ingredients['milk']
        elif (ingredient == 'coffee'):
            coffee = ingredients['coffee']
    if (resources_water - water < 0):
        printReport(resources)
        print("Not enough resources")
        break
    elif (resources_milk - milk < 0):
        printReport(resources)
        print("Not enough resources.")
        break
    elif (resources_coffee - coffee < 0): 
        printReport(resources)
        print("Not enough resources.")
        break
    
    credit = 0
    while credit < cost:
        insertCoin = float(input("Please insert coins: "))
        if (insertCoin == penny):
            credit = credit + insertCoin
            print("Current credit: ${}".format(credit))
        elif (insertCoin == dime):
            credit = credit + insertCoin
            print("Current credit: ${}".format(credit))
        elif (insertCoin == nickel):
            credit = credit + insertCoin
            print("Current credit: ${}".format(credit))
        elif (insertCoin == quarter):
            credit = credit + insertCoin
            print("Current credit: ${}".format(credit))
        elif (insertCoin == cost):
            credit = cost
            print("Current credit: ${}".format(credit))
        else: 
            pass
    print("====================")
    print("Dispatching order...")
    print("====================")

    if (order == 'espresso'):
        useWater(resources,water)
        useCoffee(resources,coffee)
    elif (order == 'latte'):
        useWater(resources,water)
        useMilk(resources,milk)
        useCoffee(resources,coffee)
    elif (order == 'cappuccino'):
        useWater(resources,water)
        useMilk(resources,milk)
        useCoffee(resources,coffee)
    else:
        pass

    printReport(resources)
    time.sleep(10)
    os.system('cls')