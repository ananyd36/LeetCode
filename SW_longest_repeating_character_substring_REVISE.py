# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.
 

#FORMULA = length of the window minus the maximum frequency of any character in the window should be less than or equal to k.
#EQUATION = # (R - L + 1) - max(count.values()) <= k


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(set(s)) == 1:
            return len(s)
        elif s == "":
            return 0
        count = {}
        max_length = 0
        L = 0
        for R in range(len(s)):
            count[s[R]] = 1 + count.get(s[R], 0)
            while (R - L + 1) - max(count.values()) > k:
                count[s[L]] -= 1
                L+=1
            max_length = max(max_length, R - L + 1)
        return max_length


## Approach:
# 1. Initialize a dictionary `count` to keep track of character frequencies in the current window.
# 2. Initialize `max_length` to store the length of the longest substring found.
# 3. Use two pointers `L` and `R` to represent the left and right ends of the current substring.
# 4. Iterate through the string with the right pointer `R`:
#    - Increment the count of the character at `R` in the `count` dictionary.
#    - While the current window size minus the maximum frequency of any character in `count` exceeds `k`, increment the left pointer `L` and decrement the count of the character at `L`.
#    - Update `max_length` with the maximum of its current value and the size of the current window.
# 5. Return `max_length` as the result.
# Time Complexity: O(n), where n is the length of the string `s`, as we traverse the string once.
# Space Complexity: O(1), since the size of the `count` dictionary is limited to the number of unique characters (uppercase English letters).
# Note: The algorithm efficiently maintains the frequency of characters in the current window and adjusts the window size based on the allowed number of replacements (`k`).
# This approach ensures that we find the longest substring with at most `k` replacements in linear time.