import string as st
import random as rn 

# Password Attempt list
password_list = []

# Fixed password 
fixed_password = "DangerousAttmpt@995*"

# Generate attacks password
for counts in range(20):
    password = "".join(rn.choices(st.ascii_letters + st.punctuation + st.digits, k=(rn.randrange(1, 20))))
    password_list.append(password)

# Add fixed password to list to make it crackable
password_list[rn.randint(0, len(password_list) - 1)] = fixed_password

# Brute force attack
start = 0
end = 10
while end > start:
    for passwd in password_list:
        print(f"Attempt: {start}: Trying: '{passwd}'\nStatus: ", end="")
        if passwd == fixed_password:
            print("SUCCESS!")
            print(f"password was successfully cracked!")
            exit()
        else:
            print("FAILED")
            print("---------\n")
        start += 1 
           
    
    
            


