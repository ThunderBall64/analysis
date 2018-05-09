#!/usr/bin/env python

# Script                : hostname.py
# Author                : billint
# Date                  : 6th May 2018
# Objective             : Connect to server and display host configuration

##########################
##### Python Script ######
##########################

import socket

# Assign variable to a socket
target = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(target)

server = 'pythonprogramming.net'
port = 80

server_ip = socket.gethostbyname(server)
print(server_ip)

request = "GET / HTTP/1.1\nHost: "+server+"\n\n"

target.connect((server,port))
target.send(request.encode())

result = target.recv(4096)

#print(result)

while (len(result) > 0):
    print(result)
    result = target.recv(1024)