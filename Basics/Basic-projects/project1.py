
def project_1():
    '''Display your name in lower, title case, and upper case.'''
    
    first_name = "scientist"
    last_name = "egong"

    formated_name = f"{first_name} {last_name}"
    uppercased_name = formated_name.upper()
    title_cased_name = formated_name.title()
    lower_case_name = formated_name.lower()


    print("These are my names in the following python methods;"
          "\nlower, upper, and title case.")
    print(lower_case_name)
    print(uppercased_name)
    print(title_cased_name)  
    print()



def project_2():
    '''concatenate first and last name'''

    first_name = "scientist".title()
    last_name = "egong".title()

    concatenated_names = first_name + " " + last_name  # Concatenate names
    print("\n Concatenated names are: ", end="")
    print(concatenated_names + "\n")
     


def project_3():
    '''Use f-string to show device IP and port.'''

    device_ip_address = "187.201.117.173"
    port_number = "49244"

    print(f"Ip address: {device_ip_address}\n"
        f"Device port number: {port_number}\n")
     

def project_4():
    """Count characters in a string"""
    string_input = input("Enter a word: ").strip()
    count_of_char = len(string_input)
    
    
    if not string_input:
        print("No input detected, type a word.")
        print()
        return

    # check for sentences
    if " " in string_input or any(punc in string_input for punc in "',.!?"):
        sentence_flag = "sentence"
        print(f"There are {count_of_char} characters in the {sentence_flag}, {string_input.title()}.")

    
    # check for letters.
    elif len(string_input) == 1 and string_input.isalpha():
        letter_flag = "letter"
        print(f"The {letter_flag} you entered is {string_input.upper()}")
        print(f"Total length of string: {count_of_char}.")

    else:
        word_flag = "word"     
        print(f"There are {count_of_char} characters in the {word_flag} {string_input.capitalize()}.")
        
   
    print('-' * 40)


def project_5():
    """Replace a word in a string"""

    string_input = input("Enter a sentence: ").title().strip()
    word_to_be_replaced = input("Enter the word you want to replace: ").title().strip()
    new_word = input("Enter the new word you want to add to the sentence: ").title().strip()

    modified_sentence = string_input.replace(word_to_be_replaced, new_word)
    print(f"Before: {string_input}.")
    print(f"After: {modified_sentence}.\n")


def main():
        while True:
            print("Here is a run down of project1\n" 
            "Enter each option to view code outputs.\n" 
            "1. Print your name in different formats (upper, lower, title).\n" 
            "2. Concatenate first and last variables names.\n"
            "3. View device Ip and port number.\n"
            "4. Count characters in a given string.\n"
            "5.Replace a word 'SSH' in the string to 'Telnet' \n")

            user_input = input("\nEnter an integer from (1 ~ 10) or type 'exit' to quit: ").strip()
            
            
            # Exit code
            if user_input.lower() == "exit":
                print("Thanks for playing with our code.")
                break
            elif user_input == "1":
                project_1()
            elif user_input == "2":
                 project_2()  
            elif user_input == "3":
                 project_3()
            elif user_input == "4":
                 project_4()
            elif user_input == "5":
                 project_5()       
            else:
                print("Invalid input, try again.")


if __name__ == '__main__':
    main()
