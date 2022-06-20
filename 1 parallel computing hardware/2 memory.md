# Memory architectures for parallel computing
Memory speed < Processor speed
- When a processor access the memory, it locks it to other processors

# Shared memory
- all processors see the same memory
- could be spread across multiple systems
- categories based on how processors are connected
  to memory and how quickly they can access it:
  - UMA: Uniform memory access
  - NUMA. Non-uniform memory access

## UMA: Uniform memory access
- All processors are connected to the same memory and they can access equaly fast
- Architecture types:
  - **SMP: Symmetric multiprocessing**
    - CPU -> cache -> system bus -> shared memory
      2 or more CPUs connected to a shared memory through a system bus.
      Each CPU has it's own cache memory, this introduces a problem called cache coherency

## NUMA: Non-uniform memory access
- Connect multiple **SMP systems** together through a physical network (called bus)
- Non uniform access because some processors have quickly access to some parts of the memory than others


# Distributed memory
- Each processor has its own local memory with it's own address space
- Processors are connected through the network

**advantage**: Scalability