
def project_1():
    '''project one
       print your name in different string methods.'''
    
    first_name = "scientist"
    last_name = "egong"

    # convert names to program specified methods.
    lower_case_name = first_name.lower() + " " + last_name.lower() # format name to lower case and concatenate.
    uppercased_name = lower_case_name.upper()
    title_cased_name = lower_case_name.title()


    print("These are my names in the following python methods;\n" \
    "upper, lower, and title case.\n")
    print(lower_case_name)  # scientist egong
    print(uppercased_name)  # SCIENTIST EGONG
    print(title_cased_name)  # Scientist Egong  
    print()

    return first_name, last_name




def project_2():
     '''concatenate first and second name'''

     first_name, second_name =  "scientist", "egong"
     first_name = first_name.title()
     second_name = second_name.title()
     concatenated_names = first_name + " " + second_name  # concatenate names
     print("\n Concatenated names are: ", end="")
     print(concatenated_names + "\n")
     


def project_3():
     '''Use f-string to show device IP and port.'''
     device_ip_address = "187.201.117.173"
     port_number = "49244"
     print(f"Ip address: {device_ip_address}\n"
           f"Device port number: {port_number}\n")
     

def main():
        while True:
            print("Here is a run down of project1\n" \
            "Enter each option to view code outputs.\n" \
            "1. Print your name in different formats (upper, lower, title).\n" \
            "2. Concatenate first and last variables names.")
            "3. View device Ip and port number.\n"

            user_input = input("\nEnter valid integers from (1 ~ 10) to proceed " \
            "or type 'exit' to exit: ")
            
            # Exit code
            if user_input == "exit":
                print("Thanks for playing with our code.")
                break
            elif user_input == "1":
                project_1()
            elif user_input == "2":
                 project_2()  
            elif user_input == "3":
                 project_3()  


if __name__ == '__main__':
    main()