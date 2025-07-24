# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res




# Approach:
# 1. Initialize a result list with the same length as nums, filled with 1s.
# 2. Calculate the prefix product for each index and store it in the result list.
# 3. Initialize a variable for the postfix product, starting at 1.
# 4. Traverse the nums array in reverse order, multiplying the current result by the postfix product.
# 5. Update the postfix product with the current element.
# 6. Return the result list.
# Time Complexity: O(n), where n is the length of the input array nums.
# Space Complexity: O(n) for the result list, as we are not using any additional space proportional to the input size.