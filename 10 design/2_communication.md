# Communication

  Share data across tasks. The best way to scale is using "divide and conquer strategy" because the orchestrator node could be a bottle neck handling all intermediate outputs.

  1. Point to point communication:
    For each link, 1 producer/sender and 1 consumer/receiver
  2. Collective communication
    Broadcast or Scatter. Producer can also gather results from each node, to combine the results and produce a final output

  This Communication can be synchronous or asynchronous, and here some considerations

   1. Overhead: Compute time/resources spent on communication
   2. Latency: Time to send message from A to B
   3. Bandwidth: Amount of data communicated per seconds (GB/s)
