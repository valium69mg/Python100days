'''
Title: Coffe Machine with OOP
Author: carlostranquilino
Date: 12.10.2023
'''

import os
import time


menu = {
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
    },
    "american": {
        "ingredients": {
            "water": 200,
            "milk": 0,
            "coffee": 50,
        },
        "cost": 1.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


class CoffeMachine:
    #ATTRIBUTES
    menu = {}
    resources = {}
    order = ""
    credit = 0.0

    def __init__(self,machineMenu,machineResources): #CONSTRUCTOR
        self.menu = machineMenu
        self.resources = machineResources
    
    def getCost(self): #RETURNS COST OF THE COFFEE
        for item in self.menu:
            if item == self.order:
                dict_attributes = self.menu[item]
                for attribute in dict_attributes:
                    if attribute == 'cost':
                        cost = float(dict_attributes[attribute])
                        return cost
    
    def getCoffeeList(self):
        list = []
        for coffee in self.menu:
            list.append(coffee)
        return list
    
    def getCredits(self):
        return self.credit 

    def getMenu(self): #PRINT MENU
        print("===========MENU=============")
        for item in self.menu:
            dict_attributes = self.menu[item]
            print("Coffee: {}".format(item))
            for attribute in dict_attributes:
                if attribute == 'cost':
                    print("Cost: ${}".format(dict_attributes[attribute]))
        print("============================")   

    def getMenuResource(self,resourceType): #GET SPECIFIC RESOURCE QUANTITY FROM THE MENU
        for item in self.menu:
            dict_attributes = self.menu[item]
            for attribute in dict_attributes:
                if attribute != 'cost':
                    resource_dict = dict_attributes[attribute]
                    for resource in resource_dict:
                        if resource == resourceType and item == self.order:
                            quantity = resource_dict[resource]
                            return quantity

    def getMachineResource(self,resourceType): #GET SPECIFIC MACHINE RESOURCE QUANTITY  
        for resource in self.resources:
            if resource == resourceType:
               quantity = self.resources[resource]
               return quantity
    
    def getResourcesNeeded(self): #RETURNS A LIST OF RESOURCES NEEDED BY THE ORDER 
        list = []
        for item in self.menu:
            dict_attributes = self.menu[item]
            for attribute in dict_attributes:
                if attribute != 'cost':
                    resource_dict = dict_attributes[attribute]
                    for resource in resource_dict:
                        if (item == self.order):
                            list.append(resource)
        return list
    

    def printMachineResources(self): #PRINT ALL RESOURCES
        print("======MACHINE RESOURCES=====")
        for resource in self.resources:
            print("Resource: {}, Quantity: {}".format(resource,self.resources[resource]))
        print("============================")

    
    
    def setOrder(self,coffeeType):
        self.order = coffeeType

    def resetCredit(self):
        self.credit = 0
        
    def insertCoins(self,coins): #INSERTS COINS
        if coins >= 0:
            self.credit = self.credit + coins

    def substractCredit(self,credit,quantity):
        self.credit = credit - quantity

    def consumeResource(self,resourceType,quantity): #CONSUMES A QUANTITY OF A RESOURCE FROM THE MACHINE
        for resource in self.resources:
            if resourceType == resource: 
                self.resources[resource] = self.resources[resource] - quantity

    def serveCoffee(self):
        print("============================")
        print("Serving coffee...")
        print("============================")
    
#LOOP VARIABLE
enoughResources = True
myMachine = CoffeMachine(menu,resources)
while True:
    os.system('cls')
    #INITIALIZE THE OBJECT
    

    #STEP 1 - SHOW MENU
    myMachine.getMenu()

    #STEP 2 - TAKE ORDER AND CHECK RESOURCES
    coffeeList = myMachine.getCoffeeList()
    correctOrder = False
    while correctOrder == False:
        inputOrder = str(input("Place your order: "))
        if inputOrder in coffeeList:
            break
        else:
            continue

    myMachine.setOrder(inputOrder)  
    

    for resource in myMachine.getResourcesNeeded():
        if myMachine.getMachineResource(resource) - myMachine.getMenuResource(resource) < 0:
            print("\n")
            print("Not enough of {}".format(resource))
            print("Availible: {}".format(myMachine.getMachineResource(resource)))
            print("Needed: {} ".format(myMachine.getMenuResource(resource)))
            enoughResources = False

    if enoughResources == True:
        #STEP 3 - PAYMENT
        correctPayment = False
        coffeCost= myMachine.getCost()
        while correctPayment == False:
            inputCoins = float(input("\nPlace your coins: "))
            myMachine.insertCoins(inputCoins)
            print("\nCurrent credits: ${}".format(myMachine.getCredits()))
            if myMachine.getCredits() >= coffeCost:
                myMachine.substractCredit(myMachine.getCredits(),myMachine.getCost())
                print("\nPayment accepted... ")
                print("Change: ${} \n".format(myMachine.getCredits()))
                myMachine.resetCredit()
                break
            else:
                continue


        #STEP 4 - PREPARE THE COFFEE

        # WHAT RECOURSES ARE NEEDED 
        listOfResources = myMachine.getResourcesNeeded()

        # CONSUME RECOURSES NEEDED 
        if ('water' in listOfResources):
            waterNeeded = myMachine.getMenuResource('water')
            waterStock = myMachine.getMachineResource('water')
            if (waterStock - waterNeeded >= 0):
                myMachine.consumeResource('water',waterNeeded)

        if ('milk' in listOfResources):
            milkNeeded = myMachine.getMenuResource('milk')
            milkStock = myMachine.getMachineResource('milk')
            if (milkStock - milkNeeded >= 0):
                myMachine.consumeResource('milk',milkNeeded)
            
        if ('coffee' in listOfResources):
            coffeeNeeded = myMachine.getMenuResource('coffee')
            coffeeStock = myMachine.getMachineResource('coffee')
            if (coffeeStock - coffeeNeeded >= 0):
                myMachine.consumeResource('coffee',coffeeNeeded)
            

        #SERVE COFFEE
        myMachine.serveCoffee()
        time.sleep(5)

    else: 
        break

