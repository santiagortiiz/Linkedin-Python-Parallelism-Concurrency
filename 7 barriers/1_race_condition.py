#!/usr/bin/env python3
""" Deciding how many bags of chips to buy for the party
This program is protected against data races because the with statements (lock/unlock)
against a shared resources, prevents the read/write of multiple threads at the same time.

However, is still vulnerable to a race condition.
"""
import threading

bags_of_chips = 1  # start with one on the list
pencil = threading.Lock()


def cpu_work(work_units):
    x = 0
    for _ in range(work_units*1_000_000):
        x += 1


def barron_shopper():
    """Do some CPU intensive work and double bags_of_chips"""
    global bags_of_chips
    cpu_work(1)  # do a bit of work first
    with pencil:
        bags_of_chips *= 2
        print('Barron DOUBLED the bags of chips.')


def olivia_shopper():
    """Do some CPU intensive work and add 3 bags_of_chips"""
    global bags_of_chips
    cpu_work(1)  # do a bit of work first
    with pencil:
        bags_of_chips += 3
        print('Olivia ADDED 3 bags of chips.')


if __name__ == '__main__':
    shoppers: list[threading.Thread] = []
    for s in range(5):
        shoppers.append(threading.Thread(name="Barron", target=barron_shopper))
        shoppers.append(threading.Thread(name="Olivia", target=olivia_shopper))
    for s in shoppers:
        s.start()
    for s in shoppers:
        s.join()
    print('We need to buy', bags_of_chips, 'bags of chips.')
