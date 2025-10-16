def celsius_calculator():
    """Convert user input to fahrenheit"""
    while True:
        print("Enter a number or exit to quit.")
        user_input = input(">>> ")

        # quit code
        if user_input.lower().strip().startswith("exit"):
            print("Thanks for playing with our code.")
            break
        else:

            try:
                integer = int(user_input)
                fahrenheit_conversion = ((integer) * (1.8) + (32))
                print(f"{integer}C = {fahrenheit_conversion}F")

            except ValueError:
                try:
                    float_integer = float(user_input)
                    fahrenheit_conversion = ((float_integer) * (1.8) + (32))
                    print(f"{float_integer}C = {fahrenheit_conversion}F")
                except ValueError:
                    print("Invalid input, try again.")   

celsius_calculator()                

