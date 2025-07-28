# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

# Example 1:


# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
# Example 2:

# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
 

# Constraints:

# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder and inorder consist of unique values.
# Each value of inorder also appears in preorder.
# preorder is guaranteed to be the preorder traversal of the tree.
# inorder is guaranteed to be the inorder traversal of the tree.




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        # catch the root of the tree and subtrees (Preorder first ele is the root)
        root = TreeNode(preorder[0]) 
        # get the index of the root in order to divide the left and right subtree
        mid = inorder.index(root.val) 
        # recursive operation for each left and right subtree
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid+1]) 
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root
    


# Approach:
# 1. The first element of the preorder list is always the root of the tree.
# 2. We find the index of this root in the inorder list to determine the left and right subtrees.
# 3. We recursively build the left subtree using the elements before the root in the inorder list and the corresponding elements in the preorder list.
# 4. We build the right subtree using the elements after the root in the inorder list and the corresponding elements in the preorder list.
# 5. This process continues until we have constructed the entire tree.
# 6. The base case for the recursion is when either the preorder or inorder list is empty, in which case we return None.
# 7. Finally, we return the root of the constructed binary tree.    
# Time Complexity: O(n), where n is the number of nodes in the tree, as we visit each node once.
# Space Complexity: O(n), for the recursion stack and the storage of the tree nodes.