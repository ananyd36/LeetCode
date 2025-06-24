# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
 


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0 , 1
        max_profit = 0

        while sell < len(prices) and buy < len(prices):
            if prices[sell] < prices[buy]:
                buy = sell
                sell+=1
            elif prices[sell] - prices[buy] >= 0:
                profit =  prices[sell] - prices[buy]
                max_profit = max(profit, max_profit)
                sell+=1

        return max_profit
    


#Approach
# 1. Initialize two pointers: `buy` at the start of the list and `sell` at the next position.
# 2. Initialize `max_profit` to 0.
# 3. Iterate through the list with the `sell` pointer:
#    - If the price at `sell` is less than the price at `buy`, update `buy` to `sell` and move `sell` forward.
#    - If the price at `sell` is greater than or equal to the price at `buy`, calculate the profit and update `max_profit` if this profit is greater than the current `max_profit`.
#    - Move the `sell` pointer forward.
# 4. Continue this process until the `sell` pointer reaches the end of the list.
# 5. Return `max_profit` as the result.
# Time Complexity: O(n), where n is the length of the input list `prices`.
# Space Complexity: O(1), as we are using a constant amount of space for variables.