def calculate_remainder():
        """Calculate the remainder of dividing two numbers."""
        while True:
                
            num1 = input("Enter a number: ")
            num2 = input("Enter another number: ")
            
            # Handle all invalid inputs.
            try:
                num1 = int(num1)
                num2 = int(num2)
                remainder = num1 % num2
                division_result = f"The remainder of dividing {num1} and {num2} is: {remainder}"
                print(division_result)

                # Code replay options.
                print("Do you want to continue or quit, enter 'y'  to continue or 'n' to quit.")
                user_input = input(">>> ").strip()
                if user_input.lower() == "n":
                   print("Thanks for playing with our remainder calculator.")
                   return
            
            except ZeroDivisionError:
                print("Number cannot be divided by 0.")
            except ValueError:
                print("Invalid input, try again.")


if __name__ == "__main__":
    calculate_remainder()