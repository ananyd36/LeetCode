# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

# All the visited cells of the path are 0.
# All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
# The length of a clear path is the number of visited cells of this path.


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        def find_path(grid):
            ROW, COL = len(grid), len(grid[0])
            queue = deque()
            visit = set()
            queue.append((0,0))
            visit.add((0,0))

            length = 1
            while queue:
                for i in range(len(queue)):
                    r,c = queue.popleft()
                    if grid[r][c] == 0 and r == ROW - 1 and c == COL - 1:
                        return length
                    
                    neighbour = [[0,1],[0,-1],[1,0],[-1,0], [1,1],[1,-1],[-1,1],[-1,-1]]
                    for dr, dc in neighbour:
                        if (
                            min(r+dr, c+dc) < 0 or
                            r+dr>=ROW or c+dc>=COL or
                            ((r+dr, c+dc)) in visit or
                            grid[r+dr][c+dc] == 1
                        ):
                            continue
                        queue.append((r+dr, c+dc))
                        visit.add((r+dr, c+dc))
                length+=1
            
            return -1
        if grid[0][0] == 0:
            return find_path(grid)
        else:
            return -1