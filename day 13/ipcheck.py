import subprocess
import os

# Step 1: Define IP List
ip_list = [
    "192.168.1.1",
    "8.8.8.8",
    "10.0.0.1",
    "192.168.56.1"
]

# Step 3 & 4: Loop and Ping
for ip in ip_list:
    print(f"Checking {ip} ...")
    
    # For Windows use: ping -n 1
    # For Linux use: ping -c 1
    command = ["ping", "-n", "1", ip]  # change -n to -c for Linux

    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Step 5: Check Status
    if result.returncode == 0:
        print(f"IP address {ip} is reachable.\n")
    else:
        print(f"IP address {ip} is unreachable.\n")