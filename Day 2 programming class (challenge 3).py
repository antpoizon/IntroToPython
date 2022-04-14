# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 16:39:28 2022

@author: Ryan Borowski
"""

wantsToPlay = input("Would you like to guess a value between 1 and 50? please enter yes or no")

if (wantsToPlay.lower() == "yes"):
    randomNumber = int(input("Please enter a random number between 1-50:"))
    if (randomNumber == 36):
        print(f"CONGRATULATIONS!!! {randomNumber} is the correct number, so you win a free* boat!!")
    elif (randomNumber >= 31 and randomNumber <= 41):
        print(f"Aw shucks, {randomNumber} was very close to the grand prize, but instead you win a years' subscription to the jelly of the month club!")
    elif (randomNumber < 31 or randomNumber > 41):
        print(f"{randomNumber} is a bad number and you win nothing.")
elif (wantsToPlay.lower() == "no"):
    print("Okay then. Goodbye!")
else:
    print("That is not an acceptable response. Goodbye!")