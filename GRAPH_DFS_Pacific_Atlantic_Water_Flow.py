# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

# The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

# The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

 

# Example 1:


# Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
# Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
# [0,4]: [0,4] -> Pacific Ocean 
#        [0,4] -> Atlantic Ocean
# [1,3]: [1,3] -> [0,3] -> Pacific Ocean 
#        [1,3] -> [1,4] -> Atlantic Ocean
# [1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
#        [1,4] -> Atlantic Ocean
# [2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
#        [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
# [3,0]: [3,0] -> Pacific Ocean 
#        [3,0] -> [4,0] -> Atlantic Ocean
# [3,1]: [3,1] -> [3,0] -> Pacific Ocean 
#        [3,1] -> [4,1] -> Atlantic Ocean
# [4,0]: [4,0] -> Pacific Ocean 
#        [4,0] -> Atlantic Ocean
# Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW  = len(heights)
        COL = len(heights[0])


        def dfs(row, col, previous, visited):
            if row < 0 or col < 0 or row >= len(heights) or col >= len(heights[0]) or heights[row][col] < previous or (row, col) in visited :
                return
            
            visited.add((row, col))
            previous = heights[row][col]

            dfs(row + 1, col, previous, visited)
            dfs(row - 1, col, previous, visited)
            dfs(row, col + 1, previous, visited)
            dfs(row, col - 1, previous, visited)

        
        pacific_set = set()
        atlantic_set = set()

        for col in range(COL):
            dfs(0, col, heights[0][col], pacific_set)
            dfs(ROW-1, col, heights[ROW-1][col], atlantic_set)
        
        for row in range(ROW):
            dfs(row, 0, heights[row][0], pacific_set)
            dfs(row, COL-1, heights[row][COL-1], atlantic_set)

        return list(pacific_set & atlantic_set)


# Time Complexity: 
# O(M×N) O(M×N) because each cell is visited at most twice (once for each ocean).
# Space Complexity: O(M×N) O(M×N) for the two sets plus the recursion stack.

# the idea is to perform DFS from the borders of the matrix that touch each ocean. We maintain two sets to keep track of cells that can reach the Pacific and Atlantic oceans. Finally, we return the intersection of these two sets as the result.