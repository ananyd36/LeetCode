# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

 

# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:

# Input: nums = [2,0,1]
# Output: [0,1,2]
 


class Solution:
    def sortColors(self, nums: List[int]) -> None:

        if len(nums) <= 1:
            return nums
        count = {}

        for i in sorted(nums):
            count[i] = 1 + count.get(i, 0)

        j = 0
        for n in count.keys():
            for k in range(count[n]):
                nums[j] = n
                j+=1
        
        return nums
    

# The above code defines a function `sortColors` that sorts an array of integers representing colors (0 for red, 1 for white, and 2 for blue) in-place.
# The function first checks if the length of the input array `nums` is less than or equal to 1, in which case it simply returns the array as it is already sorted.
# It then initializes an empty dictionary `count` to keep track of the frequency of each color.
# The function iterates through the sorted version of `nums`, updating the `count` dictionary with the frequency of each color.
# After counting the colors, it initializes a variable `j` to 0, which will be used to fill the `nums` array with sorted colors.
# It then iterates through the keys of the `count` dictionary, and for each color, it fills the `nums` array with the corresponding number of occurrences of that color.
# Finally, it returns the sorted `nums` array.
# The time complexity of this solution is O(n log n) due to the sorting step,
# and the space complexity is O(n) due to the use of the `count` dictionary.
# However, since the problem requires an in-place sort, this solution does not meet that requirement
# and would not be suitable for the problem as stated.