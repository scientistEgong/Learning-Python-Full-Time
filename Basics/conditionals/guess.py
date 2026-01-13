# Guess number game updated method.
import random as rn

# -- Main Game Loop --
while True:
    plays = 5
   


    while plays > 0:
        number = input("Guess a number between [1 - 100]: ")
        
        
        # --- Check if player guesses correctly --
        try:
            human_player = int(number)
            computer = rn.randint(1, 100)

            if human_player > computer:
                print(f"Game Response: Too high")
            elif human_player < computer:
                print(f"Game Response: Too low")
            elif human_player == computer:
                print(f"Game Response: You guessed it correctly!")

            print(f"Human Guess: {human_player}\nComputer Guess: {computer}\n")    
            plays -= 1
            print(f"You have {plays} attempts remaining.") 

        except ValueError:
           print("Error!")


    # -- Replay Option --
    while True:
        replay = input("Would you like to continue? [y/n]: ").lower()
        if replay == "y":
            break
        if replay == "n":
           print("Thanks for playing!")
           exit()
        

        else:
            print("Invalid input!")
    



        
   
        
