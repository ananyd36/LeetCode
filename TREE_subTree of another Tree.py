# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

# Example 1:



# Input: root = [1,2,3,4,5], subRoot = [2,4,5]

# Output: true

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSame(root, subRoot):
            if not root and not subRoot:
                return True
            if (not root or not subRoot) or root.val != subRoot.val:
                return False
            
            return isSame(root.left, subRoot.left) and isSame(root.right, subRoot.right)


        if not root:
            return False
        
        if isSame(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    




# Approach: The solution uses a recursive function to check if the current node of the main tree matches the root of the subtree.
# If it matches, it checks if the entire subtree structure and values match using another helper function
# `isSame`. If the current node does not match, it recursively checks the left and right subtrees of the main tree.
# Time Complexity: O(m * n), where m is the number of nodes in the main tree and n is the number of nodes in the subtree.
# Space Complexity: O(h), where h is the height of the main tree, due to the recursive stack space used by the function.    