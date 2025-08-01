# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

# Example 1:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        def dfs(row, col, i):
            # we check if we have reached the end of the word
            if i == len(word):
                return True

            if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or (row, col) in visited or board[row][col] != word[i]:
                return False

            visited.add((row, col))

            
            res = (
                dfs(row, col + 1, i + 1) or 
                dfs(row, col - 1, i + 1) or 
                dfs(row + 1, col, i + 1) or
                dfs(row - 1, col, i + 1)
            )

            visited.remove((row, col))

            return res

        # Start DFS from every cell that matches word[0]
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True

        return False



# Intuition
# Since we can only move to adjacent (horizontal or vertical) cells and can't reuse the same cell, we need a way to explore all possible 
# paths starting from any cell that matches the first character of the word.

# At every step:

# If the current board cell matches the current character in the word,
# Then recursively check the adjacent cells for the next character,

# If any path fails (i.e., no valid adjacent cell for the next character), we backtrack and try a different route.

# This naturally leads to a Depth-First Search (DFS) approach with backtracking:

# DFS to explore all potential paths,
# Backtracking to undo choices and try alternatives when a path doesn't work out.

# Approach
# Here we check if board element matches the first word char, if it matches we mark it as visited and we start the 
# recursive search for all adjacent elements, if at any point it returns false we backtrack, remove the visited node 
# and start fresh by macthing the first word char with the next board element

# Complexity
# Time complexity:
# O(Mxnx4^L) since we need to check 4 directions for next word char if first one matches, in worst case we check 
# for every element all directions. L here is the length of the word

# Space complexity:
# O(L) for the recursive stack and visited set