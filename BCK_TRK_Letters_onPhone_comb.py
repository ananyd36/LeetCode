# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]



class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        def dfs(i, path):
            if len(path) == len(digits):
                res.append("".join(path[:]))
                return
            if digits[i] == 0 or digits[i] == 1:
                return    
            for char in digitToChar[str(digits[i])]:
                path.append(char)
                dfs(i+1, path)
                path.pop()
        
        dfs(0,[])
        return res
            
