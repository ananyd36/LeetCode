# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.

 

# Example 1:

# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.
# Example 2:

# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
# Example 3:

# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.
 




class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N = len(text1)
        M = len(text2)
        dp = [[0] * (N+1) for _ in range(M+1)]

        for i in range(M):
            for j in range(N):
                if text1[j] == text2[i]:
                    dp[i+1][j+1] = 1 + dp[i][j]
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
        
        return dp[M][N]
        
        # M, N = len(text1), len(text2)

        # cache = [[-1 for _ in range(N)] for _ in range(M)]

        # def recursive(text1, text2, i1, i2):
        #     if i1 >= len(text1) or i2 >= len(text2):
        #         return 0
            
        #     if cache[i1][i2] != -1:
        #         return cache[i1][i2]


        #     if text1[i1] == text2[i2]:
        #         cache[i1][i2] = 1 + recursive(text1, text2, i1+1, i2+1)
        #     else:
        #         cache[i1][i2] =  max(recursive(text1, text2, i1+1, i2), recursive(text1, text2, i1, i2+1))

        #     return cache[i1][i2]
        
        # return recursive(text1, text2, 0, 0)

