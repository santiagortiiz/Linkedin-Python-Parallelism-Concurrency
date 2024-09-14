#!/usr/bin/env python3
""" Two shoppers adding items to a shared notepad """

import threading
import time

garlic_count = 0
pencil = threading.Lock()

def shopper():
    global garlic_count
    for i in range(5):
        # Thinking is not a step that must be protected from race conditions
        print(threading.current_thread().getName(), 'is thinking.')
        time.sleep(0.5)

        # Just lock the critical section
        pencil.acquire()
        garlic_count += 1
        print(threading.current_thread().getName(),
              f'added a garlic: total {garlic_count}.')
        pencil.release()

if __name__ == '__main__':
    barron = threading.Thread(name="Barron", target=shopper)
    olivia = threading.Thread(name="Olivia", target=shopper)
    barron.start()
    olivia.start()
    barron.join()
    olivia.join()
    print('We should buy', garlic_count, 'garlic.')
