# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

# Example 1:


# Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image above.



# BFS

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def bfs(r, c):
            queue = deque([(r, c)])
            visited.add((r, c))
            perimeter = 0

            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if (nx < 0 or ny < 0 or nx >= rows or
                        ny >= cols or grid[nx][ny] == 0
                    ):
                        perimeter += 1
                    elif (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
            return perimeter

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return bfs(i, j)
        return 0



#DFS 
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        visited = set ()

        def dfs(row, col):
            
            if min(row, col) < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == 0:
                return 1
            
            if (row, col) in visited:
                return 0

            visited.add((row,col))


            perimeter = dfs(row - 1, col) + dfs(row + 1, col) + dfs(row, col + 1) + dfs(row, col - 1)

            return perimeter

        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 :
                    return dfs(r, c)
                    
        
        return 0