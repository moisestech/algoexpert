# SOLUTION 1
# Validate Subsequence

# Complexity
# Average:  Time: O(n)  | Space: O(1)
# Worst:    Time:       | Space:
# where n is the length of the array

def isValidSubsequence(array, sequence):
  arrIdx = 0
  seqIdx = 0

  while arrIdx < len(array) and seqIdx < len(sequence):
    if array[arrIdx] == sequence[seqIdx]:
      seqIdx += 1
    arrIdx += 1
  return seqIdx == len(sequence)
