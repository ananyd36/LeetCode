# Given the root of a binary tree, return the number of “good” nodes in the binary tree.
# A node X in the tree is named “good” if in the path from the root to X there are no nodes with a value greater than X’s value.

# Example 1:
# Input: root = [3,1,4,3,null,1,5]
# Output: 4
# Explanation: The good nodes are marked in the following tree structure:
#      3* 
#     / \
#    1   4*
#   /   / \
#  3*  1   5*

# Example 2:
# Input: root = [3,3,null,4,2]
# Output: 3
# Explanation: The good nodes are marked in the following tree structure:
#      3* 
#     / 
#    3*  
#   / \
#  4*  2

# Constraints:
# The number of nodes in the tree is in the range [1, 10^4]
# -10^4 <= Node.val <= 10^4

# Definition of a Binary Tree node:
# class TreeNode:
#    def __init__(self, x):
#       self.val = x
#       self.left = None
#       self.right = None



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(cur, max_val):
            if not cur:
                return 0
            
            good = 1 if cur.val >= max_val else 0

            new_max_val = max(cur.val, max_val)

            good += dfs(cur.left, new_max_val)
            good += dfs(cur.right, new_max_val)

            return good

        return dfs(root, root.val)
    