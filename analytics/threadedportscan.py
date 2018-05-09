#!/usr/bin/env python

# Script                : threadedportscan.py
# Author                : billint
# Date                  : 6th May 2018
# Objective             : Threaded port scanner("Similiar to sockets portscan.py script")

#########################
##### Python Script #####
#########################

import socket
import threading
from queue import Queue

print_lock = threading.Lock()

target = 'pythonprogramming.net'

def portscan(port):
    target = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        connect_to_target = target.connect((target,port))
        with print_lock:
            print('port',port,'<<< OPEN Port - Possible Entry Point >>>')

        # Close connection upon successful execution of script
        connect_to_target.close()

    except:
        pass

# Define the threader
def threader():
    worker = q.get()
    portscan(worker)
    q.task_done()

q = Queue()

for x in range(30):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

for worker in range(1,101):
    q.put(worker)

q.join()