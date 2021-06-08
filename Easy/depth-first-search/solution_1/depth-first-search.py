# SOLUTION 1
# Depth First Search

# Complexity
# Average:  Time: O(v+e) | Space: O(v)
# Worst:    Time: | Space:

# Time: O(v+e)
# This algorithm is more involced because we are going to be dealing with two variables.
# 1. Vertices | Vertex is a Node in a Graph
# 2. Edges
# V is the number of vertices or nodes
# E is the number of edges each node has
# At every vertex we iterate through the children nodes

# Space: O(v)
# Storing each vertex in an array creates the space complexity
# As we go deeper in the branch we add frames to the call stack


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # O(v + e) time | O(v) space
    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
          child.depthFirstSearch(array)
        return array
