# You are given an array of distinct integers nums and a target integer target. Your task is to return a list of all unique combinations of nums where the chosen numbers sum to target.

# The same number may be chosen from nums an unlimited number of times. Two combinations are the same if the frequency of each of the chosen numbers is the same, otherwise they are different.

# You may return the combinations in any order and the order of the numbers in each combination can be in any order.

# Example 1:

# Input: 
# nums = [2,5,6,9] 
# target = 9

# Output: [[2,2,5],[9]]
# Explanation:
# 2 + 2 + 5 = 9. We use 2 twice, and 5 once.
# 9 = 9. We use 9 once.


# Intuition
# The problem asks for all combinations of numbers that sum up to a target. Since we need to find all possible solutions, this suggests an exhaustive search where we explore different possibilities. This is a classic signal to use a backtracking algorithm.

# Think of it as building a decision tree. At each step, we consider a number from the candidates list and face a choice:

# Include this number in our current combination.

# Skip this number and move to the next one.

# We continue exploring down a path (a series of "include" decisions) until the sum of our combination either equals the target (a success!) or exceeds it (a failure). When a path ends, we "backtrack" by undoing our last choice and exploring the next available option. Since we can use the same number multiple times, our "include" decision means we can try to include that same number again.

# Approach
# We'll implement this backtracking strategy with a recursive helper function, let's call it pathSum. This function will be responsible for exploring the decision tree.

# The pathSum function will need to keep track of three things:

# i: The index of the current candidate we are considering.

# path: The list of numbers forming the current combination.

# total: The current sum of the numbers in path.
# Here's the flow of the recursion:

# Base Case 1 (Success): If total equals the target, we've found a valid combination. We add a copy of the current path to our results list and stop exploring this branch.

# Base Case 2 (Failure): If total exceeds the target or if we've run out of candidates (i >= len(candidates)), this path is no longer viable. We stop and backtrack.
# Recursive Step (The Decision):

# Choice 1: Include candidates[i]. We append candidates[i] to our path. Then, we make a recursive call pathSum(i, ...), passing the same index i because we are allowed to reuse the current number.

# Backtrack: After the above recursive call returns, we must undo our choice. We pop the element from the path so we can explore the next decision.

# Choice 2: Skip candidates[i]. We make a different recursive call, pathSum(i + 1, ...), moving on to the next candidate without adding the current one to our path.

# We initiate the process by calling pathSum(0, [], 0), starting at the first candidate with an empty path and a total of zero.
# Complexity
# Time Complexity: O(N ^ T/M)
# Let N be the number of candidates, T be the target value, and M be the minimum value among the candidates. The maximum depth of the recursion tree can be up to T/M. At each level of the tree, we can have up to N branches. This results in a time complexity that is exponential, roughly bounded by O(N^T/M). The extra factor of N can be thought of as the branching work done at each node.

# Space Complexity: O(T/M)
# The space complexity is determined by the maximum depth of the recursion stack. In the worst-case scenario, the smallest candidate (let's say its value is M) is chosen repeatedly to reach the target T. The depth of the recursion would be T/M. This also corresponds to the maximum size of the path list we store during recursion.

# Code
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []

        def pathSum(i, path, total):
            if total == target:
                res.append(path.copy())
                return
            
            if total > target or i >= len(candidates):
                return
            
            path.append(candidates[i])

            pathSum(i, path, total + candidates[i])
            path.pop()

            pathSum(i+1, path, total)
        
        pathSum(0,[],0)
        return res