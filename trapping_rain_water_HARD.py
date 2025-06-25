# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

# Example 1:


# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n
        water = 0

        # Fill max_left
        max_left[0] = height[0]
        for i in range(1, n):
            max_left[i] = max(max_left[i - 1], height[i])

        # Fill max_right
        max_right[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], height[i])

        # Calculate trapped water
        for i in range(n):
            water += min(max_left[i], max_right[i]) - height[i]

        return water
    

# Approach:
# 1. Initialize two arrays `max_left` and `max_right` to store the maximum heights to the left and right of each bar.
# 2. Fill `max_left` by iterating from left to right, keeping track of the maximum height encountered so far.
# 3. Fill `max_right` by iterating from right to left, similarly keeping track of the maximum height.
# 4. Calculate the trapped water at each index by taking the minimum of `max_left` and `max_right` and subtracting the height at that index.
# 5. Sum up the trapped water for all indices to get the total amount of water trapped.
# Time Complexity: O(n), where n is the length of the input list `height`.
# Space Complexity: O(n), due to the use of two additional arrays `max_left` and `max_right`.



class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0

        l ,r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                water = leftMax - height[l]
                if water > 0 :
                    res+=water
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                water = rightMax - height[r]
                if water > 0 :
                    res+=water
        return res


# Approach:
# 1. Initialize two pointers `l` and `r` at the start and end of the height list, respectively.
# 2. Initialize `leftMax` and `rightMax` to the heights at the respective pointers.
# 3. Initialize a variable `res` to accumulate the total trapped water.
# 4. Use a while loop to iterate until the two pointers meet:
#    - If `leftMax` is less than `rightMax`, move the left pointer `l` to the right, update `leftMax`, and calculate the trapped water at that position.
#    - If `rightMax` is less than or equal to `leftMax`, move the right pointer `r` to the left, update `rightMax`, and calculate the trapped water at that position.
# 5. Continue this process until the two pointers meet.
# 6. Return the accumulated trapped water in `res`.
# Time Complexity: O(n), where n is the length of the input list `height`.
# Space Complexity: O(1), as we are using only a constant amount of space for variables.