# Semaphore
It's another sync mechanism to control access to shared resources
- Unlike a mutex, it can be used by multiple threads at the same time
- Includes a counter to track availability (how many times it has been acquired or released)
- counter > 0: Available. Semaphore can be acquired
- counter == 0: Threads trying to acquire the semaphore will be blocked and placed in a queue to wait until it's availability
- When the thread releases the semaphore, it increments the counter and if there are other threads waiting the semaphore, they will be signaled to wake up and do so.

## Common use cases
- Used to track limited resources
  - Pool of connections
- Items in a Queue

**Additional Type**: Binary Semaphore. 0 or 1 (locked/unlocked)

# Mutex VS Semaphore
- Mutex can only be acquired/released by the same thread
- Semaphore can be acquired/released by different threads
