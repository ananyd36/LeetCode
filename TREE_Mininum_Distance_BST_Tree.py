# Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different 
# nodes in the tree.

 

# Example 1:


# Input: root = [4,2,6,1,3]
# Output: 1
# Example 2:


# Input: root = [1,0,48,null,null,12,49]
# Output: 1
 



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        prev = None
        res = float('inf')

        def dfs(node):
            if not node:
                return 
            
            dfs(node.left)
            nonlocal prev, res

            if prev:
                res = min(res, node.val - prev.val)
            prev = node

            dfs(node.right)
        
            return
        
        dfs(root)
        
        return res