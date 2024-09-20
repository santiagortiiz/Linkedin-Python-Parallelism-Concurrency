# Mapping
Specify where each task will execute.
- Minimize the total execution time

- Does not apply if:
  - Single-core processors
  - Automated task scheduling
- Apply if:
  - You are using a distributing system
  - Specialized hardware with lots of parallel processors

**Strategies**
- Place tasks that can execute concurrently on different processors to increase the overall concurrency
- Place tasks that communicate to each other frequently on the same processors, to increase locality by keeping them close together