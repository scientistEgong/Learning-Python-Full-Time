# Basic atm project
# THis program simulates the basics of an ATM Machine. 
# covering the basics of balance check, deposit, withdraw. and transfer.

user_balance = 0
pin_trial = 5

while True:
    print("--- ATM SIMULATOR ---")
    print("Enter the following options to proceed.\n" \
    "1. Check balance\n" \
    "2. Deposit\n" \
    "3. Withdraw\n" \
    "4. Exit\n")
    user_option = input("Enter an option to proceed: ")

    if user_option.lower() in ["4", "quit", "q", "exit"]:
        print("Exiting...")
        break

    while pin_trial > 0:
        try:
            pin = int(input("Enter user pin: "))
            if pin == (2520):
                break
            
            # -- Validate pin --
            if (len(str(pin)) > 4)  or (len(str(pin)) < 4):
                print("Pin not complete! Try again.")
                pin_trial -= 1
                print(f"You have {pin_trial} trials remaining to input the correct pin.")


        except (ValueError, TypeError):
            print("Error in pin input!")

    if user_option.lower() in ["1", "check balance", "balance check"]:
        print(f"User Balance: ${float(user_balance):.2f}/n")

    elif user_option.lower() in ["2", "deposit"]:
        while True:
            try: 
                deposit_amount = int(input("Enter amount to deposit: "))

                if deposit_amount < 0:
                    print("Deposit amount not available! enter a valid number.")
                    continue
                
                user_balance += float(deposit_amount)
                print(f"{deposit_amount} added successfully!\nNew balance: ${user_balance:.2f}\n")
                break

            except ValueError:
                print("Error in deposit input!")      
    
    elif user_option.lower() in ["3", "withdraw"]:
         while True:
            withdraw_input = input("Enter amount to withdraw or 'q' to quit: ")
            if withdraw_input.lower() == "q":
                    break

            try: 
                withdraw_amount = int(withdraw_input)
                
                if withdraw_amount > user_balance:
                    print("Insufficient Funds! please fund your account.")
                    continue

            
                user_balance -= float(withdraw_amount)
                print(f"Account debit: ${withdraw_amount}!\nNew balance: ${user_balance:.2f}\n")
                break
               
               

            except ValueError:
                print("Error in deposit input!")      
    

