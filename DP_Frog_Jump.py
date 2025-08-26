
# Given an integer array height[] where height[i] represents the height of the i-th stair, 
# a frog starts from the first stair and wants to reach the top. From any stair i, the frog has two options: 
# it can either jump to the (i+1)th stair or the (i+2)th stair. The cost of a jump is the absolute difference in 
# height between the two stairs. Determine the minimum total cost required for the frog to reach the top.

# Input: heights[] = [20, 30, 40, 20] 
# Output: 20
# Explanation:  Minimum cost is incurred when the frog jumps from stair 0 to 1 then 1 to 3:
# jump from stair 0 to 1: cost = |30 - 20| = 10
# jump from stair 1 to 3: cost = |20-30|  = 10
# Total Cost = 10 + 10 = 20

#Space Optimization
class Solution:
    def minCost(self, height):
        n = len(height)

        prev = 0
        prev2 = 0
        
        for i in range(1, n):
            ls = prev + abs(height[i-1] - height[i])
            ss = float("inf")
            if i > 1:
                ss = prev2 + abs(height[i-2] - height[i])
            
            cur = min(ls, ss)
            
            prev2 = prev
            prev = cur
            
        
        return prev 
    

# DP - Tabulation
class Solution:
    def minCost(self, height):
        n = len(height)
        dp = [0] * (n)
        
        dp[0] = 0
        
        for i in range(1, n):
            prev = dp[i-1] + abs(height[i-1] - height[i])
            prev2 = float("inf")
            if i > 1:
                prev2 = dp[i-2] + abs(height[i-2] - height[i])
            
            dp[i] = min(prev, prev2)
        
        return dp[-1]
# DP - Memoization   
    class Solution:
        def minCost(self, height):
            memo = {}
            n = len(height)
            
            def recursive(i):
                if i == 0:
                    return 0
                
                if i in memo:
                    return memo[i]
                
                left = recursive(i - 1) + abs(height[i-1] - height[i])
                if i > 1:
                    right = recursive(i - 2) + abs(height[i-2] - height[i])
                else:
                    right = float("inf")
                
                memo[i] = min(left, right)
                
                return memo[i]
                
            
            return recursive(n-1)
        
        
        
# Here greedy solution wont work because jumping to the next stair with minimum cost at each step does 
# not guarantee a globally optimal solution. The frog might incur a higher cost later on if 
# it makes a suboptimal choice early in the journey. Dynamic programming ensures that all 
# possible paths are considered and the minimum cost is calculated for each stair based on previous computations.


# Time Complexity: O(n), where n is the number of stairs. Each stair's minimum cost is computed once and stored in the memo dictionary.
# Space Complexity: O(n) for the memo dictionary and the recursion stack in the worst case