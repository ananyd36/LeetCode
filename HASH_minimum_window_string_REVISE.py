# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

 

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.



class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                    
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""


# Approach:
# 1. Create a dictionary `countT` to count the frequency of characters in `t`.
# 2. Initialize a dictionary `window` to keep track of the characters in the current window of `s`.
# 3. Use two pointers `l` and `r` to represent the left and right ends of the current window.
# 4. Iterate through `s` with the right pointer `r`:
#    - Increment the count of the character at `r` in the `window` dictionary.
#    - If the character is in `countT` and its count matches, increment `have`.
#    - While `have` equals `need`, check if the current window is smaller than the previous best:
#      - Update the result with the current window if it is smaller.
#      - Decrement the count of the character at `l` in the `window` dictionary.
#      - If the character at `l` is in `countT` and its count drops below the required count, decrement `have`.
#      - Increment `l` to shrink the window from the left.
# 5. Return the substring from `s` that corresponds to the best result found, or an empty string if no valid window was found.
# Time Complexity: O(n + m), where n is the length of `s` and m is the length of `t`, as we traverse both strings once.
# Space Complexity: O(m), where m is the length of `t`, for storing the frequency counts in `countT` and `window`.
# Note: This approach efficiently finds the minimum window substring that contains all characters from `t` using a sliding window technique.
# This solution is optimal for the problem and handles edge cases such as empty strings and characters not present in `s`.
# The solution assumes that the input strings are valid and that there is at least one character in `t`.