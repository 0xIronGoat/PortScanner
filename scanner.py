import argparse
import socket
import sys
from time import strftime, localtime


# Define the target from arguments
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])  # Translate hostname to IPv4 if necessary
else:
    print("Invalid number of arguments provided.")
    print("Syntax: python3 scanner.py <ip or hostname>")


# Print a banner
print("-" * 50)
print(f"Scanning target: {target}")
print("Time started: " + strftime("%H:%M:%S %m %b %Y", localtime()))
print("-" * 50)

# Try connecting to each port on target in range 1 - 1024
try:
    for port in range(1025):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)  # After 1 second it will assume port closed and move on to next port
        result = s.connect_ex((target, port))  # Returns a 1 if error received connecting to port

        if result == 0:
            print(f"Port {port} is open.")
        s.close()
except KeyboardInterrupt:
    print("Exiting script.")
    sys.exit()
except socket.gaierror:
    print("Error resolving hostname.")
    sys.exit()
except socket.error:
    print("Could not connect to hostname.")
    sys.exit()
