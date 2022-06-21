# Critical sections
- Code segment that access shared resource
- Should not be executed by more than one thread at a time

# Mutex (Lock)
- Mechanism to implement mutual exclusion
- Only 1 thread or process can have posession of the lock at a time
- Limit access to critical sections

# Atomic operation
- The action of acquire the lock
- Execute a single and indivisible action, relative to other threads
- Cannot be interrupted by other concurrent threads

# Acquiring a Lock
- Threads that try to acquire a lock that's currently posses by another thread
  can pause and wait until it's available
- Don't forget to release the mutex/lock when the tasks are done

# Tip
- Keep protected sections of code as short as possible