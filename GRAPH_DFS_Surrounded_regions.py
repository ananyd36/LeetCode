# You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

# Connect: A cell is connected to adjacent cells horizontally or vertically.
# Region: To form a region connect every 'O' cell.
# Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
# To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

 

# Example 1:

# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

# Explanation:


# In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def dfs(row, col):
            if row < 0 or col < 0 or row == len(board) or col == len(board[0]) or board[row][col] !="O":
                return
            
            board[row][col] = "T"

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
        

        for row in range(len(board)):
            for col in range(len(board[0])):
                if ( 
                    board[row][col] == "O" and (row in [0, len(board)-1] or col in [0, len(board[0])-1])):
                    dfs(row, col)

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "O":
                    board[row][col] = "X"
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "T":
                    board[row][col] = "O"
        

# In this solution we did reverse thinking,
# Instead of finding the surrounding regions, we found all regionst that are not surrounded (searching for O on the edges and then doing DFS to capture the attached O, which will also be regarded as unsurrounded) and then we 
# reassigned them to "T" to be tracked later. Once we have them tracked we can then now convert all the O that are surrounded(all the rest of them) and convert them to X. Finally at the last we convert the T back to O 