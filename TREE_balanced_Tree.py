# Given a binary tree, determine if it is height-balanced.

 
# A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: true

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.bal = True
        if not root:
            return True
        
        def dfs(curr):
            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)

            if abs(left - right) > 1:
                self.bal = False
            
            return 1 + max(left, right)
        
        dfs(root)

        return self.bal


# Approach: The solution uses a depth-first search (DFS) to traverse the binary tree. For each node, it calculates the height of its left and right subtrees.
# If the difference in heights is greater than 1, it sets a flag indicating that the
# tree is not balanced. The function returns the height of the tree, and the main function checks the flag to determine if the tree is balanced.
# Time Complexity: O(n), where n is the number of nodes in the binary tree.
# Space Complexity: O(h), where h is the height of the tree, due to the
# recursive stack space used by the DFS.