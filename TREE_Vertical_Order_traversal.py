# You are given the root node of a binary tree, return the vertical order traversal of its nodes' values.

# For the vertical order traversal, list the nodes column by column starting from the leftmost column and moving to the right.

# Within each column, the nodes should be listed in the order they appear from the top of the tree to the bottom.

# If two nodes are located at the same row and column, the node that appears to the left should come before the other.



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        cols = defaultdict(list)
        que = deque([(root, 0)])

        while que:
            node, pos = que.popleft()
            if node:
                cols[pos].append(node.val)
                que.append((node.left, pos - 1))
                que.append((node.right, pos + 1))

        return [cols[x] for x in sorted(cols)]


            
# BFS without sorting

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        cols = defaultdict(list)
        queue = deque([(root, 0)])
        minCol = maxCol = 0

        while queue:
            node, col = queue.popleft()
            cols[col].append(node.val)
            minCol = min(minCol, col)
            maxCol = max(maxCol, col)

            if node.left:
                queue.append((node.left, col - 1))
            if node.right:
                queue.append((node.right, col + 1))

        return [cols[c] for c in range(minCol, maxCol + 1)]
    


# The idea is that we start with the root and for every left node we 
# decrement the column value by 1 and we increment when we go right 
# this way we can use a hashmap to store values based on col value 
# and this will club the nodes with same col values. Then we can either 
# sort the hashmap and print each col values or we can keep track of 
# all mincol and maxcol and then iterate from mincol to max col and 
# return the values. We can use a BFS to traverse through all of the nodes.


# TC : O(N)
# SC : O(N)
# # where N is the number of nodes in the tree.
# The space complexity is O(N) for the queue and the dictionary storing the columns.