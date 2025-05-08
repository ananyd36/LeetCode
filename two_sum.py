# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

# Return the answer with the smaller index first.

# Example 1:

# Input: 
# nums = [3,4,5,6], target = 7

# Output: [0,1]


# Solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}

        for i, val in enumerate(nums):
            diff = target - val
            if diff in res:
                return [res[diff],i]
            res[val] = i
        return
    

# Approach
# 1. Create an empty dictionary called res.
# 2. Iterate through the list nums using enumerate to get both the index and value of each element.
# 3. For each element, calculate the difference between the target and the current value.
# 4. Check if the difference is already in the dictionary res.
# 5. If it is, return the indices of the current value and the value that corresponds to the difference in the dictionary.
# 6. If it is not, add the current value and its index to the dictionary.
# 7. If no pair is found, return None.
# Time complexity: O(n)
# Space complexity: O(n)
# The time complexity of this solution is O(n) because we need to iterate through the entire list once.
# The space complexity is O(n) because we need to store the dictionary of indices.