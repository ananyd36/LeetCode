# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set ()
        count = 0

        def dfs(row, col):
            if min(row, col) < 0 or (row,col) in visited or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == "0":
                return

            visited.add((row,col))


            dfs(row - 1, col) 
            dfs(row + 1, col) 
            dfs(row, col + 1) 
            dfs(row, col - 1)

        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r, c) # if it does return then we dont count, else we count an island
                    count+=1
        
        return count


            