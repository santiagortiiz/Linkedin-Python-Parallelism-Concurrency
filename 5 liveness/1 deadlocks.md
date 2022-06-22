# Dining Philosopher's problem
Two people go forward and backward between 2 actions (eat & think).

To eat they need to get 2 chopsticks, grabbing one after the other (acquire method);
but if both of them grab 1 chopstick at the same time, **a deadlock is generated**
because both of them must wait until the other chopstick is released.

# Deadlock
- Each member is waiting for another member to take action, as a result
  neither member is able to make progress

# Liveness
- Properties that require a system to make progress
- Members may have to "take turns" in critical sections

# Possible Solutions
- Prioritize locks, so all members point to the same resource for the first lock;
  so if that resource is already locked, other members must wait until it is released.
- Put a timeout lock on attempts
  - if a thread cannot acquire all locks within the limit:
    - Backup and free all locks taken
    - Wait for a random amout of time before retry
    - Just try again.
