# Check if a number is positive, negative, or zero

while True:
    number_input = input("Enter a number: ")
    number = int(number_input)
    if number < 0:
        print("It's a negative number.")

    elif  number > 0:
        print("It's a positive number.")

    elif number == 0:
        print("It is zero.")
        break
    else:
        print("Invalid input.")          


# Determine if a year is a leap year.
leap_year = "Not a leap year."
while True:
    year_input = int(input("Enter a year: "))

    # If year is evenly divided by 4 and 400 then its a leap year.
    if year_input % 4 == 0:
        if year_input % 100 == 0:
            if year_input % 400 == 0:
                leap_year = True

            else:
                leap_year = False  # Not a leap year if divisible by 100.

        else:
            leap_year = True  # It's a leap year if divisible by 4.

    else:
        leap_year == False
    print(leap_year)    

#     # --- Part 1: sign check ---
# while True:
#     raw = input("Enter a number: ")
#     try:
#         number = int(raw)
#     except ValueError:
#         print("Not a valid integer.")
#         continue

#     if number < 0:
#         print("It's a negative number.")
#     elif number > 0:
#         print("It's a positive number.")
#     else:
#         print("It is zero.")
#         break


# # --- Part 2: leap year test ---
# def is_leap(y: int) -> bool:
#     # Leap year rules: divisible by 4, except centuries unless divisible by 400.
#     return (y % 4 == 0) and (y % 100 != 0 or y % 400 == 0)

# while True:
#     raw = input("Enter a year: ")
#     try:
#         year = int(raw)
#     except ValueError:
#         print("Not a valid year.")
#         continue

#     leap = is_leap(year)
#     print("Leap year." if leap else "Not a leap year.")
