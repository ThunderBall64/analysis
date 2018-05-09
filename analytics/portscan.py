#!/usr/bin/env python

# Script                : portscan.py
# Author                : billint
# Date                  : 6th May 2018
# Objective             : Scan open ports of target host

#########################
##### Python Script #####
#########################

import socket

host = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = 'pythonprogramming.net'

def portscan(port):
    try:
        host.connect((server,port))
        return True
    except:
        return False

for x in range(1,26):
    if portscan(x):
        print('Port',x,'<<< OPEN PORT DETECTED >>>')
    else:
        print('Port',x,'*** Closed.')