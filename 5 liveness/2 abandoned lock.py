#!/usr/bin/env python3
'''
Death Thread
- If some thread acquires a lock and terminates because an unexpected reason,
  it may not automatically release the lock before it disappears.
  That leaves other tasks stuck waiting
'''

""" Three philosophers, thinking and eating sushi """

import threading

chopstick_a = threading.Lock()
chopstick_b = threading.Lock()
chopstick_c = threading.Lock()
sushi_count = 500

# Error handling version
def philosopher_try_finally_version(name, first_chopstick, second_chopstick):
    global sushi_count
    while sushi_count > 0: # eat sushi until it's all gone
        first_chopstick.acquire()
        second_chopstick.acquire()
        try:
            if sushi_count > 0:
                sushi_count -= 1
                print(name, 'took a piece! Sushi remaining:', sushi_count)
            if sushi_count == 10:
                print(1/0)
        finally:
            second_chopstick.release()
            first_chopstick.release()

# Context manager version
def philosopher(name, first_chopstick, second_chopstick):
    global sushi_count
    while sushi_count > 0: # eat sushi until it's all gone
        with first_chopstick:
            with second_chopstick:
                if sushi_count > 0:
                    sushi_count -= 1
                    print(name, 'took a piece! Sushi remaining:', sushi_count)

                if sushi_count == 10:
                    print(1/0)

if __name__ == '__main__':
    threading.Thread(target=philosopher, args=('Barron', chopstick_a, chopstick_b)).start()
    threading.Thread(target=philosopher, args=('Olivia', chopstick_b, chopstick_c)).start()
    threading.Thread(target=philosopher, args=('Steve', chopstick_a, chopstick_c)).start()
