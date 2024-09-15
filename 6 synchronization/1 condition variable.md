# Problem

The mutex alone does not give a signal to the threads when the shared resource is occupied. So the threads that are waiting spent much time and energy checking whether the resource is available.

### Condition Variable
- Queue of threads waiting for a certain condition
- Associated with a mutex

### Monitor
- Works with mutex to implements a **Monitor**, which protect a section of code with mutual exclusion
- Provide the ability for threads to wait until a condition occurs

**Condition variable**
- wait: acquire the lock, check for a condition, if not satisfied, sleep
- signal: wake up one thread from condition variable queue
- broadcast: notify 1 or more threads

**multiple threads + multiple condition variables**
- implements a shared queue/buffer
- when multiple threads are putting items in the queue and putting them out, the mutex has to be used to ensure only 1 thread is doing updates at a time.
- 2 Condition variables enabled threads to signal each other when the state of the queue changes
  - wait for a BufferNotFull when adding items
  - wait for a BufferNotEmpty when taking items

