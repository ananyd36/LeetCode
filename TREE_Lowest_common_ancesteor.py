# Given a binary search tree (BST) where all node values are unique, and two nodes from the tree p and q, return the lowest common ancestor (LCA) of the two nodes.

# The lowest common ancestor between two nodes p and q is the lowest node in a tree T such that both p and q as descendants. The ancestor is allowed to be a descendant of itself.



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur


        
    #     class Solution:
    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #     if root is None:
    #         return None
        
    #     # If root is either p or q, then root is part of the LCA path
    #     if root == p or root == q:
    #         return root

    #     # Search in left and right subtrees
    #     left = self.lowestCommonAncestor(root.left, p, q)
    #     right = self.lowestCommonAncestor(root.right, p, q)

    #     # If both sides return non-null, root is the LCA
    #     if left and right:
    #         return root

    #     # Otherwise, return non-null subtree
    #     return left if left else right

        
# ✅ Test Case:
# Tree Structure:
# markdown
# Copy
# Edit
#         3
#        / \
#       5   1
#      / \  / \
#     6  2 0  8
#       / \
#      7   4
# Nodes:
# Let p = 5 and q = 1.

# We want to find the Lowest Common Ancestor (LCA) of nodes 5 and 1.

# 🔍 Step-by-Step Execution:
# Call: lowestCommonAncestor(root=3, p=5, q=1)
# root is 3 → not equal to p or q.

# Call recursively on root.left (node 5) and root.right (node 1).

# Call: lowestCommonAncestor(root=5, p=5, q=1)
# root is 5 → matches p, so return 5.

# Call: lowestCommonAncestor(root=1, p=5, q=1)
# root is 1 → matches q, so return 1.

# Back to Root (3):
# Left returned 5 (found p)

# Right returned 1 (found q)

# ✅ Since both sides returned non-null, root (3) is the Lowest Common Ancestor.

# ✅ Output:
# python
# Copy
# Edit
# LCA = TreeNode(3)
# 💡 Intuition:
# LCA is the lowest node that has both p and q as descendants (including possibly itself).

# Since 5 is in the left subtree of 3 and 1 is in the right, their LCA is 3.

# ✨ Another Test Case (Deeper Nodes):
# What if p = 7 and q = 4?

# Both nodes are in the left subtree under node 2 → so LCA should be 2.