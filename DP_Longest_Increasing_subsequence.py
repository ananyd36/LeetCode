# Given an integer array nums, return the length of the longest strictly increasing subsequence.

 

# Example 1:

# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Example 2:

# Input: nums = [0,1,0,3,2,3]
# Output: 4
# Example 3:

# Input: nums = [7,7,7,7,7,7,7]
# Output: 1




class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        dp = [1] * (len(nums))

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])

        
        return max(dp)

        
        # memo = {}
        # def recursive(i, j):
        #     if i == len(nums):
        #         return 0
            
        #     if (i, j) in memo:
        #         return memo[(i,j)]

        #     LIS = recursive(i+1, j)

        #     if j == -1 or nums[i] > nums[j]:
        #         LIS = max(LIS, 1 + recursive(i+1, i))
            
        #     memo[(i,j)] = LIS

        #     return memo[(i,j)]
        
        return recursive(0, -1)
            
            
            

