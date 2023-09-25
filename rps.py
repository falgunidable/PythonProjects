import sys
from enum import Enum

value = int(input("Enter 1,\n Enter 2,\nEnter 3:\t"))

if value < 1 | value > 3:
    print("Enter 1, 2 or 3")

class RPS(Enum):
    FIRST = 1
    SECOND = 2
    THIRD = 3

print(RPS.FIRST)
print(RPS.FIRST.value)
print(RPS)