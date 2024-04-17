class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        l = [-1,0,1,0,-1]
        def dfs(i,j):
            if i >= M or i < 0:
                return
            if j >= N or j < 0:
                return
            if grid[i][j] == 1:
                return
            if grid[i][j] == 0:
                grid[i][j] = 1

                for k in range(4):
                    dx = l[k]
                    dy = l[k+1]
                    dfs(i + dx, j + dy)
                #for dx in range(-1,2):
                    #for dy in range(-1,2):
                        #dfs(i+dx,j+dy)
                

        M = len(grid)
        N = len(grid[0])
        
        for i in range(M):
            dfs(i,0)
            dfs(i,N-1)
        
        for j in range(N):
            dfs(0,j)
            dfs(M-1,j)
        
        res = 0
        for i in range(1,M-1):
            for j in range(1,N-1):
                if grid[i][j] == 0:
                    dfs(i,j)
                    res += 1
        
        return res