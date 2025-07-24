# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

 

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
# Example 3:

# Input: nums = [1,0,1,2]
# Output: 3
 


# Inttial Brute Force Approach  67/81 Passed
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0

        for i in range(len(nums)):
            element = nums[i]
            cur_long = 1
            while True:
                if element + 1 in nums:
                    cur_long += 1
                    element += 1
                else:
                    break
            longest = max(longest, cur_long)
        return longest


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

# Approach: The solution uses a set to store the unique elements of the input list.
# It then iterates through each number in the set, checking if it is the start of a 
# consecutive sequence by checking if the previous number (num - 1) is not in the set
# If it is the start, it counts the length of the consecutive sequence by checking for
# the next numbers (num + length) in the set.
# Time Complexity: O(n), where n is the number of unique elements in the input list.
# Space Complexity: O(n), for storing the unique elements in the set.
# Note: The input list is not modified, and the function returns the length of the longest
# consecutive sequence found in the input list.
# The second approach is more efficient than the brute force approach as it avoids checking
# for each element in the list multiple times, leading to a significant reduction in time complexity.