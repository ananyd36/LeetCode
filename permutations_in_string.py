# You are given two strings s1 and s2.

# Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.

# Both strings only contain lowercase letters.

# Example 1:

# Input: s1 = "abc", s2 = "lecabee"

# Output: true
# Explanation: The substring "cab" is a permutation of "abc" and is present in "lecabee".

# Example 2:

# Input: s1 = "abc", s2 = "lecaabee"

# Output: false



class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        for r in range(len(s1) - 1,len(s2),1):
            print(sorted(s2[l:r + 1]), sorted(s1))
            if sorted(s2[l:r + 1]) == sorted(s1):
                return True
            l+=1
        return False
    

# Approach:
# 1. Initialize a left pointer `l` at the start of `s2`.
# 2. Iterate through `s2` with a right pointer `r`, starting from the end of `s1` to the end of `s2`.
# 3. For each substring from `l` to `r`, check if it is a permutation of `s1` by comparing sorted versions of both strings.
# 4. If a match is found, return True.
# 5. Increment the left pointer `l` to check the next substring.
# 6. If no permutation is found after checking all substrings, return False.
# Time Complexity: O(n * m log m), where n is the length of `s2` and m is the length of `s1`, due to sorting each substring.
# Space Complexity: O(m), where m is the length of `s1`, for storing the sorted version of `s1`.
# Note: This approach can be optimized to O(n) using a frequency count of characters instead of sorting.