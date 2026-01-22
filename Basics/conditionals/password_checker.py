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
    passwrd_input = input("Insert password: ")

    # Validate password over spaces
    if " " in passwrd_input:
        print("Spaces are not allowed!")
        continue

    password_length = len(passwrd_input)
    #  Validate coditions for password.
    password_lenth_check = (password_length > 8) 
    upper_check = any(password.isupper() for password in passwrd_input)
    digit_check = any(password.isdigit() for password in passwrd_input ) 
    lower_check = any(password.islower() for password in passwrd_input )
    special_chr = any(char in "#$%^&*(?!@#$%^&*)+{/.}:><?" for char  in passwrd_input)
    

    if not password_lenth_check:
        print("Password should be at least 8 characters.")
    elif not upper_check:
        print("password should contain at least one or more upper case letters.")
    elif not digit_check:
         print("password should contain at least one or more digits.")
    elif not  lower_check:
        print("password should contain at least one or more lower case letters.")
    elif not  special_chr:
         print("password should contain at least one or more special characters.")
    else:
        print("Strong password")           
    
