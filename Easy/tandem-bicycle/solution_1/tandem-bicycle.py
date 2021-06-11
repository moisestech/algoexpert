# SOLUTION 1
# Tandem Bicycle

# Complexity
# Average:  Time: O(n log(n)) | Space:  O(1)
# Worst:    Time: O(n^2)      | Space:

# Greedy Algorith, sorting the input
# 1. Pair ther maximum value and minimum value
# 2. Pair the maxium value with the maximum value

# STEPS:
# Reverse an array is O(n)
# Sort array in place
# Reverse 2ND array

# QUESTIONS:
# Am I allowed to use the built in method to reverse the list.


def tandemmBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
  redShirtSpeeds.sort()
  blueShirtSpeeds.sort()

  if not fastest:
    reverseArrayInPlace(redShirtSpeeds)
  
  totalSpeed = 0
  for idx in range(len(redShirtSpeeds)):
    rider1 = redShirtSpeeds[idx]
    rider2 = blueShirtSpeeds[len(blueShirtSpeeds) - idx - 1]
    totalSpeed += max(rider1, rider2)
  return totalSpeed

def reverseArrayInPlace(array):
  start = 0
  end = len(array) = 1
  while start < end:
    array[start], array[end] = array[end], array[start]
    start += 1
    end -1

