def calculation_func():
        """Add, Subtract, Multiply, and Divide two numbers."""
        while True:
            print("Select what you intend to calculate;\n" 
            "1. ADD\n" 
            "2. SUBTRACT\n" 
            "3. MULTIPLY\n" 
            "4. DIVIDE\n" 
            "5. Exit.")

            calculator_funct_option = input(">>> ").strip()
            if calculator_funct_option.lower() == "exit":
                print("Thanks for running our simple calculator.")
                break
            
            # user input.
            num1 = input("Enter a number: ")
            num2 = input("Enter a number: ")
            
            
            # specifically check for int and floats in inputs.
            try:
                val1 = int(num1)
                val2 = int(num2)
                num1, num2 = val1, val2
            
                    
            except ValueError as e:
                try:
                    float_val1 = float(num1)
                    float_val2 = float(num2)
                    num1, num2 = float_val1, float_val2
                
                except ValueError:
                    print("\nInvalid input, try again.")
                    continue
                    

            if calculator_funct_option == "1":
                print("sum: ", num1 + num2)
            elif calculator_funct_option == "2":
                print("Subtraction: ", num1 - num2)
            elif calculator_funct_option == "3":
                print("Multiplication: ", num1 * num2)
            elif calculator_funct_option == "4":
                
                # catch all zero division errorss.
                try:
                    division_of_numbers = num1 / num2
                except ZeroDivisionError:
                    print("Number cannot be divided by 0")
                    continue    
                print(division_of_numbers)

            else:
                print("Invalid input, try again.")


if __name__ == "__main__":
    calculation_func()               