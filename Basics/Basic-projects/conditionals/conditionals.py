# Write a program that prompts the user to enter a word
# using the input fucntion and compare if the length of 
# the word is equal to number 5.
word_input = input("Enter a word: ").lower()
word_length = len(word_input)

input_less_than_five = word_length < 5
input_greater_than_five = word_length > 5
equal_inputs = word_length == 5

# Conditions
if input_greater_than_five:
    print("Your input is greater than 5 character long.")
elif input_less_than_five:
    print("Your input is less than 5 characters long.")
else:
    print("Your input is 5 Character long.")        