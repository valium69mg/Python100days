'''
Title: Prime Numbers
Author: Carlos Tranquilino Carlos Roman
Date: 03/10/2023
Description: This is a program that calculates if the input number 
is prime
'''
import os

def prime_checker(number):
  isItPrime = False
  divisors = []
  prime_divisors = []
  for i in range(1,number+1):
    if (number % i == 0):
      if (i == 1):
        divisors.append(i)
        prime_divisors.append(i)
      elif (i == number):
        divisors.append(i)
        prime_divisors.append(i)
      else:
        divisors.append(i)
    else:
      pass
  if (divisors == prime_divisors):
    isItPrime = True
    print("It's a prime number.")
  else:
    isItPrime = False
    print("It's not a prime number.")

os.system('cls')
n = int(input("Insert number: ")) # Check this number
prime_checker(number=n)