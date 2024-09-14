#!/usr/bin/env python3
""" Two shoppers adding garlic and potatoes to a shared notepad """

import threading

garlic_count = 0
potato_count = 0

# RLock:
# Reentrant lock that can be acquire() multiple time before release()
# Reentrant locks support the context management protocol
# Failing to call release as many times the lock has been acquired can lead to deadlock.
pencil = threading.RLock()

def add_garlic():
    global garlic_count
    pencil.acquire()
    garlic_count += 1
    print(
        threading.current_thread().getName(),
        f'added a garlic: total {garlic_count}.'
    )
    pencil.release()

def add_potato():
    global potato_count
    pencil.acquire()
    potato_count += 1
    print(
        threading.current_thread().getName(),
        f'added a potato: total {garlic_count}.'
    )
    add_garlic()                # this will call acquire() method before release
    pencil.release()

def shopper():
    for i in range(2):
        add_garlic()
        add_potato()

if __name__ == '__main__':
    barron = threading.Thread(name="Barron", target=shopper)
    olivia = threading.Thread(name="Olivia", target=shopper)

    barron.start()
    olivia.start()

    barron.join()
    olivia.join()

    print('We should buy', garlic_count, 'garlic.')
    print('We should buy', potato_count, 'potatoes.')
