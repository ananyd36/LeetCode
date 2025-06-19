# Given an integer array nums and an integer k, return the k most frequent elements within the array.

# The test cases are generated such that the answer is always unique.

# You may return the output in any order.

# Example 1:

# Input: nums = [1,2,2,3,3,3], k = 2

# Output: [2,3]


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        # calculating the frequencies of the elements in nums
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            freq[c].append(n) # n occurs c number of times


        res = []
        for i in range(len(freq) - 1, 0, -1):  # iterating from the maximum frequency (last index)
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
                

# Approach:
# 1. Create a dictionary to count the frequency of each element in the input array `nums`.
# 2. Create a list of lists `freq` where the index represents the frequency and each sublist contains elements with that frequency.
# 3. Iterate through the `count` dictionary to populate the `freq` list.
# 4. Initialize an empty list `res` to store the k most frequent elements.
# 5. Iterate through the `freq` list in reverse order (from highest frequency to lowest).
# 6. For each frequency, append the elements to `res` until it contains k elements.
# 7. Return the `res` list containing the k most frequent elements.
# Time Complexity:
# - O(n), where n is the number of elements in `nums`, for counting frequencies.
# - O(n) for populating the `freq` list.
# - O(n) for constructing the result list.
# Space Complexity:
# - O(n) for the `count` dictionary and `freq` list.
# Note: The solution ensures that the output is unique by the nature of the problem constraints.
