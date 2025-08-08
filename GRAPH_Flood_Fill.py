# You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill:

# Begin with the starting pixel and change its color to color.
# Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or vertically) and shares the same color as the starting pixel.
# Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
# The process stops when there are no more adjacent pixels of the original color to update.
# Return the modified image after performing the flood fill.

#  Example 1:

# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2

# Output: [[2,2,2],[2,2,0],[2,0,1]]


#DFS can be faster because it goes deep into one path, changing pixels quickly, so often less overhead per step. 
# But it uses the call stack, which can cause stack overflow for large images. 
# BFS is more memory-efficient in practice because it uses a queue and explores level by level—avoiding deep recursion.


# Time complexity is O(m*n) where m is the number of rows and n is the number of columns in the grid.
# Space complexity is O(m*n) for the visited set.

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(row, col, oldColor):
            if oldColor == color:
                return
            
            if min(row, col) < 0 or row>=len(image) or col>=len(image[0]) or image[row][col] !=oldColor:
                return
            
            
            image[row][col] = color
            
            dfs(row+1, col, oldColor)
            dfs(row-1, col, oldColor)
            dfs(row, col+1, oldColor)
            dfs(row, col-1, oldColor)
        

        dfs(sr, sc, image[sr][sc])
        return image
    

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        queue = deque()
        oldColor = image[sr][sc]
        queue.append((sr, sc))
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        if image[sr][sc] == color:
            return image

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                image[r][c] = color
                
                for dr, dc in directions:
                        if min(r+dr, c+dc) < 0 or r+dr >= ROWS or c+dc >= COLS or image[r+dr][c+dc] != oldColor:
                            continue
                    
                queue.append((r+dr,c+dc))
        
        return image