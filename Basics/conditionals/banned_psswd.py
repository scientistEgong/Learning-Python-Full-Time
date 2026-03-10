#  Check if a password is on a banned list.
"""Steps for project.
    1. Create a standard list of banned passwords[Upto 15 hardcoded passwords.].
    2. Loop through for password input.
    3. Get user input.
    4. Compare to banned list.
    5. Print outputs."""

# Banned password list
banned_password = ["12345", "password", "love",
                   "python", "qwert", "online",
                   "admin", "google", "book",
                   "church", "school", "work",
                   "university", "rich", "technology",
                   "savvy", "tech", "machine learning"]

# Main program loop
while True:
    user_password = input("Type in a password or 'q' to exit program: ").strip()

    # Exit program
    if user_password.lower() == "q":
        print("Exiting...")
        break

    # Compare passwor 
    if user_password.lower() in banned_password:
        print("System detected your password was banned! Try again.")
    else:
        print("Password is safe!")    