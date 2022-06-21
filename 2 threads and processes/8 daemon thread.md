# Daemon (Background) thread
- It's a thread that has become detached from the parent thread
- Does not prevent the process from terminating
- By default new threads are spawned as non-daemon threads
- If the main thread of the process terminate, the process too
  and with it, all it's child threads.

Note:
- If you spawn daemon threads, be careful that they
  will not have negative effects if terminated abruptly.