'''
Write a program that plays the game of Rock, Paper, Scissors with the user.
The user makes a choice, the program randomly chooses, and the winner is determined.

To generate random number use random module

import random

random.randint(1,3)
'''
import random


def osom(player, comp):
    if player == comp:
        return f"Player: {player}\nComputer: {comp}\nIt's a tie"
    elif player == "Rock" and comp == "Scissors" or \
            player == "Scissors" and comp == "Paper" or \
            player == "Paper" and comp == "Rock":
        statment = f"Player: {player}\nComputer: {comp}\nYou win!!!"
        return statment
    else:
        statement = f"Player: {player}\nComputer: {comp}\nComputer wins! Nice try :)"
        return statement


pick = ["Rock", "Paper", "Scissors"]

playerPick = int(
    input("Enter your choice (1 for Rock, 2 for Paper, 3 for Scissors): "))
while playerPick > 3 or not int:
    playerPick = int(input(
        "Invalid choice.\nPlease enter again (1 for Rock, 2 for Paper, 3 for Scissors): "))
playerChoice = pick[playerPick-1]

compPick = random.randint(1, 3)
compChoice = pick[compPick-1]

result = osom(playerChoice, compChoice)
print(result)
