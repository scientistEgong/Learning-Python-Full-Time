# Print Hello five times using repeated print.
print("Hello!")
print("Hello!")
print("Hello!")
print("Hello!")
print("Hello!")
print("Project 1 done.\n")

# Concatenate a string with itself multiple times.
string_input = input("Enter a string: ").strip()
concationation_count = int(input("How many times do you want to concatenate your input: "))

concatenated_string = " ".join([string_input] * concationation_count)
print(concatenated_string)

# Simulate a login attempt.
name = input("Enter your username: ").lower()
password = input("Enter your login password: ")

check = False
if password == "hit33"and name == "scientist":
    print("Login successful!")

else:
    print("Invalid login details.")    


# Create a script that outputs todays date as a string.
from datetime import datetime as dt
today_date = dt.now()
print(str(today_date))