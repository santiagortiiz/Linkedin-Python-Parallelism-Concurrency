# Data Race VS Race condition

**Data Race**
Occurs when 2 or more threads concurrently access the same memory location, if at least one of those is writing to, that can cause the threads to overwrite each other or read wrong values.

Solution: ensurie mutual exclusion for the shared resource.

**Race Condition**
It's a flaw in the timing or ordering of a program's execution that causes incorrect behavior.

**In Practice** many race conditions coulb be caused by data races, but not always

Let's say
thread-1 sums a number: **+3**
thread-2 double that number: **x2**

**Here the order matters:**
(1 + 3) x 2 = 8
(1 x 2) + 3 = 5

**Sometimes** putting sleep statements to modify timing and execution order can help to uncover potential race conditions

# Heisenbug
A software bug that disappears when you try to study it
- means that running the program in debug mode, could hide the race condition because of the modified time and order of execution

# Who is responsible for causing a race condition?
The order in which the OS schedules threads to execute is non-deterministic.