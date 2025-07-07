# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# Example 2:

# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]




class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        quad = []
        res = []

        def kSum(k, start, target):
            if k != 2:
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i] == nums[i - 1]:
                        continue
                    quad.append(nums[i])
                    kSum(k - 1, i + 1, target - nums[i])
                    quad.pop()
                return 
        
            l,r = start, len(nums) - 1
            while l<r:
                if nums[l] + nums[r] > target:
                    r-=1
                elif nums[l] + nums[r] < target:
                    l+=1
                else:
                    res.append(quad + [nums[l], nums[r]])
                    l+=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
                    
        kSum(4,0,target)
        return res
    

# Approach:# 1. Sort the input list `nums` to facilitate the two-pointer technique.
# # 2. Initialize an empty list `quad` to store the current quadruplet and `res` to store the final results.
# # 3. Define a recursive function `kSum` that takes three parameters: `k` (the number of elements to find), `start` (the starting index for the search), and `target` (the target sum).
# # 4. If `k` is not equal to 2, iterate through the list starting from the `start` index:
# #    - Skip duplicates to avoid repeated quadruplets.
# #    - Append the current number to `quad` and call `kSum` recursively with `k - 1`, the next index, and the updated target.
# #    - After the recursive call, pop the last element from `quad` to backtrack.
# # 5. If `k` is equal to 2, use the two-pointer technique:
# #    - Initialize two pointers `l` and `r` at the start and end of the list, respectively.
# #    - While `l` is less than `r`, check the sum of the elements at the two pointers:
# #      - If the sum is greater than the target, move the right pointer `r` to the left.
# #      - If the sum is less than the target, move the left pointer `l` to the right.
# #      - If the sum equals the target, append the current quadruplet to `res`, move the left pointer `l` to the right, and skip duplicates to avoid repeated quadruplets.
# # 6. Call the `kSum` function with `k = 4`, `start = 0`, and the original target.
# # 7. Return the list `res` containing all unique quadruplets that sum to the target.
# ## Time Complexity: O(n^k), where n is the number of elements in the input list `nums`.
# ## Space Complexity: O(n), where n is the number of elements                   