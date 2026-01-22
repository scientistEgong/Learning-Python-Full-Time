# Guess number game.

import random as rn
import sys as s

# The game seeks to match user inputs with that of the computer.
while True:
    plays = 5
    replay_g = 0
    while plays > 0:
        human_player = input("Guess a number between [1 - 100]: ")
        computer = rn.randint(1, 10)
        try:
            conditions = {int(human_player) > computer : "Too high",
                    int(human_player) < computer : "Too low",
                    int(human_player) == computer: "You guessed it correctly!"}
            for conditionals in conditions:
                if conditionals:
                    print(f"Game Response: {conditions[conditionals]}\nHuman guess: {human_player}\nComputer guess: {computer}\n")

            if int(human_player) == computer:
                continue

        except ValueError:
            print("Error!")            
        plays -= 1
        
        print(f"You have {plays} time remaining.") 

    print("You have exhausted your playing power.")
    while True:
        print("Would you like to continue? Enter [y/n]")
        replay = input("Enter a response: ")
        if replay.lower() == "n":
            print("Thanks for playing!")
            