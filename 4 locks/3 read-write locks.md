# Reader-Writer Lock | Shared mutex
- Is useful when there are multiple threads that just perform
  1 action at once, so it is not necessary to lock the resource
  for writting and reading always, if just one thread needs to
  perform write operations.

## Types
- Shared read: allows multiple threads that only need
  to read simultaneously to lock it.
- Exclusive write: limits access to only 1 thread at a time, allowing
  that thread to safely write to the shared resource.
  No other thread can read or write until the resource is unlocked.

## Caveats
- The performance depends on the language implementation and use case
  - Who has priority, readers or writers?
- Usually it needs more resources to implement it

## General rule of thumb
- It's useful when:
  **Reading threads >> Writing threads**