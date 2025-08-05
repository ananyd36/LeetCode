# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.



class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2 :
                    queue.append((row,col))
                elif grid[row][col] == 1:
                    fresh+=1
        
        if fresh == 0:
            return 0
        
        minute = -1
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()

                directions = [[0,1], [1,0], [0,-1], [-1,0]]
                for dr, dc in directions:
                    if ( 
                    min(r+dr, c+dc) < 0 or
                    r+dr >= ROWS or c+dc >= COLS or
                    grid[r+dr][c+dc] == 2 or
                    grid[r+dr][c+dc] == 0
                    ):
                        continue

                    queue.append((r+dr, c+dc))
                    fresh-=1
                    grid[r+dr][c+dc] = 2
            minute+=1 
        return minute if fresh == 0 else -1

