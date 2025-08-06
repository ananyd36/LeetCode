# Given a node in a connected undirected graph, return a deep copy of the graph.

# Each node in the graph contains an integer value and a list of its neighbors.

# class Node {
#     public int val;
#     public List<Node> neighbors;
# }
# The graph is shown in the test cases as an adjacency list. An adjacency list is a mapping of nodes to lists, used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

# For simplicity, nodes values are numbered from 1 to n, where n is the total number of nodes in the graph. The index of each node within the adjacency list is the same as the node's value (1-indexed).

# The input node will always be the first node in the graph and have 1 as the value.

# Example 1:



# Input: adjList = [[2],[1,3],[2]]

# Output: [[2],[1,3],[2]]
# Explanation: There are 3 nodes in the graph.
# Node 1: val = 1 and neighbors = [2].
# Node 2: val = 2 and neighbors = [1, 3].
# Node 3: val = 3 and neighbors = [2].





"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
'''
here we can use a recursive approach that we start 
from the node and we ccreate a copy of that node and
for the neighbors we iterate throught hte neighbors and
check if the copy has already been created for that node
if yes then we assign the original copy node neighbors to
the already present copy node in hasMap else we create oone for them as well

'''
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            
            return copy
        
        return dfs(node)