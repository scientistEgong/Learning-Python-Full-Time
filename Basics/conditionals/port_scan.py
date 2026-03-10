# 32.Port scan simulation: loop through ports 20–30 and mark them open/closed (fake data).
# Imports
import random as rn
import time

# create dictionary of ports and list of random flags [open/close]
ports = {
    20: "FTP-DATA",
    21: "FTP",
    22: "SSH",
    23: "TELNET",
    25: "SMTP",
    29: "MSG-ICP",
    30: "ARIS"}

# Loop for each port in the range of 20 - 30
for port in  range(20, 31):
    # Get service name from the dict.
    service = ports.get(port, "unknown")

    # Status
    status = rn.choice(["OPEN", "CLOSED"])

    # Display outputs
    print(f"Port {port} ({service}) --- {status}")
    time.sleep(1)


            

        
    