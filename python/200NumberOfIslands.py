class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m = len(grid)
        n = len(grid[0])

        d = [[1,0],[0,1],[0,-1],[-1,0]]
        
        def dfs(x,y):
            
            if 0 <= x < m and 0 <= y < n and grid[x][y] == "1":
                
                grid[x][y] = "0"
                
                for dx, dy in d:
                    dfs(x+dx, y+dy)

        total = 0
        
        for i in range(m):
            for j in range(n):
                
                if grid[i][j] == "1":
                    total += 1
                    dfs(i,j)
        
        return total
        
        