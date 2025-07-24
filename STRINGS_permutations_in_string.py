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

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_arr = [0]*26
        s2_arr = []

        for i, string in enumerate(s1):
            s1_arr[ord(string) - ord('a')] +=1        
        l = 0
        for r in range(len(s1) - 1,len(s2),1):
            window = s2[l:r + 1]
            s2_arr = [0]*26
            for i, char in enumerate(window):
                s2_arr[ord(char) - ord('a')] +=1
                if s2_arr == s1_arr:
                    return True
            l+=1
        return False
    
# Approach: 
# 1. Create an array `s1_arr` to count the frequency of characters in `s1`.
# 2. Initialize a list `s2_arr` to count the frequency of characters in the current window of `s2`.
# 3. Iterate through `s2` with a right pointer `r`, starting from the end of `s1` to the end of `s2`.
# 4. For each character in the current window, update `s2_arr` with the frequency count.
# 5. If `s2_arr` matches `s1_arr`, return True.
# 6. Increment the left pointer `l` to check the next substring.
# 7. If no permutation is found after checking all substrings, return False.
# Time Complexity: O(n + m), where n is the length of `s2` and m is the length of `s1`, as we traverse both strings once.
# Space Complexity: O(1), since the size of the frequency arrays is constant (26 for lowercase letters).
# Note: This approach efficiently counts character frequencies and compares them, avoiding the need for sorting.
# This ensures that we can check for permutations in linear time.