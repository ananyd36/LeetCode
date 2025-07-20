# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and using only constant extra space.

 

# Example 1:

# Input: nums = [1,3,4,2,2]
# Output: 2

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # FLOYD AND TORTOISE HARE
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast  = nums[nums[fast]]
            if slow == fast:
                break

        
        slow = nums[0]

        while slow!=fast:
            fast = nums[fast]
            slow = nums[slow]
        
        return slow



        #MARKING ALGORITHM
        for i, num in enumerate(nums):
            idx = abs(num)
            if nums[idx] < 0:
                return idx
            else:
                nums[idx] = -1 * nums[idx]


# Approach: Using Floyd's Tortoise and Hare algorithm to find the duplicate number in an array where each number is in the range [1, n] and there is exactly one duplicate.
# Time Complexity: O(n)
# Space Complexity: O(1)    

# Note: The input array is modified in the marking algorithm approach, but the first approach does not modify the input array.