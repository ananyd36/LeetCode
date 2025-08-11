
# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

# You can either start from the step with index 0, or the step with index 1.

# Return the minimum cost to reach the top of the floor.

 

# Example 1:

# Input: cost = [10,15,20]
# Output: 15
# Explanation: You will start at index 1.
# - Pay 15 and climb two steps to reach the top.
# The total cost is 15.
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)
        dp = [0] * (n+1)
        for i in range(2, n+1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        return dp[n]


# minCost[i] = min(
#     minCost[i-1] + cost[i-1],  # Came from 1 step before
#     minCost[i-2] + cost[i-2]   # Came from 2 steps before
# )
# n = 3
# dp = [0, 0, 0, 0]

# i = 2:
# dp[2] = min(dp[1] + cost[1], dp[0] + cost[0])
#       = min(0 + 15, 0 + 10)
#       = min(15, 10)
#       = 10

# i = 3:
# dp[3] = min(dp[2] + cost[2], dp[1] + cost[1])
#       = min(10 + 20, 0 + 15)
#       = min(30, 15)
#       = 15