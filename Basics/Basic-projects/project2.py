def numbers_and_operators_project():
    """All Numbers and operators projects."""

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
            num1 = input("Enter a number: ")
            num2 = input("Enter a number: ")
            

            # specifically check for int and floats in inputs.
            try:
                if int(num1) and int(num2):
                    break

                elif float(num1) and float(num2):
                    break
                else:
                    print("Data types do not match, try again.")
                    
            except ValueError as e:
                print("Invalid literal for mathematical computation.")
                
            if num1.isdigit() and num2.isdigit():
                
    
                if calculator_funct_option == "1":
                    print("sum: ", num1 + num2)
                elif calculator_funct_option == "2":
                    print("Subtraction: ", num1 - num2)
                elif calculator_funct_option == "3":
                    print("Multiplication: ", num1 * num2)
                elif calculator_funct_option == "4":
                    print("Division: ", num1 / num2)
            else:
                print("Invalid input, try again.")                   
        
    def main():
        "Run the number function"
        while True:
            print("Enter the following option or type 'exit' to quit: ")
            number_funct_input = input(">>> ")
            
            number_funct_options = {
                "1", calculation_func}
            
            if number_funct_input.lower() == "exit":
                return "Exiting Number functions."
            elif number_funct_input == "1":
                calculation_func()
            else:
                print("Invalid option.")    
                 
    if __name__ == "__main__":
        main()



def main():
    """Run the script"""
    
    while True:
            print("Enter a number to proceed.\n" 
            "1. Numbers And Operators projects\n")
            
            functions_dict = {
                "1": numbers_and_operators_project
            }

            main_funct_input = input("Enter an option to proceed, or type 'exit' to quit: ")

            if main_funct_input.lower() == "exit":
                print("Thanks for playing with our code.")
                break
            elif main_funct_input in functions_dict:
                functions_dict[main_funct_input]()
            else:
                print("Invalid input.") 

if __name__ == "__main__":
    main()