# Detect weak default credentials (Admin/Admin)
# Create a list of default credentials
default_credentials = [
    ("admin", "admin"),
    ("admin", "password"),
    ("root", "root"),
    ("root", "toor"),
    ("user", "password"),
    ("guest", "guest"),
    ("admin", "1234"),
    ("admin", "123456"),
    ("administrator", "admin"),
    ("test", "test"),
    ("support", "support"),
    ("admin", ""),
    ("user", "1234"),
    ("administrator", "root"),
    ("password", "password")]

# Main code loop
while True:
    # Initialize a flag
    found = False

    # Get user inputs
    username = input("Enter device username: ").lower().strip()
    password = input("Enter device password: ").lower().strip()

    # Handle blank passwords
    if password == "":
        print("Device passwords cannot be blank!")
        continue

    # Loop through device credentials
    for usrname, pwd in default_credentials:
        # Validate credentials
        if (username == usrname) and (password == pwd):
            print("Warning! Weak device credentials detected.")
            found = True
            break
            

    if not found:
        print("Credentials appear safe.")