# SOLUTION 1
# Minimum Waiting Time

# Complexity
# Average:  Time: O(n log n) | Space: O(1)
# Worst:    Time: | Space:
# n is the number of queries in the input array

# Because we can mutate the array we can sort in place
# saving the external space

# 1. Sort the input array
# total = 0
# all querys need to wait the current index times the numbers left in the array
# if it's the last query no need to wait)

def minimumWaitingTime(queries):
  queries.sortt()

  totalWaitingTime = 0
  for idx, duration in enumerate(queries):
    queriesLeft = len(queries) - (idx + 1)
    totalWaitingTime += duration * queriesLeft

  return totalWaitingTime 
