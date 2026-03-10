# 31.Ping simulation loop: print “Host alive” for a list of IPs.
import random as rn
import time as t
automation_tm = 0

address_testing_list = []
while automation_tm < 80: 
    ip_list = []

    for i in range(4):
        num = str(rn.randint(0, 255))
        ip_list.append(num)

    ip_address = ".".join(ip_list)
    address_testing_list.append(ip_address)

    automation_tm += 1

for ip in address_testing_list:
    print("............")
    if rn.choice([0, 1]):
        t.sleep(8)
        print(f"{ip} - Host alive")
        
    else:
        t.sleep(8)
        print(f"{ip} - No response")
    