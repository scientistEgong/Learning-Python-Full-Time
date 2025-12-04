while True:
    number = input("Enter a list of  numbers seperated by comma to check the largest; or 'q' to quit: ").strip()
    if " " in number:
        print("Spaces are not allowed! Numbers should be seperated by commas.\n")
        continue

    if number.lower()  == "q":
        print("Exiting...")
        break
        
    try: 

        numerals = number.split(",")
        integer_list = []
        for i in numerals:
            integers = int(i)
            integer_list.append(integers)
            
        final_output = max(integer_list)
        output_list = []
        string_output = str(final_output)
        output_list.append(string_output)
        print(output_list)

    except ValueError:
        print("Invalid input, Try again.")       