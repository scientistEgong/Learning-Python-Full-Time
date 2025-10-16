def interest_calculator():
    """Simple Interest Calculator"""
    print("simple interest calculator".center(45, "="))

    while True:
       print("Type exit to quit or interest to continue.")
       user_input = input(">>> ").strip().lower()

       #  Quit game.
       if user_input == "exit":
           print("Thanks calculating with our interest calculator.")
           break
       
       elif user_input == "interest":
           try:
               principal = float(input("Enter principal amount: "))
               rate = float(input("Enter annual interets rate in (%): "))
               time = float(input("Enter time in years: "))
           

               # calculate interest
               interest = ((principal * rate * time) / 100)
               total_amount = principal + interest

               print(f"\nAfter {time} years at {rate}% interest rate.")
               print(f"Interest Earned: {interest:.2f}")
               print(f"Total amount Earned: {total_amount:.2f}")

            
           except  ValueError:
               print("Invalid input, enter only numeric values.")

       else:
           print("Invalid Input. Try again.")       
               

interest_calculator()            





