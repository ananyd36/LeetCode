# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:

# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.
 

# Example 1:

# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# Example 2:

# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i, val in enumerate(tokens):
            if val in ['-','+','*','/']:
                sec_ele = int(stack.pop())
                firs_ele = int(stack.pop())
                if val == '-':
                    stack.append(firs_ele - sec_ele)
                elif val == '+':
                    stack.append(firs_ele + sec_ele)
                elif val == '*':
                    stack.append(firs_ele * sec_ele)
                elif val == '/':
                    stack.append(firs_ele / sec_ele)
            else:
                stack.append(val)
            
        return int(stack[-1])
    

# Approach:
# 1. Initialize an empty stack to hold operands.
# 2. Iterate through each token in the input list:
#    - If the token is an operator ('+', '-', '*', '/'):
#      - Pop the top two elements from the stack (these are the operands).
#      - Perform the operation based on the operator:
#        - For '-', subtract the second operand from the first.
#        - For '+', add the two operands.
#        - For '*', multiply the two operands.      
#        - For '/', perform integer division (truncating towards zero).
#      - Push the result back onto the stack.
#    - If the token is a number, convert it to an integer and push it onto the stack.
# 3. After processing all tokens, the final result will be the only element left in the stack.
# 4. Return the result as an integer.