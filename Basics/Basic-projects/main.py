from remainder import calculate_remainder as cr
from calculator import calculation_func as cf

def main():
    """Run the script"""
    
    while True:
            print("Enter a number to proceed.\n" 
            "1. Calculator \n" 
            "2. Number remainder calculator \n" 
            "")

            main_funct_input = input("Enter an option to proceed, or type 'exit' to quit: ")

            if main_funct_input.lower() == "exit":
                print("Thanks for playing with our code.")
                break
            elif main_funct_input == "1":
                cf()
            elif main_funct_input == "2":
                 cr()    
            else:    
                print("Invalid input.") 

                

if __name__ == "__main__":
    main()



