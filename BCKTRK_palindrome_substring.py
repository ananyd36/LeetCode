
# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

 

# Example 1:

# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
# Example 2:

# Input: s = "a"
# Output: [["a"]]



 
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []
        def dfs(i):
            if i == len(s):
                res.append(part.copy())
                return

            for j in range(i, len(s)+1):
                if self.isPali(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()

        dfs(0)
        return res

    def isPali(self, s, i, j):
        return ",".join(s[i:j+1]) == ",".join(s[i:j+1][::-1])


# Backtracking Approach for Palindrome Partitioning
# This approach uses backtracking to explore all possible partitions of the string and checks if each partition is a palindrome.
# It recursively builds partitions and backtracks when necessary.
# The `isPali` function checks if a substring is a palindrome by comparing it to its reverse.
# The `dfs` function explores all possible partitions starting from the current index `i`, adding valid palindromic substrings to the current partition `part`.
# When the end of the string is reached, the current partition is added to the result list `res`.
# The function returns all valid partitions of the input string `s` where each substring is a palindrome.
# The time complexity is O(2^N) in the worst case, where N is the length of the string, due to the exponential number of partitions that can be formed.
# The space complexity is O(N) for the recursion stack and the storage of partitions in the result list.
# This approach efficiently finds all palindromic partitions by exploring all possible combinations and checking for
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(i, part):
            if i == len(s):
                res.append(part.copy())
                return

            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    dfs(j + 1, part + [s[i:j+1]])

        dfs(0, [])
        return res

    def isPali(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True