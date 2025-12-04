# Simple login system.

while True:
    print("-------WELCOME------------")
    user_name = input("Enter username: ")
    password = input("Enter password: ")

    if user_name.lower() == "scientist egong" and password.title() == "Success":
        print("Access Granted!")
        break
    else:
        print("Invalid login credentials!")
        