# Given an array of integers numbers that is sorted in non-decreasing order.

# Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

# There will always be exactly one valid solution.

# Your solution must use 
# O
# (
# 1
# )
# O(1) additional space.

# Example 1:

# Input: numbers = [1,2,3,4], target = 3

# Output: [1,2]
# Explanation:
# The sum of 1 and 2 is 3. Since we are assuming a 1-indexed array, index1 = 1, index2 = 2. We return [1, 2].


# Solution 1:

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        count = {}

        for i, val in enumerate(numbers):
            diff  = target - numbers[i]
            if diff in count:
                return [count[diff] + 1, i + 1]
            else:
                count[val] = i
        return 
    

#Solution 2: Two Pointer Approach

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0, len(numbers)-1


        while l<r:
            sumNum = numbers[l] + numbers[r]
            if sumNum < target:
                l+=1
                continue
            elif sumNum > target:
                r-=1
                continue
            else:
                return [l+1,r+1]


# Approach:
# 1. Initialize two pointers, `l` at the start and `r` at the end of the sorted list `numbers`.
# 2. While the left pointer is less than the right pointer:
#    - Calculate the sum of the elements at the two pointers.
#    - If the sum is less than the target, move the left pointer to the right.
#    - If the sum is greater than the target, move the right pointer to the left.
#    - If the sum equals the target, return the indices of the two elements (1-indexed).
# Time Complexity:
# - O(n), where n is the number of elements in `numbers`, since each element is processed at most once.
# Space Complexity:
# - O(1), as no additional space is used apart from the pointers.
# Note: The solution assumes that there is exactly one valid solution, as stated in the problem constraints.