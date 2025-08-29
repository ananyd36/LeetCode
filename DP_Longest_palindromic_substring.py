# Given a string s, return the longest palindromic substring in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"




class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = 0
        res = ""
        for i in range(len(s)):

            # odd length palindromes

             l, r = i, i
             while r < len(s) and l >= 0 and s[l] == s[r]:
                if r - l + 1 > length:
                    length  = r - l + 1
                    res = s[l:r+1] 
                l-=1
                r+=1

            #evn length palindromes

             l, r = i, i + 1
             while r < len(s) and l >= 0 and s[l] == s[r]:
                if r - l + 1 > length:
                    length  = r - l + 1
                    res = s[l:r+1]  
                l-=1
                r+=1
        
        return res


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ""
        maxLen = 0

        for i in range(n):
            for j in range(n - 1, i - 1, -1):
                # prune if this window can't beat current best
                if j - i + 1 <= maxLen:
                    break

                l, r = i, j
                while l < r and s[l] == s[r]:
                    l += 1
                    r -= 1

                if l >= r:  # it's a palindrome
                    res = s[i:j+1]
                    maxLen = j - i + 1
                    break  # no longer j will be longer starting at this i

        return res



# Time Complexity: O(n^2) where n is the length of the string. We have two nested loops to consider all substrings, and checking if a substring is a palindrome takes O(n) in the worst case.
# Space Complexity: O(1) if we don't consider the output string, otherwise O(n) for storing the result.
# The approach uses a center expansion technique to find all possible palindromic substrings.
# For each character (and each pair of characters for even-length palindromes), it expands outwards as long as the characters on both sides are equal.
# It keeps track of the longest palindrome found during these expansions and returns it at the end.