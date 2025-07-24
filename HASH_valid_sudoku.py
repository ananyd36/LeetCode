
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
 

# Example 1:


# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
# Example 2:

# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = collections.defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)


        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in row[r] or
                    board[r][c] in col[c] or
                    board[r][c] in square[r // 3, c // 3]):
                    return False
                
                row[r].add(board[r][c])
                col[c].add(board[r][c])
                square[r // 3, c // 3].add(board[r][c])
        return True
    

# Approach:
# 1. Initialize three dictionaries to keep track of the numbers seen in each row, column, and 3x3 sub-box.
# 2. Iterate through each cell in the 9x9 Sudoku board.
# 3. If the cell is empty (".") continue to the next cell.
# 4. Check if the number in the current cell has already been seen in the corresponding row, column, or sub-box.
# 5. If it has been seen, return False indicating the Sudoku board is invalid.
# 6. If not, add the number to the corresponding row, column, and sub-box sets.
# 7. If all cells are checked without finding duplicates, return True indicating the Sudoku board is valid.
# Time Complexity:
# - O(1), since the board size is fixed at 9x9, making the operations constant time.
# Space Complexity:
# - O(1), since the space used for the dictionaries is also constant due to the fixed size of the board.