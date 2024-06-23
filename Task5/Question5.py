'''
Write a program that randomly generates a number between 1 and 100. 
The user has to guess the number. After each guess, the program tells 
the user whether the guess is too high, too low, or correct. 
The game continues until the user guesses the correct number.

To generate random number use random module

import random

random.randint(1,3)
'''
import random


def guessNumber():
    game = True
    while game == True:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess < compNumber:
            print("Too low! Try again.")
        elif guess > compNumber:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the correct number.")
            break


compNumber = random.randint(1, 100)
guessNumber()
