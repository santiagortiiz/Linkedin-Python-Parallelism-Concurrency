# Reasons for parallel programming
- Increase the size of the problem you can take in a certain amount of time.
- Acomplish a given task faster

**Weak Scaling**
- Variable number of processors with fixed problem size per processor
- Acomplish more work in the same time
- i.e: 1 worker can prepare 10 cupcakes in 1h, but 2 workers could prepare 20 cupcakes in the same time

**Strong Scaling**
- Variable number of processors with fixed total problem size
- Acomplish same work in less time
- i.e: 1 worker can prepare 10 cupcakes in 1h, but 2 workers could do the same job in 30 minutes.

**Metrics**
- In any case, we are increasing the Throughput (T):
  - T [actions/time]= # task/ time

- Throughput is related to latency: amount of time that takes to execute a task from beginning to end.
  - Latency [s] = time/task

- Speedup is related to the program eficiency:
  - Speedup = sequential execution time / parallel execution time with N workers
i.e: 60 min /30 min = 2

- How well additional resources are utilized
  - Efficiency = speedup / # Processors


**Amdahl's law**
Estimates the speedup that a parallel program can achieve

Overall Speedup = 1 / ( (1-P) + P/S )
P: Portion of program that's parallelizable
S: Speedup of the parallelized portion

**Recommendation**
When taking measures, ensure the environment is warm up, and take an average of multiple executions

