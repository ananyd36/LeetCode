# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

 

# Example 1:


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0

        l, r = 0, len(heights)-1

        while l < r:
            area = (r - l) * min(heights[l],heights[r])
            maxArea = max(maxArea, area)
            if heights[l] < heights[r]:
                l+=1
            elif heights[r] < heights[l]:
                r-=1
            else:
                l+=1
        
        return maxArea
    

# The approach is to use two pointers, one at the beginning and one at the end of the array.
# The area is calculated as the distance between the two pointers multiplied by the height of the shorter line.
# The maximum area is updated if the current area is greater than the previous maximum.
# The pointer pointing to the shorter line is moved inward, as moving the taller line would not increase the area.
# The process continues until the two pointers meet.
# Time Complexity: O(n), where n is the length of the heights array, as we traverse the array once.
# Space Complexity: O(1), as we are using only a constant amount of extra space for the pointers and the maximum area variable.
# The two-pointer technique is efficient for this problem because it reduces the need to check every possible pair of lines, which would result in a time complexity of O(n^2).