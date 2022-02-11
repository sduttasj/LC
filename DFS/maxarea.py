#https://leetcode.com/problems/max-area-of-island/
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        def dfs(x,y):
            
            if x < 0 or y < 0:
                return 0
            if x >= ROWS or y >= COLS:
                return 0
            if grid[x][y] == 0:
                return 0
            # we can mark the already visited cell
            grid[x][y] = 0
            return 1 + dfs(x, y + 1) + dfs(x, y - 1,)+ dfs(x + 1, y)+ dfs(x  -1, y)
        # we need to find number of connected components and return that number
        
        maxarea = 0
        # traverse
        for i in range(ROWS):
            for j in range(COLS):
                #find 1
                if (grid[i][j]):
                    maxarea = max(maxarea, dfs(i,j))
                    
        return maxarea
