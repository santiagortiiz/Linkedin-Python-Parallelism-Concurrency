#!/usr/bin/env python3
""" Connecting cell phones to a charger """

import random
import threading
import time

value = 1  # 1 = binary = mutex
charger = threading.Semaphore(value=value)


def cellphone():
    name = threading.current_thread().name
    with charger:
        print(name, 'is charging...')
        time.sleep(random.uniform(1, 2))
        print(name, 'is DONE charging!')

if __name__ == '__main__':
    for phone in range(100):
        threading.Thread(target=cellphone, name=f'Phone-{phone}').start()
