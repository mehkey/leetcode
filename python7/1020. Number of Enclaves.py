class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        M = len(grid)
        N = len(grid[0])

        v= set()

        dirs = [[1,0],[-1,0],[0,1],[0,-1]]

        def dfs(r,c):
            
            if grid[r][c] == 1:
                
                grid[r][c] = 0
                
                for d in dirs:
                    nx = r+d[0]
                    ny = c+d[1]
                    if 0<= nx < M and 0 <= ny < N:
                        dfs(nx,ny)

        for i in range(M):
            dfs(i,0)
            dfs(i,N-1)

        for j in range(N):
            dfs(0,j)
            dfs(M-1,j)

        c = 0

        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    c+=1

        return c