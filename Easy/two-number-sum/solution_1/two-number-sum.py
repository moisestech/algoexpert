# SOLUTION 1
# Two Number Sum

# Complexity
# Average:  Time: O(n^2) | Space: O(1)
# Worst:    Time: | Space:

def twoNumberSum(array, targetSum):
    for i in range(len(array) - 1):
      firstNum = array[i]
      for j in range(i + 1, len(array)):
        secondNum = array[j]
        if firstNum + secondNum == targetSum:
          return [firstNum, secondNum]
    return []