# check if a number is divisible by 3 and 5.
import sys as s
import string

puntuation = string.punctuation
puntuation_list = []
for characters in puntuation:
    char = " ".join(characters.split())
    puntuation_list.append(char)
    
    

iterator = True
while iterator:
    number = input("Enter a number that is divisible by 3 and 5 or q to quit: ")

    if number.lower() == "q":
        print("Exiting..")
        s.exit()

    if (number.isalpha) or any(number in puntuation_list):
        print("strings or special characters are not allowed!")
        continue  

    try:

        number = int(number)
    except ValueError as e:

        try: 
          number = float(number)
        except ValueError:
           print("Invalid input!")

    divisible1 = ((number % 3 == 0) and (number % 5 == 0))
    division2 = ((number % 3 == 0) and (number % 5 == 0))
    if divisible1 or division2:
        response = f"{number} is divisible by 3 & 5."
    else:
       response = f"{number} is not divisible by 3 & 5."

    print(response)

