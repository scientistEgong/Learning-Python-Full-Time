import time

"""Loop through a list of devices and print config.
   Project Description:
   A device configuration is any setting/ information about a machine over a network.
   This project seeks to access the settings/configuration info of these devices, then
   it prints it to the user.
   
   Pseudocode
   - Create a list of device configuration info.
   - Loop through each device.
   - Print output."""

# Device configuration
devices = [
    {
        "name": "Router-Main",
        "ip": "192.168.1.1",
        "os": "Cisco IOS",
        "status": "active",
        "uptime": "45 days"
    },
    {
        "name": "Switch-Floor1",
        "ip": "192.168.1.2",
        "os": "Cisco IOS",
        "status": "active",
        "uptime": "30 days"
    },
    {
        "name": "Firewall-DMZ",
        "ip": "10.0.0.1",
        "os": "Palo Alto",
        "status": "inactive",
        "uptime": "0 days"
    },
    {
        "name": "Server-Database",
        "ip": "172.16.0.5",
        "os": "Linux Ubuntu",
        "status": "active",
        "uptime": "120 days"
    },
    {
        "name": "Server-Web",
        "ip": "172.16.0.6",
        "os": "Linux Ubuntu",
        "status": "active",
        "uptime": "60 days"
    }
]
# Loop and display
for a, data_info in  enumerate(devices, start=1):

    # Access device info
    name = data_info["name"]
    ip = data_info.get("ip", "unknown")
    os = data_info.get("os", "unknown")
    network_status = data_info.get("status", "unknown")
    uptime = data_info.get("uptime", "unknown")
    
    # Display configuration
    print(f"Device {a}")
    print(f"Name: {name}\nIp: {ip}\nOS: {os}\nStatus: {network_status}\nUptime: {uptime}")
    time.sleep(1)
    print()
    print("-----------------------")


