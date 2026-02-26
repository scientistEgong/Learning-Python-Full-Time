# Split an IP address into it's octet. 
ip_input = input("Enter an IP address: ")
ip_split = ip_input.split(".")

for ips in ip_split:
    print(ips, end=" " )