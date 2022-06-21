#!/usr/bin/env python3
'''
CPU resources
Cores: 4
Logical processors: 8
    That means that each core supports 2 independent application at the same time
Sockets: 1
'''

""" Threads that waste CPU cycles """

import os
import threading

# a simple function that wastes CPU cycles forever
def cpu_waster():
    while True:
        pass

# display information about this process
print('\n  Process ID: ', os.getpid())
print('Thread Count: ', threading.active_count())
for thread in threading.enumerate():
    print(thread)

# Let's create half as many logical processors as there are in this system
print('\nStarting 4 CPU Wasters...')
for i in range(4):
    threading.Thread(target=cpu_waster).start()

# display information about this process
print('\n  Process ID: ', os.getpid())
print('Thread Count: ', threading.active_count())
for thread in threading.enumerate():
    print(thread)