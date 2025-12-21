def factorial():
    """
    factorial calculation
    * Define a function
    * Explain intent of code
    * Get an integer input from the user
    * Handle errors robustly (non- integers, zero, and negative numbers)
    * Give conditions if number is zero or negative it will automatically
      print 1 as res[onses and for negative numbers it will give an error
      message that negative numbers are not allowed.

    * Display output.
    * Display should have [5! = 120]
    * just like normal calculators or humans write.

    """
    while True:
        data_input = input("Enter a number or q to quit: ")
        
        # Exit
        if data_input.lower() == "q":
            print("Exiting..")
            break


        try:
            number = int(data_input)
            fact = 1
            if number == 0:
                print(f"{number}! = 1.")  
                continue

            elif number < 0:
                print("No negative factorials!")
                continue
            
            for n in range(1, number + 1):
                fact *= n

            print(f"{number}! = {fact}.")
                
        except ValueError:
            print("Invalid input!") 


factorial()