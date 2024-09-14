# Deadlock
- All processes and threads are unable to continue executing
- If a thread tries to lock a mutex that it's already locked,
  it will enter into a waiting list for that mutex

# Reentrant mutex/lock
- There may be time when a program need to lock a mutex multiple times
  before unlocking it, in that case you should use a reentrant mutex to
  prevent deadlocks
- Type of mutex that can be locked multiple times by the same process or thread
- Internally, it keeps track of how many time it's been locked by the owning thread
- Must be unlock the same number of time before another thread unlock it