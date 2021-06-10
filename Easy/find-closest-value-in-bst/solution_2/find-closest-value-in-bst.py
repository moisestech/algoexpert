# SOLUTION 2
# Find Closest Value in BST

# Complexity
# Average:  Time: O(Log(n)) | Space: O(1) Don't use additional memory
# Worst:    Time: O(n)      | Space: O(1) Don't use additional memory

def findClosestValueInBst(tree, target):
	return findClosestValueInBstHelper(tree, target, tree.value)

def findClosestValueInBstHelper(tree, target, closest):
	# we keep track of the currentNode that we are exploring
 	# we are in linear space storing two values
 	# currentNode & closest
	currentNode = tree
	while currentNode is not None:
		if abs(target - closest) > abs(target - currentNode.value):
			closest = currentNode.value
		if target < currentNode.value:
			currentNode = currentNode.left
		elif target > currentNode.value:
			currentNode = currentNode.right
		else:
			break
	return closest

# This is the class of the input tree.
class BST:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None