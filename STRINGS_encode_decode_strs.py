# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

# Please implement encode and decode

# Example 1:

# Input: ["neet","code","love","you"]

# Output:["neet","code","love","you"]
# Example 2:

# Input: ["we","say",":","yes"]

# Output: ["we","say",":","yes"]
# Constraints:

# 0 <= strs.length < 100
# 0 <= strs[i].length < 200
# strs[i] contains only UTF-8 characters.



class Solution:

    def encode(self, strs: List[str]) -> str:
        final_str = ""
        for s in strs:
            final_str += str(len(s)) + '#' + s
        return final_str


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i 
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j+1+length
        return res
    


# Approach:
# 1. The encode function takes a list of strings and encodes it into a single string.
# 2. For each string, it appends the length of the string followed by a '#' character and then the string itself to the final encoded string.
# 3. The decode function takes the encoded string and decodes it back into a list of strings.
# 4. It iterates through the encoded string, finds the length of each string by looking for the '#' character, and then extracts the string based on that length.
# 5. The decoded strings are appended to a result list which is returned at the end.
# Time Complexity:
# - Encoding: O(n), where n is the total number of characters in all strings combined.
# - Decoding: O(n), where n is the length of the encoded string.
# Space Complexity:
# - Encoding: O(n) for the final encoded string.
# - Decoding: O(n) for the result list containing the decoded strings.
# Note: The encode and decode functions are designed to handle UTF-8 characters, ensuring that the encoding is robust for various string inputs.