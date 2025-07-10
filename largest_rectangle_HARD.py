# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

 

# Example 1:


# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0

        def find_previous(ind):
            j = ind - 1
            while j >= 0 and heights[j] >= heights[ind]:
                j -= 1
            return j    

        def find_later(ind):
            j = ind + 1
            while j < len(heights) and heights[j] >= heights[ind]:
                j += 1
            return j

        for i in range(len(heights)):
            prev = find_previous(i)
            later = find_later(i)
            
            area = (later - prev - 1) * heights[i]
            maxArea = max(area, maxArea)
        return maxArea


#   # This solution iterates through each bar in the histogram and calculates the area of the rectangle that can be formed with that bar as the shortest bar.#   # It finds the previous and next bars that are shorter than the current bar to determine the width of the rectangle.
#   # The area is then calculated as the height of the current bar multiplied by the width (the distance between the previous and next shorter bars).
#   # The maximum area found during these calculations is returned as the result.
#   # The time complexity of this solution is O(n^2) in the worst case, where n is the number of bars in the histogram.
#   # This is because for each bar, we may need to traverse the entire list to find the previous and next shorter bars.
#   # The space complexity is O(1)
#   # since we are not using any additional data structures that grow with the input size.


#Optimized Solution using Stack
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #pair = index, value
        maxArea = 0

        for i, height in enumerate(heights):
            start = i   
            while stack and height < stack[-1][1]:
                index, h = stack.pop()
                area = (i - index) * h
                maxArea = max(area, maxArea)
                start = index
            stack.append([start, height])
        
        for i, h in stack:
            maxArea = max(maxArea, (len(heights) - i) * h)
        return maxArea
    
# This solution uses a stack to keep track of the indices and heights of the bars in the histogram.
# When a bar is encountered that is shorter than the bar at the top of the stack,
# it means we can calculate the area of the rectangle formed by the bar at the top of the stack.
# The width of the rectangle is determined by the difference between the current index and the index of the bar at the top of the stack.
# After processing all bars, we handle any remaining bars in the stack to ensure we calculate the area for all rectangles.
# The time complexity is O(n), where n is the number of bars in the histogram,
# and the space complexity is O(n) for the stack.
# This approach is efficient and works well for large histograms.
# The stack-based approach ensures that we efficiently find the largest rectangle area in a histogram with asingle pass through the heights.
# The use of a stack allows us to keep track of the indices and heights of the bars, making it easy to calculate the area of rectangles as we encounter shorter bars
# or reach the end of the histogram.