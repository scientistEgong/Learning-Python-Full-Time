# Naming conventions.
# Snake Case
first_name = "Scientist"
last_name = "Egong"
print(first_name, last_name)


# Camel case
fisRTnAME = "Scientist"
LasTNaME = "Egong"
print(fisRTnAME, LasTNaME)


# Statements
print("Hey there!, python is fun.")


# Comments
print("\nComments that appear at the end of a statement"\
      " are called in-line comments.")  # Inlne comments


"""Docs comments
This comment types are usually used in functions to document what the function does."""

def calculator(a, b):
    """This is a mini calculator that collects
    two digits and returns the sum"""
    sum_of_integers = a + b

    return sum_of_integers

# collect user input
while True:
        num1 = input("Enter a valid integer: ")
        num2 = input("Enter a valid integer: ")
        try:
             num1 = int(num1)
             num2 = int(num2)
             break
        except (ValueError, ValueError) as e:
            print("Datatype not recoognised, enter a valid integer.")
        
print(calculator(a=num1, b=num2))



# String Quotation guide
first_name = 'Daniel'  # single quotation mark
second_name = "Daniel"  # Double quoation mark
print(first_name, second_name)