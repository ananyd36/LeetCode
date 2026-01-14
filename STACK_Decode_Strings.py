# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

# The test cases are generated so that the length of the output will never exceed 105.

 

# Example 1:

# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# Example 2:

# Input: s = "3[a2[c]]"
# Output: "accaccacc"


class Solution:
    def decodeString(self, s: str) -> str:
        res = ""
        stack = []
        num = 0

        for char in s:
            if char.isdigit():
                num = num*10+int(char)
            elif char == "[":
                stack.append((res, num))
                res = ""
                num = 0
            elif char == "]":
                prev_char, repeat = stack.pop()
                res = prev_char + res*repeat
            else:
                res+=char
        
        return res


#Explanation: The idea is to use a stack to keep track of the current string and the number of times it should 
# be repeated. When we encounter a digit, we build the number. When we see an opening bracket '[', we push the 
# current string and number onto the stack and reset them. When we see a closing bracket ']', we pop from the 
# stack and build the new string by repeating the current string the specified number of times. Finally, 
# we return the decoded string.


# Time Complexity: O(N) where N is the length of the string s. Each character is processed once.
# Space Complexity: O(N) in the worst case, the stack can hold all characters in the