# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true


class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) == 1:
            return False

        stack = []
        for ele in s:
            if stack and ele  ==  '}' and stack[-1] == '{':
                stack.pop()
            elif stack and ele  ==  ']' and stack[-1] == '[':
                stack.pop()
            elif stack and ele  ==  ')' and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(ele)


        if len(stack) == 0:
            return True
        return False


# approach on above solution:
# 1. Initialize an empty stack to keep track of opening brackets.
# 2. Iterate through each character in the string:
#    - If the character is an opening bracket ('(', '{', or '['), push it onto the stack.
#    - If the character is a closing bracket (')', '}', or ']'):
#      - Check if the stack is not empty and if the top of the stack matches the corresponding opening bracket.
#      - If it matches, pop the top of the stack.
#      - If it does not match or the stack is empty, return False.
#     - If the character is not a bracket, continue to the next character.
# 3. After processing all characters, check if the stack is empty:
#    - If it is empty, return True (all brackets were matched).