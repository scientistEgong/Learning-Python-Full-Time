# Write a program that displays I am thinking of a number 
# if the user inputs number 3, print you win.
# Else it should print you lose.

number_of_playing_times = 5
while number_of_playing_times > 0:

    # Catch input errors.
    number_input = input("I am thinking of a number from 1 to 10.\nGuess it: ")
    try:
        number_input = int(number_input)
        # Game conditions.
        if number_input == 3:
            print("You win.")
            break
        else:
            print("You lose.")   


    except ValueError:
        print("Invalid input!")
        continue
    


    number_of_playing_times -= 1
    print(f"You have {number_of_playing_times} playing time left to play.")

    if number_of_playing_times == 0:
        print("Play Again, Enter 'y' or 'n'.")
        replay_input = input("choose an option to replay: ")
        if replay_input.lower() == "y":
            number_of_playing_times = 5
            continue
        
        else:
            print("Game Over.")
            break