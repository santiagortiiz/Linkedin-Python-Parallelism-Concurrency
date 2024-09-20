DAG: Directed Acyclic Graph

How to get a sense of how parallel a program can be
- Measure how much time the program takes to finish its execution
- Measure the time for each step to complete

**Metrics**
- Work: Sum of time for all nodes
- Span: Sum of time along the critical path (longest path in time).
  - Indicates the shortest possible execution time if this program was parallelized as much as possible.
- Ratio of work to span
  - Ideal Parallelism = work/span = 60/45 = 1.33
    - Means that a parallel version will run 33% faster than the sequential version (best scenario)