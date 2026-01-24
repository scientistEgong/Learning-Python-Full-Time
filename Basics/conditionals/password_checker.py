# Password strength checker (length + digit + symbol).
"""
Psuedocode
----------------
1. loop through code.
2. Get password.
3. Validate password by length.
4. Validate by criterias:
    week password = [less than 8, contains only digits and lowercase.]
    medium password = [upto 8, contains digits, upper & lowercase.]
    strong password = [upto 8  and above. Contains digits, upper & lowercase, special characters.]
    
5. Display code ouput to user.
-------------------------------
CONCEPTS USED
~ Basics 
~ Loops
~ Strings 
~ Implicit functions (print)"""

# === Main code Loop ===
run = True
while run:
    password_input = input("Insert password or 'q' to quit: ")

    # Exit code
    if password_input.lower() == "q":
        print("Exiting...")
        break

    # Validate password over spaces
    if " " in password_input:
        print("Spaces are not allowed!")
        continue

    
    #  Validate coditions for password.
    password_length = len(password_input)
    password_length_check = (password_length >= 8) 
    upper_check = any(password.isupper() for password in password_input)
    digit_check = any(password.isdigit() for password in password_input ) 
    lower_check = any(password.islower() for password in password_input )
    special_chr = any(char in "#$%^&*(?!@#$%^&*)+{/.}:><?" for char  in password_input)
    
    # strong password condition
    strong_password_condition = (password_length_check
                         and (upper_check)
                         and (digit_check)
                         and (lower_check)
                         and (special_chr))

    # Store password reponses
    pass_word_conditions = {password_length_check: "Password should not be less than 8 characters.",
                      upper_check: "Password should contain one or more uppercase letter.",
                      digit_check: "Password should contain one or more digits.",
                      lower_check: "Password should contain at least one or more lowercase letter.",
                      special_chr: "Password should contain at least one or more special characters.",
                      }
    
    # Display password options 
    for condition, message in pass_word_conditions.items():
        if not condition:
            print(message)
    

    # Display strong password message
    if strong_password_condition:
        print("Strong password!")
        break
       

    
    

     
    
