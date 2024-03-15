"""
Contains functions to simulate dice rolls. The functions can simulate 20, 12, 10, 8, 6, 4, 3, 2, and 100 sided die.
"""
from random import randint


"""
Simulates a d20 dice roll.
"""
def roll_d20():
    return randint(1,20)


"""
Simulates a d12 dice roll.
"""
def roll_d12():
    return randint(1, 12)


"""
Simulates a d10 dice roll.
"""
def roll_d10():
    return randint(1, 10)


"""
Simulates a d8 dice roll.
"""
def roll_d8():
    return randint(1, 8)


"""
Simulates a d6 dice roll.
"""
def roll_d6():
    return randint(1, 6)


"""
Simulates a d4 dice roll.
"""
def roll_d4():
    return randint(1, 4)


"""
Simulates a d3 dice roll.
"""
def roll_d3():
    return randint(1, 3)


"""
Simulates a d2 dice roll.
"""
def roll_d2():
    return randint(1, 2)


"""
Simulates a d100 dice roll.
"""
def roll_d100():
    return randint(1, 100)