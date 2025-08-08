# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

# Example 1:


# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
# Example 2:

# Input: n = 1
# Output: [["Q"]]


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set()
        negDiag = set()

        board = [["."]*n for _ in range(n)]
        res = []

        def backtrack(r):
            if r==n:
                res.append(["".join(row) for row in board])
                return
            
            for c in range(n):
                if c in col or r+c in posDiag or r-c in negDiag:
                    continue
                
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = "Q"

                backtrack(r+1)

                # to check more possible solution 
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = "."
        
        backtrack(0)
        return res



# The above code implements a backtracking solution to the N-Queens problem.
# It uses sets to keep track of the columns and diagonals that are already occupied by queens
# and a 2D list to represent the chessboard. The `backtrack` function recursively places queens on the board,
# checking for conflicts with previously placed queens. When a valid configuration is found (when all queens are placed), it appends the current board configuration to the result list `res`.
# The function returns all distinct solutions to the N-Queens puzzle, where each solution
# is represented as a list of strings, with 'Q' indicating a queen and '.' indicating an empty space.
# The time complexity is O(N!), where N is the number of queens,
# as there are N! possible arrangements of N queens on an N x N board.
# The space complexity is O(N^2) for the board and O(N) for the sets used to track occupied columns and diagonals.
# This approach efficiently explores all possible placements of queens
# while avoiding conflicts, ensuring that no two queens threaten each other.


# (r+c) denotes the positive diagonal (from top-left to bottom-right),
# (r-c) denotes the negative diagonal (from top-right to bottom-left),
# and `c` denotes the column. The sets `col`, `posDiag`, and `negDiag` are used to track which columns and diagonals are already occupied by queens.
## The `board` variable is a 2D list that represents the chessboard, where each
# cell can either be a queen ('Q') or an empty space ('.'). The `backtrack` function is a recursive function that attempts to place queens row by row.
# If a queen can be placed in a cell (i.e., the column and both diagonals are not occupied), it places the queen, updates the sets, and recursively calls itself to place the next queen in the next row.
# If all queens are successfully placed (when `r` equals `n`), it appends the current board configuration to the result list `res`.
# After exploring all possibilities, it removes the queen from the current cell (backtracking) and continues to explore other cells in the current row.
# Finally, the function returns the list of all distinct solutions found.