# Imagine you have an ascendingly sorted array of unique integers that underwent a rotation at an undisclosed pivot point.
# This rotation implies that the array, initially sorted in ascending order, is divided into two subarrays at the pivot point and their ordered positions are swapped.
# The task is to develop an efficient method to find the index of a given target integer within this rotated array.
# If the target cannot be found within the array, the function should return -1.
# The algorithm should have a time complexity of O(log n), optimizing the search process through a binary search strategy.
 
# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
 
# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
 
# Example 3:
# Input: nums = [1], target = 0
# Output: -1


def findIndexInRotatedArray(nums, target):

    l, r  = 0, len(nums) - 1

    while l<=r:
        mid  = (l+r) // 2
        if nums[mid] == target:
            return mid

        if nums[l] <= nums[mid]:
            if target < nums[l]:
                l = mid + 1
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        
        else:
            if target < nums[mid]:
                r = mid - 1
            elif target > nums[r]:
                r = mid - 1
            else:
                l = mid + 1

    return -1




#Approach:# 1. Initialize two pointers, l and r, to the start and end of the array
# 2. Use a while loop to continue searching as long as l is less than or equal to r
# 3. Calculate the mid index
# 4. If the element at mid is equal to the target, return mid
# 5. If the left part of the array is sorted (nums[l] <= nums[mid]):
#    - If the target is within the range of the left part, adjust r to mid - 1
#    - Otherwise, adjust l to mid + 1
# 6. If the right part of the array is sorted (nums[mid] < nums[r]):
#    - If the target is within the range of the right part, adjust l to mid + 1
#    - Otherwise, adjust r to mid - 1
# 7. If the target is not found, return -1
# Time Complexity: O(log n) due to the binary search approach
# Space Complexity: O(1) as no additional space is used except for pointers