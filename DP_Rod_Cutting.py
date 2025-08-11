# Given a rod of length n inches and an array price[], where price[i] denotes the value of a piece of length i. Your task is to determine the maximum value obtainable by cutting up the rod and selling the pieces.

# Note: n = size of price, and price[] is 1-indexed array.

# Example:

# Input: price[] = [1, 5, 8, 9, 10, 17, 17, 20]
# Output: 22
# Explanation: The maximum obtainable value is 22 by cutting in two pieces of lengths 2 and 6, i.e., 5 + 17 = 22.

class Solution:
    def cutRod(self, price):
        n = len(price)
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        lengths = [i+1 for i in range(n)]  # lengths = 1, 2, ..., n

        for i in range(1, n + 1):           # piece length index
            for j in range(1, n + 1):       # rod length
                not_take = dp[i-1][j]
                take = 0
                if lengths[i-1] <= j:
                    take = price[i-1] + dp[i][j - lengths[i-1]]  # unbounded
                dp[i][j] = max(take, not_take)

        return dp[n][n]
