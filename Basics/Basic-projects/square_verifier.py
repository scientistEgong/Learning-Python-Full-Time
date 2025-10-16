def square_displayer():
    """Display the cube and Square of a number."""
    while True:
        print("Enter the following options to proceed.")
        print("1. Display the square of a number.\n" 
               "2. Display the cube of a number.")

        user_input = input("Enter one of the options to proceed or exit to quit: ").strip()
        if user_input.lower() == "exit":
            break
        
        # catch all errors.
        try:
            number = float(input("Enter a number you want to square or view it's cube: "))
            if user_input == "1":
                square_of_number = (number ** 2)
                print(f"The Square of {number} is {square_of_number}")

            elif user_input == "2":
                cube_of_number = (number ** 2 * number)
                print(f"The cube of {number} is {cube_of_number}.")
            else:
                print("Invalid option.")


        except ValueError:
            print("Invalid input. Try again.")   

        

square_displayer()                