#
''' 
Title: Password generator project
Author: Carlos Tranquilino Carlos Roman
Date: 02/10/2023
'''
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome, this is a program that generates a safe random password, provide the following: \n")

number_of_letters = int(input("How many letters?: "))

number_of_numbers = int(input("How many numbers?: "))
number_of_symbols = int(input("How many symbols?: "))


chosen_letters = []
chosen_numbers = []
chosen_symbols = []

for i in range (1,number_of_letters+1):
    random_letter = letters[random.randint(0,51)]
    chosen_letters.append(random_letter)

for i in range (1,number_of_numbers+1):
    random_number = numbers[random.randint(0,9)]
    chosen_numbers.append(random_number)

for i in range (1,number_of_symbols+1):
    random_symbol = symbols[random.randint(0,8)]
    chosen_symbols.append(random_symbol)


lenght_of_password = len(chosen_letters) + len(chosen_numbers) + len(chosen_symbols)
chosen_password = []
is_done = False
numberOfCycles = 0

while is_done == False:
    # To pick the category randomly
    numberOfCycles = numberOfCycles + 1
    random_category = random.randint(1,3)
    if (random_category == 1 and chosen_letters):
        random_letter = chosen_letters[random.randint(0,len(chosen_letters)-1)]
        chosen_password.append(random_letter)
        chosen_letters.remove(random_letter)
    elif (random_category == 2 and chosen_numbers):
        random_number = chosen_numbers[random.randint(0,len(chosen_numbers)-1)]
        chosen_password.append(random_number)
        chosen_numbers.remove(random_number)
    elif (random_category == 3 and chosen_symbols):
        random_symbol = chosen_symbols[random.randint(0,len(chosen_symbols)-1)]
        chosen_password.append(random_symbol)
        chosen_symbols.remove(random_symbol)
    elif (len(chosen_password) == lenght_of_password):
        is_done == True
        break
    else:
        pass

strPassword = ""  
for character in chosen_password:
    strPassword = strPassword + character

print("\nYour safe randomly generated password is: {}".format(strPassword))

