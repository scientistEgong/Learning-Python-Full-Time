# Basic atm project
# THis program simulates the basics of an ATM Machine. 
# covering the basics of balance check, deposit, withdraw. and transfer.

user_balance = 0
pin_trial = 5


# -- Pin Verification --
while pin_trial > 0:
    try:
        pin = int(input("Enter user pin: "))

        # -- Correct pin --
        if pin == (2520):
            print("Pin verified successfully!")
            break
        
        # -- Validate pin --
        if (len(str(pin)) != 4 ):
            print("Pin not complete! Try again.")
            pin_trial -= 1
            print(f"You have {pin_trial} trials remaining to input the correct pin.")


    except (ValueError, TypeError):
        print("Error in pin input!")


# -- Check if user exceeded pin attempts --
if pin_trial == 0:
    print("No more trials remaining! Your account is temproary locked for the moment.\nExiting...")
    exit()


# -- ATM Operations --
while True:
    print("--- ATM SIMULATOR ---")
    print("Enter the following options to proceed.\n" \
    "1. Check balance\n" \
    "2. Deposit\n" \
    "3. Withdraw\n" \
    "4. Exit\n")
    user_option = input("Enter an option to proceed: ")


    # -- Exit option --
    if user_option.lower() in ["4", "quit", "q", "exit"]:
        print("Exiting...")
        break

   
    # -- Check Balance Option --
    if user_option.lower().strip() in ["1", "check balance", "balance check"]:
        print(f"User Balance: ${float(user_balance):.2f}")
        print("\n")

    # -- Deposit Option --
    elif user_option.lower().strip() in ["2", "deposit"]:
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

    # -- Withdraw Option --  
    elif user_option.lower() in ["3", "withdraw"]:
         while True:
            withdraw_input = input("Enter amount to withdraw or 'q' to quit: ")
            if withdraw_input.lower() == "q":
                    break

            try: 
                withdraw_amount = int(withdraw_input)
                if withdraw_amount < 0:
                    print("Withdrawal amount must be positive!")
                    continue

                if withdraw_amount > user_balance:
                    print("Insufficient Funds! please fund your account.")
                    continue

            
                user_balance -= float(withdraw_amount)
                print(f"Account debit: ${withdraw_amount}\nNew balance: ${user_balance:.2f}\n")
                break
               
               

            except ValueError:
                print("Error in deposit input!")      
    

