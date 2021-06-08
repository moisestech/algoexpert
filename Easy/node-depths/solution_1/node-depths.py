# SOLUTION 1
# Node Depths

# Complexity
# Average: when the tree is balanced
# 	Time: O(n)  | n is the number of nodes in the Binary Tree
# 	Space: O(h)	| h is the height of the Binary Tree
# Worst: when the tree is not balanced


def nodeDepths(root):
	sumOfDepths = 0;
	stack = [{"node": root, "depth": 0}]
	while len(stack) > 0:
		nodeInfo = stack.pop()
		node, depth = nodeInfo["node"], nodeInfo["depth"]
		if node is None:
			continue
		sumOfDepths += depth
		stack.append({"node": node.left, "depth": depth + 1})
		stack.append({"node": node.right, "depth": depth + 1})
	return sumOfDepths


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None