# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

 

# Example 1:

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1



class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for a in range(1, amount+1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a-c])
        
        return dp[amount] if dp[amount]!=float("inf") else -1



        
        # global minCoin
        # minCoin = float('inf')
        # def recursive(i, cur, used):
        #     global minCoin
        #     if cur == amount:
        #         minCoin = min(minCoin, used)
        #         return
        #     if cur > amount or i == len(coins):
        #         return
            
        #     recursive(i, cur+coins[i], used+1)

        #     recursive(i+1, cur, used)

        # recursive(0, 0, 0)
        # return minCoin if minCoin != float('inf') else -1