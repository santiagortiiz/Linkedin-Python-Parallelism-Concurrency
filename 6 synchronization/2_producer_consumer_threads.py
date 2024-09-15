#!/usr/bin/env python3
""" Producers serving soup for Consumers to eat
The producer will raise an error when trying to put an item to a full queue,
this is why the consumers should be faster that the producer.

Here 2 consumers are created to achive that, but the program will never stop
if there are no more items in the queue, but the consumers are still waiting
for them.

This is why 2 additional messages are sent to the queue, in order to stop
consumers, based on a condition.
"""

from queue import Queue
import threading
import time

serving_line: Queue[str] = Queue(maxsize=5)


def soup_producer():
    for i in range(5):  # serve 5 bowls of soup
        serving_line.put_nowait(f'Bowl # {i}')

        queue_size = serving_line.qsize()
        remaining_capacity = serving_line.maxsize - queue_size

        print(f'Served Bowl # {i} - remaining capacity: {remaining_capacity}')

        time.sleep(0.2)  # time to serve a bowl of soup

    serving_line.put_nowait('no soup for you!')
    serving_line.put_nowait('no soup for you!')


def soup_consumer():
    while True:
        bowl = serving_line.get()

        if bowl == 'no soup for you!':
            t_name = threading.current_thread().name
            print(f"{t_name} breaking...")
            break

        print('Ate', bowl)
        time.sleep(0.3)  # time to eat a bowl of soup


if __name__ == '__main__':
    for consumer_n in range(2):
        threading.Thread(
            name=f"consumer_{consumer_n}",
            target=soup_consumer
        ).start()
    threading.Thread(name="producer", target=soup_producer).start()
