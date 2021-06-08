# SOLUTION 1
# Find Closest Value in BST

# Complexity
# Average:  Time: O(Log(n)) | Space: O(1) Don't use additional memory
# Worst:    Time: O(n)      | Space: O(1) Don't use additional memory

def findClosesValueInBst(tree, target):
  return findClosestValueInBstHelper(tree, target, float("inf"))

def findClosestValueInBstHelper(tree, target, closest):
  if tree is None:
    return closest
  if abs(target - closest) > abs(target - tree.value):
    closest = tree.value
  if target < tree.value:
    return findClosestValueInBstHelper(tree.left, target, closest)
  if target > tree.value:
    return findClosestValueInBstHelper(tree.right, target, closest)
  else:
    return closest