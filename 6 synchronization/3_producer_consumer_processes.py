#!/usr/bin/env python3
""" Producers serving soup for Consumers to eat.

Due to the GIL, threading is mostly useful for I/O bound task,
because when we have CPU bound tasks, the processor will be bussy
and the GIL does not allows other threads to run in the meanwhile.

This is why multiprocessing is preffered to be used for CPU bound tasks.

Note: sleep method simulates I/O bound task.
"""
import multiprocessing as mp
import time

serving_line_queue: mp.Queue = mp.Queue(5)


def cpu_work(work_units: int):
    """This func. simulates a CPU intensive operation, that will
    keep the processor bussy for a period of time.
    """
    x = 0
    for _ in range(work_units * 1_000_000):
        x += 1


def soup_producer(serving_line: mp.Queue):
    for i in range(20):  # serve 20 bowls of soup
        serving_line.put_nowait('Bowl #'+str(i))
        capacity = serving_line._maxsize - serving_line.qsize()
        print(f'Served Bowl # {i} - remaining capacity: {capacity}')
        time.sleep(0.2)  # time to serve a bowl of soup
    serving_line.put_nowait('no soup for you!')
    serving_line.put_nowait('no soup for you!')


def soup_consumer(serving_line: mp.Queue):
    while True:
        bowl = serving_line.get()
        if bowl == 'no soup for you!':
            break
        print('Ate', bowl)
        cpu_work(4)  # time to eat a bowl of soup


if __name__ == '__main__':
    for consumer in range(2):
        mp.Process(target=soup_consumer, args=(serving_line_queue,)).start()
    mp.Process(target=soup_producer, args=(serving_line_queue,)).start()
