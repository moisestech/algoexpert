# SOLUTION 1
# Node Depths

# Complexity
# Average: when the tree is balanced
# 	Time: O(n)  | n is the number of nodes in the Binary Tree
# 	Space: O(h)	| h is the height of the Binary Tree
# Worst: when the tree is not balanced

def nodeDepths(root, depth = 0):
	# Handle base case of recursion
	if root is None:
		return 0
	return depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None