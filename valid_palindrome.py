# Valid Palindrome
 
# Given a string s, return true if it is a palindrome, otherwise return false.

# A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

# Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

# Example 1:

# Input: s = "Was it a car or a cat I saw?"

# Output: true
# Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

# Example 2:

# Input: s = "tab a cat"

# Output: false
# Explanation: "tabacat" is not a palindrome.


class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""

        for char in s:
            if char.isalnum():
                new_str += char.lower()
        
        return new_str == new_str[::-1]
    


# Approach:
# 1. Initialize an empty string `new_str` to store alphanumeric characters in lowercase.
# 2. Iterate through each character in the input string `s`.
# 3. For each character, check if it is alphanumeric using `char.isalnum()`.
# 4. If it is alphanumeric, convert it to lowercase and append it to `new_str`.
# 5. After constructing `new_str`, check if it is equal to its reverse (`new_str[::-1]`).
# 6. Return `True` if they are equal (indicating a palindrome), otherwise return `False`.
# Time Complexity:
# - O(n), where n is the length of the input string `s`, for iterating through the characters.
# Space Complexity:
# - O(n), for storing the filtered and lowercased characters in `new_str`.
# Note: The solution effectively ignores non-alphanumeric characters and is case-insensitive, making it suitable for checking palindromes in a wide range of input strings.