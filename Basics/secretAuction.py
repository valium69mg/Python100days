'''
Title: Secret Auction
Author: Carlos Tranquilino Carlos Roman
Date: 04.10.2023
Description: this program is made to learn about dictionaries
'''
import os 

auctionOn = True
moreParticipants = False
bids = {}


def auctionWinner(bids):
    max_value = 0
    auctionWinner = ""
    for key in bids:
        if ((bids[key]) > max_value):
            max_value = bids[key] 
            auctionWinner = key 
        else:
            pass
    return auctionWinner

while auctionOn:
    os.system('cls')
    bet = int(input("Type your bid: "))
    name = str(input("Provide your name: "))
    bids[name] = bet
    more = str(input("More participants? (y/n)"))
    if (more == 'y'):
        auctionOn = True
    elif (more == 'n'):
        auctionOn = False
    else:
        pass


os.system('cls')
print("The winner is: " + auctionWinner(bids))
