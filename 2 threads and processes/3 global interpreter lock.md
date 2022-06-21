# Global interpreter lock (GIL)
- Mechanism that limits python to only execute one thread at a time

# CPython
- Default and most widely used Python interpreter
- Written in C and Python
- Uses GIL for thread-safe (memory management) operation

# Interpreters
- Cython
- Jython: Java based
- IronPython: .NET based
- PyPY-STM:

# Parallel programming
- Python multiprocessing package
- Create independent Python instances
- Don't share resources
- Need more resources than multi-threads