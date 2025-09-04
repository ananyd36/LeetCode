# Given the root of a binary tree, return the level order traversal of its nodes' values. 
# (i.e., from left to right, level by level).

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#DFS Approach for Level Order Traversal
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def dfs(cur, level = 0):
            if not cur:
                return 0
            
            if level == len(res):
                res.append([]) # to accomodate the next coming values at the level
            
            res[level].append(cur.val)

            dfs(cur.left, level + 1)
            dfs(cur.right, level + 1)

            return 
        
        dfs(root)

        return res


#BFS Approach for Level Order Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        queue = deque()

        level = 0

        if root:
            queue.append(root)

        while len(queue) > 0:
            res.append([])
            for i in range(len(queue)):
                cur = queue.popleft()
                
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

                res[level].append(cur.val)
            
            level+=1
        
        return res

