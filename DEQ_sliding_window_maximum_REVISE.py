# You are given an array of integers nums and an integer k. There is a sliding window of size k that starts at the left edge of the array. The window slides one position to the right until it reaches the right edge of the array.

# Return a list that contains the maximum element in the window at each step.

# Example 1:

# Input: nums = [1,2,1,0,4,2,6], k = 3

# Output: [2,2,4,4,6]

# Explanation: 
# Window position            Max
# ---------------           -----
# [1  2  1] 0  4  2  6        2
#  1 [2  1  0] 4  2  6        2
#  1  2 [1  0  4] 2  6        4
#  1  2  1 [0  4  2] 6        4
#  1  2  1  0 [4  2  6]       6


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        output = []
        l, r = 0, 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if r + 1 >= k:
                output.append(nums[q[0]])
                l+=1
            r+=1
        return output
    

# Approach:
# 1. Initialize a deque to keep track of indices of the maximum elements in the current window.
# 2. Initialize an empty list to store the results.
# 3. Use two pointers, `l` and `r`, to represent the left and right edges of the sliding window.
# 4. Iterate through the array using the right pointer `r`:
#    - While the deque is not empty and the current element is greater than the element at the index stored at the back of the deque, pop elements from the back of the deque.
#    - Append the current index `r` to the deque.
#    - If the left pointer `l` is greater than the index at the front of the deque, pop the front element from the deque.
#    - If the right pointer `r` has reached the size of the window (i.e., `r + 1 >= k`), append the maximum element (the element at the index stored at the front of the deque) to the output list and increment the left pointer `l`.
# 5. Increment the right pointer `r` to move the window to the right.
# 6. Return the output list containing the maximum elements for each sliding window position.