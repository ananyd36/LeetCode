# You are given an integer n. Return all well-formed parentheses strings that you can generate with n pairs of parentheses.

# Example 1:

# Input: n = 1

# Output: ["()"]
# Example 2:

# Input: n = 3

# Output: ["((()))","(()())","(())()","()(())","()()()"]
# You may return the answer in any order.



class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # they are two constraints to this problem
        # 1. we have n open and n close parentheses based on the input
        # 2. we can only add a closing parantheses when we the count of open para >  closing para at the node.
        # This is a backtracking problem where we set our constraints and create a recursive solution

        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN==closedN==n:
                res.append("".join(stack))
                return 

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()


        backtrack(0, 0) 
        return res
    

# Approach:
# 1. Initialize a stack to keep track of the current parentheses string.
# 2. Initialize an empty list to store the results.
# 3. Define a recursive function `backtrack` that takes two parameters: `openN` (number of open parentheses used) and `closedN` (number of closed parentheses used).
# 4. In the `backtrack` function:
#    - If both `openN` and `closedN` are equal to `n`, it means we have a valid parentheses string. Append the current string in the stack to the results list.
#    - If `openN` is less than `n`, append an open parenthesis to the stack and call `backtrack` with `openN + 1`.      
#    - If `closedN` is less than `openN`, append a closed parenthesis to the stack and call `backtrack` with `closedN + 1`.
# 5. Call the `backtrack` function with initial values of `openN` and `closedN` set to 0.
# 6. Return the results list containing all valid parentheses strings.