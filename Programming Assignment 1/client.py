'''
Aaron Samuel
UCID: as3655
Section 012
'''
#! /usr/bin/env python3
# Echo Client
import sys
import socket

# Get the server hostname, port and data length as command line arguments
host = sys.argv[1]
port = int(sys.argv[2])
count = int(sys.argv[3])
data = 'X' * count # Initialize data to be sent
counter = 0

# Create UDP client socket. Note the use of SOCK_DGRAM
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientsocket.settimeout(1.0);
while counter < 3:
    try:
        # Send data to server
        print("Sending data to   " + host + ", " + str(port) + ": " + data)
        clientsocket.sendto(data.encode(), (host, port))
        # Receive the server response
        dataEcho, address = clientsocket.recvfrom(count)
        print("Receive data from " + address[0] + ", " + str(address[1]) + ": " + dataEcho.decode())
    except:
        counter += 1
        dataEcho = None
    if dataEcho is not None:
        counter = 3

#Close the client socket
clientsocket.close()
