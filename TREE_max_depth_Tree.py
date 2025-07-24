# Given the root of a binary tree, return its depth.

# The depth of a binary tree is defined as the number of nodes along the longest path from the root node down to the farthest leaf node.

# Example 1:



# Input: root = [1,2,3,null,null,4]

# Output: 3


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        left_depth = 0
        right_depth = 0
        if not root:
            return 0
        
        if root.left:
            left_depth = self.maxDepth(root.left)
        if root.right:
            right_depth = self.maxDepth(root.right)
        
        depth = 1 + max(left_depth, right_depth)
        
        return depth