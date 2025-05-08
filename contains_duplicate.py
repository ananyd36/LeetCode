##Question
#Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Example 1:

# Input: nums = [1, 2, 3, 3]

# Output: true

# Solution


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
    

# Approach 
# validated if the length of list is equal to the lenght of the set of the list
# Time complexity: O(n)
# Space complexity: O(n)
# The set() function creates a set object, which is an unordered collection of unique elements.
# The len() function returns the number of elements in the set.
# The time complexity of this solution is O(n) because we need to iterate through the entire list to create the set.
# The space complexity is also O(n) because we need to store the set of unique elements.