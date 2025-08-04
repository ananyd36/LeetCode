
# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:

# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:

# Input: nums = [1]
# Output: [[1]]
 

# DFS Approach for Permutations

# Below is the code that implements the DFS approach for generating all permutations of a list of distinct integers. 
# It uses a recursive depth-first search (DFS) strategy to explore all possible arrangements of the elements in the list.


def permute(self, nums: List[int]) -> List[List[int]]:
    res = []
    visited = set() # to keep track of visited elements
    def dfs(path):
        if len(path) == len(nums):   # if the path length is equal to the length of nums, we have a valid permutation
            # we append a copy of the path to the result
            # we use path.copy() to create a new list with the same elements as path
            # this is necessary because we will modify path in the next iterations
            res.append(path.copy())
            return
        for j in range(len(nums)):  
            if nums[j] in visited:      
                continue
            visited.add(nums[j])
            path.append(nums[j])    
            dfs(path)
            path.pop()
            visited.remove(nums[j])
    
    dfs([])
    return res


# Backtracking Approach for Permutations
# This approach uses backtracking to generate all permutations of the input list.
# It explores all possible arrangements of the elements in the list by swapping them recursively.



# swaping recursively
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def permutations(index):
            if index == len(nums):
                res.append(nums.copy())
                return 
            for i in range(index, len(nums)):
                tmp = nums[index]
                nums[index] = nums[i]
                nums[i] = tmp
                permutations(index + 1)
                tmp = nums[index]
                nums[index] = nums[i]
                nums[i] = tmp
        
        permutations(0)
        return res


