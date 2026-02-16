# Validate if input is a valid Ipv4 address.
# project loop
while True:
    ipv4_input = input("Enter a valid ipv4 address: ").strip()

    # seperate address by dots
    seperated_address = ipv4_input.split(".")

    # Validate if address is upto 4 decimal places.
    if len(seperated_address) != 4:
        print("Invalid address!")
        continue
    
    # check for special characters.
    if any(char for char in seperated_address if char in "/,=][/;:?><*&%$^]"):
            print("Special characters should not be included in Ip addresses.")
            continue

    # Validate each octet.
    is_valid = True
    for address_part in seperated_address:

        # Validate inputs for alphabets.
        if address_part.isalpha():
            print("Invalid address!")
            is_valid = False
            break
        
        try:
            # Validate integer and range (0 - 255)
            if address_part != str(int(address_part)):
                print("Invalid address!")
                is_valid = False
                break
            
            if not 0 <= int(address_part) <= 255:
                print("Address should not exceed the range of (0  ~ 255)!")
                is_valid = False
                break

        except ValueError:
            print("Invalid address!")
            is_valid = False
            break


    # Display valid address
    if is_valid:
        print("Valid Ipv4 address!")   

        