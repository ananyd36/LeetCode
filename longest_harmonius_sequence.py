# We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

# Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

 

# Example 1:

# Input: nums = [1,3,2,2,5,2,3,7]

# Output: 5

# Explanation:

# The longest harmonious subsequence is [3,2,2,2,3].

# Example 2:

# Input: nums = [1,2,3,4]

# Output: 2

# Example 3:

# Input: nums = [1,1,1,1]

# Output: 0



# Constraints:

# 1 <= nums.length <= 2 * 104
# -109 <= nums[i] <= 109

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = Counter(nums)
        res = 0
        for num in count:
            if num + 1 in count:
                res = max(res, count[num] + count[num + 1])
        return res


#Approach:
# 1. Count the occurrences of each number in the array using a Counter.
# 2. Initialize a variable `res` to keep track of the maximum length of a harmonious subsequence.
# 3. Iterate through each unique number in the count:
#     - If the next consecutive number (num + 1) exists in the count:
#         - Calculate the length of the harmonious subsequence formed by `num` and `num + 1` frequencies.
#         - Update `res` with the maximum length found so far.
