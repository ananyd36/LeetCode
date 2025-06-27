# Given a string s, find the length of the longest substring without duplicate characters.

# A substring is a contiguous sequence of characters within a string.

# Example 1:

# Input: s = "zxyzxyz"

# Output: 3
# Explanation: The string "xyz" is the longest without duplicate characters.

# Example 2:

# Input: s = "xxxx"

# Output: 1



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0
        l , r = 0, 1
        max_length = 1
        while l < len(s) and r < len(s):
            if s[r] not in s[l:r]:
                r+=1
                max_length = max(max_length, r - l) 
            else:
                l += 1
                r = l + 1
        return max_length


# Approach:
# 1. Initialize two pointers `l` and `r` to represent the left and right ends of the substring.
# 2. Initialize `max_length` to keep track of the longest substring found.
# 3. Use a while loop to iterate through the string:
#    - If the character at `r` is not in the substring from `l` to `r`, increment `r` and update `max_length`.
#    - If the character at `r` is already in the substring, increment `l` to move the left pointer forward and reset `r` to `l + 1`.
# 4. Continue this process until `r` reaches the end of the string.
# 5. Return `max_length` as the result.
# Time Complexity: O(n^2) in the worst case, where n is the length of the string, due to the substring check.
# Space Complexity: O(n) in the worst case for the substring check, but can be optimized to O(1) using a set to track characters.
# Note: The time complexity can be improved to O(n) using a sliding window approach with a set to track characters.
# However, the current implementation is straightforward and easy to understand.



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        res = 0
        l=0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            res = max(res,r-l+1)
        return res


# Approach:
# 1. Initialize a set `charSet` to keep track of characters in the current substring.
# 2. Initialize `res` to store the length of the longest substring found.
# 3. Use a variable `l` to represent the left pointer of the substring.
# 4. Iterate through the string with a right pointer `r`:
#    - If the character at `r` is already in `charSet`, remove characters from the left pointer `l` until the character at `r` can be added.
#    - Add the character at `r` to `charSet`.
#    - Update `res` with the maximum length of the substring found so far.