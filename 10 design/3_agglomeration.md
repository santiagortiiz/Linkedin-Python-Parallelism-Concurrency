# Agglomeration

If there are more tasks that processors, it's needed to optimize the efficiency by using abstraction.

- Combine tasks and replicate data/computation to increase efficiency
- Granularity: Measure over the time spent on communication
  - Granularity = computation/communication
- **Fine Grained Parallelism**
  - Large number of small tasks
  - Good distribution of workload (load balancing)
  - Low computation-to-communication ratio (spent more time in communication)
- **Coarse Grained Parallelism**
  - Small number of large tasks
  - High computation-to-communication ratio
  - Inefficient load balancing (spent more time on computation)