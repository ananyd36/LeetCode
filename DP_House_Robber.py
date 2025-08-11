class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 1:
            return 
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        dp = [0] * n

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        return dp[n-1]



# Here the idea is that at every house we have two choices:
# 1. Rob the current house and add its value to the maximum amount robbed from two houses before.
# 2. Skip the current house and take the maximum amount robbed from the previous house.
# We use dynamic programming to keep track of the maximum amount robbed up to each house, and we return the maximum amount robbed at the last house.
# Time complexity is O(n) where n is the number of houses.
# Space complexity is O(n) for the dp array, but we can optimize it to O