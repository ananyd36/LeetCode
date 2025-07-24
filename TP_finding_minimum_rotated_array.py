# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.

 

# Example 1:

# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.
# Example 2:

# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l,r  = 0, len(nums) - 1

        while l<=r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            m = (l+r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        
        return res
    

## Approach:# 1. Initialize `res` to the first element of the array.
# 2. Set `l` to 0 and `r` to the last index of the array.
# 3. Use a while loop to continue until `l` is less than or equal to `r`.
# 4. If the first element is less than the last element, it means the array is not rotated and sorted already, so update `res` to the minimum of `res` and the first
#    element, then break the loop.
# 5. Calculate the middle index `m` as the average of `l` and `r`.
# 6. Update `res` to the minimum of `res` and the element at index `m`.
# 7. If the element at index `m` is greater than or equal to the element at index `l`, it means the left half is sorted, so
#    move the left pointer `l` to `m + 1`.
# 8. Otherwise, it means the right half is sorted, so move the right pointer `r` to `m - 1`.
# 9. The loop continues until the left pointer exceeds the right pointer.
# 10. Finally, return `res`, which is the minimum element in the rotated sorted array.
# The time complexity of this solution is O(log n) due to the binary search approach.
# The space complexity is O(1) since we are using a constant amount of extra space.