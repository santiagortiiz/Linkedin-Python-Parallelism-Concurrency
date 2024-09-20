# Steps

# Partitioning

  Break the problem down into discrete pieces of work

   - Domain decomposition
     - Focuses on dividing the data associated with the problem into lots of small, and if possible, equally-sized partitions.
       - Options: Block decomposition or Cyclic Decomposition
     - Consider the computations to be performed and associating them with that partition data
   - Functional decomposition
     - Considers all of the computational work that a program needs to do and then divides that into separate tasks that performs different portions of the overall work.
     - Then, considers data requirements for the tasks