# Diameter of Binary Tree
# Solved 
# The diameter of a binary tree is defined as the length of the longest path between any two nodes within the tree. The path does not necessarily have to pass through the root.

# The length of a path between two nodes in a binary tree is the number of edges between the nodes.

# Given the root of a binary tree root, return the diameter of the tree.

# Example 1:



# Input: root = [1,null,2,3,4,5]

# Output: 3
# Explanation: 3 is the length of the path [1,2,3,5] or [5,3,2,4].



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:    
        self.res = 0

        def dfs(curr):
            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)

            self.res = max(self.res, left + right)

            return 1 + max(left, right)

        dfs(root)

        return self.res


# Approach: The solution uses a depth-first search (DFS) to traverse the binary tree. For each node, 
# it calculates the maximum depth of its left and right subtrees.
# The diameter is updated as the maximum of the current diameter and the sum of the left and right subtree depths.
# Time Complexity: O(n), where n is the number of nodes in the binary tree.
# Space Complexity: O(h), where h is the height of the tree, due to the