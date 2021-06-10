# SOLUTION 1
# Branch Sums

# Complexity
# Average:  Time: O(n) | Space: O(n)
# Worst:    Time: | Space:

# Time: we have to traverse all the node values in order to add the sums
  # at everysingle node all that we are doing is constant time operations
# Space: more complicated because it's affected by the list of branch sums that we have to return
  # the branch sums array is the length of the number of leafs in the binary tree
  # it's also affected by the recursive nature of our algorithm adding to the callstack
  # in a balanced Binary Tree, every new level is a power^2
  # We know that we are going to be bounded by O(n) because we are not going to exceed n branch sums

# Edge Case
  # when a node has no children

class BinaryTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

def branchSums(root):
  sums = []
  calculateBranchSums(root, 0, sums)
  return sums

def calculateBranchSums(node, runningSum, sums):
  if node is None:
    return

  newRunningSum = runningSum + node.value
  if node.left is None and node.right is None:
    sums.append(newRunningSum)
    return

  calculateBranchSums(node.left, newRunningSum, sums)
  calculateBranchSums(node.right, newRunningSum, sums)