#!/usr/bin/env python3
""" Chopping vegetables with a ThreadPool """

import threading
from concurrent.futures import ThreadPoolExecutor  # Useful for IO-bound tasks


def vegetable_chopper(vegetable_id):
    name = threading.current_thread().name
    print(f"{name} chopped vegetable {vegetable_id}")


if __name__ == '__main__':
    # If max workers is not specified,
    # it creates 5 times as many threads as CPUs
    pool = ThreadPoolExecutor(max_workers=5)
    for vegetable in range(100):
        # threading.Thread(target=vegetable_chopper, args=(vegetable,)).start()
        pool.submit(vegetable_chopper, vegetable)
    pool.shutdown()
