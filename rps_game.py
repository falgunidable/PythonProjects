import sys
import random
from enum import Enum

def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSOR = 3

    # print(RPS(2))

    value = input("\nEnter 1 for Rock: \nEnter 2 for Paper: \nEnter 3 for Scissor: \n\n")

    if value not in ["1", "2", "3"]:
        print("You must enter 1, 2, or 3.")
        return play_rps()
    
    player = int(value)
    computerchoice = random.choice("123")
    computer = int(computerchoice)

    print("\nYou Entered: " + str(RPS(player)).replace("RPS.",""))
    print("\nPython Entered: " + str(RPS(computer)).replace("RPS.","") + "\n")

    if player == 2 and computer == 1:
        print("You Win !!\n")
    elif player == 1 and computer == 3:
        print("You Win !!\n")
    elif player == 3 and computer == 2:
        print("You Win !!\n")
    elif player == computer:
        print("\nIt's a draw !!\n")
    else:
        print("\nPython Wins !!\n")

    print("\nPlay again?")

    while True:
        choice = input("\nY for Yes or \nQ to Quit\n")
        if choice.lower() not in ["y", "q"]:
            continue
        else:
            break

    if choice.lower() == 'y':
        return play_rps()
    else:
        print("\nThank You for playing !!\n")
        sys.exit("BYE !\n\n")

play_rps()
