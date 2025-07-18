# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:

# Input: temperatures = [30,60,90]
# Output: [1,1,0]
 



class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # pair: [temp, index]
        output = [0] * len(temperatures)

        for i , temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackT, stackInd = stack.pop()
                output[stackInd]  = (i - stackInd)
            stack.append([temp, i])
        return output

                
## Approach:# 1. Initialize an empty stack to keep track of temperatures and their indices.
# 2. Initialize an output list with the same length as the input temperatures, filled with zeros.
# 3. Iterate through the temperatures using an index `i`:
#    - While the stack is not empty and the current temperature is greater than the temperature at the top of the stack:
#      - Pop the top element from the stack, which contains the temperature and its index.
#      - Calculate the difference between the current index `i` and the popped index, and store it in the output list at the popped index.
#    - Append the current temperature and its index as a pair to the stack.
# 4. After processing all temperatures, return the output list containing the number of days to wait for a warmer temperature for each day.
## Time Complexity: O(n), where n is the number of days in the input temperatures list.
## Space Complexity: O(n), where n is the number of days in the input temperatures list
## This is because we use a stack to store the temperatures and their indices, and the output list has the same length as the input temperatures list.
## The stack will contain at most n elements in the worst case, and the output list will always have a length of n.
## The overall space complexity is O(n) due to the stack and output list.
## The time complexity is O(n) because we iterate through the temperatures list once, and each temperature is pushed and popped from the stack at most once.
## Therefore, the algorithm runs in linear time with respect to the number of days in the input temperatures list.