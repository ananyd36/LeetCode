class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        maxSum = nums[0]


        for n in nums:
            curSum = max(curSum, 0)
            curSum += n
            maxSum = max(curSum, maxSum)
        
        return maxSum


# Kadane's Algorithm
# Intuition
# The problem asks for the contiguous subarray with the largest sum. A brute-force approach would
# involve checking all possible subarrays, which would be inefficient. Instead, we can use a dynamic
# programming approach known as Kadane's Algorithm.
# The key idea is to iterate through the array while keeping track of the maximum sum of the subarray
# that ends at the current position. If the sum becomes negative, we reset it to zero,
# as starting a new subarray from the next element would yield a higher sum.
# We also maintain a global maximum sum that gets updated whenever we find a new maximum.
# Approach
# We initialize two variables: curSum to keep track of the current subarray sum and maxSum to store
# the maximum sum found so far. We iterate through each number in the array, updating cur
# Sum by adding the current number. If curSum drops below zero, we reset it to zero.
# After updating curSum, we compare it with maxSum and update maxSum if curSum is greater.
# Finally, we return maxSum as the result.
