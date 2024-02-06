'''
Title: CAESARS CIPHER ENCRYPTION
Author: Carlos Tranquilino Carlos Roman
Date: 03/10/2023
Description: This program takes a message and encodes with a particular algorithm.
It also takes the encrypted message and reverts it to original message.
'''
import os

#Encrypt and Decrypt functions
def encrypt(text,shift):
    words = text.split()
    encrypted_words = []
    encrypted_word = ""
    for word in words:
        for letter in word:
            if (alphabet.index(letter)+shift < 26): 
                letter = alphabet[alphabet.index(letter)+shift]
                
            else:
                letter = alphabet[(alphabet.index(letter)+shift)-26]
                
            encrypted_word = encrypted_word + letter
        encrypted_words.append(encrypted_word)
        encrypted_word = ""    

    return encrypted_words

def decrypt(text,shift):
    words = text.split()
    decrypted_words = []
    decrypted_word = ""
    for word in words:
        for letter in word:
            if (alphabet.index(letter)-shift >= 0): 
                letter = alphabet[alphabet.index(letter)-shift]
                
            else:
                letter = alphabet[(alphabet.index(letter)-shift)+26]
                
            decrypted_word = decrypted_word + letter
        decrypted_words.append(decrypted_word)
        decrypted_word = ""    
    return decrypted_words


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Initial input and console clear
os.system('cls')
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


#Decision tree and callback functions
if (direction == 'encode'):
    encrypted_message = encrypt(text,shift)
    encrypted_message_str =""
    for word in encrypted_message:
        encrypted_message_str = encrypted_message_str + (word + " ")
    print("Your encripted message is: {}".format(encrypted_message_str))
elif (direction == 'decode'):
    decrypted_message = decrypt(text,shift)
    decrypted_message_str =""
    for word in decrypted_message:
        decrypted_message_str = decrypted_message_str + (word + " ")
    print("Your encripted message is: {}".format(decrypted_message_str))
else:
    print("Not a valid mode.")



 
