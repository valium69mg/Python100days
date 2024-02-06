'''
Title: HANGED MAN GAME
Author: Carlos Tranquilino Carlos Roman
Date: 02/10/2023
Description: This program is an excercise of that involves: WHILE LOOPS, IF STATEMENTS, FOR LOOPS AND MORE!
'''
import random
import os

words = ['beekepeer','bear','strawberry','arthurus','python','taco','burrito','quesadilla','mango','avocado']

def drawHangedMan(stage): # Seven stages (Arguments from 1 to 7)
    #METHODS

    #STEP 0 
    def initialState():
        print("-------")
        print("      |")
        print("      |")
        print("      |")
        print("      |")
        print("      |")
        print("=============")

    #STEP 1
    def putRope():
        print("-------")
        print(" |    |")
        print("      |")
        print("      |")
        print("      |")
        print("      |")
        print("=============")
    #STEP 2
    def putHead():
        print("-------")
        print(" |    |")
        print(" O    |")
        print("      |")
        print("      |")
        print("      |")
        print("=============")
    #STEP 3
    def putTorso():
        print("-------")
        print(" |    |")
        print(" O    |")
        print(" |    |")
        print("      |")
        print("      |")
        print("=============")
    #STEP 4
    def putRightArm():
        print("-------")
        print(" |    |")
        print(" O    |")
        print("/|    |")
        print("      |")
        print("      |")
        print("=============")
    #STEP 5
    def putLeftArm():
        print("-------")
        print(" |    |")
        print(" O    |")
        print("/|\   |")
        print("      |")
        print("      |")
        print("=============")
    #STEP 6
    def putRightLeg():
        print("-------")
        print(" |    |")
        print(" O    |")
        print("/|\   |")
        print("/     |")
        print("      |")
        print("=============")
    #STEP 7
    def putLeftLeg():
        print("-------")
        print(" |    |")
        print(" O    |")
        print("/|\   |")
        print("/ \   |")
        print("      |")
        print("=============")
        

    #INITIAL STATE
    if (stage < 8 and stage >= 0):
        if (stage  == 0):
            initialState()
        elif (stage  == 1):
            putRope()
        elif (stage  == 2):
            putHead()
        elif (stage  == 3):
            putTorso()
        elif (stage  == 4):
            putRightArm()
        elif (stage == 5):
            putLeftArm()
        elif (stage  == 6):
            putRightLeg()
        elif (stage  == 7):
            putLeftLeg()
        else:
            pass
    else:
        pass

def getRandomWord(): # Return list with the letters of the random word
    random_word = words[random.randint(0,len(words)-1)]
    random_word_list = []
    for letter in random_word:
        random_word_list.append(letter)
    return random_word_list

def getWordLength(random_word): # Return the word length in int
    number_of_letters = 0
    for letter in random_word:
        number_of_letters = number_of_letters + 1
    return number_of_letters

def letterUnderscores(random_word_length): # returns the underscores for de hanged man with a word length input
    word_underscore = []
    for i in range(0,random_word_length):
        word_underscore.append("_")
    return word_underscore

def hangedManLetters(word): #Receives a list argument (the random word)
    stage = 1
    gameOver = False
    correctGuess = False
    drawHangedMan(stage)
    print("Welcome to the HANGED MAN game!")
    while (gameOver == False):
        if (word != guessed_letters and stage < 7): # GAME GOING
            
            input_letter = str(input("Input a letter: "))
            repeatedGuess = False
            for letter in guessed_letters: #CHECK IF IT IS ALREADY ON THE GUESSED WORD
                if (letter == input_letter):
                    repeatedGuess = True
                else:
                    pass   
            
            for i in range(0,len(word)): # CHECK IF ANY LETTER MATCHES
                if (input_letter == word[i]):
                        guessed_letters[i] = input_letter
                        correctGuess = True
                else:
                    pass            
            
            if (correctGuess == True and repeatedGuess == False): # MATCH
                os.system('cls')
                drawHangedMan(stage)
                print("\nCorrect!")
                print(guessed_letters)
                
                correctGuess = False
            elif(correctGuess == False): # NO MATCH
                stage = stage + 1
                os.system('cls')
                drawHangedMan(stage)
                print("\nFalse!")
                print(guessed_letters)
            elif(repeatedGuess == True):
                os.system('cls')
                drawHangedMan(stage)
                print("\nRepeated Entry.\n")
            else:
                pass
        elif (word == guessed_letters): # USER WON 
            print("\nYou won!")
            gameOver=True 
            break      
        elif (stage == 7): # OUT OF TRIES
            print("\nYou lost!")
            gameOver=False  
            break 
        else: 
            break    
        print("Tries left: {}".format(7-stage))
       
# INITIALIZATION VALUES
random_word = getRandomWord()
random_word_length = getWordLength(random_word)
guessed_letters = letterUnderscores(random_word_length)

hangedManLetters(random_word) #Initialize game with a random word

