# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

# The path sum of a path is the sum of the node's values in the path.

# Given the root of a binary tree, return the maximum path sum of any non-empty path.

 

# Example 1:


# Input: root = [1,2,3]
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.



# Definition for a binary tree node.
# This class is provided for context and to make the solution self-contained.
class TreeNode:
    """
    Represents a single node in a binary tree.
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Contains the solution for the Binary Tree Maximum Path Sum problem.
    """
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        Calculates the maximum path sum for a given binary tree.

        A "path" is defined as any sequence of nodes from some starting node to any node
        in the tree along the parent-child connections. The path must contain at least
        one node and does not need to pass through the root.

        The core idea is to use a Depth First Search (DFS) approach. For each node,
        we calculate the maximum path sum that *ends* at this node and can extend upwards
        to its parent. This is `node.val + max(left_child_path, right_child_path)`.

        Simultaneously, we calculate the maximum path sum that is "centered" at the
        current node, which includes the node itself, its left child's path, and its
        right child's path (`node.val + left_path + right_path`). This value is used
        to update a global maximum, as this "split" path cannot extend further up
        the tree.

        Args:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            int: The maximum path sum found in the tree.
        """
        # Using a list for 'res' to make it mutable across recursive calls.
        # This allows the helper function `dfs` to modify the same variable.
        # It's initialized with root.val to handle single-node trees and negative values.
        res = [root.val]

        def dfs(node: Optional[TreeNode]) -> int:
            """
            A recursive helper function to perform DFS traversal.

            For each node, it does two things:
            1. Updates the overall maximum path sum (`res`) if a path through the
               current node (including both its left and right children) is greater.
            2. Returns the maximum path sum that *starts* at the current node and goes
               downwards (either left or right), to be used by its parent.

            Args:
                node (Optional[TreeNode]): The current node in the traversal.

            Returns:
                int: The maximum path sum starting from `node` and extending down
                     one branch (left or right).
            """
            # Base case: A null node contributes 0 to the path sum.
            if not node:
                return 0
            
            # Recursively find the max path sum from the left and right children.
            leftMax = dfs(node.left)
            rightMax = dfs(node.right)
            
            # A path cannot include a negative contribution from a child.
            # If a child's path sum is negative, we treat it as 0 (i.e., we don't include it).
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # --- Critical Step 1: Update the global maximum ---
            # This is the case where the current node is the "root" of the path.
            # The path goes from the left subtree, through the current node, to the right subtree.
            # This path cannot be extended upwards to the node's parent.
            current_path_sum = node.val + leftMax + rightMax
            res[0] = max(res[0], current_path_sum)

            # --- Critical Step 2: Return value for the parent ---
            # A node can only pass up a single path to its parent, not a split one.
            # So, we return the sum of the node's value and the greater of its child paths.
            return node.val + max(leftMax, rightMax)
        
        # Start the DFS from the root node.
        dfs(root)
        
        # The final result is stored in the mutable list.
        return res[0]

# ----------------------------------------------------------------------------
# Complexity Analysis
# ----------------------------------------------------------------------------
#
# Time Complexity: O(N)
#   - Where N is the total number of nodes in the tree.
#   - The DFS algorithm visits each node exactly once.
#
# Space Complexity: O(H)
#   - Where H is the height of the tree.
#   - This is the space used by the recursion stack.
#   - In the best case (a completely balanced tree), H = log(N), so space is O(log N).
#   - In the worst case (a skewed tree, like a linked list), H = N, so space is O(N).
#
# ----------------------------------------------------------------------------


# ----------------------------------------------------------------------------
# Example Usage and Test Case
# ----------------------------------------------------------------------------
if __name__ == '__main__':
    # Let's build an example tree to test the solution.
    #       -10
    #       /  \
    #      9    20
    #          /  \
    #         15   7
    #
    # The maximum path is 15 -> 20 -> 7, which sums to 15 + 20 + 7 = 42.

    print("Running example test case...")
    
    # Construct the tree
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    # Create an instance of the solution and run it
    solution_instance = Solution()
    max_sum = solution_instance.maxPathSum(root)
    
    # Print the result
    print(f"Constructed Tree: [-10, 9, 20, null, null, 15, 7]")
    print(f"Maximum Path Sum: {max_sum}")
    print(f"Expected Result: 42")
    
    assert max_sum == 42
    
    print("\nTest case passed! ✨")