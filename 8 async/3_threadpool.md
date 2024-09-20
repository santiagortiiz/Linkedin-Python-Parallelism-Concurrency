# Threadpool
- Creates and maintains a collection of worker threads
- Reuses existing threads to execute tasks
- Many tasks for a threadpool, is like a TODO list for the threads
- Reusing threads with the threadpool, reduces overhead with creating new threads
- Advantage when the time to execute a task is less than the time required to create a new thread.