'''
Title: Blackjack
Author: carlostr
Date: 04.10.2023
'''
import os
import random

def drawHand():
    hand = []
    card1 = random.randint(1,15)
    card2 = random.randint(1,15)
    hand.append(card1)
    hand.append(card2)
    return hand


def drawCard():
    card = card1 = random.randint(1,15)
    return card

def registerUsers():
    users = []
    registerDone = False
    while (registerDone == False):
        name = str(input("Type a player's name: "))
        users.append(name)
        anotherUser = str(input("Add another player? (y/n)"))
        if (anotherUser == "y"):
            registerDone = False
        elif (anotherUser == "n"):
            registerDone = True
    return users

def playGame(users):
    finishGame = False
    userHands = {}
    numberOfUsers = len(users)
    foldUsers = []
    for user in users:
            userHands[user] = drawHand()
    while (finishGame == False):
        for user in users:
            if (user not in foldUsers):
                os.system('cls')
                drawAnother = str(input("Draw another card, {}? (y/n)".format(user)))
                if (drawAnother == "y"):
                    userHands[user].append(drawCard())
                elif (drawAnother == "n"):
                    foldUsers.append(user)
            else:
                pass    
            
        if (len(foldUsers) == len(users)):
            finishGame = True
        else:
            pass
    for user in userHands:
        sumOfCards = 0
        for card in userHands[user]:
            sumOfCards = sumOfCards + card
        userHands[user] = sumOfCards
    return userHands

def winner(usersDictionary):
    winner_key = ""
    max_value = 0
    for user in usersDictionary:
        if (usersDictionary[user] < 21):
            if (usersDictionary[user] > max_value):
                max_value = usersDictionary[user]
                winner_key = user
            else:
                pass
        elif (usersDictionary[user] == 21):
            max_value = 21
            usersDictionary[user] ="21!"
            winner_key = user
        elif (usersDictionary[user] > 21):
            usersDictionary[user] = "ABOVE 21."   
        
    usersDictionary[winner_key] = "WINNER."       
     
    return usersDictionary
        
os.system('cls')
users = registerUsers() #Register users and draw hands
print("The players are: {}".format(users))
hands = playGame(users) #Start drawing cards 
print("These are the players cards: {}".format(hands))
winners = winner(hands)
print("Results of the game: {}".format(winners))