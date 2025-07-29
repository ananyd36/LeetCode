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

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(start, path, total):
            # terminating conditions
            if total == target:
                res.append(path.copy()) # copy because we need to maintain the path
                return
            if start >= len(nums) or total > target:
                return
            
            # lets work on the branching and recursive dfs
            #first we will be adding the start candidate into our path
            path.append(nums[start])
            # then after adding we will check for conditions and start a recursive stack
            dfs(start, path, total + nums[start]) # updated total amount
            # if it returns with the updated res via recursion or termination condition we remove it from path
            path.pop()
            # and then move on with the rest of the values
            dfs(start + 1, path, total) # not adding nums[i] since that path is now backtracked to original checkpoint
        
        dfs(0,[],0)


        return res
    


# Approach:
# 1. We define a recursive function `dfs` that takes the current index, the current path, and the total sum so far.
# 2. If the total sum equals the target, we append a copy of the current
# path to the result list.
# 3. If the total sum exceeds the target or if we have processed all elements,
# we return from the function.
# 4. We then add the current number to the path and call `dfs` recursively
# with the same index to allow for repeated use of the same number.
# 5. After the recursive call, we remove the last number from the path (backtracking) and call `dfs` again with the next index to explore other combinations.
# 6. Finally, we return the result list containing all unique combinations that sum to the target.
# Time Complexity: O(2^n), where n is the number of elements in `nums`. This is because we explore all possible combinations of the elements.
# Space Complexity: O(n), where n is the maximum depth of the recursion stack, which can go up to the length of the `nums` list in the worst case.