# Rock, Paper, Scissor game
import random as rn

# Initialize game loop
while True:
    user_input = input("Type in a choice either (rock/paper/scissors) or 'q' to quit: ")
    
    # list of computer choices 
    compt_choice_list = ["rock", "paper", "scissors"]

    # Initialize computer options
    compt_index = rn.randint(0, 2)
    computer = compt_choice_list[compt_index]

    # Exit game
    if user_input.lower() == "q":
        print("Exiting...")
        break

    # Validate invalid inputs
    if user_input.lower() not in compt_choice_list:
        print("Invalid input! Try again.")
        continue

    # Game conditions
    game_conditions = ((computer == "rock" and user_input == "scissors") 
                       or (computer == "scissors" and user_input == "paper")
                       or (computer == "paper" and user_input == "rock"))
    
    # Determine game outcomes.
    if game_conditions:
        print("computer win!")
    elif computer == user_input:
        print("It is a tie!")
    else:
        print("You win!")

    # Replay options
    print("Would you like to continue, enter (y/n)?")
    replay = input(">>> ")
    if replay.lower() == "n":
        print("Thanks for playing!")
        break        