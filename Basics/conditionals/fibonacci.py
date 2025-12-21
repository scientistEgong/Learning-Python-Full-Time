def fibonacci_sequence():
    """
    Docstring for Basics.conditionals.fibonacci
    Define a function
    Write out the intent of the function.
    Run an iteration
    Inputs:
    - The range of the sequence.
    - The first two numbers in a single input.
    - Type casting and case converison.
    - conditions for handling errors.
    loops to get the fibonacci sequence
    converting ouputs into list in list (I love it this way.)
    print output.
    
    """
    print('DISPLAY FIBONACCI SERIES IN A SEQUENCE.')
    while True:

        series_range = input("Enter range of fibonacci sequence to start.\nE.g first 4, 5, 9 series or (q to quit): ")
        if series_range.lower() == "q":
            print("Exiting...")
            break

        
        sequence_default_number = input("Enter the first two sequence numbers e.g (0, 1) or (1, 1) seperated by comma: ")
        if any (char for char in sequence_default_number if char in ".;'/=-") or len(sequence_default_number) <= 1:
            print("Numbers must be seperated with commas.\n")
            continue

        cleaned_numbers = sequence_default_number.replace(" ", "").split(",")
        x, y = [num for num in cleaned_numbers]
        
        try:
            num1 = int(x)
            num2 = int(y)
            counter = int(series_range)
            while True:
                checks = (
                    (num1 > 1) or 
                    (num1 < 0) or
                    (num2 != 1)
                    )
                
                if not checks:
                    print("Input verified!\n")
                    break
                else:
                   print("Invalid default input.")
                   continue
            
            data = [num1, num2]
            for n in range(counter - 2):
                c = num1 + num2
                num1 = num2
                num2 = c
                data.append(num2)
            
            print(f"\nFibonacci series for {counter} consecutive figures are:")
            print(data)      

        except ValueError:
            print("Invalid input!")
        





def nth_fibonacci_number():
    """
    Input: Which position? (1st, 2nd, 4th, etc.)
    Edge cases: Handle 0, negative, text
    Logic: How do you calculate just that one number?
    Output: Single Fibonacci number 
    """


def quit():
    print("Exiting..")
     


def main():
    """Run all scripts"""
    while True:
        print("----Fibonacci sequence Generator---")
        print("1. Generate Fibonacci sequence.\n" 
        "2. Get Nth fibonacci seris.\n" 
        "3. Quit.\n")
        main_options = input("Enter one of the options to proceed: ")
        if main_options == "1":
            fibonacci_sequence()
        elif main_options == "2":
            nth_fibonacci_number()
        elif main_options == "3":
            quit()
            break
        else:
            print("Invalid input, Try again.")


if __name__ == "__main__":
    main()