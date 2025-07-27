# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) in the tree.

# A binary search tree satisfies the following constraints:

# The left subtree of every node contains only nodes with keys less than the node's key.
# The right subtree of every node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees are also binary search trees.
# Example 1:



# Input: root = [2,1,3], k = 1

# Output: 1


# DFS` Approach for Kth Smallest Element in BST`
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)

        dfs(root)
        print(res)
        if len(res) < k:
            return 0

        return res[k-1]
    

#ITERATIVE
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            k-=1
            if k == 0:
                return cur.val
            cur = cur.right
