#Guess the number - Game
#import Leo`s_brain

import os
import random

willingness_to_play = ("yes")

while willingness_to_play == ("yes"):

    # Clear Screen
    clear = lambda: os.system('cls')
    clear()

    # Game
    number = int(random.randint(1,10))
    guess = 0
    attempt = 0
    print("\nChoose a number between 1 and 10")
    
    while guess != number:
        guess = int(input("What is your guess ?"))
        attempt += 1
        if guess == number:
            print("\nYou won !\nScore", 10 - attempt)
        elif guess < number:
            print("\nChoice a larger number")
        else:
            print("\nChoice a lower number")
            
    willingness_to_play = input("\nDo you want to play again? (yes) (no)")

print("\nEnd game")