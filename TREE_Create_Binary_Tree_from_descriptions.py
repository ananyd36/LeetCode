# You are given a 2D integer array descriptions where descriptions[i] = [parenti, childi, isLefti] indicates that parenti is the parent of childi in a binary tree of unique values. Furthermore,

# If isLefti == 1, then childi is the left child of parenti.
# If isLefti == 0, then childi is the right child of parenti.
# Construct the binary tree described by descriptions and return its root.

# The test cases will be generated such that the binary tree is valid.

 

# Example 1:


# Input: descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
# Output: [50,20,80,15,17,19]
# Explanation: The root node is the node with value 50 since it has no parent.
# The resulting binary tree is shown in the diagram.
# Example 2:


# Input: descriptions = [[1,2,1],[2,3,0],[3,4,1]]
# Output: [1,2,null,null,3,4]
# Explanation: The root node is the node with value 1 since it has no parent.
# The resulting binary tree is shown in the diagram.



class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        children = set()
        for parent, child, isLeft in descriptions:
            children.add(child)
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            if child not in nodes:
                nodes[child] = TreeNode(child)
            if isLeft:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]
        
        for parent, child, isLeft in descriptions:
            if parent not in children:
                return nodes[parent]
        
        
        # all_nodes = set()
        # for parent, child, _ in descriptions:
        #     all_nodes.add(parent)
        #     all_nodes.add(child)

        # # Find root (node that is never a child)
        # for _, child, _ in descriptions:
        #     if child in all_nodes:
        #         all_nodes.remove(child)
        # root_val = list(all_nodes)[0]
        # root = TreeNode(root_val)

        # queue = deque([root])

        # while queue:
        #     new_root = queue.popleft()
        #     for parent, child, isLeft in descriptions:
        #         if parent == new_root.val:
        #             node = TreeNode(child)
        #             if isLeft == 1:
        #                 new_root.left = node
        #             else:
        #                 new_root.right = node
        #             queue.append(node)

        # return root
