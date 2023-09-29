import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3

# print(RPS(2))
playagain = True

while playagain:
    value = int(input("\nEnter 1 for Rock: \nEnter 2 for Paper: \nEnter 3 for Scissor: \n\n"))


    if value < 1 or value > 3:
        print("\nYou must enter 1, 2 or 3 !!\n\n")
    else:
        computerchoice = random.choice("123")
        computer = int(computerchoice)

        print("\nYou Entered: " + str(RPS(value)).replace("RPS.",""))
        print("\nPython Entered: " + str(RPS(computer)).replace("RPS.","") + "\n")

        if value == 2 and computer == 1:
            print("You Win !!\n")
        elif value == 1 and computer == 3:
            print("You Win !!\n")
        elif value == 3 and computer == 2:
            print("You Win !!\n")
        elif value == computer:
            print("\nIt's a draw !!\n")
        else:
            print("\nPython Wins !!\n")

        choice = input("Want to try your luck again:\n\nType:\n Y to Yes\n Q to Quit\n\n")

        if choice.lower() == 'y':
            continue
        else:
            print("\nThank You for playing !!\n")
            playagain = False

sys.exit("BYE !\n\n")